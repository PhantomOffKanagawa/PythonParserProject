# Generated from ./grammars/main.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u010b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5S\n\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("z\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u0081\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\5\25\u0092\n\25\3\25\6\25\u0095\n\25\r")
        buf.write("\25\16\25\u0096\3\25\3\25\6\25\u009b\n\25\r\25\16\25\u009c")
        buf.write("\5\25\u009f\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u00aa\n\26\3\27\3\27\3\27\7\27\u00af\n\27")
        buf.write("\f\27\16\27\u00b2\13\27\3\27\3\27\3\27\3\27\7\27\u00b8")
        buf.write("\n\27\f\27\16\27\u00bb\13\27\3\27\5\27\u00be\n\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\7\31\u00c5\n\31\f\31\16\31\u00c8")
        buf.write("\13\31\3\32\6\32\u00cb\n\32\r\32\16\32\u00cc\3\33\5\33")
        buf.write("\u00d0\n\33\3\33\7\33\u00d3\n\33\f\33\16\33\u00d6\13\33")
        buf.write("\3\33\3\33\5\33\u00da\n\33\3\34\3\34\7\34\u00de\n\34\f")
        buf.write("\34\16\34\u00e1\13\34\3\35\3\35\3\35\3\35\3\35\7\35\u00e8")
        buf.write("\n\35\f\35\16\35\u00eb\13\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\7\35\u00f5\n\35\f\35\16\35\u00f8\13\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0102\n")
        buf.write("\35\f\35\16\35\u0105\13\35\3\35\3\35\3\35\5\35\u010a\n")
        buf.write("\35\5\u00e9\u00f6\u0103\2\36\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36\3\2\f\3\2\13\13\6\2\'\',-//\61\61\3\2\62;\4\2$$^")
        buf.write("^\4\2))^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2\"\"\4\2\f\f\17\17\2\u0129\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\3")
        buf.write(";\3\2\2\2\5>\3\2\2\2\7E\3\2\2\2\tR\3\2\2\2\13T\3\2\2\2")
        buf.write("\rV\3\2\2\2\17X\3\2\2\2\21Z\3\2\2\2\23\\\3\2\2\2\25_\3")
        buf.write("\2\2\2\27d\3\2\2\2\31i\3\2\2\2\33k\3\2\2\2\35m\3\2\2\2")
        buf.write("\37y\3\2\2\2!\u0080\3\2\2\2#\u0082\3\2\2\2%\u0086\3\2")
        buf.write("\2\2\'\u008c\3\2\2\2)\u0091\3\2\2\2+\u00a9\3\2\2\2-\u00bd")
        buf.write("\3\2\2\2/\u00bf\3\2\2\2\61\u00c2\3\2\2\2\63\u00ca\3\2")
        buf.write("\2\2\65\u00d9\3\2\2\2\67\u00db\3\2\2\29\u0109\3\2\2\2")
        buf.write(";<\7k\2\2<=\7p\2\2=\4\3\2\2\2>?\7t\2\2?@\7c\2\2@A\7p\2")
        buf.write("\2AB\7i\2\2BC\7g\2\2CD\7*\2\2D\6\3\2\2\2EF\t\2\2\2FG\3")
        buf.write("\2\2\2GH\b\4\2\2H\b\3\2\2\2IS\7?\2\2JK\7-\2\2KS\7?\2\2")
        buf.write("LM\7/\2\2MS\7?\2\2NO\7,\2\2OS\7?\2\2PQ\7\61\2\2QS\7?\2")
        buf.write("\2RI\3\2\2\2RJ\3\2\2\2RL\3\2\2\2RN\3\2\2\2RP\3\2\2\2S")
        buf.write("\n\3\2\2\2TU\t\3\2\2U\f\3\2\2\2VW\7]\2\2W\16\3\2\2\2X")
        buf.write("Y\7_\2\2Y\20\3\2\2\2Z[\7.\2\2[\22\3\2\2\2\\]\7k\2\2]^")
        buf.write("\7h\2\2^\24\3\2\2\2_`\7g\2\2`a\7n\2\2ab\7k\2\2bc\7h\2")
        buf.write("\2c\26\3\2\2\2de\7g\2\2ef\7n\2\2fg\7u\2\2gh\7g\2\2h\30")
        buf.write("\3\2\2\2ij\7<\2\2j\32\3\2\2\2kl\7*\2\2l\34\3\2\2\2mn\7")
        buf.write("+\2\2n\36\3\2\2\2op\7?\2\2pz\7?\2\2qr\7#\2\2rz\7?\2\2")
        buf.write("sz\7>\2\2tu\7>\2\2uz\7?\2\2vz\7@\2\2wx\7@\2\2xz\7?\2\2")
        buf.write("yo\3\2\2\2yq\3\2\2\2ys\3\2\2\2yt\3\2\2\2yv\3\2\2\2yw\3")
        buf.write("\2\2\2z \3\2\2\2{|\7c\2\2|}\7p\2\2}\u0081\7f\2\2~\177")
        buf.write("\7q\2\2\177\u0081\7t\2\2\u0080{\3\2\2\2\u0080~\3\2\2\2")
        buf.write("\u0081\"\3\2\2\2\u0082\u0083\7p\2\2\u0083\u0084\7q\2\2")
        buf.write("\u0084\u0085\7v\2\2\u0085$\3\2\2\2\u0086\u0087\7y\2\2")
        buf.write("\u0087\u0088\7j\2\2\u0088\u0089\7k\2\2\u0089\u008a\7n")
        buf.write("\2\2\u008a\u008b\7g\2\2\u008b&\3\2\2\2\u008c\u008d\7h")
        buf.write("\2\2\u008d\u008e\7q\2\2\u008e\u008f\7t\2\2\u008f(\3\2")
        buf.write("\2\2\u0090\u0092\7/\2\2\u0091\u0090\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0095\t\4\2\2\u0094")
        buf.write("\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u009e\3\2\2\2\u0098\u009a\7")
        buf.write("\60\2\2\u0099\u009b\t\4\2\2\u009a\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d\u009f\3\2\2\2\u009e\u0098\3\2\2\2\u009e\u009f\3")
        buf.write("\2\2\2\u009f*\3\2\2\2\u00a0\u00a1\7V\2\2\u00a1\u00a2\7")
        buf.write("t\2\2\u00a2\u00a3\7w\2\2\u00a3\u00aa\7g\2\2\u00a4\u00a5")
        buf.write("\7H\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7n\2\2\u00a7\u00a8")
        buf.write("\7u\2\2\u00a8\u00aa\7g\2\2\u00a9\u00a0\3\2\2\2\u00a9\u00a4")
        buf.write("\3\2\2\2\u00aa,\3\2\2\2\u00ab\u00b0\7$\2\2\u00ac\u00af")
        buf.write("\5/\30\2\u00ad\u00af\n\5\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b3\u00be\7$\2\2\u00b4\u00b9\7)\2\2\u00b5\u00b8")
        buf.write("\5/\30\2\u00b6\u00b8\n\6\2\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00b9\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3")
        buf.write("\2\2\2\u00bc\u00be\7)\2\2\u00bd\u00ab\3\2\2\2\u00bd\u00b4")
        buf.write("\3\2\2\2\u00be.\3\2\2\2\u00bf\u00c0\7^\2\2\u00c0\u00c1")
        buf.write("\t\7\2\2\u00c1\60\3\2\2\2\u00c2\u00c6\t\b\2\2\u00c3\u00c5")
        buf.write("\t\t\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\62\3\2\2\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c9\u00cb\t\n\2\2\u00ca\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3")
        buf.write("\2\2\2\u00cd\64\3\2\2\2\u00ce\u00d0\7\17\2\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d4\3\2\2\2\u00d1")
        buf.write("\u00d3\t\n\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7\3")
        buf.write("\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00da\7\f\2\2\u00d8\u00da")
        buf.write("\7\17\2\2\u00d9\u00cf\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da")
        buf.write("\66\3\2\2\2\u00db\u00df\7%\2\2\u00dc\u00de\n\13\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00df\u00e0\3\2\2\2\u00e08\3\2\2\2\u00e1\u00df\3\2\2")
        buf.write("\2\u00e2\u00e3\7$\2\2\u00e3\u00e4\7$\2\2\u00e4\u00e5\7")
        buf.write("$\2\2\u00e5\u00e9\3\2\2\2\u00e6\u00e8\13\2\2\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00ea\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00ec\u00ed\7$\2\2\u00ed\u00ee\7$\2\2\u00ee\u010a\7$")
        buf.write("\2\2\u00ef\u00f0\7)\2\2\u00f0\u00f1\7)\2\2\u00f1\u00f2")
        buf.write("\7)\2\2\u00f2\u00f6\3\2\2\2\u00f3\u00f5\13\2\2\2\u00f4")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8\u00f6\3")
        buf.write("\2\2\2\u00f9\u00fa\7)\2\2\u00fa\u00fb\7)\2\2\u00fb\u010a")
        buf.write("\7)\2\2\u00fc\u00fd\7b\2\2\u00fd\u00fe\7b\2\2\u00fe\u00ff")
        buf.write("\7b\2\2\u00ff\u0103\3\2\2\2\u0100\u0102\13\2\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0103\u0101\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0103\3")
        buf.write("\2\2\2\u0106\u0107\7b\2\2\u0107\u0108\7b\2\2\u0108\u010a")
        buf.write("\7b\2\2\u0109\u00e2\3\2\2\2\u0109\u00ef\3\2\2\2\u0109")
        buf.write("\u00fc\3\2\2\2\u010a:\3\2\2\2\32\2Ry\u0080\u0091\u0096")
        buf.write("\u009c\u009e\u00a9\u00ae\u00b0\u00b7\u00b9\u00bd\u00c6")
        buf.write("\u00cc\u00cf\u00d4\u00d9\u00df\u00e9\u00f6\u0103\u0109")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class mainLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS_SKIPPED = 3
    ASSIGNMENT_OP = 4
    ARITHMETIC_OP = 5
    LBRACKET = 6
    RBRACKET = 7
    COMMA = 8
    IF = 9
    ELIF = 10
    ELSE = 11
    COLON = 12
    LPAREN = 13
    RPAREN = 14
    COMPARISON_OP = 15
    LOGICAL_OP = 16
    NOT_OP = 17
    WHILE = 18
    FOR = 19
    NUMBER = 20
    BOOLEAN = 21
    STRING = 22
    ESC = 23
    VARIABLE = 24
    WS = 25
    NEWLINE = 26
    SINGLE_LINE_COMMENT = 27
    MULTI_LINE_COMMENT = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'in'", "'range('", "'['", "']'", "','", "'if'", "'elif'", "'else'", 
            "':'", "'('", "')'", "'not'", "'while'", "'for'" ]

    symbolicNames = [ "<INVALID>",
            "WS_SKIPPED", "ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", 
            "RBRACKET", "COMMA", "IF", "ELIF", "ELSE", "COLON", "LPAREN", 
            "RPAREN", "COMPARISON_OP", "LOGICAL_OP", "NOT_OP", "WHILE", 
            "FOR", "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS", 
            "NEWLINE", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "WS_SKIPPED", "ASSIGNMENT_OP", "ARITHMETIC_OP", 
                  "LBRACKET", "RBRACKET", "COMMA", "IF", "ELIF", "ELSE", 
                  "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
                  "NOT_OP", "WHILE", "FOR", "NUMBER", "BOOLEAN", "STRING", 
                  "ESC", "VARIABLE", "WS", "NEWLINE", "SINGLE_LINE_COMMENT", 
                  "MULTI_LINE_COMMENT" ]

    grammarFileName = "main.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


