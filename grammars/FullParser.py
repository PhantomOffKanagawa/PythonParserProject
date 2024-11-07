# Generated from ./grammars/FullParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3!")
        buf.write("\u0138\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\5\2\60\n")
        buf.write("\2\3\2\3\2\5\2\64\n\2\3\2\7\2\67\n\2\f\2\16\2:\13\2\7")
        buf.write("\2<\n\2\f\2\16\2?\13\2\3\2\5\2B\n\2\3\2\3\2\5\2F\n\2\3")
        buf.write("\2\7\2I\n\2\f\2\16\2L\13\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4W\n\4\3\5\3\5\3\6\3\6\5\6]\n\6\3\6\3\6\5\6")
        buf.write("a\n\6\3\6\3\6\5\6e\n\6\3\6\3\6\3\6\7\6j\n\6\f\6\16\6m")
        buf.write("\13\6\3\6\5\6p\n\6\3\7\3\7\3\7\5\7u\n\7\3\7\3\7\5\7y\n")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\5\b\u0081\n\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\5\t\u0088\n\t\3\t\3\t\5\t\u008c\n\t\3\t\3\t\5\t")
        buf.write("\u0090\n\t\3\t\3\t\3\t\3\n\3\n\5\n\u0097\n\n\3\n\3\n\5")
        buf.write("\n\u009b\n\n\3\n\3\n\5\n\u009f\n\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00af")
        buf.write("\n\f\3\f\3\f\5\f\u00b3\n\f\3\f\3\f\5\f\u00b7\n\f\3\f\3")
        buf.write("\f\5\f\u00bb\n\f\3\f\3\f\3\f\5\f\u00c0\n\f\3\r\3\r\3\16")
        buf.write("\3\16\7\16\u00c6\n\16\f\16\16\16\u00c9\13\16\3\16\3\16")
        buf.write("\3\17\3\17\5\17\u00cf\n\17\3\17\3\17\5\17\u00d3\n\17\3")
        buf.write("\17\3\17\3\20\3\20\5\20\u00d9\n\20\3\20\3\20\5\20\u00dd")
        buf.write("\n\20\3\20\3\20\5\20\u00e1\n\20\7\20\u00e3\n\20\f\20\16")
        buf.write("\20\u00e6\13\20\3\21\3\21\5\21\u00ea\n\21\3\21\3\21\5")
        buf.write("\21\u00ee\n\21\3\21\3\21\5\21\u00f2\n\21\3\21\3\21\5\21")
        buf.write("\u00f6\n\21\7\21\u00f8\n\21\f\21\16\21\u00fb\13\21\5\21")
        buf.write("\u00fd\n\21\3\21\5\21\u0100\n\21\3\21\3\21\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u010f")
        buf.write("\n\23\3\24\3\24\3\25\3\25\3\26\5\26\u0116\n\26\3\26\3")
        buf.write("\26\5\26\u011a\n\26\3\26\3\26\5\26\u011e\n\26\3\26\7\26")
        buf.write("\u0121\n\26\f\26\16\26\u0124\13\26\3\27\3\27\5\27\u0128")
        buf.write("\n\27\3\27\3\27\3\27\5\27\u012d\n\27\3\27\3\27\5\27\u0131")
        buf.write("\n\27\3\27\3\27\3\27\5\27\u0136\n\27\3\27\2\2\30\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,\2\5\3\2\31\32")
        buf.write("\4\2\33\33\37\37\3\2\22\23\2\u015c\2=\3\2\2\2\4M\3\2\2")
        buf.write("\2\6V\3\2\2\2\bX\3\2\2\2\nZ\3\2\2\2\fq\3\2\2\2\16}\3\2")
        buf.write("\2\2\20\u0085\3\2\2\2\22\u0094\3\2\2\2\24\u00a3\3\2\2")
        buf.write("\2\26\u00bf\3\2\2\2\30\u00c1\3\2\2\2\32\u00c3\3\2\2\2")
        buf.write("\34\u00cc\3\2\2\2\36\u00d6\3\2\2\2 \u00e7\3\2\2\2\"\u0103")
        buf.write("\3\2\2\2$\u010e\3\2\2\2&\u0110\3\2\2\2(\u0112\3\2\2\2")
        buf.write("*\u0115\3\2\2\2,\u0135\3\2\2\2.\60\7 \2\2/.\3\2\2\2/\60")
        buf.write("\3\2\2\2\60\61\3\2\2\2\61\63\5\6\4\2\62\64\7 \2\2\63\62")
        buf.write("\3\2\2\2\63\64\3\2\2\2\648\3\2\2\2\65\67\7\5\2\2\66\65")
        buf.write("\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29<\3\2\2\2:")
        buf.write("8\3\2\2\2;/\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>A\3")
        buf.write("\2\2\2?=\3\2\2\2@B\7 \2\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2")
        buf.write("\2CE\5\6\4\2DF\7 \2\2ED\3\2\2\2EF\3\2\2\2FJ\3\2\2\2GI")
        buf.write("\7\5\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\3\3")
        buf.write("\2\2\2LJ\3\2\2\2MN\7\3\2\2NO\5\2\2\2OP\7\4\2\2P\5\3\2")
        buf.write("\2\2QW\5\34\17\2RW\5\b\5\2SW\5\n\6\2TW\5\20\t\2UW\5\22")
        buf.write("\n\2VQ\3\2\2\2VR\3\2\2\2VS\3\2\2\2VT\3\2\2\2VU\3\2\2\2")
        buf.write("W\7\3\2\2\2XY\t\2\2\2Y\t\3\2\2\2Z\\\7\f\2\2[]\7 \2\2\\")
        buf.write("[\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^`\5*\26\2_a\7 \2\2`_\3")
        buf.write("\2\2\2`a\3\2\2\2ab\3\2\2\2bd\7\17\2\2ce\7 \2\2dc\3\2\2")
        buf.write("\2de\3\2\2\2ef\3\2\2\2fg\7\5\2\2gk\5\4\3\2hj\5\f\7\2i")
        buf.write("h\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2lo\3\2\2\2mk\3")
        buf.write("\2\2\2np\5\16\b\2on\3\2\2\2op\3\2\2\2p\13\3\2\2\2qr\7")
        buf.write("\r\2\2rt\5*\26\2su\7 \2\2ts\3\2\2\2tu\3\2\2\2uv\3\2\2")
        buf.write("\2vx\7\17\2\2wy\7 \2\2xw\3\2\2\2xy\3\2\2\2yz\3\2\2\2z")
        buf.write("{\7\5\2\2{|\5\4\3\2|\r\3\2\2\2}~\7\16\2\2~\u0080\7\17")
        buf.write("\2\2\177\u0081\7 \2\2\u0080\177\3\2\2\2\u0080\u0081\3")
        buf.write("\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\7\5\2\2\u0083\u0084")
        buf.write("\5\4\3\2\u0084\17\3\2\2\2\u0085\u0087\7\25\2\2\u0086\u0088")
        buf.write("\7 \2\2\u0087\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0089\u008b\5*\26\2\u008a\u008c\7 \2\2")
        buf.write("\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3")
        buf.write("\2\2\2\u008d\u008f\7\17\2\2\u008e\u0090\7 \2\2\u008f\u008e")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\u0092\7\5\2\2\u0092\u0093\5\4\3\2\u0093\21\3\2\2\2\u0094")
        buf.write("\u0096\7\26\2\2\u0095\u0097\7 \2\2\u0096\u0095\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\5")
        buf.write("\24\13\2\u0099\u009b\7 \2\2\u009a\u0099\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\7\17\2")
        buf.write("\2\u009d\u009f\7 \2\2\u009e\u009d\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\7\5\2\2\u00a1")
        buf.write("\u00a2\5\4\3\2\u00a2\23\3\2\2\2\u00a3\u00a4\7\37\2\2\u00a4")
        buf.write("\u00a5\7 \2\2\u00a5\u00a6\7\30\2\2\u00a6\u00a7\7 \2\2")
        buf.write("\u00a7\u00a8\5\26\f\2\u00a8\25\3\2\2\2\u00a9\u00c0\7\37")
        buf.write("\2\2\u00aa\u00c0\5 \21\2\u00ab\u00ac\7\27\2\2\u00ac\u00ae")
        buf.write("\7\20\2\2\u00ad\u00af\7 \2\2\u00ae\u00ad\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\5\"\22")
        buf.write("\2\u00b1\u00b3\7 \2\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\7\13\2\2\u00b5")
        buf.write("\u00b7\7 \2\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00b8\3\2\2\2\u00b8\u00ba\5\"\22\2\u00b9\u00bb")
        buf.write("\7 \2\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bc\u00bd\b\f\1\2\u00bd\u00be\7\21\2")
        buf.write("\2\u00be\u00c0\3\2\2\2\u00bf\u00a9\3\2\2\2\u00bf\u00aa")
        buf.write("\3\2\2\2\u00bf\u00ab\3\2\2\2\u00c0\27\3\2\2\2\u00c1\u00c2")
        buf.write("\5\32\16\2\u00c2\31\3\2\2\2\u00c3\u00c7\5\2\2\2\u00c4")
        buf.write("\u00c6\7\4\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3")
        buf.write("\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb\7\2\2\3\u00cb\33")
        buf.write("\3\2\2\2\u00cc\u00ce\7\37\2\2\u00cd\u00cf\7 \2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\u00d2\5&\24\2\u00d1\u00d3\7 \2\2\u00d2\u00d1\3")
        buf.write("\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5")
        buf.write("\5\36\20\2\u00d5\35\3\2\2\2\u00d6\u00d8\5$\23\2\u00d7")
        buf.write("\u00d9\7 \2\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00e4\3\2\2\2\u00da\u00dc\5(\25\2\u00db\u00dd\7")
        buf.write(" \2\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de")
        buf.write("\3\2\2\2\u00de\u00e0\5$\23\2\u00df\u00e1\7 \2\2\u00e0")
        buf.write("\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2")
        buf.write("\u00e2\u00da\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3")
        buf.write("\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\37\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e7\u00fc\7\t\2\2\u00e8\u00ea\7 \2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\u00ed\5$\23\2\u00ec\u00ee\7 \2\2\u00ed\u00ec\3")
        buf.write("\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f9\3\2\2\2\u00ef\u00f1")
        buf.write("\7\13\2\2\u00f0\u00f2\7 \2\2\u00f1\u00f0\3\2\2\2\u00f1")
        buf.write("\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\5$\23\2")
        buf.write("\u00f4\u00f6\7 \2\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00ef\3\2\2\2\u00f8\u00fb")
        buf.write("\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00e9\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u0100\7")
        buf.write(" \2\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101")
        buf.write("\3\2\2\2\u0101\u0102\7\n\2\2\u0102!\3\2\2\2\u0103\u0104")
        buf.write("\t\3\2\2\u0104#\3\2\2\2\u0105\u010f\7\33\2\2\u0106\u010f")
        buf.write("\7\37\2\2\u0107\u010f\7\34\2\2\u0108\u010f\7\35\2\2\u0109")
        buf.write("\u010a\7\20\2\2\u010a\u010b\5\36\20\2\u010b\u010c\7\21")
        buf.write("\2\2\u010c\u010f\3\2\2\2\u010d\u010f\5 \21\2\u010e\u0105")
        buf.write("\3\2\2\2\u010e\u0106\3\2\2\2\u010e\u0107\3\2\2\2\u010e")
        buf.write("\u0108\3\2\2\2\u010e\u0109\3\2\2\2\u010e\u010d\3\2\2\2")
        buf.write("\u010f%\3\2\2\2\u0110\u0111\7\7\2\2\u0111\'\3\2\2\2\u0112")
        buf.write("\u0113\7\b\2\2\u0113)\3\2\2\2\u0114\u0116\7 \2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u0122\5,\27\2\u0118\u011a\7 \2\2\u0119\u0118\3")
        buf.write("\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d")
        buf.write("\t\4\2\2\u011c\u011e\7 \2\2\u011d\u011c\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121\5,\27\2")
        buf.write("\u0120\u0119\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3")
        buf.write("\2\2\2\u0122\u0123\3\2\2\2\u0123+\3\2\2\2\u0124\u0122")
        buf.write("\3\2\2\2\u0125\u0127\7\24\2\2\u0126\u0128\7 \2\2\u0127")
        buf.write("\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129\u0136\5,\27\2\u012a\u012c\7\20\2\2\u012b\u012d")
        buf.write("\7 \2\2\u012c\u012b\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u0130\5*\26\2\u012f\u0131\7 \2\2")
        buf.write("\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3")
        buf.write("\2\2\2\u0132\u0133\7\21\2\2\u0133\u0136\3\2\2\2\u0134")
        buf.write("\u0136\5$\23\2\u0135\u0125\3\2\2\2\u0135\u012a\3\2\2\2")
        buf.write("\u0135\u0134\3\2\2\2\u0136-\3\2\2\2\64/\638=AEJV\\`dk")
        buf.write("otx\u0080\u0087\u008b\u008f\u0096\u009a\u009e\u00ae\u00b2")
        buf.write("\u00b6\u00ba\u00bf\u00c7\u00ce\u00d2\u00d8\u00dc\u00e0")
        buf.write("\u00e4\u00e9\u00ed\u00f1\u00f5\u00f9\u00fc\u00ff\u010e")
        buf.write("\u0115\u0119\u011d\u0122\u0127\u012c\u0130\u0135")
        return buf.getvalue()


