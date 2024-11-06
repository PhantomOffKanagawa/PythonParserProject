# Generated from ./grammars/full.g4 by ANTLR 4.9.2
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
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\5\4G\n\4\3\4")
        buf.write("\6\4J\n\4\r\4\16\4K\3\4\3\4\6\4P\n\4\r\4\16\4Q\5\4T\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5_\n\5\3\6\3")
        buf.write("\6\3\6\7\6d\n\6\f\6\16\6g\13\6\3\6\3\6\3\6\3\6\7\6m\n")
        buf.write("\6\f\6\16\6p\13\6\3\6\5\6s\n\6\3\7\3\7\3\7\3\b\3\b\7\b")
        buf.write("z\n\b\f\b\16\b}\13\b\3\t\6\t\u0080\n\t\r\t\16\t\u0081")
        buf.write("\3\n\5\n\u0085\n\n\3\n\7\n\u0088\n\n\f\n\16\n\u008b\13")
        buf.write("\n\3\n\3\n\5\n\u008f\n\n\3\13\3\13\3\13\3\13\3\f\3\f\7")
        buf.write("\f\u0097\n\f\f\f\16\f\u009a\13\f\3\r\3\r\3\r\3\r\3\r\7")
        buf.write("\r\u00a1\n\r\f\r\16\r\u00a4\13\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\7\r\u00ae\n\r\f\r\16\r\u00b1\13\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\7\r\u00bb\n\r\f\r\16\r\u00be\13")
        buf.write("\r\3\r\3\r\3\r\5\r\u00c3\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00ce\n\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u00f5\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u00fc")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\5\u00a2\u00af\u00bc\2\36\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36\3\2\f\3\2\62;\4\2$$^^\4\2))^^\n\2")
        buf.write("$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\3\2\"\"\3\2")
        buf.write("\13\13\4\2\f\f\17\17\6\2\'\',-//\61\61\2\u0129\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\3;\3\2\2\2\5>\3\2\2\2\7F\3\2\2\2\t^\3\2\2")
        buf.write("\2\13r\3\2\2\2\rt\3\2\2\2\17w\3\2\2\2\21\177\3\2\2\2\23")
        buf.write("\u008e\3\2\2\2\25\u0090\3\2\2\2\27\u0094\3\2\2\2\31\u00c2")
        buf.write("\3\2\2\2\33\u00cd\3\2\2\2\35\u00cf\3\2\2\2\37\u00d1\3")
        buf.write("\2\2\2!\u00d3\3\2\2\2#\u00d5\3\2\2\2%\u00d7\3\2\2\2\'")
        buf.write("\u00da\3\2\2\2)\u00df\3\2\2\2+\u00e4\3\2\2\2-\u00e6\3")
        buf.write("\2\2\2/\u00e8\3\2\2\2\61\u00f4\3\2\2\2\63\u00fb\3\2\2")
        buf.write("\2\65\u00fd\3\2\2\2\67\u0101\3\2\2\29\u0107\3\2\2\2;<")
        buf.write("\7k\2\2<=\7p\2\2=\4\3\2\2\2>?\7t\2\2?@\7c\2\2@A\7p\2\2")
        buf.write("AB\7i\2\2BC\7g\2\2CD\7*\2\2D\6\3\2\2\2EG\7/\2\2FE\3\2")
        buf.write("\2\2FG\3\2\2\2GI\3\2\2\2HJ\t\2\2\2IH\3\2\2\2JK\3\2\2\2")
        buf.write("KI\3\2\2\2KL\3\2\2\2LS\3\2\2\2MO\7\60\2\2NP\t\2\2\2ON")
        buf.write("\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3\2\2\2SM\3\2")
        buf.write("\2\2ST\3\2\2\2T\b\3\2\2\2UV\7V\2\2VW\7t\2\2WX\7w\2\2X")
        buf.write("_\7g\2\2YZ\7H\2\2Z[\7c\2\2[\\\7n\2\2\\]\7u\2\2]_\7g\2")
        buf.write("\2^U\3\2\2\2^Y\3\2\2\2_\n\3\2\2\2`e\7$\2\2ad\5\r\7\2b")
        buf.write("d\n\3\2\2ca\3\2\2\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3")
        buf.write("\2\2\2fh\3\2\2\2ge\3\2\2\2hs\7$\2\2in\7)\2\2jm\5\r\7\2")
        buf.write("km\n\4\2\2lj\3\2\2\2lk\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3")
        buf.write("\2\2\2oq\3\2\2\2pn\3\2\2\2qs\7)\2\2r`\3\2\2\2ri\3\2\2")
        buf.write("\2s\f\3\2\2\2tu\7^\2\2uv\t\5\2\2v\16\3\2\2\2w{\t\6\2\2")
        buf.write("xz\t\7\2\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\20")
        buf.write("\3\2\2\2}{\3\2\2\2~\u0080\t\b\2\2\177~\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\22")
        buf.write("\3\2\2\2\u0083\u0085\7\17\2\2\u0084\u0083\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0089\3\2\2\2\u0086\u0088\t\b\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3")
        buf.write("\2\2\2\u0089\u008a\3\2\2\2\u008a\u008c\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008c\u008f\7\f\2\2\u008d\u008f\7\17\2\2\u008e")
        buf.write("\u0084\3\2\2\2\u008e\u008d\3\2\2\2\u008f\24\3\2\2\2\u0090")
        buf.write("\u0091\t\t\2\2\u0091\u0092\3\2\2\2\u0092\u0093\b\13\2")
        buf.write("\2\u0093\26\3\2\2\2\u0094\u0098\7%\2\2\u0095\u0097\n\n")
        buf.write("\2\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\30\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009b\u009c\7$\2\2\u009c\u009d\7$\2\2\u009d\u009e")
        buf.write("\7$\2\2\u009e\u00a2\3\2\2\2\u009f\u00a1\13\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a2\u00a0\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3")
        buf.write("\2\2\2\u00a5\u00a6\7$\2\2\u00a6\u00a7\7$\2\2\u00a7\u00c3")
        buf.write("\7$\2\2\u00a8\u00a9\7)\2\2\u00a9\u00aa\7)\2\2\u00aa\u00ab")
        buf.write("\7)\2\2\u00ab\u00af\3\2\2\2\u00ac\u00ae\13\2\2\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00af\u00ad\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b2\u00b3\7)\2\2\u00b3\u00b4\7)\2\2\u00b4\u00c3")
        buf.write("\7)\2\2\u00b5\u00b6\7b\2\2\u00b6\u00b7\7b\2\2\u00b7\u00b8")
        buf.write("\7b\2\2\u00b8\u00bc\3\2\2\2\u00b9\u00bb\13\2\2\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00bc\3")
        buf.write("\2\2\2\u00bf\u00c0\7b\2\2\u00c0\u00c1\7b\2\2\u00c1\u00c3")
        buf.write("\7b\2\2\u00c2\u009b\3\2\2\2\u00c2\u00a8\3\2\2\2\u00c2")
        buf.write("\u00b5\3\2\2\2\u00c3\32\3\2\2\2\u00c4\u00ce\7?\2\2\u00c5")
        buf.write("\u00c6\7-\2\2\u00c6\u00ce\7?\2\2\u00c7\u00c8\7/\2\2\u00c8")
        buf.write("\u00ce\7?\2\2\u00c9\u00ca\7,\2\2\u00ca\u00ce\7?\2\2\u00cb")
        buf.write("\u00cc\7\61\2\2\u00cc\u00ce\7?\2\2\u00cd\u00c4\3\2\2\2")
        buf.write("\u00cd\u00c5\3\2\2\2\u00cd\u00c7\3\2\2\2\u00cd\u00c9\3")
        buf.write("\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\34\3\2\2\2\u00cf\u00d0")
        buf.write("\t\13\2\2\u00d0\36\3\2\2\2\u00d1\u00d2\7]\2\2\u00d2 \3")
        buf.write("\2\2\2\u00d3\u00d4\7_\2\2\u00d4\"\3\2\2\2\u00d5\u00d6")
        buf.write("\7.\2\2\u00d6$\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7h\2\2\u00d9&\3\2\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7h\2\2\u00de(\3")
        buf.write("\2\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7u\2\2\u00e2\u00e3\7g\2\2\u00e3*\3\2\2\2\u00e4\u00e5")
        buf.write("\7<\2\2\u00e5,\3\2\2\2\u00e6\u00e7\7*\2\2\u00e7.\3\2\2")
        buf.write("\2\u00e8\u00e9\7+\2\2\u00e9\60\3\2\2\2\u00ea\u00eb\7?")
        buf.write("\2\2\u00eb\u00f5\7?\2\2\u00ec\u00ed\7#\2\2\u00ed\u00f5")
        buf.write("\7?\2\2\u00ee\u00f5\7>\2\2\u00ef\u00f0\7>\2\2\u00f0\u00f5")
        buf.write("\7?\2\2\u00f1\u00f5\7@\2\2\u00f2\u00f3\7@\2\2\u00f3\u00f5")
        buf.write("\7?\2\2\u00f4\u00ea\3\2\2\2\u00f4\u00ec\3\2\2\2\u00f4")
        buf.write("\u00ee\3\2\2\2\u00f4\u00ef\3\2\2\2\u00f4\u00f1\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f5\62\3\2\2\2\u00f6\u00f7\7c\2")
        buf.write("\2\u00f7\u00f8\7p\2\2\u00f8\u00fc\7f\2\2\u00f9\u00fa\7")
        buf.write("q\2\2\u00fa\u00fc\7t\2\2\u00fb\u00f6\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\64\3\2\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7v\2\2\u0100\66\3\2\2\2\u0101\u0102")
        buf.write("\7y\2\2\u0102\u0103\7j\2\2\u0103\u0104\7k\2\2\u0104\u0105")
        buf.write("\7n\2\2\u0105\u0106\7g\2\2\u01068\3\2\2\2\u0107\u0108")
        buf.write("\7h\2\2\u0108\u0109\7q\2\2\u0109\u010a\7t\2\2\u010a:\3")
        buf.write("\2\2\2\32\2FKQS^celnr{\u0081\u0084\u0089\u008e\u0098\u00a2")
        buf.write("\u00af\u00bc\u00c2\u00cd\u00f4\u00fb\3\b\2\2")
        return buf.getvalue()


class fullLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NUMBER = 3
    BOOLEAN = 4
    STRING = 5
    ESC = 6
    VARIABLE = 7
    WS = 8
    NEWLINE = 9
    WS_SKIPPED = 10
    SINGLE_LINE_COMMENT = 11
    MULTI_LINE_COMMENT = 12
    ASSIGNMENT_OP = 13
    ARITHMETIC_OP = 14
    LBRACKET = 15
    RBRACKET = 16
    COMMA = 17
    IF = 18
    ELIF = 19
    ELSE = 20
    COLON = 21
    LPAREN = 22
    RPAREN = 23
    COMPARISON_OP = 24
    LOGICAL_OP = 25
    NOT_OP = 26
    WHILE = 27
    FOR = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'in'", "'range('", "'['", "']'", "','", "'if'", "'elif'", "'else'", 
            "':'", "'('", "')'", "'not'", "'while'", "'for'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS", "NEWLINE", 
            "WS_SKIPPED", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "ASSIGNMENT_OP", 
            "ARITHMETIC_OP", "LBRACKET", "RBRACKET", "COMMA", "IF", "ELIF", 
            "ELSE", "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
            "NOT_OP", "WHILE", "FOR" ]

    ruleNames = [ "T__0", "T__1", "NUMBER", "BOOLEAN", "STRING", "ESC", 
                  "VARIABLE", "WS", "NEWLINE", "WS_SKIPPED", "SINGLE_LINE_COMMENT", 
                  "MULTI_LINE_COMMENT", "ASSIGNMENT_OP", "ARITHMETIC_OP", 
                  "LBRACKET", "RBRACKET", "COMMA", "IF", "ELIF", "ELSE", 
                  "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
                  "NOT_OP", "WHILE", "FOR" ]

    grammarFileName = "full.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


