import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #   test comment
    def test_comment_1(self):
        """single line comment"""
        self.assertTrue(TestLexer.test("##this is comment##","<EOF>",101))
    def test_comment_2(self):
        """2 line comment"""
        self.assertTrue(TestLexer.test("##comment \n in 2 line##","<EOF>",102))
    def test_comment_3(self):
        """multiple line comment"""
        self.assertTrue(TestLexer.test("##comment \n in \n multiple \n line##","<EOF>",103))
    def test_comment_4(self):
        """error comment do not have ## at the end"""
        self.assertTrue(TestLexer.test("##comment \n in \n multiple \n line","Error Token #",104))
    def test_comment_5(self):
        """error comment, start with # in middle"""
        self.assertTrue(TestLexer.test("#comment \n in \n multiple \n line#","Error Token #",105))
    # test identifier
    def test_identifier_6(self):
        """all are lowercase"""
        self.assertTrue(TestLexer.test("lowercase","lowercase,<EOF>",106))
    def test_identifier_7(self):
        """all are UPPERCASE"""
        self.assertTrue(TestLexer.test("UPPERCASE","UPPERCASE,<EOF>",107))
    def test_identifier_8(self):
        """all are lowerUPPERcase"""
        self.assertTrue(TestLexer.test("lowerUPPERcase","lowerUPPERcase,<EOF>",108))
    def test_identifier_9(self):
        """all are lower22UPPE3Rcase"""
        self.assertTrue(TestLexer.test("lower22UPPE3Rcase","lower22UPPE3Rcase,<EOF>",109))
    def test_identifier_10(self):
        """start with _"""
        self.assertTrue(TestLexer.test("_identify","_identify,<EOF>",110))
    def test_identifier_11(self):
        """start with number"""
        self.assertTrue(TestLexer.test("13identify","13,identify,<EOF>",111))
    def test_identifier_12(self):
        """lower upper _ digit"""
        self.assertTrue(TestLexer.test("iAM_22","iAM_22,<EOF>",112))
    def test_identifier_13(self):
        """_ digit upper _ digit"""
        self.assertTrue(TestLexer.test("_123iAM_22","_123iAM_22,<EOF>",113))
    def test_identifier_14(self):
        """error """
        self.assertTrue(TestLexer.test("_123?iAM_22","_123,Error Token ?",114))
    def test_identifier_14(self):
        """error """
        self.assertTrue(TestLexer.test("_123?iAM_22","_123,Error Token ?",114))
    def test_identifier_15(self):
        """Escape """
        self.assertTrue(TestLexer.test("_123iAM_22\n","_123iAM_22,<EOF>",115))
    def test_do_identify_16(self):
        """do_idenfity start with _"""
        self.assertTrue(TestLexer.test("$_thanh22","$_thanh22,<EOF>",116))
    def test_do_identify_17(self):
        """do_idenfity but only $"""
        self.assertTrue(TestLexer.test("$","Error Token $",117))
    def test_do_identify_18(self):
        """do_idenfity start with number"""
        self.assertTrue(TestLexer.test("$123thanh","$123thanh,<EOF>",118))
    def test_do_identify_19(self):
        """do_idenfity _ upper lower"""
        self.assertTrue(TestLexer.test("$_Iam22","$_Iam22,<EOF>",119))
    def test_do_identify_20(self):
        """$ in the middle"""
        self.assertTrue(TestLexer.test("Iam$22","Iam,$22,<EOF>",120))
    def test_keyword_21(self):
        """some keyword"""
        self.assertTrue(TestLexer.test("Break Continue If Elseif Else Foreach True False","Break,Continue,If,Elseif,Else,Foreach,True,False,<EOF>",121))
    def test_keyword_22(self):
        """some keyword"""
        self.assertTrue(TestLexer.test("Array In Int Float Boolean String Return Null Class","Array,In,Int,Float,Boolean,String,Return,Null,Class,<EOF>",122))
    def test_keyword_23(self):
        """some keyword"""
        self.assertTrue(TestLexer.test("Val Var Self Constructor Destructor New By","Val,Var,Self,Constructor,Destructor,New,By,<EOF>",123))
    def test_keyword_24(self):
        """mix keyword with ID"""
        self.assertTrue(TestLexer.test("Int int $True True True123","Int,int,$True,True,True123,<EOF>",124))
    def test_keyword_25(self):
        """mix keyword with ID"""
        self.assertTrue(TestLexer.test("Int 123int $True True True123","Int,123,int,$True,True,True123,<EOF>",125))
    def test_keyword_26(self):
        """mix keyword with unknown"""
        self.assertTrue(TestLexer.test("Int?123","Int,Error Token ?",126))
    def test_keyword_27(self):
        """mix keyword with do identify"""
        self.assertTrue(TestLexer.test("Int$ta123","Int,$ta123,<EOF>",127))
    def test_operator_28(self):
        """int operator"""
        self.assertTrue(TestLexer.test("+-*/%==!=<><=>=","+,-,*,/,%,==,!=,<,>,<=,>=,<EOF>",128))  
    def test_operator_29(self):
        """float operator"""
        self.assertTrue(TestLexer.test("+-*/<><=>=","+,-,*,/,<,>,<=,>=,<EOF>",129))
    def test_operator_30(self):
        """boolean + string operator"""
        self.assertTrue(TestLexer.test("!&&||==.+.==!=","!,&&,||,==.,+.,==,!=,<EOF>",130))
    def test_seperator_31(self):
        """seperator"""
        self.assertTrue(TestLexer.test("()[].;:{},","(,),[,],.,;,:,{,},,,<EOF>",131))
    def test_seperator_32(self):
        """seperator with error"""
        self.assertTrue(TestLexer.test("()[]@.;:{},","(,),[,],Error Token @",132))
    def test_literal_33(self):
        """Integer"""
        self.assertTrue(TestLexer.test("0","0,<EOF>",133))
    def test_literal_34(self):
        """Integer begin with 0 but not octal"""
        self.assertTrue(TestLexer.test("08","0,8,<EOF>",134))
    def test_literal_35(self):
        """Octal begin with nonzero"""
        self.assertTrue(TestLexer.test("06475","06475,<EOF>",135))
    def test_literal_36(self):
        """Octal begin with zero"""
        self.assertTrue(TestLexer.test("006475","0,06475,<EOF>",136))
    def test_literal_37(self):
        """Hexa"""
        self.assertTrue(TestLexer.test("0x1256AD","0x1256AD,<EOF>",137))        
    def test_literal_38(self):
        """Hexa but with lowercase"""
        self.assertTrue(TestLexer.test("0x1256ad","0x1256,ad,<EOF>",138))        
    def test_literal_39(self):
        """Hexa but with _"""
        self.assertTrue(TestLexer.test("0X1256_AD","0X1256AD,<EOF>",139))        
    def test_literal_40(self):
        """Binary"""
        self.assertTrue(TestLexer.test("0b01001","0,b01001,<EOF>",140))        
    def test_literal_41(self):
        """Binary with 2"""
        self.assertTrue(TestLexer.test("0b012001","0,b012001,<EOF>",141))
    def test_literal_42(self):
        """litteral but have _ in the middle"""
        self.assertTrue(TestLexer.test("123_1123","1231123,<EOF>",142))
    def test_literal_43(self):
        """litteral but have multiple _ in the middle"""
        self.assertTrue(TestLexer.test("123__1123","123,__1123,<EOF>",143))   
    def test_literal_44(self):
        """float number"""
        self.assertTrue(TestLexer.test("1.234","1.234,<EOF>",144))   
    def test_literal_45(self):
        """float number"""
        self.assertTrue(TestLexer.test("1.3e4","1.3e4,<EOF>",145))   
    def test_literal_46(self):
        """float number"""
        self.assertTrue(TestLexer.test("8E-12","8E-12,<EOF>",146))
    def test_literal_47(self):
        """float number"""
        self.assertTrue(TestLexer.test("8E.-12","8,E,.,-,12,<EOF>",147))
    def test_literal_48(self):
        """float number"""
        self.assertTrue(TestLexer.test("8E.12","8,E,.,12,<EOF>",148))
    def test_literal_49(self):
        """float number"""
        self.assertTrue(TestLexer.test("123_412.1234","123412.1234,<EOF>",149))
    def test_boolean_50(self):
        """boolean"""
        self.assertTrue(TestLexer.test("the boolean can be True or False","the,boolean,can,be,True,or,False,<EOF>",150))
    def test_combine_51(self):
        """"""
        self.assertTrue(TestLexer.test("0X12BD3 1231 0b123 0b0101","0X12BD3,1231,0b1,23,0,b0101,<EOF>",151))
    def test_combine_52(self):
        """"""
        self.assertTrue(TestLexer.test("0X12BH3 123_1 0b_123 0b0101","0X12B,H3,1231,0,b_123,0,b0101,<EOF>",152))
    def test_combine_53(self):
        """"""
        self.assertTrue(TestLexer.test("0X12BH3 123_1 0_b123 0b0101","0X12B,H3,1231,0,_b123,0,b0101,<EOF>",153))                         
    def test_wrong_hex_54(self):
        """"""
        self.assertTrue(TestLexer.test("1x123AB","1,x123AB,<EOF>",154))                         
    def test_wrong_oct_55(self):
        """"""
        self.assertTrue(TestLexer.test("0p13","0,p13,<EOF>",155))        
    def test_float_56(self):
        """float with only dot"""
        self.assertTrue(TestLexer.test("14.","14.,<EOF>",156))        
    def test_float_57(self):
        """float with only dot and exp"""
        self.assertTrue(TestLexer.test("14.e+20","14.e+20,<EOF>",157))        
    def test_float_58(self):
        """float with all zero"""
        self.assertTrue(TestLexer.test("000.00e-00","0,0,0.00e-00,<EOF>",158))        
    def test_float_59(self):
        """float with all zero"""
        self.assertTrue(TestLexer.test("0.00e-00","0.00e-00,<EOF>",159))        
    def test_expression_60(self):
        """"""
        self.assertTrue(TestLexer.test("Val Number = 3","Val,Number,=,3,<EOF>",160))        
    def test_expression_61(self):
        """"""
        self.assertTrue(TestLexer.test("Var $Number = 3","Var,$Number,=,3,<EOF>",161))        
    def test_expression_62(self):
        """"""
        self.assertTrue(TestLexer.test("Var $Number, num_ber = 3, axs","Var,$Number,,,num_ber,=,3,,,axs,<EOF>",162))        
    def test_expression_63(self):
        """random"""
        self.assertTrue(TestLexer.test("abc + 00 >= 12 + 6","abc,+,0,0,>=,12,+,6,<EOF>",163)) 
    def test_string_64(self):
        """"""
        self.assertTrue(TestLexer.test('"just a normal string"',"just a normal string,<EOF>",164)) 
    def test_string_65(self):
        """"""
        self.assertTrue(TestLexer.test("just a normal string","just,a,normal,string,<EOF>",165)) 
    def test_string_66(self):
        """"""
        self.assertTrue(TestLexer.test('"She asks: \'"What time is it?\'" "','She asks: \'"What time is it?\'" ,<EOF>',166))       
    def test_string_67(self):
        """escape string"""
        self.assertTrue(TestLexer.test('" String \\n 123ha \\f \\n"',' String \\n 123ha \\f \\n,<EOF>',167))       
    def test_string_68(self):
        """complicated '" """
        self.assertTrue(TestLexer.test('" String1 \'" Inside \'" with the quote \'" "',' String1 \'" Inside \'" with the quote \'" ,<EOF>',168))
    def test_string_69(self):
        """String but not ending with " """
        self.assertTrue(TestLexer.test('" Error String','Unclosed String:  Error String',169))
    def test_string_70(self):
        """String but not begining with " """
        self.assertTrue(TestLexer.test('Error String"','Error,String,Unclosed String: ',170))
    def test_string_71(self):
        """Combine 2 string """
        self.assertTrue(TestLexer.test('"String 1" "String 2"','String 1,String 2,<EOF>',171))
    def test_string_72(self):
        """Combine with one empty string """
        self.assertTrue(TestLexer.test('"" "String 2"',',String 2,<EOF>',172))
    def test_string_73(self):
        """Combine string with other type """
        self.assertTrue(TestLexer.test('{123"tada"}','{,123,tada,},<EOF>',173))
    def test_string_74(self):
        """Combine string with other type """
        self.assertTrue(TestLexer.test('" 123 "123ab##ppl##"string"',' 123 ,123,ab,string,<EOF>',174))
    def test_string_75(self):
        """Multiple with unclosed string """
        self.assertTrue(TestLexer.test('"String \n line 2','Unclosed String: String ',175))
    def test_array_76(self):
        """Simple Array """
        self.assertTrue(TestLexer.test('Array(1,5,7,2)','Array(1,5,7,2),<EOF>',176))
    def test_array_77(self):
        """Array but with different element"""
        self.assertTrue(TestLexer.test('Array(1,5.2,7,2)','Array,(,1,,,5.2,,,7,,,2,),<EOF>',177))
    def test_array_78(self):
        """Array with float"""
        self.assertTrue(TestLexer.test('Array(1.3,5.2,7.8,2.4)','Array(1.3,5.2,7.8,2.4),<EOF>',178))
    def test_array_79(self):
        """Array with float and string"""
        self.assertTrue(TestLexer.test('Array(1.3,5.2,"7.8",2.4)','Array,(,1.3,,,5.2,,,7.8,,,2.4,),<EOF>',179))
    def test_array_80(self):
        """Array with all string"""
        self.assertTrue(TestLexer.test('Array("ABC","DEF","GHI","LMN")','Array("ABC","DEF","GHI","LMN"),<EOF>',180))
    def test_array_81(self):
        """Multiple Array """
        self.assertTrue(TestLexer.test('Array(Array(1,2,3),Array(4,5,6))','Array(Array(1,2,3),Array(4,5,6)),<EOF>',181))
    def test_array_82(self):
        """Multiple Array with different element"""
        self.assertTrue(TestLexer.test('Array(Array(1,2,3),Array("4",5,6))','Array,(,Array(1,2,3),,,Array,(,4,,,5,,,6,),),<EOF>',182))
    def test_array_83(self):
        """Multiple Array with different element"""
        self.assertTrue(TestLexer.test('Array(Array(True,False),Array(False,False))','Array(Array(True,False),Array(False,False)),<EOF>',183))
    def test_array_84(self):
        """Multiple Array with different element"""
        self.assertTrue(TestLexer.test('Array(Array(True,123),Array(False,456))','Array,(,Array,(,True,,,123,),,,Array,(,False,,,456,),),<EOF>',184))
    def test_array_85(self):
        """Multiple Array with different number"""
        self.assertTrue(TestLexer.test('Array(Array(125,123),Array(13))','Array(Array(125,123),Array(13)),<EOF>',185))
    def test_combine_86(self):
        """Add library"""
        self.assertTrue(TestLexer.test('#import <math.h>','Error Token #',186))
    def test_combine_87(self):
        """Variable assessment"""
        self.assertTrue(TestLexer.test('Var x = 1.2','Var,x,=,1.2,<EOF>',187))
    def test_combine_88(self):
        """Class declaration"""
        self.assertTrue(TestLexer.test('Class Area: Circle','Class,Area,:,Circle,<EOF>',188))
    def test_combine_89(self):
        """Static attribute"""
        self.assertTrue(TestLexer.test('Shape::$length','Shape,::,$length,<EOF>',189))
    def test_combine_90(self):
        """return"""
        self.assertTrue(TestLexer.test('Return Self.area + Self.volume','Return,Self,.,area,+,Self,.,volume,<EOF>',190))
    def test_combine_91(self):
        """function call"""
        self.assertTrue(TestLexer.test('Function: func() a[3]','Function,:,func,(,),a,[,3,],<EOF>',191))
    def test_combine_92(self):
        """[]"""
        self.assertTrue(TestLexer.test('[1][2][4]','[,1,],[,2,],[,4,],<EOF>',192))
    def test_combine_93(self):
        """number with weird format"""
        self.assertTrue(TestLexer.test('42e12ab__te','42e12,ab__te,<EOF>',193))
    def test_combine_94(self):
        """space"""
        self.assertTrue(TestLexer.test('   \n \t \n \t','<EOF>',194))
    def test_combine_95(self):
        """float with double dot"""
        self.assertTrue(TestLexer.test('3..12','3.,.,12,<EOF>',195))
    def test_combine_96(self):
        """combine all literal"""
        self.assertTrue(TestLexer.test('3 is Int, True is Boolean?','3,is,Int,,,True,is,Boolean,Error Token ?',196))
    def test_combine_97(self):
        """array sub"""
        self.assertTrue(TestLexer.test('a[1+func(5)]','a,[,1,+,func,(,5,),],<EOF>',197))
    def test_combine_98(self):
        """random"""
        self.assertTrue(TestLexer.test('1.x=420.4e+5','1.,x,=,420.4e+5,<EOF>',198))
    def test_combine_99(self):
        """combine 2 string with one unclosed"""
        self.assertTrue(TestLexer.test('"String 1 "String 2"','String 1 ,String,2,Unclosed String: ',199))
    def test_combine_100(self):
        """weird comment"""
        self.assertTrue(TestLexer.test('## ## #','Error Token #',200))