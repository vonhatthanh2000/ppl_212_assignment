import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_0(self):
        line = '''Class Simple{}'''
        expect = '''Program([ClassDecl(Id(Simple),[])])'''
        self.assertTrue(TestAST.test(line, expect, 0))

    def test_1(self):
        line = '''Class Simple{}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 1))

    def test_2(self):
        line = '''Class Simple{Val $Shape: Int = 3;}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3)))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 2))

    def test_3(self):
        line = '''Class Simple{Val $Shape: Int = 3;ta{a = 1+2;}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(ta),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 3))

    def test_4(self):
        line = '''Class Simple{Val $Shape: Int = 3;ta(a,b:Int){a = 1+2;}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 4))

    def test_5(self):
        line = '''Class Simple{Val $Shape: Int = 3;ta(a,b:Int){a = 1+2;}$staticfun(){}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 5))

    def test_6(self):
        line = '''Class Simple{Val $Shape: Int = 3;ta(a,b:Int){a = 1+2;}$staticfun(){}Constructor(){Return;}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([Return()]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 6))

    def test_7(self):
        line = '''Class Simple{Val $Shape: Int = 3;ta(a,b:Int){a = 1+2;}$staticfun(){}Constructor(a,b:Float){Return;}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([Return()]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 7))

    def test_8(self):
        line = '''Class Simple{Val $Shape: Int = 3;ta(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 8))

    def test_9(self):
        line = '''Class Simple{Val $Shape: Int = 3;ta(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 9))

    def test_10(self):
        line = '''Class Simple{Val $Shape: Int = 3;ta(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){Continue;}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Continue]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 10))

    def test_11(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int = 1, 2;ta(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){If (a+b){Return;}}}Class Simple2{}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([If(BinaryOp(+,Id(a),Id(b)),Block([Return()]))]))]),ClassDecl(Id(Simple2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 11))

    def test_12(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;ta(a,b:Int){a = 1+2;}$staticfun(){}Constructor(a,b:Int){}}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 12))

    def test_13(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;ta(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2)))])])'''
        self.assertTrue(TestAST.test(line, expect, 13))

    def test_14(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;ta(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Int = 0x123A;}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(4666)))])])'''
        self.assertTrue(TestAST.test(line, expect, 14))

    def test_15(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;ta(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x,$b: Int = 0x123A,0b101 + 023;}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(4666))),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(5),IntLit(19))))])])'''
        self.assertTrue(TestAST.test(line, expect, 15))

    def test_16(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,3e-10;Var x,$b: Int = 0x123A,0b101 + 023;}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(3e-10))),AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(4666))),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(5),IntLit(19))))])])'''
        self.assertTrue(TestAST.test(line, expect, 16))

    def test_17(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;tloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Int,2] = Array(1,2,3);}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(tloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,IntType),[IntLit(1),IntLit(2),IntLit(3)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 17))

    def test_18(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;hloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(1,2,3);}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(hloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[IntLit(1),IntLit(2),IntLit(3)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 18))

    def test_19(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(1,2,3);}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[IntLit(1),IntLit(2),IntLit(3)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 19))

    def test_20(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[game,0b1010],0124] = Array(1,2,3);}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(84,ArrayType(10,ClassType(Id(game)))),[IntLit(1),IntLit(2),IntLit(3)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 20))

    def test_21(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],12] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(12,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 21))

    def test_22(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2-3+5, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 22))

    def test_23(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2*3+5, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 23))

    def test_24(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2*3+5%15,2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(%,IntLit(5),IntLit(15))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 24))

    def test_25(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+2*3+5 || 1%5, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),IntLit(5)),BinaryOp(%,IntLit(1),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 25))

    def test_26(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+-2*3+5 || 1%5, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,IntLit(1),BinaryOp(*,UnaryOp(-,IntLit(2)),IntLit(3))),IntLit(5)),BinaryOp(%,IntLit(1),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 26))

    def test_27(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =1+(-2)*3+5 || 1%5, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,IntLit(1),BinaryOp(*,UnaryOp(-,IntLit(2)),IntLit(3))),IntLit(5)),BinaryOp(%,IntLit(1),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 27))

    def test_28(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =(1+(-2))*3+5 || 1%5, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(*,BinaryOp(+,IntLit(1),UnaryOp(-,IntLit(2))),IntLit(3)),IntLit(5)),BinaryOp(%,IntLit(1),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 28))

    def test_29(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =(1+(-2))*3+5 || !(1%5), 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(*,BinaryOp(+,IntLit(1),UnaryOp(-,IntLit(2))),IntLit(3)),IntLit(5)),UnaryOp(!,BinaryOp(%,IntLit(1),IntLit(5)))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 29))

    def test_30(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =(1+(-2))*3+5 || 30 > (32 <1), 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(>,BinaryOp(||,BinaryOp(+,BinaryOp(*,BinaryOp(+,IntLit(1),UnaryOp(-,IntLit(2))),IntLit(3)),IntLit(5)),IntLit(30)),BinaryOp(<,IntLit(32),IntLit(1))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 30))

    def test_31(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =(1+(-2))*3+5 || (1+4) > 5, 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(>,BinaryOp(||,BinaryOp(+,BinaryOp(*,BinaryOp(+,IntLit(1),UnaryOp(-,IntLit(2))),IntLit(3)),IntLit(5)),BinaryOp(+,IntLit(1),IntLit(4))),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 31))

    def test_32(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =(1+(-2))*3+5 || ((1+4) > 5), 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(*,BinaryOp(+,IntLit(1),UnaryOp(-,IntLit(2))),IntLit(3)),IntLit(5)),BinaryOp(>,BinaryOp(+,IntLit(1),IntLit(4)),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 32))

    def test_33(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =Self.ID() + 3 || ((1+4) > 5), 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,CallExpr(Self(),Id(ID),[]),IntLit(3)),BinaryOp(>,BinaryOp(+,IntLit(1),IntLit(4)),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 33))

    def test_34(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =Self.ID + 3 || ((1+4) > 5), 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,FieldAccess(Self(),Id(ID)),IntLit(3)),BinaryOp(>,BinaryOp(+,IntLit(1),IntLit(4)),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 34))

    def test_35(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =New X() + Self.ID() + 3 || ((1+4) > 5), 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,NewExpr(Id(X),[]),CallExpr(Self(),Id(ID),[])),IntLit(3)),BinaryOp(>,BinaryOp(+,IntLit(1),IntLit(4)),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 35))

    def test_36(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =New X() + Self.ID() + 3 || ((1+4) > 5), a[1] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,NewExpr(Id(X),[]),CallExpr(Self(),Id(ID),[])),IntLit(3)),BinaryOp(>,BinaryOp(+,IntLit(1),IntLit(4)),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1)]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 36))

    def test_37(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =New X(a+b) + Self.ID() + 3 || ((1+4) > 5), a[1] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,NewExpr(Id(X),[BinaryOp(+,Id(a),Id(b))]),CallExpr(Self(),Id(ID),[])),IntLit(3)),BinaryOp(>,BinaryOp(+,IntLit(1),IntLit(4)),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1)]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 37))

    def test_38(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =New X(a+b) + Self.ID() + 3 && ((1+4) > 5), a[1][2] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(&&,BinaryOp(+,BinaryOp(+,NewExpr(Id(X),[BinaryOp(+,Id(a),Id(b))]),CallExpr(Self(),Id(ID),[])),IntLit(3)),BinaryOp(>,BinaryOp(+,IntLit(1),IntLit(4)),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 38))

    def test_39(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =New X(a+b) + Self.ID() + 3 || ((1---4) > 5), a[1][2] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,NewExpr(Id(X),[BinaryOp(+,Id(a),Id(b))]),CallExpr(Self(),Id(ID),[])),IntLit(3)),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 39))

    def test_40(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =New X(a+b) + Self.ID() + 3 || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,NewExpr(Id(X),[BinaryOp(+,Id(a),Id(b))]),CallExpr(Self(),Id(ID),[])),IntLit(3)),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 40))

    def test_41(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: String = "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 41))

    def test_42(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 42))

    def test_43(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){a = 1+a;}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),Id(a)))]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 43))

    def test_44(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 44))

    def test_45(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}Else{}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),Block([]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 45))

    def test_46(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}Else{If(1+2){}}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),Block([If(BinaryOp(+,IntLit(1),IntLit(2)),Block([]))]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 46))

    def test_47(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}Elseif(1+2){If(1+2){}}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),If(BinaryOp(+,IntLit(1),IntLit(2)),Block([If(BinaryOp(+,IntLit(1),IntLit(2)),Block([]))])))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 47))

    def test_48(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}Elseif(1+2){a = 1;}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),If(BinaryOp(+,IntLit(1),IntLit(2)),Block([AssignStmt(Id(a),IntLit(1))])))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 48))

    def test_49(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}Elseif(5){a = 1;}Else{}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),If(IntLit(5),Block([AssignStmt(Id(a),IntLit(1))]),Block([])))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 49))

    def test_50(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}Elseif(4+6){If(a){}}Else{}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),If(BinaryOp(+,IntLit(4),IntLit(6)),Block([If(Id(a),Block([]))]),Block([])))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2)))])])'''
        self.assertTrue(TestAST.test(line, expect, 50))

    def test_51(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){Foreach (i In 1 .. 100 By 2){}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([])])])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2)))])])'''
        self.assertTrue(TestAST.test(line, expect, 51))

    def test_52(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){Foreach (i In 1 .. 100 By 2){a = 1 + 2;}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])])])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 52))

    def test_53(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){Foreach (i In 1 .. 100){}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),Block([])])])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 53))

    def test_54(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){Foreach (i In 1 .. 100){b = a +. b;}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),Block([AssignStmt(Id(b),BinaryOp(+.,Id(a),Id(b)))])])])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 54))

    def test_55(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){Return a+b;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 55))

    def test_56(self):
        line = '''Class Simple{Var a: Int = b+5;function(){Return a+b;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,Id(b),IntLit(5)))),MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 56))

    def test_57(self):
        line = '''Class Simple{block(){a = b+5;}function(){Return a+b;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(block),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(b),IntLit(5)))])),MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 57))

    def test_58(self):
        line = '''Class Simple{ta(){{a = b+5;}}function(){Return a+b;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(ta),Instance,[],Block([Block([AssignStmt(Id(a),BinaryOp(+,Id(b),IntLit(5)))])])),MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 58))

    def test_59(self):
        line = '''Class Simple{ta(a,b: String){{a = b+5;}}function(){Return a+b;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(ta),Instance,[param(Id(a),StringType),param(Id(b),StringType)],Block([Block([AssignStmt(Id(a),BinaryOp(+,Id(b),IntLit(5)))])])),MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 59))

    def test_60(self):
        line = '''Class Simple{ta(a,b: String){Var a,b: Array[Int,3] = 1+3,Array(2,5);}function(){Return a+b;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(ta),Instance,[param(Id(a),StringType),param(Id(b),StringType)],Block([VarDecl(Id(a),ArrayType(3,IntType),BinaryOp(+,IntLit(1),IntLit(3))),VarDecl(Id(b),ArrayType(3,IntType),[IntLit(2),IntLit(5)])])),MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 60))

    def test_61(self):
        line = '''Class Simple{ta(a,b: String){Var a,b: Array[Int,3] = Array(1,4),Array(2,5);}function(){Return a+b;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(ta),Instance,[param(Id(a),StringType),param(Id(b),StringType)],Block([VarDecl(Id(a),ArrayType(3,IntType),[IntLit(1),IntLit(4)]),VarDecl(Id(b),ArrayType(3,IntType),[IntLit(2),IntLit(5)])])),MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 61))

    def test_62(self):
        line = '''Class Simple{ta(a,b: String){a = b[1][2][3+4];}function(){Return a+b;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(ta),Instance,[param(Id(a),StringType),param(Id(b),StringType)],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(1),IntLit(2),BinaryOp(+,IntLit(3),IntLit(4))]))])),MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 62))

    def test_63(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,$b: Int =1+Self.a, 2;ta(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),FieldAccess(Self(),Id(a))))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(2))),MethodDecl(Id(ta),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2)))])])'''
        self.assertTrue(TestAST.test(line, expect, 63))

    def test_64(self):
        line = '''Class Simple{ta(a,b: String){a = b[1][2][3+4];}function(){a.y = 1/4;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(ta),Instance,[param(Id(a),StringType),param(Id(b),StringType)],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(1),IntLit(2),BinaryOp(+,IntLit(3),IntLit(4))]))])),MethodDecl(Id(function),Instance,[],Block([AssignStmt(FieldAccess(Id(a),Id(y)),BinaryOp(/,IntLit(1),IntLit(4)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 64))

    def test_65(self):
        line = '''Class Simple{ta(a,b: String;t,h: Int){a = b[1][2][3+4];}function(){a.y = 1/4;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(ta),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(t),IntType),param(Id(h),IntType)],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(1),IntLit(2),BinaryOp(+,IntLit(3),IntLit(4))]))])),MethodDecl(Id(function),Instance,[],Block([AssignStmt(FieldAccess(Id(a),Id(y)),BinaryOp(/,IntLit(1),IntLit(4)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 65))

    def test_66(self):
        line = '''Class Simple{ta(a,b: String;t,h: Int){Val x, y: Int = 1, 6;}}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(ta),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(t),IntType),param(Id(h),IntType)],Block([ConstDecl(Id(x),IntType,IntLit(1)),ConstDecl(Id(y),IntType,IntLit(6))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 66))

    def test_67(self):
        line = '''Class a { Val x : a = New a();}'''
        expect = '''Program([ClassDecl(Id(a),[AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(a)),NewExpr(Id(a),[])))])])'''
        self.assertTrue(TestAST.test(line, expect, 67))

    def test_68(self):
        line = '''Class name { Var tada: Array[Int,0112] = Array(2,3);}'''
        expect = '''Program([ClassDecl(Id(name),[AttributeDecl(Instance,VarDecl(Id(tada),ArrayType(74,IntType),[IntLit(2),IntLit(3)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 68))

    def test_69(self):
        line = '''Class daylaclass { name(x,c:Int; a,b:Boolean){}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(x),IntType),param(Id(c),IntType),param(Id(a),BoolType),param(Id(b),BoolType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 69))

    def test_70(self):
        line = '''Class daylaclass {name(a,b:Float){Var x: Int = 2+3*4-(4+1);}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([VarDecl(Id(x),IntType,BinaryOp(-,BinaryOp(+,IntLit(2),BinaryOp(*,IntLit(3),IntLit(4))),BinaryOp(+,IntLit(4),IntLit(1))))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 70))

    def test_71(self):
        line = '''Class daylaclass {name(a,b:Float){Foreach (i In 1 .. 1+2){}}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([For(Id(i),IntLit(1),BinaryOp(+,IntLit(1),IntLit(2)),Block([])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 71))

    def test_72(self):
        line = '''Class daylaclass {name(a,b:Float){Foreach (i In 1 .. 1+2 By 1){}}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([For(Id(i),IntLit(1),BinaryOp(+,IntLit(1),IntLit(2)),IntLit(1),Block([])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 72))

    def test_73(self):
        line = '''Class daylaclass {name(a,b:Float){Foreach (i In 1 .. 1+2 By 1){Return;}}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([For(Id(i),IntLit(1),BinaryOp(+,IntLit(1),IntLit(2)),IntLit(1),Block([Return()])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 73))

    def test_74(self):
        line = '''Class daylaclass {name(a,b:Float){Foreach (i In 1 .. 1+2 By 1){Return;Break; If(1+1){}}}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([For(Id(i),IntLit(1),BinaryOp(+,IntLit(1),IntLit(2)),IntLit(1),Block([Return(),Break,If(BinaryOp(+,IntLit(1),IntLit(1)),Block([]))])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 74))

    def test_75(self):
        line = '''Class daylaclass {name(a,b:Float){Foreach (i In 1 .. 1+2 By 1){a = a + 4 - 5 + (3+7);}}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([For(Id(i),IntLit(1),BinaryOp(+,IntLit(1),IntLit(2)),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(+,Id(a),IntLit(4)),IntLit(5)),BinaryOp(+,IntLit(3),IntLit(7))))])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 75))

    def test_76(self):
        line = '''Class daylaclass {name(a,b:Float){a = "tham" +. "lam";}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([AssignStmt(Id(a),BinaryOp(+.,StringLit(tham),StringLit(lam)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 76))

    def test_77(self):
        line = '''Class daylaclass {name(a,b:Float){Val a,b,c: Int = 0b101,0123,53;}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([ConstDecl(Id(a),IntType,IntLit(5)),ConstDecl(Id(b),IntType,IntLit(83)),ConstDecl(Id(c),IntType,IntLit(53))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 77))

    def test_78(self):
        line = '''Class daylaclass {name(a,b:Float){Val a,b,c: Int = 0b101+12,0123,53;}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(5),IntLit(12))),ConstDecl(Id(b),IntType,IntLit(83)),ConstDecl(Id(c),IntType,IntLit(53))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 78))

    def test_79(self):
        line = '''Class daylaclass {name(a,b:Float){Val a,b,c: Int = 0b101+12,0123,53;If(a>b){Continue;}}}'''
        expect = '''Program([ClassDecl(Id(daylaclass),[MethodDecl(Id(name),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(5),IntLit(12))),ConstDecl(Id(b),IntType,IntLit(83)),ConstDecl(Id(c),IntType,IntLit(53)),If(BinaryOp(>,Id(a),Id(b)),Block([Continue]))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 79))

    def test_80(self):
        line = '''Class a { Val x : a = New a();}'''
        expect = '''Program([ClassDecl(Id(a),[AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(a)),NewExpr(Id(a),[])))])])'''
        self.assertTrue(TestAST.test(line, expect, 80))

    def test_81(self):
        line = '''Class Program { main() { }}'''
        expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 81))

    def test_82(self):
        line = '''Class vas { x(a:Int){a.b = 2;}}'''
        expect = '''Program([ClassDecl(Id(vas),[MethodDecl(Id(x),Instance,[param(Id(a),IntType)],Block([AssignStmt(FieldAccess(Id(a),Id(b)),IntLit(2))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 82))

    def test_83(self):
        line = '''Class Prograsm { maisn() {x = New a(x,y,2);}}'''
        expect = '''Program([ClassDecl(Id(Prograsm),[MethodDecl(Id(maisn),Instance,[],Block([AssignStmt(Id(x),NewExpr(Id(a),[Id(x),Id(y),IntLit(2)]))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 83))

    def test_84(self):
        line = '''Class ns { Val $y,x,a: Float = 1.62,.3E-7,1.4e2;}'''
        expect = '''Program([ClassDecl(Id(ns),[AttributeDecl(Static,ConstDecl(Id($y),FloatType,FloatLit(1.62))),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,FloatLit(3e-08))),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(140.0)))])])'''
        self.assertTrue(TestAST.test(line, expect, 84))

    def test_85(self):
        line = '''Class v { Var d : s = New x(5,2,"text");}'''
        expect = '''Program([ClassDecl(Id(v),[AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(s)),NewExpr(Id(x),[IntLit(5),IntLit(2),StringLit(text)])))])])'''
        self.assertTrue(TestAST.test(line, expect, 85))

    def test_86(self):
        line = '''Class vas { name(vari:Boolean){b::$_w.l.i = 2;}}'''
        expect = '''Program([ClassDecl(Id(vas),[MethodDecl(Id(name),Instance,[param(Id(vari),BoolType)],Block([AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(b),Id($_w)),Id(l)),Id(i)),IntLit(2))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 86))

    def test_87(self):
        line = '''Class x { Val $a,x : x = New n(2),New n(23);}'''
        expect = '''Program([ClassDecl(Id(x),[AttributeDecl(Static,ConstDecl(Id($a),ClassType(Id(x)),NewExpr(Id(n),[IntLit(2)]))),AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(x)),NewExpr(Id(n),[IntLit(23)])))])])'''
        self.assertTrue(TestAST.test(line, expect, 87))

    def test_88(self):
        line = ''' Class vas { x(a,b:Int){x = 2 *3;}}'''
        expect = '''Program([ClassDecl(Id(vas),[MethodDecl(Id(x),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(x),BinaryOp(*,IntLit(2),IntLit(3)))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 88))

    def test_89(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: Int =New X(a+b) + Self.ID() + 3 || ((1---4) > 5),a[1][2] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,BinaryOp(+,NewExpr(Id(X),[BinaryOp(+,Id(a),Id(b))]),CallExpr(Self(),Id(ID),[])),IntLit(3)),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 89))

    def test_90(self):
        line = '''Class Simple{Val $Shape: Int;Var a,b_thanh: Int = Self.ID() + 3 || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,None)),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(||,BinaryOp(+,CallExpr(Self(),Id(ID),[]),IntLit(3)),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b_thanh),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 90))

    def test_91(self):
        line = '''Class Simple{Val $Shape: Int = 3;Var a,b: String = "string1" || a == b, a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(==,BinaryOp(||,StringLit(string1),Id(a)),Id(b)))),AttributeDecl(Instance,VarDecl(Id(b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 91))

    def test_92(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Return; Break; Continue;}}Var a,b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Return(),Break,Continue]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 92))

    def test_93(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){a = 1+a; If(a+b){}}}Var a,b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),Id(a))),If(BinaryOp(+,Id(a),Id(b)),Block([]))]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Instance,VarDecl(Id(b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 93))

    def test_94(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2];}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 94))

    def test_95(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 95))

    def test_96(self):
        line = '''Class Simple{Val $Shape,ta: Int = 3,9;function(){If(a>b){Break; Continue;}Else{If(1+2){}}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),AttributeDecl(Instance,ConstDecl(Id(ta),IntType,IntLit(9))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),Block([If(BinaryOp(+,IntLit(1),IntLit(2)),Block([]))]))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 96))

    def test_97(self):
        line = '''Class Simple{function(){If(a>b){Break; Continue;}Elseif(1+2){If(1+2){}}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2];}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),If(BinaryOp(+,IntLit(1),IntLit(2)),Block([If(BinaryOp(+,IntLit(1),IntLit(2)),Block([]))])))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 97))

    def test_98(self):
        line = '''Class Simple{Val $Shape: Int = 3;function(){If(a>b){Break; Continue;}Elseif(1+2){a = 1;}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2];}'''
        expect = '''Program([ClassDecl(Id(Simple),[AttributeDecl(Static,ConstDecl(Id($Shape),IntType,IntLit(3))),MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Break,Continue]),If(BinaryOp(+,IntLit(1),IntLit(2)),Block([AssignStmt(Id(a),IntLit(1))])))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 98))

    def test_99(self):
        line = '''Class Simple{function(){If(a>b){}Elseif(1+2){a = 1;}Else{}}Var a,$b: String= "string1" || ((1---4) > 5), a[1][a[3+4]] + 2;gloat(a,b:Int){a = 1+2;}$staticfun(){}Destructor(){}}Class Simple2{Val a,_tb: Float = 1.4,4.2;Var x: Array[Array[Int,0b1010],2] = Array(Array(1,2,3),Array(0x123A,0b101,042));}'''
        expect = '''Program([ClassDecl(Id(Simple),[MethodDecl(Id(function),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([]),If(BinaryOp(+,IntLit(1),IntLit(2)),Block([AssignStmt(Id(a),IntLit(1))]),Block([])))])),AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(||,StringLit(string1),BinaryOp(>,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(4)))),IntLit(5))))),AttributeDecl(Static,VarDecl(Id($b),StringType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[BinaryOp(+,IntLit(3),IntLit(4))])]),IntLit(2)))),MethodDecl(Id(gloat),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),IntLit(2)))])),MethodDecl(Id($staticfun),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Simple2),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(_tb),FloatType,FloatLit(4.2))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(2,ArrayType(10,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4666),IntLit(5),IntLit(34)]]))])])'''
        self.assertTrue(TestAST.test(line, expect, 99))
