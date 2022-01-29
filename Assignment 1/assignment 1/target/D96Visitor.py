# Generated from main/d96/parser/D96.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration_part.
    def visitClass_declaration_part(self, ctx:D96Parser.Class_declaration_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_keyword.
    def visitClass_keyword(self, ctx:D96Parser.Class_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_lit.
    def visitAttribute_lit(self, ctx:D96Parser.Attribute_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_list.
    def visitAttribute_list(self, ctx:D96Parser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_name.
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_lit.
    def visitMethod_lit(self, ctx:D96Parser.Method_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_constructor.
    def visitMethod_constructor(self, ctx:D96Parser.Method_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#main_destructor.
    def visitMain_destructor(self, ctx:D96Parser.Main_destructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal_method.
    def visitNormal_method(self, ctx:D96Parser.Normal_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_list.
    def visitParameter_list(self, ctx:D96Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier_list.
    def visitIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stm_no_return.
    def visitBlock_stm_no_return(self, ctx:D96Parser.Block_stm_no_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stm_no_return.
    def visitStm_no_return(self, ctx:D96Parser.Stm_no_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stm.
    def visitBlock_stm(self, ctx:D96Parser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stm.
    def visitStm(self, ctx:D96Parser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_statement.
    def visitVariable_statement(self, ctx:D96Parser.Variable_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_list.
    def visitVariable_list(self, ctx:D96Parser.Variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignment_statement.
    def visitAssignment_statement(self, ctx:D96Parser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statement.
    def visitIf_statement(self, ctx:D96Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_statement.
    def visitFor_in_statement(self, ctx:D96Parser.For_in_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statement.
    def visitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statement.
    def visitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statement.
    def visitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_statement.
    def visitMethod_statement(self, ctx:D96Parser.Method_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parenth_exp.
    def visitParenth_exp(self, ctx:D96Parser.Parenth_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_create.
    def visitObject_create(self, ctx:D96Parser.Object_createContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#new_keyword.
    def visitNew_keyword(self, ctx:D96Parser.New_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_access_exp.
    def visitStatic_access_exp(self, ctx:D96Parser.Static_access_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_access_exp.
    def visitInstance_access_exp(self, ctx:D96Parser.Instance_access_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#self_keyword.
    def visitSelf_keyword(self, ctx:D96Parser.Self_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_exp.
    def visitIndex_exp(self, ctx:D96Parser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arithmetic_exp.
    def visitArithmetic_exp(self, ctx:D96Parser.Arithmetic_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#not_logical_expr.
    def visitNot_logical_expr(self, ctx:D96Parser.Not_logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mod_expr.
    def visitMod_expr(self, ctx:D96Parser.Mod_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_expr.
    def visitLogical_expr(self, ctx:D96Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_expr.
    def visitRelational_expr(self, ctx:D96Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relatonal_bool.
    def visitRelatonal_bool(self, ctx:D96Parser.Relatonal_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_number.
    def visitRelational_number(self, ctx:D96Parser.Relational_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_expr.
    def visitString_expr(self, ctx:D96Parser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_component.
    def visitArray_component(self, ctx:D96Parser.Array_componentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_op.
    def visitString_op(self, ctx:D96Parser.String_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_op_bool.
    def visitRelational_op_bool(self, ctx:D96Parser.Relational_op_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_op_number.
    def visitRelational_op_number(self, ctx:D96Parser.Relational_op_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_op.
    def visitLogical_op(self, ctx:D96Parser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#add_op.
    def visitAdd_op(self, ctx:D96Parser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_op.
    def visitMulti_op(self, ctx:D96Parser.Multi_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#negation_op.
    def visitNegation_op(self, ctx:D96Parser.Negation_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#negation_number.
    def visitNegation_number(self, ctx:D96Parser.Negation_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#main_keyword.
    def visitMain_keyword(self, ctx:D96Parser.Main_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier.
    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_declaration.
    def visitArray_declaration(self, ctx:D96Parser.Array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_attribute.
    def visitArray_attribute(self, ctx:D96Parser.Array_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)



del D96Parser