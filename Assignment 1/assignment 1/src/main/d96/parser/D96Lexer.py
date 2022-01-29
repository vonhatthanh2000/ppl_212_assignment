# Generated from main/d96/parser/D96.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\5!\u0178\n!\3!\3!\3!\3!\7!\u017e\n!\f")
        buf.write("!\16!\u0181\13!\3\"\3\"\3\"\3\"\3\"\6\"\u0188\n\"\r\"")
        buf.write("\16\"\u0189\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\7\65\u01bc\n\65\f\65\16\65\u01bf")
        buf.write("\13\65\3\66\3\66\3\66\3\66\5\66\u01c5\n\66\3\66\3\66\3")
        buf.write("\67\3\67\3\67\5\67\u01cc\n\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u01d2\n\67\7\67\u01d4\n\67\f\67\16\67\u01d7\13\67\38")
        buf.write("\38\38\38\58\u01dd\n8\38\38\38\38\58\u01e3\n8\78\u01e5")
        buf.write("\n8\f8\168\u01e8\138\39\39\39\39\59\u01ee\n9\39\39\39")
        buf.write("\39\59\u01f4\n9\79\u01f6\n9\f9\169\u01f9\139\3:\3:\3:")
        buf.write("\5:\u01fe\n:\3:\3:\3:\3:\5:\u0204\n:\7:\u0206\n:\f:\16")
        buf.write(":\u0209\13:\5:\u020b\n:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3?\3@\3@\3@\3@\3@\3@\5@\u021e\n@\3@\3@\3@\5@\u0223\n")
        buf.write("@\3A\3A\3B\3B\7B\u0229\nB\fB\16B\u022c\13B\3C\3C\5C\u0230")
        buf.write("\nC\3C\6C\u0233\nC\rC\16C\u0234\3D\3D\5D\u0239\nD\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u024a\nE\3")
        buf.write("F\3F\3F\3F\5F\u0250\nF\3G\3G\7G\u0254\nG\fG\16G\u0257")
        buf.write("\13G\3G\3G\3G\3H\3H\7H\u025e\nH\fH\16H\u0261\13H\3H\3")
        buf.write("H\3H\3H\3H\3I\3I\7I\u026a\nI\fI\16I\u026d\13I\3I\3I\3")
        buf.write("J\3J\3J\3J\5J\u0275\nJ\3K\3K\3K\3K\3K\5K\u027c\nK\3K\3")
        buf.write("K\3L\3L\3L\3L\3L\5L\u0285\nL\3L\3L\3M\3M\3M\3M\3M\5M\u028e")
        buf.write("\nM\3M\3M\3N\3N\3N\3N\3N\5N\u0297\nN\3N\3N\3O\3O\3O\3")
        buf.write("O\5O\u029f\nO\3P\3P\3P\3P\5P\u02a5\nP\3Q\3Q\3Q\3Q\5Q\u02ab")
        buf.write("\nQ\3R\3R\3R\3R\5R\u02b1\nR\3S\3S\3S\3S\3S\3T\3T\3T\3")
        buf.write("T\5T\u02bc\nT\3U\3U\3U\3U\7U\u02c2\nU\fU\16U\u02c5\13")
        buf.write("U\3V\3V\3V\3V\7V\u02cb\nV\fV\16V\u02ce\13V\3W\3W\3W\3")
        buf.write("W\7W\u02d4\nW\fW\16W\u02d7\13W\3X\3X\3X\3X\7X\u02dd\n")
        buf.write("X\fX\16X\u02e0\13X\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^")
        buf.write("\3^\3_\3_\3`\3`\3a\3a\3a\3b\3b\3c\3c\3d\3d\3d\3d\7d\u02fd")
        buf.write("\nd\fd\16d\u0300\13d\3d\3d\3d\3d\3d\3e\6e\u0308\ne\re")
        buf.write("\16e\u0309\3e\3e\3f\3f\3\u02fe\2g\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\2=\2?\2A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a")
        buf.write("/c\60e\61g\62i\63k\64m\2o\2q\2s\2u\2w\2y\2{\2}\65\177")
        buf.write("\2\u0081\2\u0083\2\u0085\2\u0087\66\u0089\2\u008b\2\u008d")
        buf.write("\67\u008f8\u00919\u0093:\u0095\2\u0097\2\u0099\2\u009b")
        buf.write("\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5;\u00a7\2\u00a9")
        buf.write("\2\u00ab\2\u00ad\2\u00af\2\u00b1<\u00b3=\u00b5>\u00b7")
        buf.write("?\u00b9@\u00bbA\u00bdB\u00bfC\u00c1D\u00c3E\u00c5F\u00c7")
        buf.write("G\u00c9H\u00cbI\3\2\22\3\2c|\3\2C\\\3\2\63;\3\2\62;\3")
        buf.write("\2\639\4\2ZZzz\4\2\63;CH\4\2DDdd\3\2\62\63\4\2\62;CH\3")
        buf.write("\2\629\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^cdhhp")
        buf.write("pttvv\5\2\n\f\16\17\"\"\2\u0332\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2}\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2")
        buf.write("\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9")
        buf.write("\3\2\2\2\2\u00cb\3\2\2\2\3\u00cd\3\2\2\2\5\u00d2\3\2\2")
        buf.write("\2\7\u00d4\3\2\2\2\t\u00d6\3\2\2\2\13\u00de\3\2\2\2\r")
        buf.write("\u00e4\3\2\2\2\17\u00ed\3\2\2\2\21\u00f0\3\2\2\2\23\u00f7")
        buf.write("\3\2\2\2\25\u00fc\3\2\2\2\27\u0104\3\2\2\2\31\u0109\3")
        buf.write("\2\2\2\33\u010f\3\2\2\2\35\u0115\3\2\2\2\37\u0118\3\2")
        buf.write("\2\2!\u011c\3\2\2\2#\u0122\3\2\2\2%\u012a\3\2\2\2\'\u0131")
        buf.write("\3\2\2\2)\u0138\3\2\2\2+\u013d\3\2\2\2-\u0143\3\2\2\2")
        buf.write("/\u0147\3\2\2\2\61\u014b\3\2\2\2\63\u0150\3\2\2\2\65\u015c")
        buf.write("\3\2\2\2\67\u0167\3\2\2\29\u016b\3\2\2\2;\u016e\3\2\2")
        buf.write("\2=\u0170\3\2\2\2?\u0172\3\2\2\2A\u0177\3\2\2\2C\u0182")
        buf.write("\3\2\2\2E\u018b\3\2\2\2G\u018d\3\2\2\2I\u018f\3\2\2\2")
        buf.write("K\u0191\3\2\2\2M\u0193\3\2\2\2O\u0195\3\2\2\2Q\u0197\3")
        buf.write("\2\2\2S\u019a\3\2\2\2U\u019d\3\2\2\2W\u01a1\3\2\2\2Y\u01a4")
        buf.write("\3\2\2\2[\u01a7\3\2\2\2]\u01a9\3\2\2\2_\u01ac\3\2\2\2")
        buf.write("a\u01ae\3\2\2\2c\u01b1\3\2\2\2e\u01b3\3\2\2\2g\u01b6\3")
        buf.write("\2\2\2i\u01b9\3\2\2\2k\u01c4\3\2\2\2m\u01c8\3\2\2\2o\u01d8")
        buf.write("\3\2\2\2q\u01e9\3\2\2\2s\u020a\3\2\2\2u\u020c\3\2\2\2")
        buf.write("w\u020e\3\2\2\2y\u0210\3\2\2\2{\u0212\3\2\2\2}\u0214\3")
        buf.write("\2\2\2\177\u0222\3\2\2\2\u0081\u0224\3\2\2\2\u0083\u0226")
        buf.write("\3\2\2\2\u0085\u022d\3\2\2\2\u0087\u0238\3\2\2\2\u0089")
        buf.write("\u0249\3\2\2\2\u008b\u024f\3\2\2\2\u008d\u0251\3\2\2\2")
        buf.write("\u008f\u025b\3\2\2\2\u0091\u0267\3\2\2\2\u0093\u0274\3")
        buf.write("\2\2\2\u0095\u0276\3\2\2\2\u0097\u027f\3\2\2\2\u0099\u0288")
        buf.write("\3\2\2\2\u009b\u0291\3\2\2\2\u009d\u029e\3\2\2\2\u009f")
        buf.write("\u02a4\3\2\2\2\u00a1\u02aa\3\2\2\2\u00a3\u02b0\3\2\2\2")
        buf.write("\u00a5\u02b2\3\2\2\2\u00a7\u02bb\3\2\2\2\u00a9\u02bd\3")
        buf.write("\2\2\2\u00ab\u02c6\3\2\2\2\u00ad\u02cf\3\2\2\2\u00af\u02d8")
        buf.write("\3\2\2\2\u00b1\u02e1\3\2\2\2\u00b3\u02e3\3\2\2\2\u00b5")
        buf.write("\u02e5\3\2\2\2\u00b7\u02e7\3\2\2\2\u00b9\u02e9\3\2\2\2")
        buf.write("\u00bb\u02eb\3\2\2\2\u00bd\u02ed\3\2\2\2\u00bf\u02ef\3")
        buf.write("\2\2\2\u00c1\u02f1\3\2\2\2\u00c3\u02f4\3\2\2\2\u00c5\u02f6")
        buf.write("\3\2\2\2\u00c7\u02f8\3\2\2\2\u00c9\u0307\3\2\2\2\u00cb")
        buf.write("\u030d\3\2\2\2\u00cd\u00ce\7o\2\2\u00ce\u00cf\7c\2\2\u00cf")
        buf.write("\u00d0\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\4\3\2\2\2\u00d2")
        buf.write("\u00d3\59\35\2\u00d3\6\3\2\2\2\u00d4\u00d5\5\'\24\2\u00d5")
        buf.write("\b\3\2\2\2\u00d6\u00d7\7R\2\2\u00d7\u00d8\7t\2\2\u00d8")
        buf.write("\u00d9\7q\2\2\u00d9\u00da\7i\2\2\u00da\u00db\7t\2\2\u00db")
        buf.write("\u00dc\7c\2\2\u00dc\u00dd\7o\2\2\u00dd\n\3\2\2\2\u00de")
        buf.write("\u00df\7D\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7g\2\2\u00e1")
        buf.write("\u00e2\7c\2\2\u00e2\u00e3\7m\2\2\u00e3\f\3\2\2\2\u00e4")
        buf.write("\u00e5\7E\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7")
        buf.write("\u00e8\7v\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea")
        buf.write("\u00eb\7w\2\2\u00eb\u00ec\7g\2\2\u00ec\16\3\2\2\2\u00ed")
        buf.write("\u00ee\7K\2\2\u00ee\u00ef\7h\2\2\u00ef\20\3\2\2\2\u00f0")
        buf.write("\u00f1\7G\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7u\2\2\u00f3")
        buf.write("\u00f4\7g\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7h\2\2\u00f6")
        buf.write("\22\3\2\2\2\u00f7\u00f8\7G\2\2\u00f8\u00f9\7n\2\2\u00f9")
        buf.write("\u00fa\7u\2\2\u00fa\u00fb\7g\2\2\u00fb\24\3\2\2\2\u00fc")
        buf.write("\u00fd\7H\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100\u0101\7c\2\2\u0101\u0102\7e\2\2\u0102")
        buf.write("\u0103\7j\2\2\u0103\26\3\2\2\2\u0104\u0105\7V\2\2\u0105")
        buf.write("\u0106\7t\2\2\u0106\u0107\7w\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write("\30\3\2\2\2\u0109\u010a\7H\2\2\u010a\u010b\7c\2\2\u010b")
        buf.write("\u010c\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e\7g\2\2\u010e")
        buf.write("\32\3\2\2\2\u010f\u0110\7C\2\2\u0110\u0111\7t\2\2\u0111")
        buf.write("\u0112\7t\2\2\u0112\u0113\7c\2\2\u0113\u0114\7{\2\2\u0114")
        buf.write("\34\3\2\2\2\u0115\u0116\7K\2\2\u0116\u0117\7p\2\2\u0117")
        buf.write("\36\3\2\2\2\u0118\u0119\7K\2\2\u0119\u011a\7p\2\2\u011a")
        buf.write("\u011b\7v\2\2\u011b \3\2\2\2\u011c\u011d\7H\2\2\u011d")
        buf.write("\u011e\7n\2\2\u011e\u011f\7q\2\2\u011f\u0120\7c\2\2\u0120")
        buf.write("\u0121\7v\2\2\u0121\"\3\2\2\2\u0122\u0123\7D\2\2\u0123")
        buf.write("\u0124\7q\2\2\u0124\u0125\7q\2\2\u0125\u0126\7n\2\2\u0126")
        buf.write("\u0127\7g\2\2\u0127\u0128\7c\2\2\u0128\u0129\7p\2\2\u0129")
        buf.write("$\3\2\2\2\u012a\u012b\7U\2\2\u012b\u012c\7v\2\2\u012c")
        buf.write("\u012d\7t\2\2\u012d\u012e\7k\2\2\u012e\u012f\7p\2\2\u012f")
        buf.write("\u0130\7i\2\2\u0130&\3\2\2\2\u0131\u0132\7T\2\2\u0132")
        buf.write("\u0133\7g\2\2\u0133\u0134\7v\2\2\u0134\u0135\7w\2\2\u0135")
        buf.write("\u0136\7t\2\2\u0136\u0137\7p\2\2\u0137(\3\2\2\2\u0138")
        buf.write("\u0139\7P\2\2\u0139\u013a\7w\2\2\u013a\u013b\7n\2\2\u013b")
        buf.write("\u013c\7n\2\2\u013c*\3\2\2\2\u013d\u013e\7E\2\2\u013e")
        buf.write("\u013f\7n\2\2\u013f\u0140\7c\2\2\u0140\u0141\7u\2\2\u0141")
        buf.write("\u0142\7u\2\2\u0142,\3\2\2\2\u0143\u0144\7X\2\2\u0144")
        buf.write("\u0145\7c\2\2\u0145\u0146\7n\2\2\u0146.\3\2\2\2\u0147")
        buf.write("\u0148\7X\2\2\u0148\u0149\7c\2\2\u0149\u014a\7t\2\2\u014a")
        buf.write("\60\3\2\2\2\u014b\u014c\7U\2\2\u014c\u014d\7g\2\2\u014d")
        buf.write("\u014e\7n\2\2\u014e\u014f\7h\2\2\u014f\62\3\2\2\2\u0150")
        buf.write("\u0151\7E\2\2\u0151\u0152\7q\2\2\u0152\u0153\7p\2\2\u0153")
        buf.write("\u0154\7u\2\2\u0154\u0155\7v\2\2\u0155\u0156\7t\2\2\u0156")
        buf.write("\u0157\7w\2\2\u0157\u0158\7e\2\2\u0158\u0159\7v\2\2\u0159")
        buf.write("\u015a\7q\2\2\u015a\u015b\7t\2\2\u015b\64\3\2\2\2\u015c")
        buf.write("\u015d\7F\2\2\u015d\u015e\7g\2\2\u015e\u015f\7u\2\2\u015f")
        buf.write("\u0160\7v\2\2\u0160\u0161\7t\2\2\u0161\u0162\7w\2\2\u0162")
        buf.write("\u0163\7e\2\2\u0163\u0164\7v\2\2\u0164\u0165\7q\2\2\u0165")
        buf.write("\u0166\7t\2\2\u0166\66\3\2\2\2\u0167\u0168\7P\2\2\u0168")
        buf.write("\u0169\7g\2\2\u0169\u016a\7y\2\2\u016a8\3\2\2\2\u016b")
        buf.write("\u016c\7D\2\2\u016c\u016d\7{\2\2\u016d:\3\2\2\2\u016e")
        buf.write("\u016f\t\2\2\2\u016f<\3\2\2\2\u0170\u0171\t\3\2\2\u0171")
        buf.write(">\3\2\2\2\u0172\u0173\7a\2\2\u0173@\3\2\2\2\u0174\u0178")
        buf.write("\5;\36\2\u0175\u0178\5=\37\2\u0176\u0178\5? \2\u0177\u0174")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0176\3\2\2\2\u0178")
        buf.write("\u017f\3\2\2\2\u0179\u017e\5;\36\2\u017a\u017e\5=\37\2")
        buf.write("\u017b\u017e\5? \2\u017c\u017e\5{>\2\u017d\u0179\3\2\2")
        buf.write("\2\u017d\u017a\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180B\3\2\2\2\u0181\u017f\3\2\2\2\u0182")
        buf.write("\u0187\7&\2\2\u0183\u0188\5;\36\2\u0184\u0188\5=\37\2")
        buf.write("\u0185\u0188\5? \2\u0186\u0188\5{>\2\u0187\u0183\3\2\2")
        buf.write("\2\u0187\u0184\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018aD\3\2\2\2\u018b\u018c\7-\2\2\u018c")
        buf.write("F\3\2\2\2\u018d\u018e\7/\2\2\u018eH\3\2\2\2\u018f\u0190")
        buf.write("\7,\2\2\u0190J\3\2\2\2\u0191\u0192\7\61\2\2\u0192L\3\2")
        buf.write("\2\2\u0193\u0194\7\'\2\2\u0194N\3\2\2\2\u0195\u0196\7")
        buf.write("#\2\2\u0196P\3\2\2\2\u0197\u0198\7(\2\2\u0198\u0199\7")
        buf.write("(\2\2\u0199R\3\2\2\2\u019a\u019b\7~\2\2\u019b\u019c\7")
        buf.write("~\2\2\u019cT\3\2\2\2\u019d\u019e\7?\2\2\u019e\u019f\7")
        buf.write("?\2\2\u019f\u01a0\7\60\2\2\u01a0V\3\2\2\2\u01a1\u01a2")
        buf.write("\7-\2\2\u01a2\u01a3\7\60\2\2\u01a3X\3\2\2\2\u01a4\u01a5")
        buf.write("\7?\2\2\u01a5\u01a6\7?\2\2\u01a6Z\3\2\2\2\u01a7\u01a8")
        buf.write("\7?\2\2\u01a8\\\3\2\2\2\u01a9\u01aa\7#\2\2\u01aa\u01ab")
        buf.write("\7?\2\2\u01ab^\3\2\2\2\u01ac\u01ad\7>\2\2\u01ad`\3\2\2")
        buf.write("\2\u01ae\u01af\7>\2\2\u01af\u01b0\7?\2\2\u01b0b\3\2\2")
        buf.write("\2\u01b1\u01b2\7@\2\2\u01b2d\3\2\2\2\u01b3\u01b4\7@\2")
        buf.write("\2\u01b4\u01b5\7?\2\2\u01b5f\3\2\2\2\u01b6\u01b7\7<\2")
        buf.write("\2\u01b7\u01b8\7<\2\2\u01b8h\3\2\2\2\u01b9\u01bd\t\4\2")
        buf.write("\2\u01ba\u01bc\t\5\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write("j\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c5\5m\67\2\u01c1")
        buf.write("\u01c5\5o8\2\u01c2\u01c5\5q9\2\u01c3\u01c5\5s:\2\u01c4")
        buf.write("\u01c0\3\2\2\2\u01c4\u01c1\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\b")
        buf.write("\66\2\2\u01c7l\3\2\2\2\u01c8\u01c9\7\62\2\2\u01c9\u01d5")
        buf.write("\t\6\2\2\u01ca\u01cc\5? \2\u01cb\u01ca\3\2\2\2\u01cb\u01cc")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d1\5y=\2\u01ce\u01cf")
        buf.write("\5? \2\u01cf\u01d0\5y=\2\u01d0\u01d2\3\2\2\2\u01d1\u01ce")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3")
        buf.write("\u01cb\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d6\3\2\2\2\u01d6n\3\2\2\2\u01d7\u01d5\3\2\2")
        buf.write("\2\u01d8\u01d9\7\62\2\2\u01d9\u01da\t\7\2\2\u01da\u01e6")
        buf.write("\t\b\2\2\u01db\u01dd\5? \2\u01dc\u01db\3\2\2\2\u01dc\u01dd")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01e2\5w<\2\u01df\u01e0")
        buf.write("\5? \2\u01e0\u01e1\5w<\2\u01e1\u01e3\3\2\2\2\u01e2\u01df")
        buf.write("\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4")
        buf.write("\u01dc\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2")
        buf.write("\u01e6\u01e7\3\2\2\2\u01e7p\3\2\2\2\u01e8\u01e6\3\2\2")
        buf.write("\2\u01e9\u01ea\7\62\2\2\u01ea\u01eb\t\t\2\2\u01eb\u01f7")
        buf.write("\7\63\2\2\u01ec\u01ee\5? \2\u01ed\u01ec\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f3\5u;\2\u01f0")
        buf.write("\u01f1\5? \2\u01f1\u01f2\5u;\2\u01f2\u01f4\3\2\2\2\u01f3")
        buf.write("\u01f0\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6\3\2\2\2")
        buf.write("\u01f5\u01ed\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3")
        buf.write("\2\2\2\u01f7\u01f8\3\2\2\2\u01f8r\3\2\2\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01fa\u020b\7\62\2\2\u01fb\u0207\t\4\2\2\u01fc")
        buf.write("\u01fe\5? \2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0203\5{>\2\u0200\u0201\5? \2\u0201")
        buf.write("\u0202\5{>\2\u0202\u0204\3\2\2\2\u0203\u0200\3\2\2\2\u0203")
        buf.write("\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u01fd\3\2\2\2")
        buf.write("\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3")
        buf.write("\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u01fa")
        buf.write("\3\2\2\2\u020a\u01fb\3\2\2\2\u020bt\3\2\2\2\u020c\u020d")
        buf.write("\t\n\2\2\u020dv\3\2\2\2\u020e\u020f\t\13\2\2\u020fx\3")
        buf.write("\2\2\2\u0210\u0211\t\f\2\2\u0211z\3\2\2\2\u0212\u0213")
        buf.write("\t\5\2\2\u0213|\3\2\2\2\u0214\u0215\5\177@\2\u0215\u0216")
        buf.write("\b?\3\2\u0216~\3\2\2\2\u0217\u021d\5\u0081A\2\u0218\u021e")
        buf.write("\5\u0083B\2\u0219\u021e\5\u0085C\2\u021a\u021b\5\u0083")
        buf.write("B\2\u021b\u021c\5\u0085C\2\u021c\u021e\3\2\2\2\u021d\u0218")
        buf.write("\3\2\2\2\u021d\u0219\3\2\2\2\u021d\u021a\3\2\2\2\u021e")
        buf.write("\u0223\3\2\2\2\u021f\u0220\5\u0083B\2\u0220\u0221\5\u0085")
        buf.write("C\2\u0221\u0223\3\2\2\2\u0222\u0217\3\2\2\2\u0222\u021f")
        buf.write("\3\2\2\2\u0223\u0080\3\2\2\2\u0224\u0225\5s:\2\u0225\u0082")
        buf.write("\3\2\2\2\u0226\u022a\5\u00bf`\2\u0227\u0229\5{>\2\u0228")
        buf.write("\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2")
        buf.write("\u022a\u022b\3\2\2\2\u022b\u0084\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022d\u022f\t\r\2\2\u022e\u0230\t\16\2\2\u022f")
        buf.write("\u022e\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0232\3\2\2\2")
        buf.write("\u0231\u0233\5{>\2\u0232\u0231\3\2\2\2\u0233\u0234\3\2")
        buf.write("\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0086")
        buf.write("\3\2\2\2\u0236\u0239\5\27\f\2\u0237\u0239\5\31\r\2\u0238")
        buf.write("\u0236\3\2\2\2\u0238\u0237\3\2\2\2\u0239\u0088\3\2\2\2")
        buf.write("\u023a\u023b\7^\2\2\u023b\u024a\7)\2\2\u023c\u023d\7^")
        buf.write("\2\2\u023d\u024a\7^\2\2\u023e\u023f\7^\2\2\u023f\u024a")
        buf.write("\7d\2\2\u0240\u0241\7^\2\2\u0241\u024a\7h\2\2\u0242\u0243")
        buf.write("\7^\2\2\u0243\u024a\7p\2\2\u0244\u0245\7^\2\2\u0245\u024a")
        buf.write("\7t\2\2\u0246\u0247\7^\2\2\u0247\u024a\7v\2\2\u0248\u024a")
        buf.write("\7)\2\2\u0249\u023a\3\2\2\2\u0249\u023c\3\2\2\2\u0249")
        buf.write("\u023e\3\2\2\2\u0249\u0240\3\2\2\2\u0249\u0242\3\2\2\2")
        buf.write("\u0249\u0244\3\2\2\2\u0249\u0246\3\2\2\2\u0249\u0248\3")
        buf.write("\2\2\2\u024a\u008a\3\2\2\2\u024b\u0250\n\17\2\2\u024c")
        buf.write("\u0250\5\u0089E\2\u024d\u024e\7)\2\2\u024e\u0250\7$\2")
        buf.write("\2\u024f\u024b\3\2\2\2\u024f\u024c\3\2\2\2\u024f\u024d")
        buf.write("\3\2\2\2\u0250\u008c\3\2\2\2\u0251\u0255\7$\2\2\u0252")
        buf.write("\u0254\5\u008bF\2\u0253\u0252\3\2\2\2\u0254\u0257\3\2")
        buf.write("\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0258")
        buf.write("\3\2\2\2\u0257\u0255\3\2\2\2\u0258\u0259\7$\2\2\u0259")
        buf.write("\u025a\bG\4\2\u025a\u008e\3\2\2\2\u025b\u025f\7$\2\2\u025c")
        buf.write("\u025e\5\u008bF\2\u025d\u025c\3\2\2\2\u025e\u0261\3\2")
        buf.write("\2\2\u025f\u025d\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0262")
        buf.write("\3\2\2\2\u0261\u025f\3\2\2\2\u0262\u0263\7^\2\2\u0263")
        buf.write("\u0264\n\20\2\2\u0264\u0265\3\2\2\2\u0265\u0266\bH\5\2")
        buf.write("\u0266\u0090\3\2\2\2\u0267\u026b\7$\2\2\u0268\u026a\5")
        buf.write("\u008bF\2\u0269\u0268\3\2\2\2\u026a\u026d\3\2\2\2\u026b")
        buf.write("\u0269\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026e\3\2\2\2")
        buf.write("\u026d\u026b\3\2\2\2\u026e\u026f\bI\6\2\u026f\u0092\3")
        buf.write("\2\2\2\u0270\u0275\5\u0095K\2\u0271\u0275\5\u0097L\2\u0272")
        buf.write("\u0275\5\u0099M\2\u0273\u0275\5\u009bN\2\u0274\u0270\3")
        buf.write("\2\2\2\u0274\u0271\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0273")
        buf.write("\3\2\2\2\u0275\u0094\3\2\2\2\u0276\u0277\5\33\16\2\u0277")
        buf.write("\u027b\5\u00b1Y\2\u0278\u0279\5k\66\2\u0279\u027a\5\u009d")
        buf.write("O\2\u027a\u027c\3\2\2\2\u027b\u0278\3\2\2\2\u027b\u027c")
        buf.write("\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u027e\5\u00b3Z\2\u027e")
        buf.write("\u0096\3\2\2\2\u027f\u0280\5\33\16\2\u0280\u0284\5\u00b1")
        buf.write("Y\2\u0281\u0282\5}?\2\u0282\u0283\5\u009fP\2\u0283\u0285")
        buf.write("\3\2\2\2\u0284\u0281\3\2\2\2\u0284\u0285\3\2\2\2\u0285")
        buf.write("\u0286\3\2\2\2\u0286\u0287\5\u00b3Z\2\u0287\u0098\3\2")
        buf.write("\2\2\u0288\u0289\5\33\16\2\u0289\u028d\5\u00b1Y\2\u028a")
        buf.write("\u028b\5\u0087D\2\u028b\u028c\5\u00a1Q\2\u028c\u028e\3")
        buf.write("\2\2\2\u028d\u028a\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u028f")
        buf.write("\3\2\2\2\u028f\u0290\5\u00b3Z\2\u0290\u009a\3\2\2\2\u0291")
        buf.write("\u0292\5\33\16\2\u0292\u0296\5\u00b1Y\2\u0293\u0294\5")
        buf.write("\u008dG\2\u0294\u0295\5\u00a3R\2\u0295\u0297\3\2\2\2\u0296")
        buf.write("\u0293\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0298\3\2\2\2")
        buf.write("\u0298\u0299\5\u00b3Z\2\u0299\u009c\3\2\2\2\u029a\u029b")
        buf.write("\5\u00c3b\2\u029b\u029c\5k\66\2\u029c\u029d\5\u009dO\2")
        buf.write("\u029d\u029f\3\2\2\2\u029e\u029a\3\2\2\2\u029e\u029f\3")
        buf.write("\2\2\2\u029f\u009e\3\2\2\2\u02a0\u02a1\5\u00c3b\2\u02a1")
        buf.write("\u02a2\5}?\2\u02a2\u02a3\5\u009fP\2\u02a3\u02a5\3\2\2")
        buf.write("\2\u02a4\u02a0\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u00a0")
        buf.write("\3\2\2\2\u02a6\u02a7\5\u00c3b\2\u02a7\u02a8\5\u0087D\2")
        buf.write("\u02a8\u02a9\5\u00a1Q\2\u02a9\u02ab\3\2\2\2\u02aa\u02a6")
        buf.write("\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab\u00a2\3\2\2\2\u02ac")
        buf.write("\u02ad\5\u00c3b\2\u02ad\u02ae\5\u008dG\2\u02ae\u02af\5")
        buf.write("\u00a3R\2\u02af\u02b1\3\2\2\2\u02b0\u02ac\3\2\2\2\u02b0")
        buf.write("\u02b1\3\2\2\2\u02b1\u00a4\3\2\2\2\u02b2\u02b3\5\33\16")
        buf.write("\2\u02b3\u02b4\5\u00b1Y\2\u02b4\u02b5\5\u00a7T\2\u02b5")
        buf.write("\u02b6\5\u00b3Z\2\u02b6\u00a6\3\2\2\2\u02b7\u02bc\5\u00a9")
        buf.write("U\2\u02b8\u02bc\5\u00abV\2\u02b9\u02bc\5\u00adW\2\u02ba")
        buf.write("\u02bc\5\u00afX\2\u02bb\u02b7\3\2\2\2\u02bb\u02b8\3\2")
        buf.write("\2\2\u02bb\u02b9\3\2\2\2\u02bb\u02ba\3\2\2\2\u02bc\u00a8")
        buf.write("\3\2\2\2\u02bd\u02c3\5\u0095K\2\u02be\u02bf\5\u00c3b\2")
        buf.write("\u02bf\u02c0\5\u0095K\2\u02c0\u02c2\3\2\2\2\u02c1\u02be")
        buf.write("\3\2\2\2\u02c2\u02c5\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c3")
        buf.write("\u02c4\3\2\2\2\u02c4\u00aa\3\2\2\2\u02c5\u02c3\3\2\2\2")
        buf.write("\u02c6\u02cc\5\u0097L\2\u02c7\u02c8\5\u00c3b\2\u02c8\u02c9")
        buf.write("\5\u0097L\2\u02c9\u02cb\3\2\2\2\u02ca\u02c7\3\2\2\2\u02cb")
        buf.write("\u02ce\3\2\2\2\u02cc\u02ca\3\2\2\2\u02cc\u02cd\3\2\2\2")
        buf.write("\u02cd\u00ac\3\2\2\2\u02ce\u02cc\3\2\2\2\u02cf\u02d5\5")
        buf.write("\u0099M\2\u02d0\u02d1\5\u00c3b\2\u02d1\u02d2\5\u0099M")
        buf.write("\2\u02d2\u02d4\3\2\2\2\u02d3\u02d0\3\2\2\2\u02d4\u02d7")
        buf.write("\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6")
        buf.write("\u00ae\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02de\5\u009b")
        buf.write("N\2\u02d9\u02da\5\u00c3b\2\u02da\u02db\5\u009bN\2\u02db")
        buf.write("\u02dd\3\2\2\2\u02dc\u02d9\3\2\2\2\u02dd\u02e0\3\2\2\2")
        buf.write("\u02de\u02dc\3\2\2\2\u02de\u02df\3\2\2\2\u02df\u00b0\3")
        buf.write("\2\2\2\u02e0\u02de\3\2\2\2\u02e1\u02e2\7*\2\2\u02e2\u00b2")
        buf.write("\3\2\2\2\u02e3\u02e4\7+\2\2\u02e4\u00b4\3\2\2\2\u02e5")
        buf.write("\u02e6\7}\2\2\u02e6\u00b6\3\2\2\2\u02e7\u02e8\7\177\2")
        buf.write("\2\u02e8\u00b8\3\2\2\2\u02e9\u02ea\7]\2\2\u02ea\u00ba")
        buf.write("\3\2\2\2\u02eb\u02ec\7_\2\2\u02ec\u00bc\3\2\2\2\u02ed")
        buf.write("\u02ee\7<\2\2\u02ee\u00be\3\2\2\2\u02ef\u02f0\7\60\2\2")
        buf.write("\u02f0\u00c0\3\2\2\2\u02f1\u02f2\7\60\2\2\u02f2\u02f3")
        buf.write("\7\60\2\2\u02f3\u00c2\3\2\2\2\u02f4\u02f5\7.\2\2\u02f5")
        buf.write("\u00c4\3\2\2\2\u02f6\u02f7\7=\2\2\u02f7\u00c6\3\2\2\2")
        buf.write("\u02f8\u02f9\7%\2\2\u02f9\u02fa\7%\2\2\u02fa\u02fe\3\2")
        buf.write("\2\2\u02fb\u02fd\13\2\2\2\u02fc\u02fb\3\2\2\2\u02fd\u0300")
        buf.write("\3\2\2\2\u02fe\u02ff\3\2\2\2\u02fe\u02fc\3\2\2\2\u02ff")
        buf.write("\u0301\3\2\2\2\u0300\u02fe\3\2\2\2\u0301\u0302\7%\2\2")
        buf.write("\u0302\u0303\7%\2\2\u0303\u0304\3\2\2\2\u0304\u0305\b")
        buf.write("d\7\2\u0305\u00c8\3\2\2\2\u0306\u0308\t\21\2\2\u0307\u0306")
        buf.write("\3\2\2\2\u0308\u0309\3\2\2\2\u0309\u0307\3\2\2\2\u0309")
        buf.write("\u030a\3\2\2\2\u030a\u030b\3\2\2\2\u030b\u030c\be\7\2")
        buf.write("\u030c\u00ca\3\2\2\2\u030d\u030e\13\2\2\2\u030e\u00cc")
        buf.write("\3\2\2\2\62\2\u0177\u017d\u017f\u0187\u0189\u01bd\u01c4")
        buf.write("\u01cb\u01d1\u01d5\u01dc\u01e2\u01e6\u01ed\u01f3\u01f7")
        buf.write("\u01fd\u0203\u0207\u020a\u021d\u0222\u022a\u022f\u0234")
        buf.write("\u0238\u0249\u024f\u0255\u025f\u026b\u0274\u027b\u0284")
        buf.write("\u028d\u0296\u029e\u02a4\u02aa\u02b0\u02bb\u02c3\u02cc")
        buf.write("\u02d5\u02de\u02fe\u0309\b\3\66\2\3?\3\3G\4\3H\5\3I\6")
        buf.write("\b\2\2")
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
    TRUE = 11
    FALSE = 12
    ARRAY = 13
    IN = 14
    INT = 15
    FLOAT = 16
    BOOLEAN = 17
    STRING = 18
    RETURN = 19
    NULL = 20
    CLASS = 21
    VAL = 22
    VAR = 23
    Self = 24
    CONSTRUCTOR = 25
    DESTRUCTOR = 26
    NEW = 27
    BY = 28
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
    Bool_LIT = 52
    STRING_LIT = 53
    ILLEGAL_ESCAPE = 54
    UNCLOSE_STRING = 55
    ARRAY_LIT = 56
    MUL_ARRAY = 57
    LB = 58
    RB = 59
    LP = 60
    RP = 61
    LS = 62
    RS = 63
    COLON = 64
    DOT = 65
    DOUBLE_DOT = 66
    CM = 67
    SEMI = 68
    COMMENT = 69
    WS = 70
    ERROR_CHAR = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Program'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", 
            "'Class'", "'Val'", "'Var'", "'Self'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'==.'", "'+.'", "'=='", "'='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "':'", "'.'", "'..'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "By_keyword", "Return_word", "Program", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
            "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
            "CLASS", "VAL", "VAR", "Self", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "ID", "DO_ID", "ADD", "MINUS", "PRODUCT", "DIVIDE", 
            "MOD", "NOT", "AND", "OR", "COMPARE_STRING", "ADD_STRING", "EQUAL", 
            "ASSIGN", "DIFFER", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
            "DOUBLE_COLON", "NONZERO_INT", "INT_LIT", "FLOAT_LIT", "Bool_LIT", 
            "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ARRAY_LIT", 
            "MUL_ARRAY", "LB", "RB", "LP", "RP", "LS", "RS", "COLON", "DOT", 
            "DOUBLE_DOT", "CM", "SEMI", "COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "By_keyword", "Return_word", "Program", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                  "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                  "RETURN", "NULL", "CLASS", "VAL", "VAR", "Self", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "LOWERCASE", "UPPERCASE", "UNDERSCORE", 
                  "ID", "DO_ID", "ADD", "MINUS", "PRODUCT", "DIVIDE", "MOD", 
                  "NOT", "AND", "OR", "COMPARE_STRING", "ADD_STRING", "EQUAL", 
                  "ASSIGN", "DIFFER", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                  "DOUBLE_COLON", "NONZERO_INT", "INT_LIT", "OCTAL", "HEXA", 
                  "BINARY", "DEC", "BINARY_DIGIT", "HEX_DIGIT", "OCTAL_DIGIT", 
                  "DIGIT", "FLOAT_LIT", "FLOAT_LIT_PART", "INT_PART", "DEC_PART", 
                  "EXP_PART", "Bool_LIT", "ESCAPE_SEQUENCE", "CHAR_STRING", 
                  "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ARRAY_LIT", 
                  "ARRAY_INT", "ARRAY_FLOAT", "ARRAY_BOOLEAN", "ARRAY_STRING", 
                  "INT_LIST", "FLOAT_LIST", "BOOLEAN_LIST", "STRING_LIST", 
                  "MUL_ARRAY", "MUL_ARRAY_LIT", "MUL_ARRAY_INT", "MUL_ARRAY_FLOAT", 
                  "MUL_ARRAY_BOOLEAN", "MUL_ARRAY_STRING", "LB", "RB", "LP", 
                  "RP", "LS", "RS", "COLON", "DOT", "DOUBLE_DOT", "CM", 
                  "SEMI", "COMMENT", "WS", "ERROR_CHAR" ]

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
            actions[69] = self.STRING_LIT_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.UNCLOSE_STRING_action 
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
     


