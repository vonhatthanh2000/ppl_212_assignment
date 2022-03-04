import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_0(self):
        input = """
        Class main{}
        
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 0))

    def test_1(self):
        input = """
        Class Shape: Circle {
            circle(){
                Return Self.radius * pi;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1))

    def test_2(self):
        input = """
        Class Test{
            add_number(){
                a = 1+2+3;
            }
        }
        
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 2))

    def test_3(self):
        input = """
        Class Test{
            $getnumber(){
                Return Self.length + Self.width;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 3))

    def test_4(self):
        input = """
        Class Test{
            $getnumber(){
                Return Self.length + Self.width;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 4))

    def test_5(self):
        input = """
        Class Test{
            Var Shape: String = "12312";
            Val width: Int = 3;
            Var Area, Volume: Int;
            getWidth(){
                Return width;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 5))

    def test_6(self):
        input = """
        Class main{
            Constructor(){
            Return;
        }
        }
        """
        expect = 'Error on line 4 col 12: Return'
        self.assertTrue(TestParser.test(input, expect, 6))

    def test_7(self):
        input = """
        Class Test{
            Var Shape: String = "12312";
            Val width: Float = 3.23 + 4;
            Var Area, Volume: Int;
            getWidth(){
                Return width;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 7))

    def test_8(self):
        input = """
        Class Test{
            Var Shape: String = "12312";
            Val width: Float = 3.23 + 4;
            Var Area, Volume: Int;
            getWidth(x,y,z:Int){
                Return width;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 8))

    def test_9(self):
        input = """
        Class Test{
            Var Shape: String = "12312";
            Val width: Float = 3.23 + 4;
            Var Area, Volume: Int;
            getWidth(x,y,z:Int;__a,$b:String){
                Return width;
            }
        }
        Class Program{
            main(){

            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 9))

    def test_10(self):
        input = """
        Class Test{
            Var Shape: String = "12312";
            Val width: Float = 3.23 + 4;
            Var Area, Volume: Int;
            getWidth(x,y,z:Int;__a,$b:String){
                Return width;
            }
            Constructor(){

            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 10))

    def test_11(self):
        input = """
        Class Test{
            Var Shape: String = "12312";
            Val width: Float = 3.23 + 4;
            Var Area, Volume: Int;
            getWidth(x,y,z:Int;__a,$b:String){
                Return width;
            }
            Constructor(){
                Var $amilo: Boolean = 1>2<3;
            }
        }
        """
        expect = 'Error on line 10 col 20: $amilo'
        self.assertTrue(TestParser.test(input, expect, 11))

    def test_12(self):
        input = """
        Class Test{
            Var Shape: Array[Float,0b1010];
            Val width: Float = 3.23 + 4;
            Var Area, Volume: Int;
            getWidth(x,y,z:Int;__a,$b:String){
                Return width;
            }
            Constructor(){
                Var amilo: Boolean = 3+4*4;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 12))

    def test_13(self):
        input = """
        Class Test{
            Var Shape: Array[Float,0b1010];
            Val width: Float = 3.23 + 4;
            Var Area, Volume: Int;
            getWidth(x,y__,z:Int;__a,c_23:String){
                Return width;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 13))

    def test_14(self):
        input = """
        Class Test{
            Var Shape: Array[Float,0b1010];
            Val width: Float = New hi(12+3,7+2);
            Var Area, Volume: Int;
            getWidth(x,y__,z:Int;__a,c_23:String){
                Return width;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 14))

    def test_15(self):
        input = """
        Class Test{
            Var Shape: Array[Float,0b1010];
            Val width: Float = 3.23 + 4;
            Var Area, Volume: Int;
            getWidth(x,y__,z:Int;__a,c_23:String){
                Return Self.length + 24;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 15))

    def test_16(self):
        input = """
        Class Test{
            Var Shape: Array[Float,0b1010];
            Val width: Float = 3.23 + x[2+3];
            Var Area, Volume: Int;
            getWidth(x,y__,z:Int;__a,c_23:String){
                Return Self.length + 24;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 16))

    def test_17(self):
        input = """
        Class Test{
            Var Shape: Array[Float,0b1010];
            Val width: Float = 3.23 + x[2+3];
            Var Area, Volume: Int = New a();
            getWidth(x,y__,z:Int;__a,c_23:String){
                Return Self.length + 24;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 17))

    def test_18(self):
        input = """
        Class Program{
            main(){
                s = r * r * a;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 18))

    def test_19(self):
        input = """
        Class Program{
            main(){
                s = New a(a12,_hi);
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 19))

    def test_20(self):
        input = """
        Class Program{
            main(){
                s = New a(12+8,_hi);
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 20))

    def test_21(self):
        input = """
        Class Program{
            Var $num1: $class = New abs(ab,12+7);
            main(){
                s = New a(12+8,_hi);
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 21))

    def test_22(self):
        input = """
        Class Program{
            main(){
                Var $num1: $class = New abs(ab,12+7);
                s = New a(12+8,_hi);
            }
        }
        """
        expect = 'Error on line 4 col 20: $num1'
        self.assertTrue(TestParser.test(input, expect, 22))

    def test_23(self):
        input = """
        Class Program{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(){
                s = New a(12+8,_hi);
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 23))

    def test_24(self):
        input = """
        Class Program{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(){
                s = New a(12+8,_hi);
                x = ar[1][3];
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 24))

    def test_25(self):
        input = """
        Class Program{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(){
                s = New a(12+8,_hi);
                x = ar[1][3];
                Return a;
            }
        }
        """
        expect = 'Error on line 7 col 16: Return'
        self.assertTrue(TestParser.test(input, expect, 25))

    def test_26(self):
        input = """
        Class Shape{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            Circle(a:String, b:Int){
                s = New a(12+8,_hi);
                x = ar[1][3];
                ta = Out.print(6);
                Return a;
            }
        }
        """
        expect = 'Error on line 4 col 27: ,'
        self.assertTrue(TestParser.test(input, expect, 26))

    def test_27(self):
        input = """
        Class Shape{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            Circle(a:String; b:Int){
                s = New a(12+8,_hi);
                x = ar[1][3];
                ta = Out.print(6);
                Return a;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 27))

    def test_28(self):
        input = """
        Class Shape{
            Var $num1: Array[Int;9] = New abs(ab,12+7);
            Circle(a:String; b:Int){
                Return a;
            }
        }
        """
        expect = 'Error on line 3 col 32: ;'
        self.assertTrue(TestParser.test(input, expect, 28))

    def test_29(self):
        input = """
        Class Program{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(a:Int){
                s = New a(12+8,_hi);
                x = ar[1][3];
            }
        }
        """
        expect = 'Error on line 4 col 17: a'
        self.assertTrue(TestParser.test(input, expect, 29))

    def test_30(self):
        input = """
        Class Program{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(){
                s = New a(12+8,_hi);
                Val $a: Float = 3.14;
            }
        }
        """
        expect = 'Error on line 6 col 20: $a'
        self.assertTrue(TestParser.test(input, expect, 30))

    def test_31(self):
        input = """
        Class Program{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(){
                s = New a(12+8,_hi);
                Val a: Float = 3.14;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 31))

    def test_32(self):
        input = """
        Class Program{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(){
                s = New a(12+8,_hi);
                Val a: Float = 3..1;
            }
        }
        """
        expect = 'Error on line 6 col 33: .'
        self.assertTrue(TestParser.test(input, expect, 32))

    def test_33(self):
        input = """
        Class class1: class2{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 33))

    def test_34(self):
        input = """
        Class class1: class2:{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
        }
        """
        expect = 'Error on line 2 col 28: :'
        self.assertTrue(TestParser.test(input, expect, 34))

    def test_35(self):
        input = """
        Class class1: class2{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(){
                a = $abc + abc;
            }
        }
        """
        expect = 'Error on line 5 col 20: $abc'
        self.assertTrue(TestParser.test(input, expect, 35))

    def test_36(self):
        input = """
        Class class1: class2{
            Var $num1: Array[Int,9] = New abs(ab,12+7);
            main(){
                a = a::$abc + abc;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 36))

    def test_37(self):
        input = """
        Class class1{
            Var $num1,num2,num3: Array[Int,9] = New abs(ab,12+7);
            main(){
                a = a::$abc + abc;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 37))

    def test_38(self):
        input = """
        Class class1{
            Var $num1,num2,num3: Array[Int,9] = New abs(ab,12+7);
            main(){
                a = a::$abc + abc.abc;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 38))

    def test_39(self):
        input = """
        Class class1{
            Var $num1,num2,num3: Array[Int,9] = New abs(ab,12+7);
            main(){
                a = a::$abc.a() + abc.abc;
            }
        }
        """
        expect = 'Error on line 5 col 27: .'
        self.assertTrue(TestParser.test(input, expect, 39))

    def test_40(self):
        input = """
        Class class1{
            Var $num1,num2,num3: Array[Int,9] = New abs(ab,12+7);
            main(){
                a = a::$abc + abc.abc.a();
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 40))

    def test_41(self):
        input = """
        Class class1{
            Var 8cas2: Int;
            main(){
                a = a::$abc + abc.abc.a();
            }
        }
        """
        expect = 'Error on line 3 col 16: 8'
        self.assertTrue(TestParser.test(input, expect, 41))

    def test_42(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                a = a::$abc + abc.abc.a();
                If(a<b){
                    a = a + b;
                }
                Else{
                    Return a;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 42))

    def test_43(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                a = a::$abc + abc.abc.a();
                If(a<b){
                    a = a + b;
                }
                Else{
                    Return a;
                
            }
        }
        """
        expect = 'Error on line 14 col 8: <EOF>'
        self.assertTrue(TestParser.test(input, expect, 43))

    def test_44(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                a = a::$abc + abc.abc.a();
                If(a<b){
                    a = a + b;
                }
                Else{
                    Return a
                }       
            }
        }
        """
        expect = 'Error on line 11 col 16: }'
        self.assertTrue(TestParser.test(input, expect, 44))

    def test_45(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                a = a::$abc + abc.abc.a();
                Foreach (abc In 1 .. 10 By 2){
                    a = a + b;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 45))

    def test_46(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                a = a::$abc + abc.abc;
                Foreach (abc In 1+2 .. 10*2 By 2+2){
                    a = a + b;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 46))

    def test_47(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                a = a::$abc + abc.abc.a();
                Foreach (abc In 1+2 .. 10*2){
                    a = a + b;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 47))

    def test_48(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                a = a::$abc + abc.abc.a();
                Foreach (abc In 1+2 .. 10*2){
                    a = a + b;
                    Break;
                    Continue;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 48))

    def test_49(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                Continue;
                a = a::$abc + abc.abc.a();
                Foreach (abc In 1+2 .. 10*2){
                    a = a + b;
                    Break;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 49))

    def test_50(self):
        input = """
        Class class1{
            Var cas2: Int;
            Continue;
            main(){
                a = a::$abc + abc.abc.a();
                Foreach (abc In 1+2 .. 10*2){
                    a = a + b;
                    Break;
                }
            }
        }
        """
        expect = 'Error on line 4 col 12: Continue'
        self.assertTrue(TestParser.test(input, expect, 50))

    def test_51(self):
        input = """
        Class class1{
            Var cas2: Int;
            main(){
                a = a::$abc && abc.abc.a();
                Foreach (abc In 1+2 .. 10*2){
                    a = a || b;
                    Break;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 51))

    def test_52(self):
        input = """
        Class class1{
            Var !cas2: Int;
            main(){
                a = a::$abc && abc.abc.a();
            }
        }
        """
        expect = 'Error on line 3 col 16: !'
        self.assertTrue(TestParser.test(input, expect, 52))

    def test_53(self):
        input = """
        Class class1{
            Var (cas2: Int);
            main(){
                a = a::$abc && abc.abc.a();
            }
        }
        """
        expect = 'Error on line 3 col 16: ('
        self.assertTrue(TestParser.test(input, expect, 53))

    def test_54(self):
        input = """
        Class class1{
            Var cas2: Int;
            ##This is comment but error
            main(){
                a = a::$abc && abc.abc.a();
            }
        }
        """
        expect = '#'
        self.assertTrue(TestParser.test(input, expect, 54))

    def test_55(self):
        input = """
        Class class1{
            Var cas2: Int;
            ##This is comment but not error##
            main(){
                a = a::$abc && abc.abc.a();
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 55))

    def test_56(self):
        input = """
        Class class1{
            Var cas2,__asd_2: Int = 123_42e12;
            main(){
                a = a::$abc && abc.abc.a();
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 56))

    def test_57(self):
        input = """
        Class class1{
            Var cas2,__asd_2: Int == 123_42e12;
            main(){
                a = a::$abc && abc.abc.a();
            }
        }
        """
        expect = 'Error on line 3 col 34: =='
        self.assertTrue(TestParser.test(input, expect, 57))

    def test_58(self):
        input = """
        Class Program{
            main(){
                a = 7*2 + ab[1][2];
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 58))

    def test_59(self):
        input = """
        Clas Program{
            main(){
                a = 7*2 + ab[1][2];
            }
        }
        """
        expect = 'Error on line 2 col 8: Clas'
        self.assertTrue(TestParser.test(input, expect, 59))

    def test_60(self):
        input = """
        Class Class{
            main(){
                a = 7*2 + ab[1][2];
            }
        }
        """
        expect = 'Error on line 2 col 14: Class'
        self.assertTrue(TestParser.test(input, expect, 60))

    def test_61(self):
        input = """
        Class If{
            main(){
                a = 7*2 + ab[1][2];
            }
        }
        """
        expect = 'Error on line 2 col 14: If'
        self.assertTrue(TestParser.test(input, expect, 61))

    def test_62(self):
        input = """
        Class Test{
            main(){
                {}{}{}
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 62))

    def test_63(self):
        input = """
        Class Test{
            main(){
                {}{Break;}{}{Continue;}{}
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 63))

    def test_64(self):
        input = """
        Class Test{
            main(){
                {}Break;{}Continue;{}
            }
        }
        """
        expect = 'Error on line 4 col 18: Break'
        self.assertTrue(TestParser.test(input, expect, 64))

    def test_65(self):
        input = """
        Class Test{
            main(){
                {}{Break;{}}Continue;{}
            }
        }
        """
        expect = 'Error on line 4 col 28: Continue'
        self.assertTrue(TestParser.test(input, expect, 65))

    def test_66(self):
        input = """
        Class Test{
            abd(number:Int=8){
                Return a;
            }
        }
        """
        expect = 'Error on line 3 col 26: ='
        self.assertTrue(TestParser.test(input, expect, 66))

    def test_67(self):
        input = """
        Class Test{
            Destructor(number:Int=8){
                a = a + b;
            }
        }
        """
        expect = 'Error on line 3 col 23: number'
        self.assertTrue(TestParser.test(input, expect, 67))

    def test_68(self):
        input = """
        Class Test{
            Destructor(){
                a = a + b;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 68))

    def test_69(self):
        input = """
        Class Test{
            Destructor(){
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 69))

    def test_70(self):
        input = """
        Class Test{
            Destructor(){
                Return a + b;
            }
        }
        """
        expect = 'Error on line 4 col 16: Return'
        self.assertTrue(TestParser.test(input, expect, 70))

    def test_71(self):
        input = """
        Class Test{
            Var test: Boolean = a || b;
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 71))

    def test_72(self):
        input = """
        Class Test{
            Var test: Boolean = a ! b;
        }
        """
        expect = 'Error on line 3 col 34: !'
        self.assertTrue(TestParser.test(input, expect, 72))

    def test_73(self):
        input = """
        Class Test{
            Var test: Boolean = a < b ;
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 73))

    def test_74(self):
        input = """
        Class Test{
            Var string: STRING = "ASCAS" +. "TASD";
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 74))

    def test_75(self):
        input = """
        Class Test{
            Var string: STRING = "ASCAS" ==. "TASD";
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 75))

    def test_76(self):
        input = """
        Class Test{
            Var string: STRING = "ASCAS" + "TASD";
        }
        """
        expect = 'Error on line 3 col 41: +'
        self.assertTrue(TestParser.test(input, expect, 76))

    def test_77(self):
        input = """
        Class Test{
            test(){
                Foreach (a In 1+2 .. 120/5){
                    ABD.Printout();
                    Continue;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 77))

    def test_78(self):
        input = """
        Class Test{
            test(){
                Foreach (a In 1+2 .. 120.12/5){
                    ABD.Printout();
                    Continue;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 78))

    def test_79(self):
        input = """
        Class Test{
            test(){
                Foreach (a In 1+2 .. 120.12/5){
                    ABD.Printout();
                    NOTKEY;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 79))

    def test_80(self):
        input = """
        Class Test{
            test(){
                Var s,b: Int;
                r=2.0;
                Var a,b: Array[Int,5];
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 80))

    def test_81(self):
        input = """
        Class Test{
            test(){
                s = r*r+Self.Pi+a.a.a();
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 81))

    def test_82(self):
        input = """
        Class Test{
            test(){
                Self.x = t * $a;
            }
        }
        """
        expect = 'Error on line 4 col 29: $a'
        self.assertTrue(TestParser.test(input, expect, 82))

    def test_83(self):
        input = """
        Class Test::$tada{
            test(){
                Self.x = t * a;
            }
        }
        """
        expect = 'Error on line 2 col 18: ::'
        self.assertTrue(TestParser.test(input, expect, 83))

    def test_84(self):
        input = """
        Class Test{
            $tada(){
                Self.x = t * a;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 84))

    def test_85(self):
        input = """
        Class Test{
            $tada(){
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 85))

    def test_86(self):
        input = """
        Class Test{
            $tada(){
                Out.printInt(Shape::numOfShape);
            }
        }
        """
        expect = 'Error on line 4 col 36: numOfShape'
        self.assertTrue(TestParser.test(input, expect, 86))

    def test_87(self):
        input = """
        Class Test{
            $tada(){
                Out.printInt(Shape.$numOfShape);
            }
        }
        """
        expect = 'Error on line 4 col 35: $numOfShape'
        self.assertTrue(TestParser.test(input, expect, 87))

    def test_88(self):
        input = """
        Class Test{
            $tada(){
                Return a*b;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 88))

    def test_89(self):
        input = """
        Class main{}
        Class Program(){
            main(){}
        }
        """
        expect = 'Error on line 3 col 21: ('
        self.assertTrue(TestParser.test(input, expect, 89))

    def test_90(self):
        input = """
        Class main{}
        Class Program{
            main(){}
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 90))

    def test_91(self):
        input = """
        Class Test{
            $tada(){
                Return Self.abd +3;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 91))

    def test_92(self):
        input = """
        Class Test{
            $tada(){
                Return Self.If +3;
            }
        }
        """
        expect = 'Error on line 4 col 28: If'
        self.assertTrue(TestParser.test(input, expect, 92))

    def test_93(self):
        input = """
        Class Test{
            $tada(x,y,z){
                Return Self.id +3;
            }
        }
        """
        expect = 'Error on line 3 col 23: )'
        self.assertTrue(TestParser.test(input, expect, 93))

    def test_94(self):
        input = """
        Class Test{
            $tada(){
                Return -3+1+4;
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 94))

    def test_95(self):
        input = """
        Class Test{
            $tada(){
                Return +3+1+4;
            }
        }
        """
        expect = 'Error on line 4 col 23: +'
        self.assertTrue(TestParser.test(input, expect, 95))

    def test_96(self):
        input = """
        Class Test{
            $tada(){
                Return 3+.1+4;
            }
        }
        """
        expect = 'Error on line 4 col 24: +.'
        self.assertTrue(TestParser.test(input, expect, 96))

    def test_97(self):
        input = """
        Class Test{
            $tada(){
                If(a+b){
                    a = a +b;
                }
                Elseif(a>b){
                    a = a / b;
                }
                Else{
                    b = b - a;
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 97))

    def test_98(self):
        input = """
        Class Test{
            $tada(){
                If(a+b){
                    a = a +b;
                }
                Elseif(){
                    a = a / b;
                }
                Else{
                    b = b - a;
                }
            }
        }
        """
        expect = 'Error on line 7 col 23: )'
        self.assertTrue(TestParser.test(input, expect, 98))

    def test_99(self):
        input = """
        Class Test{
            $tada(){
                If(a+b){
                    a = a +b;
                }
                Elseif(a>b){
                    a = a > (B + a)/a + New a();
                }
                Else{
                    
                }
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 99))

