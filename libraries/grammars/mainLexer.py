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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u00ee\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3C\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16j\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\5\17q\n\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\5\23\u0082\n")
        buf.write("\23\3\23\6\23\u0085\n\23\r\23\16\23\u0086\3\23\3\23\6")
        buf.write("\23\u008b\n\23\r\23\16\23\u008c\5\23\u008f\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u009a\n\24")
        buf.write("\3\25\3\25\3\25\7\25\u009f\n\25\f\25\16\25\u00a2\13\25")
        buf.write("\3\25\3\25\3\25\3\25\7\25\u00a8\n\25\f\25\16\25\u00ab")
        buf.write("\13\25\3\25\5\25\u00ae\n\25\3\26\3\26\3\26\3\27\3\27\7")
        buf.write("\27\u00b5\n\27\f\27\16\27\u00b8\13\27\3\30\6\30\u00bb")
        buf.write("\n\30\r\30\16\30\u00bc\3\31\3\31\7\31\u00c1\n\31\f\31")
        buf.write("\16\31\u00c4\13\31\3\32\3\32\3\32\3\32\3\32\7\32\u00cb")
        buf.write("\n\32\f\32\16\32\u00ce\13\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\7\32\u00d8\n\32\f\32\16\32\u00db\13\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u00e5\n")
        buf.write("\32\f\32\16\32\u00e8\13\32\3\32\3\32\3\32\5\32\u00ed\n")
        buf.write("\32\5\u00cc\u00d9\u00e6\2\33\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\3\2\f\4\2\13")
        buf.write("\f\17\17\6\2\'\',-//\61\61\3\2\62;\4\2$$^^\4\2))^^\n\2")
        buf.write("$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\3\2\"\"\4\2")
        buf.write("\f\f\17\17\2\u0109\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\3")
        buf.write("\65\3\2\2\2\5B\3\2\2\2\7D\3\2\2\2\tF\3\2\2\2\13H\3\2\2")
        buf.write("\2\rJ\3\2\2\2\17L\3\2\2\2\21O\3\2\2\2\23T\3\2\2\2\25Y")
        buf.write("\3\2\2\2\27[\3\2\2\2\31]\3\2\2\2\33i\3\2\2\2\35p\3\2\2")
        buf.write("\2\37r\3\2\2\2!v\3\2\2\2#|\3\2\2\2%\u0081\3\2\2\2\'\u0099")
        buf.write("\3\2\2\2)\u00ad\3\2\2\2+\u00af\3\2\2\2-\u00b2\3\2\2\2")
        buf.write("/\u00ba\3\2\2\2\61\u00be\3\2\2\2\63\u00ec\3\2\2\2\65\66")
        buf.write("\t\2\2\2\66\67\3\2\2\2\678\b\2\2\28\4\3\2\2\29C\7?\2\2")
        buf.write(":;\7-\2\2;C\7?\2\2<=\7/\2\2=C\7?\2\2>?\7,\2\2?C\7?\2\2")
        buf.write("@A\7\61\2\2AC\7?\2\2B9\3\2\2\2B:\3\2\2\2B<\3\2\2\2B>\3")
        buf.write("\2\2\2B@\3\2\2\2C\6\3\2\2\2DE\t\3\2\2E\b\3\2\2\2FG\7]")
        buf.write("\2\2G\n\3\2\2\2HI\7_\2\2I\f\3\2\2\2JK\7.\2\2K\16\3\2\2")
        buf.write("\2LM\7k\2\2MN\7h\2\2N\20\3\2\2\2OP\7g\2\2PQ\7n\2\2QR\7")
        buf.write("k\2\2RS\7h\2\2S\22\3\2\2\2TU\7g\2\2UV\7n\2\2VW\7u\2\2")
        buf.write("WX\7g\2\2X\24\3\2\2\2YZ\7<\2\2Z\26\3\2\2\2[\\\7*\2\2\\")
        buf.write("\30\3\2\2\2]^\7+\2\2^\32\3\2\2\2_`\7?\2\2`j\7?\2\2ab\7")
        buf.write("#\2\2bj\7?\2\2cj\7>\2\2de\7>\2\2ej\7?\2\2fj\7@\2\2gh\7")
        buf.write("@\2\2hj\7?\2\2i_\3\2\2\2ia\3\2\2\2ic\3\2\2\2id\3\2\2\2")
        buf.write("if\3\2\2\2ig\3\2\2\2j\34\3\2\2\2kl\7c\2\2lm\7p\2\2mq\7")
        buf.write("f\2\2no\7q\2\2oq\7t\2\2pk\3\2\2\2pn\3\2\2\2q\36\3\2\2")
        buf.write("\2rs\7p\2\2st\7q\2\2tu\7v\2\2u \3\2\2\2vw\7y\2\2wx\7j")
        buf.write("\2\2xy\7k\2\2yz\7n\2\2z{\7g\2\2{\"\3\2\2\2|}\7h\2\2}~")
        buf.write("\7q\2\2~\177\7t\2\2\177$\3\2\2\2\u0080\u0082\7/\2\2\u0081")
        buf.write("\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2")
        buf.write("\u0083\u0085\t\4\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3")
        buf.write("\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u008e")
        buf.write("\3\2\2\2\u0088\u008a\7\60\2\2\u0089\u008b\t\4\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u0088\3")
        buf.write("\2\2\2\u008e\u008f\3\2\2\2\u008f&\3\2\2\2\u0090\u0091")
        buf.write("\7V\2\2\u0091\u0092\7t\2\2\u0092\u0093\7w\2\2\u0093\u009a")
        buf.write("\7g\2\2\u0094\u0095\7H\2\2\u0095\u0096\7c\2\2\u0096\u0097")
        buf.write("\7n\2\2\u0097\u0098\7u\2\2\u0098\u009a\7g\2\2\u0099\u0090")
        buf.write("\3\2\2\2\u0099\u0094\3\2\2\2\u009a(\3\2\2\2\u009b\u00a0")
        buf.write("\7$\2\2\u009c\u009f\5+\26\2\u009d\u009f\n\5\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a2\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3")
        buf.write("\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00ae\7$\2\2\u00a4\u00a9")
        buf.write("\7)\2\2\u00a5\u00a8\5+\26\2\u00a6\u00a8\n\6\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ae\7)\2\2\u00ad\u009b")
        buf.write("\3\2\2\2\u00ad\u00a4\3\2\2\2\u00ae*\3\2\2\2\u00af\u00b0")
        buf.write("\7^\2\2\u00b0\u00b1\t\7\2\2\u00b1,\3\2\2\2\u00b2\u00b6")
        buf.write("\t\b\2\2\u00b3\u00b5\t\t\2\2\u00b4\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7.\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00bb\t\n\2")
        buf.write("\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\60\3\2\2\2\u00be\u00c2")
        buf.write("\7%\2\2\u00bf\u00c1\n\13\2\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write("\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\62\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c6\7$\2")
        buf.write("\2\u00c6\u00c7\7$\2\2\u00c7\u00c8\7$\2\2\u00c8\u00cc\3")
        buf.write("\2\2\2\u00c9\u00cb\13\2\2\2\u00ca\u00c9\3\2\2\2\u00cb")
        buf.write("\u00ce\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7")
        buf.write("$\2\2\u00d0\u00d1\7$\2\2\u00d1\u00ed\7$\2\2\u00d2\u00d3")
        buf.write("\7)\2\2\u00d3\u00d4\7)\2\2\u00d4\u00d5\7)\2\2\u00d5\u00d9")
        buf.write("\3\2\2\2\u00d6\u00d8\13\2\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\u00db\3\2\2\2\u00d9\u00da\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\7")
        buf.write(")\2\2\u00dd\u00de\7)\2\2\u00de\u00ed\7)\2\2\u00df\u00e0")
        buf.write("\7b\2\2\u00e0\u00e1\7b\2\2\u00e1\u00e2\7b\2\2\u00e2\u00e6")
        buf.write("\3\2\2\2\u00e3\u00e5\13\2\2\2\u00e4\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e8\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2")
        buf.write("\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\7")
        buf.write("b\2\2\u00ea\u00eb\7b\2\2\u00eb\u00ed\7b\2\2\u00ec\u00c5")
        buf.write("\3\2\2\2\u00ec\u00d2\3\2\2\2\u00ec\u00df\3\2\2\2\u00ed")
        buf.write("\64\3\2\2\2\27\2Bip\u0081\u0086\u008c\u008e\u0099\u009e")
        buf.write("\u00a0\u00a7\u00a9\u00ad\u00b6\u00bc\u00c2\u00cc\u00d9")
        buf.write("\u00e6\u00ec\3\b\2\2")
        return buf.getvalue()


class mainLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS_SKIPPED = 1
    ASSIGNMENT_OP = 2
    ARITHMETIC_OP = 3
    LBRACKET = 4
    RBRACKET = 5
    COMMA = 6
    IF = 7
    ELIF = 8
    ELSE = 9
    COLON = 10
    LPAREN = 11
    RPAREN = 12
    COMPARISON_OP = 13
    LOGICAL_OP = 14
    NOT_OP = 15
    WHILE = 16
    FOR = 17
    NUMBER = 18
    BOOLEAN = 19
    STRING = 20
    ESC = 21
    VARIABLE = 22
    WS = 23
    SINGLE_LINE_COMMENT = 24
    MULTI_LINE_COMMENT = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "','", "'if'", "'elif'", "'else'", "':'", "'('", 
            "')'", "'not'", "'while'", "'for'" ]

    symbolicNames = [ "<INVALID>",
            "WS_SKIPPED", "ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", 
            "RBRACKET", "COMMA", "IF", "ELIF", "ELSE", "COLON", "LPAREN", 
            "RPAREN", "COMPARISON_OP", "LOGICAL_OP", "NOT_OP", "WHILE", 
            "FOR", "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS", 
            "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

    ruleNames = [ "WS_SKIPPED", "ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", 
                  "RBRACKET", "COMMA", "IF", "ELIF", "ELSE", "COLON", "LPAREN", 
                  "RPAREN", "COMPARISON_OP", "LOGICAL_OP", "NOT_OP", "WHILE", 
                  "FOR", "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", 
                  "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

    grammarFileName = "main.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


