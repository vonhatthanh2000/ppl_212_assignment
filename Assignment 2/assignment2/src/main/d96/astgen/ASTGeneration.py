from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce



class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(ctx.class_declaration().accept(self))
    
    def visitClass_declaration(self,ctx: D96Parser.Class_declarationContext):
        return reduce(lambda prev,curr: prev + [curr.accept(self)],ctx.class_declaration_part(),[])

    def visitClass_declaration_part(self, ctx:D96Parser.Class_declaration_partContext):
        mem_list = []
        for x in ctx.member():
            mem_list += x.accept(self)
        ids = None
        if ctx.main_keyword(): ids = Id(ctx.main_keyword().getText())
        elif ctx.ID(0): ids = Id(ctx.ID(0).getText())
        elif ctx.Program(): ids = Id(ctx.Program().getText())
        parent = None
        if ctx.ID(1):parent = Id(ctx.ID(1).getText())
        return ClassDecl(ids,mem_list,parent)
        
    def visitMember(self, ctx:D96Parser.MemberContext):
        if ctx.attribute_lit():
            return ctx.attribute_lit().accept(self)
        elif ctx.method_lit():
            return ctx.method_lit().accept(self)
        
    def visitAttribute_lit(self, ctx:D96Parser.Attribute_litContext):
        # instance_static = ctx.attribute_list().accept(self)[0]
        id_list = ctx.attribute_list().accept(self)
        exp_list = ctx.expr_list().accept(self) if ctx.expr_list() else None
        # lst=ConstDecl(id_list[1],ctx.type_name().accept(self), None)
        decl_return = None
        type_name = ctx.type_name().accept(self)
        if type_name[0] == 2:  decl_return = NullLiteral()
        lst = []
    
        if ctx.VAL():
            for i in range(len(id_list)):
                lst += [AttributeDecl(id_list[i][0],ConstDecl(id_list[i][1],type_name[1],exp_list[i]if exp_list != None else decl_return))]
        elif ctx.VAR():
            for i in range(len(id_list)):
                lst += [AttributeDecl(id_list[i][0],VarDecl(id_list[i][1],type_name[1],exp_list[i]if exp_list != None else decl_return))]
        return lst
        
    
    def visitAttribute_list(self,ctx:D96Parser.Attribute_listContext):
        # attri_list = list(map(lambda x: x.accept(self)[1],ctx.attribute()))
        return reduce(lambda prev,curr: prev + [curr.accept(self)],ctx.attribute(),[])
        

    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        if ctx.ID():
            return (Instance(),Id(ctx.ID().getText()))
        elif ctx.DO_ID():
            return (Static(),Id(ctx.DO_ID().getText()))
    

    def visitArray_declaration(self,ctx:D96Parser.Array_declarationContext):
        type_na = ctx.type_name().accept(self)
        array_size = ctx.array_type().accept(self)
        return (1,ArrayType(array_size,type_na[1]))
    
    def visitType_name(self,ctx:D96Parser.Type_nameContext):
        if ctx.INT(): return (1,IntType())
        elif ctx.FLOAT(): return (1,FloatType())
        elif ctx.BOOLEAN(): return (1,BoolType())
        elif ctx.STRING(): return (1,StringType())
        elif ctx.array_declaration():
            return ctx.array_declaration().accept(self)
        elif ctx.attribute():
            ids = ctx.attribute().accept(self)
            return (2,ClassType(ids[1]))
        else: return None

    ## Read Int_lit
    def visitINT_LIT(self,int_lit:str):
        def int_lit_base(str):
            if len(str) == 1: return (str,10)
            elif str[0:2] == '0x' or str[0:2] == '0X':
                return (str[2:],16) 
            elif str[0:2] == '0b' or str[0:2] == '0B':
                return (str[2:],2)
            elif str[0] == '0': return (str[1:],8)
            else: return (str,10) 
        lit_base = int_lit_base(int_lit)
        return int(lit_base[0],lit_base[1])
    
    ## array size
    def visitArray_type(self,ctx:D96Parser.Array_typeContext):
        if ctx.NONZERO_INT():
            return int(ctx.NONZERO_INT().getText())
        if ctx.INT_LIT():
            return self.visitINT_LIT(ctx.INT_LIT().getText())
    
    ##visit expression_list
    def visitExpr_list(self,ctx:D96Parser.Expr_listContext):
        lst = []
        for i in ctx.expr():
            lst += [i.accept(self)]
        return lst
        # return list(map(lambda x: x.accept(self),ctx.expr()))
    def visitExpr(self,ctx:D96Parser.ExprContext):
        return ctx.string_expr().accept(self)
    ### String
    def visitString_expr(self,ctx:D96Parser.String_exprContext):
        if ctx.getChildCount()==3:
            return BinaryOp(ctx.string_op().accept(self),ctx.relational_expr()[0].accept(self),ctx.relational_expr()[1].accept(self))
        else: return ctx.relational_expr()[0].accept(self)
    
    ###Relational
    def visitRelational_expr(self,ctx:D96Parser.Relational_exprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.relational_op().accept(self),ctx.logical_expr()[0].accept(self),ctx.logical_expr()[1].accept(self))
        else: return ctx.logical_expr()[0].accept(self)
    
    ### Logical
    def visitLogical_expr(self,ctx:D96Parser.Logical_exprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.logical_op().accept(self),ctx.logical_expr().accept(self),ctx.add_expr().accept(self))
        else: return ctx.add_expr().accept(self)

    ## Add
    def visitAdd_expr(self,ctx:D96Parser.Add_exprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.add_op().accept(self),ctx.add_expr().accept(self),ctx.mul_expr().accept(self))
        else: return ctx.mul_expr().accept(self)
    
    ### Mul
    def visitMul_expr(self,ctx:D96Parser.Mul_exprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.multi_op().accept(self),ctx.mul_expr().accept(self),ctx.log_expr().accept(self))
        else: return ctx.log_expr().accept(self)

    ### Negation
    def visitLog_expr(self,ctx:D96Parser.Log_exprContext):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.negation_op().accept(self),ctx.log_expr().accept(self))
        else: return ctx.sign_expr().accept(self)
    
    ### Sign
    def visitSign_expr(self,ctx:D96Parser.Sign_exprContext):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.negation_number().accept(self),ctx.sign_expr().accept(self))
        else: return ctx.index_expr().accept(self)

    ### index expr
    def visitIndex_expr(self,ctx:D96Parser.Index_exprContext):
        if ctx.getChildCount() == 2:
            return ArrayCell(ctx.index_expr().accept(self),ctx.index_op().accept(self))
        else: return ctx.instance_access_expr().accept(self)
    def visitIndex_op(self,ctx:D96Parser.Index_opContext):
        return list(map(lambda x: x.accept(self),ctx.expr()))

    ###instance_access_expr
    def visitInstance_access_expr(self,ctx:D96Parser.Instance_access_exprContext):
        if ctx.getChildCount() == 1: return ctx.static_access_expr().accept(self)
        else:
            if ctx.LB():
                if ctx.expr_list():
                    return CallExpr(ctx.instance_access_expr().accept(self),ctx.static_access_expr().accept(self),ctx.expr_list().accept(self))
                else: return CallExpr(ctx.instance_access_expr().accept(self),ctx.static_access_expr().accept(self),[])
            else: return FieldAccess(ctx.instance_access_expr().accept(self),ctx.static_access_expr().accept(self))
   
    ### Static
    def visitStatic_access_expr(self,ctx:D96Parser.Static_access_exprContext):
        if ctx.getChildCount() == 1: return ctx.new_expr(0).accept(self)
        else:
            if ctx.LB():
                return CallExpr(ctx.new_expr(0).accept(self),ctx.new_expr(1).accept(self),ctx.expr_list().accept(self) if ctx.expr_list() else [])
            else: return FieldAccess(ctx.new_expr(0).accept(self),ctx.new_expr(1).accept(self))
  
    #### New
    def visitNew_expr(self,ctx:D96Parser.New_exprContext):
        if ctx.getChildCount() == 1: return ctx.parenth_exp().accept(self)
        else:
            lst = ctx.expr_list().accept(self) if ctx.expr_list() else []
            return NewExpr(Id(ctx.ID().getText()),lst)

    ####parenth_exp
    def visitParenth_exp(self,ctx:D96Parser.Parenth_expContext):
        if ctx.getChildCount() == 3:
            return ctx.expr().accept(self)
        else:
            return ctx.operative().accept(self)
            
    ### operative
    def visitOperative(self,ctx:D96Parser.OperativeContext):
        if ctx.literal(): return ctx.literal().accept(self)
        elif ctx.array_lit(): return ctx.array_lit().accept(self)
        elif ctx.array_attribute(): return ctx.array_attribute().accept(self)
        elif ctx.Self(): return SelfLiteral()
        elif ctx.ID(): return Id(ctx.ID().getText())
        else: return Id(ctx.DO_ID().getText())
        
    def visitLiteral(self,ctx:D96Parser.LiteralContext):
        if ctx.NONZERO_INT(): return IntLiteral(int(ctx.NONZERO_INT().getText()))
        elif ctx.INT_LIT(): return IntLiteral(self.visitINT_LIT(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT(): return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT(): return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.boollit(): return ctx.boollit().accept(self)
    def visitArray_lit(self,ctx:D96Parser.Array_litContext):
        return ArrayLiteral(ctx.expr_list().accept(self)if ctx.expr_list() else [])
        
    
    def visitArray_attribute(self,ctx:D96Parser.Array_attributeContext):
        lst = list(map(lambda x: x.accept(self),ctx.expr()))
        return ArrayCell(Id(ctx.ID().getText()),lst)
        
    def visitBoollit(self,ctx:D96Parser.BoollitContext):
        return BooleanLiteral(ctx.getChild(0).getText()=='True')


    def visitString_op(self,ctx:D96Parser.String_opContext):
        return ctx.getChild(0).getText()
    def visitRelational_op(self,ctx:D96Parser.Relational_opContext):
        return ctx.getChild(0).getText()
    def visitLogical_op(self,ctx:D96Parser.Logical_opContext):
        return ctx.getChild(0).getText()
    def visitAdd_op(self,ctx:D96Parser.Add_opContext):
        return ctx.getChild(0).getText()
    def visitMulti_op(self,ctx:D96Parser.Multi_opContext):
        return ctx.getChild(0).getText()
    def visitNegation_op(self,ctx:D96Parser.Negation_opContext):
        return ctx.getChild(0).getText()    
    def visitNegation_number(self,ctx:D96Parser.Negation_numberContext):
        return ctx.getChild(0).getText()    

##------------------------------------------------------------------------------##
## method declararion ######

    def visitMethod_lit(self,ctx:D96Parser.Method_litContext):
        if ctx.normal_method(): return ctx.normal_method().accept(self)
        elif ctx.method_constructor(): return ctx.method_constructor().accept(self)
        elif ctx.main_destructor(): return ctx.main_destructor().accept(self)
        
    def visitNormal_method(self,ctx:D96Parser.Normal_methodContext):
        instance_static =  ctx.identifier().accept(self)[0]
        name = ctx.identifier().accept(self)[1]
        para_list=[]
        if ctx.parameter_list():
            para_list += ctx.parameter_list().accept(self)
        
        block = ctx.block_stm().accept(self) if ctx.block_stm() else None    
        return [MethodDecl(instance_static,name,para_list,block)]

    #### Main, destructor
    def visitMain_destructor(self,ctx:D96Parser.Main_destructorContext):
        block = ctx.block_stm_no_return().accept(self) if ctx.block_stm_no_return() else None  
        if ctx.main_keyword():
            return [MethodDecl(Static(),Id(ctx.main_keyword().getText()),[],block)]
        elif ctx.DESTRUCTOR():
            return [MethodDecl(Instance(),Id("Destructor"),[],block)]

    ### Constructor
    def visitMethod_constructor(self,ctx:D96Parser.Method_constructorContext):
        para_list=[]
        if ctx.parameter_list():
            para_list += ctx.parameter_list().accept(self)
        block = ctx.block_stm().accept(self) if ctx.block_stm() else None 
        return [MethodDecl(Instance(),Id("Constructor"),para_list,block)]


    def visitParameter_list(self,ctx:D96Parser.Parameter_listContext):
        return reduce(lambda prev,curr: prev + curr.accept(self),ctx.identifier_list(),[])
        

    def visitIdentifier_list(self,ctx:D96Parser.Identifier_listContext):
        return list(map(lambda x: VarDecl(x.accept(self)[1],ctx.type_name().accept(self)[1]),ctx.identifier()))
    
    def visitIdentifier(self,ctx:D96Parser.IdentifierContext):
        if ctx.ID():
            return (Instance(),Id(ctx.ID().getText()))
        elif ctx.DO_ID():
            return (Static(),Id(ctx.DO_ID().getText()))

    ####### BLOCK ###########
    def visitBlock_stm(self,ctx:D96Parser.Block_stmContext):
        block_list = []
        for x in ctx.stm():
            block_list += x.accept(self)
        return Block(block_list)

    def visitStm(self,ctx:D96Parser.StmContext):
        if ctx.variable_statement(): return ctx.variable_statement().accept(self)
        elif ctx.assignment_statement(): return ctx.assignment_statement().accept(self)
        elif ctx.if_statement(): return ctx.if_statement().accept(self)
        elif ctx.for_in_statement(): return ctx.for_in_statement().accept(self)
        elif ctx.break_statement(): return ctx.break_statement().accept(self)
        elif ctx.continue_statement(): return ctx.continue_statement().accept(self)
        elif ctx.return_statement(): return ctx.return_statement().accept(self)
        elif ctx.method_statement(): return ctx.method_statement().accept(self)
        elif ctx.block_stm(): return [ctx.block_stm().accept(self)]
    ### BLOCK NO RETURN
    def visitBlock_stm_no_return(self,ctx:D96Parser.Block_stm_no_returnContext):
        block_list = []
        for x in ctx.stm_no_return():
            block_list += x.accept(self)
        return Block(block_list)

    def visitStm_no_return(self,ctx:D96Parser.Stm_no_returnContext):
        if ctx.variable_statement(): return ctx.variable_statement().accept(self)
        elif ctx.assignment_statement(): return ctx.assignment_statement().accept(self)
        elif ctx.if_statement(): return ctx.if_statement().accept(self)
        elif ctx.for_in_statement(): return ctx.for_in_statement().accept(self)
        elif ctx.break_statement(): return ctx.break_statement().accept(self)
        elif ctx.continue_statement(): return ctx.continue_statement().accept(self)
        elif ctx.method_statement(): return ctx.method_statement().accept(self)
        else: return [ctx.block_stm_no_return().accept(self)]
    
    ####Variable
    def visitVariable_statement(self,ctx:D96Parser.Variable_statementContext):
        id_list = ctx.variable_list().accept(self)
        exp_list = ctx.expr_list().accept(self) if ctx.expr_list() else None
        decl_return = None
        type_name = ctx.type_name().accept(self)
        if type_name[0] == 2:  decl_return = NullLiteral()
        lst = []
        if ctx.VAL():
            for i in range(len(id_list)):
                lst += [ConstDecl(id_list[i],type_name[1],exp_list[i]if exp_list != None else decl_return)]
        elif ctx.VAR():
            for i in range(len(id_list)):
                lst += [VarDecl(id_list[i],type_name[1],exp_list[i]if exp_list != None else decl_return)]
        return lst
    def visitVariable_list(self,ctx:D96Parser.Variable_listContext):
        # attri_list = list(map(lambda x: x.accept(self)[1],ctx.attribute()))
        return reduce(lambda prev,curr: prev + [Id(curr.getText())],ctx.ID(),[])
        
    #######
    ## Assignment statement
    ####    
    def visitAssignment_statement(self,ctx:D96Parser.Assignment_statementContext):
        left = None
        if ctx.ID(): left = Id(ctx.ID().getText())
        elif ctx.index_expr(): left = ctx.index_expr().accept(self)
        elif ctx.array_attribute(): left = ctx.array_attribute().accept(self)
        return [Assign(left,ctx.expr().accept(self))]

    ###### IF else
    def visitIf_statement(self,ctx:D96Parser.If_statementContext):
        exprs = list(map(lambda expr: expr.accept(self), ctx.expr()))
        blockstm = list(map(lambda expr: expr.accept(self), ctx.block_stm()))
        if len(blockstm) == 3:
            return [If(exprs[0],blockstm[0],If(exprs[1],blockstm[1],blockstm[2]))]
        elif len(blockstm) == 2:
            if ctx.ELSEIF(): return [If(exprs[0],blockstm[0],(If(exprs[1],blockstm[1],None)))]
            else: return [If(exprs[0],blockstm[0],blockstm[1])]
        else: return [If(exprs[0],blockstm[0],None)]

    ###For in
    def visitFor_in_statement(self,ctx:D96Parser.For_in_statementContext):
        ids = Id(ctx.ID().getText())
        exprs = list(map(lambda x: x.accept(self),ctx.expr()))
        block_stm = ctx.block_stm().accept(self)
        return [For(ids,exprs[0],exprs[1],block_stm,exprs[2]if len(exprs)==3 else None)]

    ### break statement
    def visitBreak_statement(self,ctx:D96Parser.Break_statementContext):
        return [Break()]
    
    ## Continue statement
    def visitContinue_statement(self,ctx:D96Parser.Continue_statementContext):
        return [Continue()]

    ### Return statement
    def visitReturn_statement(self,ctx:D96Parser.Return_statementContext):
        return [Return(ctx.expr().accept(self) if ctx.expr() else None)]

    ## Method statement
    def visitMethod_statement(self,ctx:D96Parser.Method_statementContext):
        return [ctx.instance_access_stmt().accept(self)] if ctx.instance_access_stmt() else [ctx.static_access_stmt().accept(self)]
    def visitInstance_access_stmt(self,ctx:D96Parser.Instance_access_stmtContext):
        return CallStmt(ctx.instance_access_expr().accept(self),Id(ctx.ID().getText()),ctx.expr_list().accept(self) if ctx.expr_list() else [])
           
   
    ### Static
    def visitStatic_access_stmt(self,ctx:D96Parser.Static_access_stmtContext):
        return CallStmt(ctx.instance_access_expr.accept(self),Id(ctx.DO_ID().getText()),ctx.expr_list().accept(self) if ctx.expr_list() else [])