class FullParser ( Parser ):

    grammarFileName = "FullParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'['", "']'", 
                     "','", "'if'", "'elif'", "'else'", "':'", "'('", "')'", 
                     "<INVALID>", "<INVALID>", "'not'", "'while'", "'for'", 
                     "'range'", "'in'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NEWLINE", "SPACES", 
                      "ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", "RBRACKET", 
                      "COMMA", "IF", "ELIF", "ELSE", "COLON", "LPAREN", 
                      "RPAREN", "COMPARISON_OP", "LOGICAL_OP", "NOT_OP", 
                      "WHILE", "FOR", "RANGE", "IN", "SINGLE_LINE_COMMENT", 
                      "MULTI_LINE_COMMENT", "NUMBER", "BOOLEAN", "STRING", 
                      "ESC", "VARIABLE", "WS", "WS_SKIPPED" ]

    RULE_first_block = 0
    RULE_block = 1
    RULE_line = 2
    RULE_comment = 3
    RULE_if_block = 4
    RULE_elif_block = 5
    RULE_else_block = 6
    RULE_while_block = 7
    RULE_for_block = 8
    RULE_for_condition = 9
    RULE_iterable = 10
    RULE_stat = 11
    RULE_expr = 12
    RULE_assignment = 13
    RULE_expression = 14
    RULE_array = 15
    RULE_count = 16
    RULE_value = 17
    RULE_assignment_operator = 18
    RULE_operator = 19
    RULE_condition = 20
    RULE_comparison_condition = 21

    ruleNames =  [ "first_block", "block", "line", "comment", "if_block", 
                   "elif_block", "else_block", "while_block", "for_block", 
                   "for_condition", "iterable", "stat", "expr", "assignment", 
                   "expression", "array", "count", "value", "assignment_operator", 
                   "operator", "condition", "comparison_condition" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    NEWLINE=3
    SPACES=4
    ASSIGNMENT_OP=5
    ARITHMETIC_OP=6
    LBRACKET=7
    RBRACKET=8
    COMMA=9
    IF=10
    ELIF=11
    ELSE=12
    COLON=13
    LPAREN=14
    RPAREN=15
    COMPARISON_OP=16
    LOGICAL_OP=17
    NOT_OP=18
    WHILE=19
    FOR=20
    RANGE=21
    IN=22
    SINGLE_LINE_COMMENT=23
    MULTI_LINE_COMMENT=24
    NUMBER=25
    BOOLEAN=26
    STRING=27
    ESC=28
    VARIABLE=29
    WS=30
    WS_SKIPPED=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class First_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullParser.LineContext)
            else:
                return self.getTypedRuleContext(FullParser.LineContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.NEWLINE)
            else:
                return self.getToken(FullParser.NEWLINE, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def getRuleIndex(self):
            return FullParser.RULE_first_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirst_block" ):
                listener.enterFirst_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirst_block" ):
                listener.exitFirst_block(self)




    def first_block(self):

        localctx = FullParser.First_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_first_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==FullParser.WS:
                        self.state = 44
                        self.match(FullParser.WS)


                    self.state = 47
                    self.line()
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 48
                        self.match(FullParser.WS)


                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==FullParser.NEWLINE:
                        self.state = 51
                        self.match(FullParser.NEWLINE)
                        self.state = 56
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 62
                self.match(FullParser.WS)


            self.state = 65
            self.line()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 66
                self.match(FullParser.WS)


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FullParser.NEWLINE:
                self.state = 69
                self.match(FullParser.NEWLINE)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(FullParser.INDENT, 0)

        def first_block(self):
            return self.getTypedRuleContext(FullParser.First_blockContext,0)


        def DEDENT(self):
            return self.getToken(FullParser.DEDENT, 0)

        def getRuleIndex(self):
            return FullParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = FullParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(FullParser.INDENT)
            self.state = 76
            self.first_block()
            self.state = 77
            self.match(FullParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(FullParser.AssignmentContext,0)


        def comment(self):
            return self.getTypedRuleContext(FullParser.CommentContext,0)


        def if_block(self):
            return self.getTypedRuleContext(FullParser.If_blockContext,0)


        def while_block(self):
            return self.getTypedRuleContext(FullParser.While_blockContext,0)


        def for_block(self):
            return self.getTypedRuleContext(FullParser.For_blockContext,0)


        def getRuleIndex(self):
            return FullParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = FullParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_line)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FullParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.assignment()
                pass
            elif token in [FullParser.SINGLE_LINE_COMMENT, FullParser.MULTI_LINE_COMMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.comment()
                pass
            elif token in [FullParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.if_block()
                pass
            elif token in [FullParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.while_block()
                pass
            elif token in [FullParser.FOR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.for_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_LINE_COMMENT(self):
            return self.getToken(FullParser.SINGLE_LINE_COMMENT, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(FullParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return FullParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = FullParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==FullParser.SINGLE_LINE_COMMENT or _la==FullParser.MULTI_LINE_COMMENT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(FullParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(FullParser.ConditionContext,0)


        def COLON(self):
            return self.getToken(FullParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(FullParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(FullParser.BlockContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def elif_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullParser.Elif_blockContext)
            else:
                return self.getTypedRuleContext(FullParser.Elif_blockContext,i)


        def else_block(self):
            return self.getTypedRuleContext(FullParser.Else_blockContext,0)


        def getRuleIndex(self):
            return FullParser.RULE_if_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_block" ):
                listener.enterIf_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_block" ):
                listener.exitIf_block(self)




    def if_block(self):

        localctx = FullParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(FullParser.IF)
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(FullParser.WS)


            self.state = 92
            self.condition()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 93
                self.match(FullParser.WS)


            self.state = 96
            self.match(FullParser.COLON)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 97
                self.match(FullParser.WS)


            self.state = 100
            self.match(FullParser.NEWLINE)
            self.state = 101
            self.block()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FullParser.ELIF:
                self.state = 102
                self.elif_block()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.ELSE:
                self.state = 108
                self.else_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Elif_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(FullParser.ELIF, 0)

        def condition(self):
            return self.getTypedRuleContext(FullParser.ConditionContext,0)


        def COLON(self):
            return self.getToken(FullParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(FullParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(FullParser.BlockContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def getRuleIndex(self):
            return FullParser.RULE_elif_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_block" ):
                listener.enterElif_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_block" ):
                listener.exitElif_block(self)




    def elif_block(self):

        localctx = FullParser.Elif_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elif_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(FullParser.ELIF)
            self.state = 112
            self.condition()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 113
                self.match(FullParser.WS)


            self.state = 116
            self.match(FullParser.COLON)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 117
                self.match(FullParser.WS)


            self.state = 120
            self.match(FullParser.NEWLINE)
            self.state = 121
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(FullParser.ELSE, 0)

        def COLON(self):
            return self.getToken(FullParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(FullParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(FullParser.BlockContext,0)


        def WS(self):
            return self.getToken(FullParser.WS, 0)

        def getRuleIndex(self):
            return FullParser.RULE_else_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_block" ):
                listener.enterElse_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_block" ):
                listener.exitElse_block(self)




    def else_block(self):

        localctx = FullParser.Else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_else_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(FullParser.ELSE)
            self.state = 124
            self.match(FullParser.COLON)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 125
                self.match(FullParser.WS)


            self.state = 128
            self.match(FullParser.NEWLINE)
            self.state = 129
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(FullParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(FullParser.ConditionContext,0)


        def COLON(self):
            return self.getToken(FullParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(FullParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(FullParser.BlockContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def getRuleIndex(self):
            return FullParser.RULE_while_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_block" ):
                listener.enterWhile_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_block" ):
                listener.exitWhile_block(self)




    def while_block(self):

        localctx = FullParser.While_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(FullParser.WHILE)
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 132
                self.match(FullParser.WS)


            self.state = 135
            self.condition()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 136
                self.match(FullParser.WS)


            self.state = 139
            self.match(FullParser.COLON)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 140
                self.match(FullParser.WS)


            self.state = 143
            self.match(FullParser.NEWLINE)
            self.state = 144
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(FullParser.FOR, 0)

        def for_condition(self):
            return self.getTypedRuleContext(FullParser.For_conditionContext,0)


        def COLON(self):
            return self.getToken(FullParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(FullParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(FullParser.BlockContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def getRuleIndex(self):
            return FullParser.RULE_for_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_block" ):
                listener.enterFor_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_block" ):
                listener.exitFor_block(self)




    def for_block(self):

        localctx = FullParser.For_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(FullParser.FOR)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 147
                self.match(FullParser.WS)


            self.state = 150
            self.for_condition()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 151
                self.match(FullParser.WS)


            self.state = 154
            self.match(FullParser.COLON)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 155
                self.match(FullParser.WS)


            self.state = 158
            self.match(FullParser.NEWLINE)
            self.state = 159
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(FullParser.VARIABLE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def IN(self):
            return self.getToken(FullParser.IN, 0)

        def iterable(self):
            return self.getTypedRuleContext(FullParser.IterableContext,0)


        def getRuleIndex(self):
            return FullParser.RULE_for_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_condition" ):
                listener.enterFor_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_condition" ):
                listener.exitFor_condition(self)




    def for_condition(self):

        localctx = FullParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(FullParser.VARIABLE)
            self.state = 162
            self.match(FullParser.WS)
            self.state = 163
            self.match(FullParser.IN)
            self.state = 164
            self.match(FullParser.WS)
            self.state = 165
            self.iterable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(FullParser.VARIABLE, 0)

        def array(self):
            return self.getTypedRuleContext(FullParser.ArrayContext,0)


        def RANGE(self):
            return self.getToken(FullParser.RANGE, 0)

        def LPAREN(self):
            return self.getToken(FullParser.LPAREN, 0)

        def count(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullParser.CountContext)
            else:
                return self.getTypedRuleContext(FullParser.CountContext,i)


        def RPAREN(self):
            return self.getToken(FullParser.RPAREN, 0)

        def COMMA(self):
            return self.getToken(FullParser.COMMA, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def getRuleIndex(self):
            return FullParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = FullParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_iterable)
        self._la = 0 # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FullParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(FullParser.VARIABLE)
                pass
            elif token in [FullParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.array()
                pass
            elif token in [FullParser.RANGE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.match(FullParser.RANGE)
                self.state = 170
                self.match(FullParser.LPAREN)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FullParser.WS:
                    self.state = 171
                    self.match(FullParser.WS)


                self.state = 174
                self.count()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FullParser.WS:
                    self.state = 175
                    self.match(FullParser.WS)


                self.state = 178
                self.match(FullParser.COMMA)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FullParser.WS:
                    self.state = 179
                    self.match(FullParser.WS)


                self.state = 182
                self.count()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FullParser.WS:
                    self.state = 183
                    self.match(FullParser.WS)


                0,2
                self.state = 187
                self.match(FullParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(FullParser.ExprContext,0)


        def getRuleIndex(self):
            return FullParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = FullParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def first_block(self):
            return self.getTypedRuleContext(FullParser.First_blockContext,0)


        def EOF(self):
            return self.getToken(FullParser.EOF, 0)

        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.DEDENT)
            else:
                return self.getToken(FullParser.DEDENT, i)

        def getRuleIndex(self):
            return FullParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = FullParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.first_block()

            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FullParser.DEDENT:
                self.state = 194
                self.match(FullParser.DEDENT)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self.match(FullParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(FullParser.VARIABLE, 0)

        def assignment_operator(self):
            return self.getTypedRuleContext(FullParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(FullParser.ExpressionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def getRuleIndex(self):
            return FullParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = FullParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(FullParser.VARIABLE)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 203
                self.match(FullParser.WS)


            self.state = 206
            self.assignment_operator()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 207
                self.match(FullParser.WS)


            self.state = 210
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullParser.ValueContext)
            else:
                return self.getTypedRuleContext(FullParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullParser.OperatorContext)
            else:
                return self.getTypedRuleContext(FullParser.OperatorContext,i)


        def getRuleIndex(self):
            return FullParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = FullParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.value()
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 213
                self.match(FullParser.WS)


            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FullParser.ARITHMETIC_OP:
                self.state = 216
                self.operator()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FullParser.WS:
                    self.state = 217
                    self.match(FullParser.WS)


                self.state = 220
                self.value()
                self.state = 222
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 221
                    self.match(FullParser.WS)


                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(FullParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(FullParser.RBRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullParser.ValueContext)
            else:
                return self.getTypedRuleContext(FullParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.COMMA)
            else:
                return self.getToken(FullParser.COMMA, i)

        def getRuleIndex(self):
            return FullParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = FullParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(FullParser.LBRACKET)
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FullParser.WS:
                    self.state = 230
                    self.match(FullParser.WS)


                self.state = 233
                self.value()
                self.state = 235
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 234
                    self.match(FullParser.WS)


                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==FullParser.COMMA:
                    self.state = 237
                    self.match(FullParser.COMMA)
                    self.state = 239
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==FullParser.WS:
                        self.state = 238
                        self.match(FullParser.WS)


                    self.state = 241
                    self.value()
                    self.state = 243
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 242
                        self.match(FullParser.WS)


                    self.state = 249
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 252
                self.match(FullParser.WS)


            self.state = 255
            self.match(FullParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(FullParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(FullParser.VARIABLE, 0)

        def getRuleIndex(self):
            return FullParser.RULE_count

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCount" ):
                listener.enterCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCount" ):
                listener.exitCount(self)




    def count(self):

        localctx = FullParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_count)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            _la = self._input.LA(1)
            if not(_la==FullParser.NUMBER or _la==FullParser.VARIABLE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(FullParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(FullParser.VARIABLE, 0)

        def BOOLEAN(self):
            return self.getToken(FullParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(FullParser.STRING, 0)

        def LPAREN(self):
            return self.getToken(FullParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(FullParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(FullParser.RPAREN, 0)

        def array(self):
            return self.getTypedRuleContext(FullParser.ArrayContext,0)


        def getRuleIndex(self):
            return FullParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = FullParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_value)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FullParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(FullParser.NUMBER)
                pass
            elif token in [FullParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(FullParser.VARIABLE)
                pass
            elif token in [FullParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                self.match(FullParser.BOOLEAN)
                pass
            elif token in [FullParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.match(FullParser.STRING)
                pass
            elif token in [FullParser.LPAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 263
                self.match(FullParser.LPAREN)
                self.state = 264
                self.expression()
                self.state = 265
                self.match(FullParser.RPAREN)
                pass
            elif token in [FullParser.LBRACKET]:
                self.enterOuterAlt(localctx, 6)
                self.state = 267
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT_OP(self):
            return self.getToken(FullParser.ASSIGNMENT_OP, 0)

        def getRuleIndex(self):
            return FullParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = FullParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(FullParser.ASSIGNMENT_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARITHMETIC_OP(self):
            return self.getToken(FullParser.ARITHMETIC_OP, 0)

        def getRuleIndex(self):
            return FullParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = FullParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(FullParser.ARITHMETIC_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FullParser.Comparison_conditionContext)
            else:
                return self.getTypedRuleContext(FullParser.Comparison_conditionContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.LOGICAL_OP)
            else:
                return self.getToken(FullParser.LOGICAL_OP, i)

        def COMPARISON_OP(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.COMPARISON_OP)
            else:
                return self.getToken(FullParser.COMPARISON_OP, i)

        def getRuleIndex(self):
            return FullParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = FullParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FullParser.WS:
                self.state = 274
                self.match(FullParser.WS)


            self.state = 277
            self.comparison_condition()
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 279
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==FullParser.WS:
                        self.state = 278
                        self.match(FullParser.WS)


                    self.state = 281
                    _la = self._input.LA(1)
                    if not(_la==FullParser.COMPARISON_OP or _la==FullParser.LOGICAL_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 283
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==FullParser.WS:
                        self.state = 282
                        self.match(FullParser.WS)


                    self.state = 285
                    self.comparison_condition() 
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comparison_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(FullParser.NOT_OP, 0)

        def comparison_condition(self):
            return self.getTypedRuleContext(FullParser.Comparison_conditionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(FullParser.WS)
            else:
                return self.getToken(FullParser.WS, i)

        def LPAREN(self):
            return self.getToken(FullParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(FullParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(FullParser.RPAREN, 0)

        def value(self):
            return self.getTypedRuleContext(FullParser.ValueContext,0)


        def getRuleIndex(self):
            return FullParser.RULE_comparison_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_condition" ):
                listener.enterComparison_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_condition" ):
                listener.exitComparison_condition(self)




    def comparison_condition(self):

        localctx = FullParser.Comparison_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_comparison_condition)
        self._la = 0 # Token type
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(FullParser.NOT_OP)
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FullParser.WS:
                    self.state = 292
                    self.match(FullParser.WS)


                self.state = 295
                self.comparison_condition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(FullParser.LPAREN)
                self.state = 298
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 297
                    self.match(FullParser.WS)


                self.state = 300
                self.condition()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FullParser.WS:
                    self.state = 301
                    self.match(FullParser.WS)


                self.state = 304
                self.match(FullParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





