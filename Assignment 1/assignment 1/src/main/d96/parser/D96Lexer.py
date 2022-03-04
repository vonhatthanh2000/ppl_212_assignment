# Generated from main/d96/parser/D96.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u030f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\5!\u0176\n!\3!\3!\3!\3!\7!\u017c\n!\f")
        buf.write("!\16!\u017f\13!\3\"\3\"\3\"\3\"\3\"\6\"\u0186\n\"\r\"")
        buf.write("\16\"\u0187\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\7\65\u01ba\n\65\f\65\16\65\u01bd")
        buf.write("\13\65\3\66\3\66\3\66\3\66\5\66\u01c3\n\66\3\66\3\66\3")
        buf.write("\67\3\67\3\67\5\67\u01ca\n\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u01d0\n\67\7\67\u01d2\n\67\f\67\16\67\u01d5\13\67\38")
        buf.write("\38\38\38\58\u01db\n8\38\38\38\38\58\u01e1\n8\78\u01e3")
        buf.write("\n8\f8\168\u01e6\138\39\39\39\39\59\u01ec\n9\39\39\39")
        buf.write("\39\59\u01f2\n9\79\u01f4\n9\f9\169\u01f7\139\3:\3:\3:")
        buf.write("\5:\u01fc\n:\3:\3:\3:\3:\5:\u0202\n:\7:\u0204\n:\f:\16")
        buf.write(":\u0207\13:\5:\u0209\n:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3?\3@\3@\3@\3@\3@\3@\5@\u021c\n@\3@\3@\3@\5@\u0221\n")
        buf.write("@\3A\3A\3B\3B\7B\u0227\nB\fB\16B\u022a\13B\3C\3C\5C\u022e")
        buf.write("\nC\3C\6C\u0231\nC\rC\16C\u0232\3D\3D\3D\3D\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\3D\5D\u0244\nD\3E\3E\3E\3E\5E\u024a")
        buf.write("\nE\3F\3F\7F\u024e\nF\fF\16F\u0251\13F\3F\3F\3F\3G\3G")
        buf.write("\7G\u0258\nG\fG\16G\u025b\13G\3G\3G\3G\3G\3G\3H\3H\7H")
        buf.write("\u0264\nH\fH\16H\u0267\13H\3H\3H\3I\3I\3I\3I\5I\u026f")
        buf.write("\nI\3J\3J\3J\3J\3J\5J\u0276\nJ\3J\3J\3K\3K\3K\3K\3K\5")
        buf.write("K\u027f\nK\3K\3K\3L\3L\3L\3L\5L\u0287\nL\3L\3L\5L\u028b")
        buf.write("\nL\3L\3L\3M\3M\3M\3M\3M\5M\u0294\nM\3M\3M\3N\3N\3N\3")
        buf.write("N\5N\u029c\nN\3O\3O\3O\3O\5O\u02a2\nO\3P\3P\3P\5P\u02a7")
        buf.write("\nP\3P\3P\5P\u02ab\nP\3Q\3Q\3Q\3Q\5Q\u02b1\nQ\3R\3R\3")
        buf.write("R\3R\3R\3S\3S\3S\3S\5S\u02bc\nS\3T\3T\3T\3T\7T\u02c2\n")
        buf.write("T\fT\16T\u02c5\13T\3U\3U\3U\3U\7U\u02cb\nU\fU\16U\u02ce")
        buf.write("\13U\3V\3V\3V\3V\7V\u02d4\nV\fV\16V\u02d7\13V\3W\3W\3")
        buf.write("W\3W\7W\u02dd\nW\fW\16W\u02e0\13W\3X\3X\3Y\3Y\3Z\3Z\3")
        buf.write("[\3[\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3`\3a\3a\3b\3b\3")
        buf.write("c\3c\3c\3c\7c\u02fd\nc\fc\16c\u0300\13c\3c\3c\3c\3c\3")
        buf.write("c\3d\6d\u0308\nd\rd\16d\u0309\3d\3d\3e\3e\3\u02fe\2f\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\2=\2?\2A\37C E!G\"I#K$M%O&")
        buf.write("Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\2o\2q\2s\2u\2")
        buf.write("w\2y\2{\2}\65\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\66\u008d\67\u008f8\u00919\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3:\u00a5")
        buf.write("\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af;\u00b1<\u00b3")
        buf.write("=\u00b5>\u00b7?\u00b9@\u00bbA\u00bdB\u00bfC\u00c1D\u00c3")
        buf.write("E\u00c5F\u00c7G\u00c9H\3\2\22\3\2c|\3\2C\\\3\2\63;\3\2")
        buf.write("\62;\3\2\639\4\2ZZzz\4\2\63;CH\4\2DDdd\3\2\62\63\4\2\62")
        buf.write(";CH\3\2\629\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^")
        buf.write("cdhhppttvv\5\2\n\f\16\17\"\"\2\u0333\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2}\3\2\2\2\2\u008b\3\2")
        buf.write("\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2")
        buf.write("\u00a3\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1")
        buf.write("\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2")
        buf.write("\2\2\u00c9\3\2\2\2\3\u00cb\3\2\2\2\5\u00d0\3\2\2\2\7\u00d2")
        buf.write("\3\2\2\2\t\u00d4\3\2\2\2\13\u00dc\3\2\2\2\r\u00e2\3\2")
        buf.write("\2\2\17\u00eb\3\2\2\2\21\u00ee\3\2\2\2\23\u00f5\3\2\2")
        buf.write("\2\25\u00fa\3\2\2\2\27\u0102\3\2\2\2\31\u0108\3\2\2\2")
        buf.write("\33\u010b\3\2\2\2\35\u010f\3\2\2\2\37\u0115\3\2\2\2!\u011d")
        buf.write("\3\2\2\2#\u0124\3\2\2\2%\u012b\3\2\2\2\'\u0130\3\2\2\2")
        buf.write(")\u0136\3\2\2\2+\u013a\3\2\2\2-\u013e\3\2\2\2/\u0143\3")
        buf.write("\2\2\2\61\u014f\3\2\2\2\63\u015a\3\2\2\2\65\u015e\3\2")
        buf.write("\2\2\67\u0161\3\2\2\29\u0166\3\2\2\2;\u016c\3\2\2\2=\u016e")
        buf.write("\3\2\2\2?\u0170\3\2\2\2A\u0175\3\2\2\2C\u0180\3\2\2\2")
        buf.write("E\u0189\3\2\2\2G\u018b\3\2\2\2I\u018d\3\2\2\2K\u018f\3")
        buf.write("\2\2\2M\u0191\3\2\2\2O\u0193\3\2\2\2Q\u0195\3\2\2\2S\u0198")
        buf.write("\3\2\2\2U\u019b\3\2\2\2W\u019f\3\2\2\2Y\u01a2\3\2\2\2")
        buf.write("[\u01a5\3\2\2\2]\u01a7\3\2\2\2_\u01aa\3\2\2\2a\u01ac\3")
        buf.write("\2\2\2c\u01af\3\2\2\2e\u01b1\3\2\2\2g\u01b4\3\2\2\2i\u01b7")
        buf.write("\3\2\2\2k\u01c2\3\2\2\2m\u01c6\3\2\2\2o\u01d6\3\2\2\2")
        buf.write("q\u01e7\3\2\2\2s\u0208\3\2\2\2u\u020a\3\2\2\2w\u020c\3")
        buf.write("\2\2\2y\u020e\3\2\2\2{\u0210\3\2\2\2}\u0212\3\2\2\2\177")
        buf.write("\u0220\3\2\2\2\u0081\u0222\3\2\2\2\u0083\u0224\3\2\2\2")
        buf.write("\u0085\u022b\3\2\2\2\u0087\u0243\3\2\2\2\u0089\u0249\3")
        buf.write("\2\2\2\u008b\u024b\3\2\2\2\u008d\u0255\3\2\2\2\u008f\u0261")
        buf.write("\3\2\2\2\u0091\u026e\3\2\2\2\u0093\u0270\3\2\2\2\u0095")
        buf.write("\u0279\3\2\2\2\u0097\u0282\3\2\2\2\u0099\u028e\3\2\2\2")
        buf.write("\u009b\u029b\3\2\2\2\u009d\u02a1\3\2\2\2\u009f\u02aa\3")
        buf.write("\2\2\2\u00a1\u02b0\3\2\2\2\u00a3\u02b2\3\2\2\2\u00a5\u02bb")
        buf.write("\3\2\2\2\u00a7\u02bd\3\2\2\2\u00a9\u02c6\3\2\2\2\u00ab")
        buf.write("\u02cf\3\2\2\2\u00ad\u02d8\3\2\2\2\u00af\u02e1\3\2\2\2")
        buf.write("\u00b1\u02e3\3\2\2\2\u00b3\u02e5\3\2\2\2\u00b5\u02e7\3")
        buf.write("\2\2\2\u00b7\u02e9\3\2\2\2\u00b9\u02eb\3\2\2\2\u00bb\u02ed")
        buf.write("\3\2\2\2\u00bd\u02ef\3\2\2\2\u00bf\u02f1\3\2\2\2\u00c1")
        buf.write("\u02f4\3\2\2\2\u00c3\u02f6\3\2\2\2\u00c5\u02f8\3\2\2\2")
        buf.write("\u00c7\u0307\3\2\2\2\u00c9\u030d\3\2\2\2\u00cb\u00cc\7")
        buf.write("o\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\4\3\2\2\2\u00d0\u00d1\5\65\33\2\u00d1\6")
        buf.write("\3\2\2\2\u00d2\u00d3\5#\22\2\u00d3\b\3\2\2\2\u00d4\u00d5")
        buf.write("\7R\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7i\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7o\2\2\u00db\n\3\2\2\2\u00dc\u00dd\7D\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7m\2\2\u00e1\f\3\2\2\2\u00e2\u00e3\7E\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\16\3\2\2\2\u00eb\u00ec\7K\2\2\u00ec\u00ed")
        buf.write("\7h\2\2\u00ed\20\3\2\2\2\u00ee\u00ef\7G\2\2\u00ef\u00f0")
        buf.write("\7n\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7h\2\2\u00f4\22\3\2\2\2\u00f5\u00f6")
        buf.write("\7G\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9")
        buf.write("\7g\2\2\u00f9\24\3\2\2\2\u00fa\u00fb\7H\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7e\2\2\u0100\u0101\7j\2\2\u0101\26")
        buf.write("\3\2\2\2\u0102\u0103\7C\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7t\2\2\u0105\u0106\7c\2\2\u0106\u0107\7{\2\2\u0107\30")
        buf.write("\3\2\2\2\u0108\u0109\7K\2\2\u0109\u010a\7p\2\2\u010a\32")
        buf.write("\3\2\2\2\u010b\u010c\7K\2\2\u010c\u010d\7p\2\2\u010d\u010e")
        buf.write("\7v\2\2\u010e\34\3\2\2\2\u010f\u0110\7H\2\2\u0110\u0111")
        buf.write("\7n\2\2\u0111\u0112\7q\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7v\2\2\u0114\36\3\2\2\2\u0115\u0116\7D\2\2\u0116\u0117")
        buf.write("\7q\2\2\u0117\u0118\7q\2\2\u0118\u0119\7n\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\u011b\7c\2\2\u011b\u011c\7p\2\2\u011c \3")
        buf.write("\2\2\2\u011d\u011e\7U\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7t\2\2\u0120\u0121\7k\2\2\u0121\u0122\7p\2\2\u0122\u0123")
        buf.write("\7i\2\2\u0123\"\3\2\2\2\u0124\u0125\7T\2\2\u0125\u0126")
        buf.write("\7g\2\2\u0126\u0127\7v\2\2\u0127\u0128\7w\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129\u012a\7p\2\2\u012a$\3\2\2\2\u012b\u012c")
        buf.write("\7P\2\2\u012c\u012d\7w\2\2\u012d\u012e\7n\2\2\u012e\u012f")
        buf.write("\7n\2\2\u012f&\3\2\2\2\u0130\u0131\7E\2\2\u0131\u0132")
        buf.write("\7n\2\2\u0132\u0133\7c\2\2\u0133\u0134\7u\2\2\u0134\u0135")
        buf.write("\7u\2\2\u0135(\3\2\2\2\u0136\u0137\7X\2\2\u0137\u0138")
        buf.write("\7c\2\2\u0138\u0139\7n\2\2\u0139*\3\2\2\2\u013a\u013b")
        buf.write("\7X\2\2\u013b\u013c\7c\2\2\u013c\u013d\7t\2\2\u013d,\3")
        buf.write("\2\2\2\u013e\u013f\7U\2\2\u013f\u0140\7g\2\2\u0140\u0141")
        buf.write("\7n\2\2\u0141\u0142\7h\2\2\u0142.\3\2\2\2\u0143\u0144")
        buf.write("\7E\2\2\u0144\u0145\7q\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7u\2\2\u0147\u0148\7v\2\2\u0148\u0149\7t\2\2\u0149\u014a")
        buf.write("\7w\2\2\u014a\u014b\7e\2\2\u014b\u014c\7v\2\2\u014c\u014d")
        buf.write("\7q\2\2\u014d\u014e\7t\2\2\u014e\60\3\2\2\2\u014f\u0150")
        buf.write("\7F\2\2\u0150\u0151\7g\2\2\u0151\u0152\7u\2\2\u0152\u0153")
        buf.write("\7v\2\2\u0153\u0154\7t\2\2\u0154\u0155\7w\2\2\u0155\u0156")
        buf.write("\7e\2\2\u0156\u0157\7v\2\2\u0157\u0158\7q\2\2\u0158\u0159")
        buf.write("\7t\2\2\u0159\62\3\2\2\2\u015a\u015b\7P\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c\u015d\7y\2\2\u015d\64\3\2\2\2\u015e\u015f")
        buf.write("\7D\2\2\u015f\u0160\7{\2\2\u0160\66\3\2\2\2\u0161\u0162")
        buf.write("\7V\2\2\u0162\u0163\7t\2\2\u0163\u0164\7w\2\2\u0164\u0165")
        buf.write("\7g\2\2\u01658\3\2\2\2\u0166\u0167\7H\2\2\u0167\u0168")
        buf.write("\7c\2\2\u0168\u0169\7n\2\2\u0169\u016a\7u\2\2\u016a\u016b")
        buf.write("\7g\2\2\u016b:\3\2\2\2\u016c\u016d\t\2\2\2\u016d<\3\2")
        buf.write("\2\2\u016e\u016f\t\3\2\2\u016f>\3\2\2\2\u0170\u0171\7")
        buf.write("a\2\2\u0171@\3\2\2\2\u0172\u0176\5;\36\2\u0173\u0176\5")
        buf.write("=\37\2\u0174\u0176\5? \2\u0175\u0172\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0175\u0174\3\2\2\2\u0176\u017d\3\2\2\2\u0177")
        buf.write("\u017c\5;\36\2\u0178\u017c\5=\37\2\u0179\u017c\5? \2\u017a")
        buf.write("\u017c\5{>\2\u017b\u0177\3\2\2\2\u017b\u0178\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2")
        buf.write("\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017eB\3\2\2")
        buf.write("\2\u017f\u017d\3\2\2\2\u0180\u0185\7&\2\2\u0181\u0186")
        buf.write("\5;\36\2\u0182\u0186\5=\37\2\u0183\u0186\5? \2\u0184\u0186")
        buf.write("\5{>\2\u0185\u0181\3\2\2\2\u0185\u0182\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188D\3\2\2\2\u0189")
        buf.write("\u018a\7-\2\2\u018aF\3\2\2\2\u018b\u018c\7/\2\2\u018c")
        buf.write("H\3\2\2\2\u018d\u018e\7,\2\2\u018eJ\3\2\2\2\u018f\u0190")
        buf.write("\7\61\2\2\u0190L\3\2\2\2\u0191\u0192\7\'\2\2\u0192N\3")
        buf.write("\2\2\2\u0193\u0194\7#\2\2\u0194P\3\2\2\2\u0195\u0196\7")
        buf.write("(\2\2\u0196\u0197\7(\2\2\u0197R\3\2\2\2\u0198\u0199\7")
        buf.write("~\2\2\u0199\u019a\7~\2\2\u019aT\3\2\2\2\u019b\u019c\7")
        buf.write("?\2\2\u019c\u019d\7?\2\2\u019d\u019e\7\60\2\2\u019eV\3")
        buf.write("\2\2\2\u019f\u01a0\7-\2\2\u01a0\u01a1\7\60\2\2\u01a1X")
        buf.write("\3\2\2\2\u01a2\u01a3\7?\2\2\u01a3\u01a4\7?\2\2\u01a4Z")
        buf.write("\3\2\2\2\u01a5\u01a6\7?\2\2\u01a6\\\3\2\2\2\u01a7\u01a8")
        buf.write("\7#\2\2\u01a8\u01a9\7?\2\2\u01a9^\3\2\2\2\u01aa\u01ab")
        buf.write("\7>\2\2\u01ab`\3\2\2\2\u01ac\u01ad\7>\2\2\u01ad\u01ae")
        buf.write("\7?\2\2\u01aeb\3\2\2\2\u01af\u01b0\7@\2\2\u01b0d\3\2\2")
        buf.write("\2\u01b1\u01b2\7@\2\2\u01b2\u01b3\7?\2\2\u01b3f\3\2\2")
        buf.write("\2\u01b4\u01b5\7<\2\2\u01b5\u01b6\7<\2\2\u01b6h\3\2\2")
        buf.write("\2\u01b7\u01bb\t\4\2\2\u01b8\u01ba\t\5\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bcj\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01c3\5m\67\2\u01bf\u01c3\5o8\2\u01c0\u01c3\5q9\2\u01c1")
        buf.write("\u01c3\5s:\2\u01c2\u01be\3\2\2\2\u01c2\u01bf\3\2\2\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c5\b\66\2\2\u01c5l\3\2\2\2\u01c6\u01c7\7\62")
        buf.write("\2\2\u01c7\u01d3\t\6\2\2\u01c8\u01ca\5? \2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write("\u01cf\5y=\2\u01cc\u01cd\5? \2\u01cd\u01ce\5y=\2\u01ce")
        buf.write("\u01d0\3\2\2\2\u01cf\u01cc\3\2\2\2\u01cf\u01d0\3\2\2\2")
        buf.write("\u01d0\u01d2\3\2\2\2\u01d1\u01c9\3\2\2\2\u01d2\u01d5\3")
        buf.write("\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4n")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\7\62\2\2\u01d7")
        buf.write("\u01d8\t\7\2\2\u01d8\u01e4\t\b\2\2\u01d9\u01db\5? \2\u01da")
        buf.write("\u01d9\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\3\2\2\2")
        buf.write("\u01dc\u01e0\5w<\2\u01dd\u01de\5? \2\u01de\u01df\5w<\2")
        buf.write("\u01df\u01e1\3\2\2\2\u01e0\u01dd\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01da\3\2\2\2\u01e3\u01e6")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("p\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\7\62\2\2\u01e8")
        buf.write("\u01e9\t\t\2\2\u01e9\u01f5\7\63\2\2\u01ea\u01ec\5? \2")
        buf.write("\u01eb\u01ea\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ed\3")
        buf.write("\2\2\2\u01ed\u01f1\5u;\2\u01ee\u01ef\5? \2\u01ef\u01f0")
        buf.write("\5u;\2\u01f0\u01f2\3\2\2\2\u01f1\u01ee\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01eb\3\2\2\2\u01f4")
        buf.write("\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6r\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u0209\7\62\2")
        buf.write("\2\u01f9\u0205\t\4\2\2\u01fa\u01fc\5? \2\u01fb\u01fa\3")
        buf.write("\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u0201")
        buf.write("\5{>\2\u01fe\u01ff\5? \2\u01ff\u0200\5{>\2\u0200\u0202")
        buf.write("\3\2\2\2\u0201\u01fe\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("\u0204\3\2\2\2\u0203\u01fb\3\2\2\2\u0204\u0207\3\2\2\2")
        buf.write("\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0209\3")
        buf.write("\2\2\2\u0207\u0205\3\2\2\2\u0208\u01f8\3\2\2\2\u0208\u01f9")
        buf.write("\3\2\2\2\u0209t\3\2\2\2\u020a\u020b\t\n\2\2\u020bv\3\2")
        buf.write("\2\2\u020c\u020d\t\13\2\2\u020dx\3\2\2\2\u020e\u020f\t")
        buf.write("\f\2\2\u020fz\3\2\2\2\u0210\u0211\t\5\2\2\u0211|\3\2\2")
        buf.write("\2\u0212\u0213\5\177@\2\u0213\u0214\b?\3\2\u0214~\3\2")
        buf.write("\2\2\u0215\u021b\5\u0081A\2\u0216\u021c\5\u0083B\2\u0217")
        buf.write("\u021c\5\u0085C\2\u0218\u0219\5\u0083B\2\u0219\u021a\5")
        buf.write("\u0085C\2\u021a\u021c\3\2\2\2\u021b\u0216\3\2\2\2\u021b")
        buf.write("\u0217\3\2\2\2\u021b\u0218\3\2\2\2\u021c\u0221\3\2\2\2")
        buf.write("\u021d\u021e\5\u0083B\2\u021e\u021f\5\u0085C\2\u021f\u0221")
        buf.write("\3\2\2\2\u0220\u0215\3\2\2\2\u0220\u021d\3\2\2\2\u0221")
        buf.write("\u0080\3\2\2\2\u0222\u0223\5s:\2\u0223\u0082\3\2\2\2\u0224")
        buf.write("\u0228\5\u00bd_\2\u0225\u0227\5{>\2\u0226\u0225\3\2\2")
        buf.write("\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229")
        buf.write("\3\2\2\2\u0229\u0084\3\2\2\2\u022a\u0228\3\2\2\2\u022b")
        buf.write("\u022d\t\r\2\2\u022c\u022e\t\16\2\2\u022d\u022c\3\2\2")
        buf.write("\2\u022d\u022e\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u0231")
        buf.write("\5{>\2\u0230\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0230")
        buf.write("\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0086\3\2\2\2\u0234")
        buf.write("\u0235\7^\2\2\u0235\u0244\7)\2\2\u0236\u0237\7^\2\2\u0237")
        buf.write("\u0244\7^\2\2\u0238\u0239\7^\2\2\u0239\u0244\7d\2\2\u023a")
        buf.write("\u023b\7^\2\2\u023b\u0244\7h\2\2\u023c\u023d\7^\2\2\u023d")
        buf.write("\u0244\7p\2\2\u023e\u023f\7^\2\2\u023f\u0244\7t\2\2\u0240")
        buf.write("\u0241\7^\2\2\u0241\u0244\7v\2\2\u0242\u0244\7)\2\2\u0243")
        buf.write("\u0234\3\2\2\2\u0243\u0236\3\2\2\2\u0243\u0238\3\2\2\2")
        buf.write("\u0243\u023a\3\2\2\2\u0243\u023c\3\2\2\2\u0243\u023e\3")
        buf.write("\2\2\2\u0243\u0240\3\2\2\2\u0243\u0242\3\2\2\2\u0244\u0088")
        buf.write("\3\2\2\2\u0245\u024a\n\17\2\2\u0246\u024a\5\u0087D\2\u0247")
        buf.write("\u0248\7)\2\2\u0248\u024a\7$\2\2\u0249\u0245\3\2\2\2\u0249")
        buf.write("\u0246\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u008a\3\2\2\2")
        buf.write("\u024b\u024f\7$\2\2\u024c\u024e\5\u0089E\2\u024d\u024c")
        buf.write("\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f")
        buf.write("\u0250\3\2\2\2\u0250\u0252\3\2\2\2\u0251\u024f\3\2\2\2")
        buf.write("\u0252\u0253\7$\2\2\u0253\u0254\bF\4\2\u0254\u008c\3\2")
        buf.write("\2\2\u0255\u0259\7$\2\2\u0256\u0258\5\u0089E\2\u0257\u0256")
        buf.write("\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2\2\u0259")
        buf.write("\u025a\3\2\2\2\u025a\u025c\3\2\2\2\u025b\u0259\3\2\2\2")
        buf.write("\u025c\u025d\7^\2\2\u025d\u025e\n\20\2\2\u025e\u025f\3")
        buf.write("\2\2\2\u025f\u0260\bG\5\2\u0260\u008e\3\2\2\2\u0261\u0265")
        buf.write("\7$\2\2\u0262\u0264\5\u0089E\2\u0263\u0262\3\2\2\2\u0264")
        buf.write("\u0267\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2")
        buf.write("\u0266\u0268\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u0269\b")
        buf.write("H\6\2\u0269\u0090\3\2\2\2\u026a\u026f\5\u0093J\2\u026b")
        buf.write("\u026f\5\u0095K\2\u026c\u026f\5\u0097L\2\u026d\u026f\5")
        buf.write("\u0099M\2\u026e\u026a\3\2\2\2\u026e\u026b\3\2\2\2\u026e")
        buf.write("\u026c\3\2\2\2\u026e\u026d\3\2\2\2\u026f\u0092\3\2\2\2")
        buf.write("\u0270\u0271\5\27\f\2\u0271\u0275\5\u00afX\2\u0272\u0273")
        buf.write("\5k\66\2\u0273\u0274\5\u009bN\2\u0274\u0276\3\2\2\2\u0275")
        buf.write("\u0272\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u0278\5\u00b1Y\2\u0278\u0094\3\2\2\2\u0279\u027a")
        buf.write("\5\27\f\2\u027a\u027e\5\u00afX\2\u027b\u027c\5}?\2\u027c")
        buf.write("\u027d\5\u009dO\2\u027d\u027f\3\2\2\2\u027e\u027b\3\2")
        buf.write("\2\2\u027e\u027f\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0281")
        buf.write("\5\u00b1Y\2\u0281\u0096\3\2\2\2\u0282\u0283\5\27\f\2\u0283")
        buf.write("\u028a\5\u00afX\2\u0284\u0287\5\67\34\2\u0285\u0287\5")
        buf.write("9\35\2\u0286\u0284\3\2\2\2\u0286\u0285\3\2\2\2\u0287\u0288")
        buf.write("\3\2\2\2\u0288\u0289\5\u009fP\2\u0289\u028b\3\2\2\2\u028a")
        buf.write("\u0286\3\2\2\2\u028a\u028b\3\2\2\2\u028b\u028c\3\2\2\2")
        buf.write("\u028c\u028d\5\u00b1Y\2\u028d\u0098\3\2\2\2\u028e\u028f")
        buf.write("\5\27\f\2\u028f\u0293\5\u00afX\2\u0290\u0291\5\u008bF")
        buf.write("\2\u0291\u0292\5\u00a1Q\2\u0292\u0294\3\2\2\2\u0293\u0290")
        buf.write("\3\2\2\2\u0293\u0294\3\2\2\2\u0294\u0295\3\2\2\2\u0295")
        buf.write("\u0296\5\u00b1Y\2\u0296\u009a\3\2\2\2\u0297\u0298\5\u00c1")
        buf.write("a\2\u0298\u0299\5k\66\2\u0299\u029a\5\u009bN\2\u029a\u029c")
        buf.write("\3\2\2\2\u029b\u0297\3\2\2\2\u029b\u029c\3\2\2\2\u029c")
        buf.write("\u009c\3\2\2\2\u029d\u029e\5\u00c1a\2\u029e\u029f\5}?")
        buf.write("\2\u029f\u02a0\5\u009dO\2\u02a0\u02a2\3\2\2\2\u02a1\u029d")
        buf.write("\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u009e\3\2\2\2\u02a3")
        buf.write("\u02a6\5\u00c1a\2\u02a4\u02a7\5\67\34\2\u02a5\u02a7\5")
        buf.write("9\35\2\u02a6\u02a4\3\2\2\2\u02a6\u02a5\3\2\2\2\u02a7\u02a8")
        buf.write("\3\2\2\2\u02a8\u02a9\5\u009fP\2\u02a9\u02ab\3\2\2\2\u02aa")
        buf.write("\u02a3\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab\u00a0\3\2\2\2")
        buf.write("\u02ac\u02ad\5\u00c1a\2\u02ad\u02ae\5\u008bF\2\u02ae\u02af")
        buf.write("\5\u00a1Q\2\u02af\u02b1\3\2\2\2\u02b0\u02ac\3\2\2\2\u02b0")
        buf.write("\u02b1\3\2\2\2\u02b1\u00a2\3\2\2\2\u02b2\u02b3\5\27\f")
        buf.write("\2\u02b3\u02b4\5\u00afX\2\u02b4\u02b5\5\u00a5S\2\u02b5")
        buf.write("\u02b6\5\u00b1Y\2\u02b6\u00a4\3\2\2\2\u02b7\u02bc\5\u00a7")
        buf.write("T\2\u02b8\u02bc\5\u00a9U\2\u02b9\u02bc\5\u00abV\2\u02ba")
        buf.write("\u02bc\5\u00adW\2\u02bb\u02b7\3\2\2\2\u02bb\u02b8\3\2")
        buf.write("\2\2\u02bb\u02b9\3\2\2\2\u02bb\u02ba\3\2\2\2\u02bc\u00a6")
        buf.write("\3\2\2\2\u02bd\u02c3\5\u0093J\2\u02be\u02bf\5\u00c1a\2")
        buf.write("\u02bf\u02c0\5\u0093J\2\u02c0\u02c2\3\2\2\2\u02c1\u02be")
        buf.write("\3\2\2\2\u02c2\u02c5\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c3")
        buf.write("\u02c4\3\2\2\2\u02c4\u00a8\3\2\2\2\u02c5\u02c3\3\2\2\2")
        buf.write("\u02c6\u02cc\5\u0095K\2\u02c7\u02c8\5\u00c1a\2\u02c8\u02c9")
        buf.write("\5\u0095K\2\u02c9\u02cb\3\2\2\2\u02ca\u02c7\3\2\2\2\u02cb")
        buf.write("\u02ce\3\2\2\2\u02cc\u02ca\3\2\2\2\u02cc\u02cd\3\2\2\2")
        buf.write("\u02cd\u00aa\3\2\2\2\u02ce\u02cc\3\2\2\2\u02cf\u02d5\5")
        buf.write("\u0097L\2\u02d0\u02d1\5\u00c1a\2\u02d1\u02d2\5\u0097L")
        buf.write("\2\u02d2\u02d4\3\2\2\2\u02d3\u02d0\3\2\2\2\u02d4\u02d7")
        buf.write("\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6")
        buf.write("\u00ac\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02de\5\u0099")
        buf.write("M\2\u02d9\u02da\5\u00c1a\2\u02da\u02db\5\u0099M\2\u02db")
        buf.write("\u02dd\3\2\2\2\u02dc\u02d9\3\2\2\2\u02dd\u02e0\3\2\2\2")
        buf.write("\u02de\u02dc\3\2\2\2\u02de\u02df\3\2\2\2\u02df\u00ae\3")
        buf.write("\2\2\2\u02e0\u02de\3\2\2\2\u02e1\u02e2\7*\2\2\u02e2\u00b0")
        buf.write("\3\2\2\2\u02e3\u02e4\7+\2\2\u02e4\u00b2\3\2\2\2\u02e5")
        buf.write("\u02e6\7}\2\2\u02e6\u00b4\3\2\2\2\u02e7\u02e8\7\177\2")
        buf.write("\2\u02e8\u00b6\3\2\2\2\u02e9\u02ea\7]\2\2\u02ea\u00b8")
        buf.write("\3\2\2\2\u02eb\u02ec\7_\2\2\u02ec\u00ba\3\2\2\2\u02ed")
        buf.write("\u02ee\7<\2\2\u02ee\u00bc\3\2\2\2\u02ef\u02f0\7\60\2\2")
        buf.write("\u02f0\u00be\3\2\2\2\u02f1\u02f2\7\60\2\2\u02f2\u02f3")
        buf.write("\7\60\2\2\u02f3\u00c0\3\2\2\2\u02f4\u02f5\7.\2\2\u02f5")
        buf.write("\u00c2\3\2\2\2\u02f6\u02f7\7=\2\2\u02f7\u00c4\3\2\2\2")
        buf.write("\u02f8\u02f9\7%\2\2\u02f9\u02fa\7%\2\2\u02fa\u02fe\3\2")
        buf.write("\2\2\u02fb\u02fd\13\2\2\2\u02fc\u02fb\3\2\2\2\u02fd\u0300")
        buf.write("\3\2\2\2\u02fe\u02ff\3\2\2\2\u02fe\u02fc\3\2\2\2\u02ff")
        buf.write("\u0301\3\2\2\2\u0300\u02fe\3\2\2\2\u0301\u0302\7%\2\2")
        buf.write("\u0302\u0303\7%\2\2\u0303\u0304\3\2\2\2\u0304\u0305\b")
        buf.write("c\7\2\u0305\u00c6\3\2\2\2\u0306\u0308\t\21\2\2\u0307\u0306")
        buf.write("\3\2\2\2\u0308\u0309\3\2\2\2\u0309\u0307\3\2\2\2\u0309")
        buf.write("\u030a\3\2\2\2\u030a\u030b\3\2\2\2\u030b\u030c\bd\7\2")
        buf.write("\u030c\u00c8\3\2\2\2\u030d\u030e\13\2\2\2\u030e\u00ca")
        buf.write("\3\2\2\2\63\2\u0175\u017b\u017d\u0185\u0187\u01bb\u01c2")
        buf.write("\u01c9\u01cf\u01d3\u01da\u01e0\u01e4\u01eb\u01f1\u01f5")
        buf.write("\u01fb\u0201\u0205\u0208\u021b\u0220\u0228\u022d\u0232")
        buf.write("\u0243\u0249\u024f\u0259\u0265\u026e\u0275\u027e\u0286")
        buf.write("\u028a\u0293\u029b\u02a1\u02a6\u02aa\u02b0\u02bb\u02c3")
        buf.write("\u02cc\u02d5\u02de\u02fe\u0309\b\3\66\2\3?\3\3F\4\3G\5")
        buf.write("\3H\6\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    By_keyword = 2
    Return_word = 3
    Program = 4
    BREAK = 5
    CONTINUE = 6
    IF = 7
    ELSEIF = 8
    ELSE = 9
    FOREACH = 10
    ARRAY = 11
    IN = 12
    INT = 13
    FLOAT = 14
    BOOLEAN = 15
    STRING = 16
    RETURN = 17
    NULL = 18
    CLASS = 19
    VAL = 20
    VAR = 21
    Self = 22
    CONSTRUCTOR = 23
    DESTRUCTOR = 24
    NEW = 25
    BY = 26
    TRUE = 27
    FALSE = 28
    ID = 29
    DO_ID = 30
    ADD = 31
    MINUS = 32
    PRODUCT = 33
    DIVIDE = 34
    MOD = 35
    NOT = 36
    AND = 37
    OR = 38
    COMPARE_STRING = 39
    ADD_STRING = 40
    EQUAL = 41
    ASSIGN = 42
    DIFFER = 43
    LESS = 44
    LESS_EQUAL = 45
    GREATER = 46
    GREATER_EQUAL = 47
    DOUBLE_COLON = 48
    NONZERO_INT = 49
    INT_LIT = 50
    FLOAT_LIT = 51
    STRING_LIT = 52
    ILLEGAL_ESCAPE = 53
    UNCLOSE_STRING = 54
    ARRAY_LIT = 55
    MUL_ARRAY = 56
    LB = 57
    RB = 58
    LP = 59
    RP = 60
    LS = 61
    RS = 62
    COLON = 63
    DOT = 64
    DOUBLE_DOT = 65
    CM = 66
    SEMI = 67
    COMMENT = 68
    WS = 69
    ERROR_CHAR = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Program'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Self'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'True'", "'False'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'==.'", "'+.'", "'=='", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "':'", "'.'", "'..'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "By_keyword", "Return_word", "Program", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", "IN", "INT", "FLOAT", 
            "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", 
            "Self", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "TRUE", "FALSE", 
            "ID", "DO_ID", "ADD", "MINUS", "PRODUCT", "DIVIDE", "MOD", "NOT", 
            "AND", "OR", "COMPARE_STRING", "ADD_STRING", "EQUAL", "ASSIGN", 
            "DIFFER", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
            "DOUBLE_COLON", "NONZERO_INT", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ARRAY_LIT", "MUL_ARRAY", 
            "LB", "RB", "LP", "RP", "LS", "RS", "COLON", "DOT", "DOUBLE_DOT", 
            "CM", "SEMI", "COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "By_keyword", "Return_word", "Program", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", 
                  "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                  "CLASS", "VAL", "VAR", "Self", "CONSTRUCTOR", "DESTRUCTOR", 
                  "NEW", "BY", "TRUE", "FALSE", "LOWERCASE", "UPPERCASE", 
                  "UNDERSCORE", "ID", "DO_ID", "ADD", "MINUS", "PRODUCT", 
                  "DIVIDE", "MOD", "NOT", "AND", "OR", "COMPARE_STRING", 
                  "ADD_STRING", "EQUAL", "ASSIGN", "DIFFER", "LESS", "LESS_EQUAL", 
                  "GREATER", "GREATER_EQUAL", "DOUBLE_COLON", "NONZERO_INT", 
                  "INT_LIT", "OCTAL", "HEXA", "BINARY", "DEC", "BINARY_DIGIT", 
                  "HEX_DIGIT", "OCTAL_DIGIT", "DIGIT", "FLOAT_LIT", "FLOAT_LIT_PART", 
                  "INT_PART", "DEC_PART", "EXP_PART", "ESCAPE_SEQUENCE", 
                  "CHAR_STRING", "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ARRAY_LIT", "ARRAY_INT", "ARRAY_FLOAT", "ARRAY_BOOLEAN", 
                  "ARRAY_STRING", "INT_LIST", "FLOAT_LIST", "BOOLEAN_LIST", 
                  "STRING_LIST", "MUL_ARRAY", "MUL_ARRAY_LIT", "MUL_ARRAY_INT", 
                  "MUL_ARRAY_FLOAT", "MUL_ARRAY_BOOLEAN", "MUL_ARRAY_STRING", 
                  "LB", "RB", "LP", "RP", "LS", "RS", "COLON", "DOT", "DOUBLE_DOT", 
                  "CM", "SEMI", "COMMENT", "WS", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.INT_LIT_action 
            actions[61] = self.FLOAT_LIT_action 
            actions[68] = self.STRING_LIT_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.strip('"')
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text.replace('"','',1)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace('"','',1)
     


