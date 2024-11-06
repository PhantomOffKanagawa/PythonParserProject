# Generated from ./grammars/full.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("\u0122\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\5\2-\n\2\3\2\3\2\5\2\61\n")
        buf.write("\2\3\2\3\2\3\3\3\3\5\3\67\n\3\3\3\3\3\5\3;\n\3\3\3\3\3")
        buf.write("\5\3?\n\3\7\3A\n\3\f\3\16\3D\13\3\3\4\3\4\5\4H\n\4\3\4")
        buf.write("\3\4\5\4L\n\4\3\4\3\4\5\4P\n\4\3\4\3\4\5\4T\n\4\7\4V\n")
        buf.write("\4\f\4\16\4Y\13\4\5\4[\n\4\3\4\5\4^\n\4\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6m\n\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\5\nv\n\n\3\n\3\n\5\nz\n\n\3\n\3")
        buf.write("\n\5\n~\n\n\3\n\7\n\u0081\n\n\f\n\16\n\u0084\13\n\3\13")
        buf.write("\3\13\5\13\u0088\n\13\3\13\3\13\3\13\5\13\u008d\n\13\3")
        buf.write("\13\3\13\5\13\u0091\n\13\3\13\3\13\3\13\5\13\u0096\n\13")
        buf.write("\3\f\3\f\5\f\u009a\n\f\3\r\3\r\3\r\3\16\5\16\u00a0\n\16")
        buf.write("\3\16\3\16\5\16\u00a4\n\16\3\16\3\16\7\16\u00a8\n\16\f")
        buf.write("\16\16\16\u00ab\13\16\3\16\5\16\u00ae\n\16\3\16\3\16\5")
        buf.write("\16\u00b2\n\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00ba")
        buf.write("\n\17\3\20\3\20\3\21\3\21\5\21\u00c0\n\21\3\21\3\21\5")
        buf.write("\21\u00c4\n\21\3\21\3\21\5\21\u00c8\n\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00cf\n\21\3\21\3\21\5\21\u00d3\n\21\3")
        buf.write("\21\3\21\3\21\7\21\u00d8\n\21\f\21\16\21\u00db\13\21\3")
        buf.write("\21\3\21\5\21\u00df\n\21\3\21\3\21\5\21\u00e3\n\21\3\21")
        buf.write("\3\21\5\21\u00e7\n\21\3\22\3\22\5\22\u00eb\n\22\3\22\3")
        buf.write("\22\5\22\u00ef\n\22\3\22\3\22\5\22\u00f3\n\22\3\22\3\22")
        buf.write("\3\23\3\23\5\23\u00f9\n\23\3\23\3\23\5\23\u00fd\n\23\3")
        buf.write("\23\3\23\5\23\u0101\n\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u010f\n\25\3\25\3")
        buf.write("\25\5\25\u0113\n\25\3\25\3\25\5\25\u0117\n\25\3\25\3\25")
        buf.write("\5\25\u011b\n\25\3\25\3\25\3\25\5\25\u0120\n\25\3\25\2")
        buf.write("\2\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(\2\5")
        buf.write("\4\2\5\5\t\t\3\2\32\33\3\2\r\16\2\u0148\2*\3\2\2\2\4\64")
        buf.write("\3\2\2\2\6E\3\2\2\2\ba\3\2\2\2\nl\3\2\2\2\fn\3\2\2\2\16")
        buf.write("p\3\2\2\2\20r\3\2\2\2\22u\3\2\2\2\24\u0095\3\2\2\2\26")
        buf.write("\u0099\3\2\2\2\30\u009b\3\2\2\2\32\u00a9\3\2\2\2\34\u00b9")
        buf.write("\3\2\2\2\36\u00bb\3\2\2\2 \u00bd\3\2\2\2\"\u00e8\3\2\2")
        buf.write("\2$\u00f6\3\2\2\2&\u0104\3\2\2\2(\u011f\3\2\2\2*,\7\t")
        buf.write("\2\2+-\7\n\2\2,+\3\2\2\2,-\3\2\2\2-.\3\2\2\2.\60\5\f\7")
        buf.write("\2/\61\7\n\2\2\60/\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2")
        buf.write("\62\63\5\4\3\2\63\3\3\2\2\2\64\66\5\n\6\2\65\67\7\n\2")
        buf.write("\2\66\65\3\2\2\2\66\67\3\2\2\2\67B\3\2\2\28:\5\16\b\2")
        buf.write("9;\7\n\2\2:9\3\2\2\2:;\3\2\2\2;<\3\2\2\2<>\5\n\6\2=?\7")
        buf.write("\n\2\2>=\3\2\2\2>?\3\2\2\2?A\3\2\2\2@8\3\2\2\2AD\3\2\2")
        buf.write("\2B@\3\2\2\2BC\3\2\2\2C\5\3\2\2\2DB\3\2\2\2EZ\7\21\2\2")
        buf.write("FH\7\n\2\2GF\3\2\2\2GH\3\2\2\2HI\3\2\2\2IK\5\n\6\2JL\7")
        buf.write("\n\2\2KJ\3\2\2\2KL\3\2\2\2LW\3\2\2\2MO\7\23\2\2NP\7\n")
        buf.write("\2\2ON\3\2\2\2OP\3\2\2\2PQ\3\2\2\2QS\5\n\6\2RT\7\n\2\2")
        buf.write("SR\3\2\2\2ST\3\2\2\2TV\3\2\2\2UM\3\2\2\2VY\3\2\2\2WU\3")
        buf.write("\2\2\2WX\3\2\2\2X[\3\2\2\2YW\3\2\2\2ZG\3\2\2\2Z[\3\2\2")
        buf.write("\2[]\3\2\2\2\\^\7\n\2\2]\\\3\2\2\2]^\3\2\2\2^_\3\2\2\2")
        buf.write("_`\7\22\2\2`\7\3\2\2\2ab\t\2\2\2b\t\3\2\2\2cm\7\5\2\2")
        buf.write("dm\7\t\2\2em\7\6\2\2fm\7\7\2\2gh\7\30\2\2hi\5\4\3\2ij")
        buf.write("\7\31\2\2jm\3\2\2\2km\5\6\4\2lc\3\2\2\2ld\3\2\2\2le\3")
        buf.write("\2\2\2lf\3\2\2\2lg\3\2\2\2lk\3\2\2\2m\13\3\2\2\2no\7\17")
        buf.write("\2\2o\r\3\2\2\2pq\7\20\2\2q\17\3\2\2\2rs\5\22\n\2s\21")
        buf.write("\3\2\2\2tv\7\n\2\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2\2w\u0082")
        buf.write("\5\24\13\2xz\7\n\2\2yx\3\2\2\2yz\3\2\2\2z{\3\2\2\2{}\t")
        buf.write("\3\2\2|~\7\n\2\2}|\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0081\5\24\13\2\u0080y\3\2\2\2\u0081\u0084\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\23\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0085\u0087\7\34\2\2\u0086\u0088\7\n\2")
        buf.write("\2\u0087\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u0096\5\24\13\2\u008a\u008c\7\30\2\2\u008b")
        buf.write("\u008d\7\n\2\2\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u0090\5\22\n\2\u008f\u0091")
        buf.write("\7\n\2\2\u0090\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\u0093\7\31\2\2\u0093\u0096\3\2\2")
        buf.write("\2\u0094\u0096\5\n\6\2\u0095\u0085\3\2\2\2\u0095\u008a")
        buf.write("\3\2\2\2\u0095\u0094\3\2\2\2\u0096\25\3\2\2\2\u0097\u009a")
        buf.write("\5\30\r\2\u0098\u009a\7\2\2\3\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\27\3\2\2\2\u009b\u009c\5\32\16\2")
        buf.write("\u009c\u009d\7\2\2\3\u009d\31\3\2\2\2\u009e\u00a0\7\n")
        buf.write("\2\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\u00a3\5\34\17\2\u00a2\u00a4\7\n\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a6\7\13\2\2\u00a6\u00a8\3\2\2\2\u00a7\u009f")
        buf.write("\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ac\u00ae\7\n\2\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3")
        buf.write("\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\5\34\17\2\u00b0")
        buf.write("\u00b2\7\n\2\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\33\3\2\2\2\u00b3\u00ba\5\2\2\2\u00b4\u00ba\5\36")
        buf.write("\20\2\u00b5\u00ba\5 \21\2\u00b6\u00ba\5\"\22\2\u00b7\u00ba")
        buf.write("\5$\23\2\u00b8\u00ba\3\2\2\2\u00b9\u00b3\3\2\2\2\u00b9")
        buf.write("\u00b4\3\2\2\2\u00b9\u00b5\3\2\2\2\u00b9\u00b6\3\2\2\2")
        buf.write("\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\35\3\2")
        buf.write("\2\2\u00bb\u00bc\t\4\2\2\u00bc\37\3\2\2\2\u00bd\u00bf")
        buf.write("\7\24\2\2\u00be\u00c0\7\n\2\2\u00bf\u00be\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\5\20\t")
        buf.write("\2\u00c2\u00c4\7\n\2\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\7\27\2\2\u00c6")
        buf.write("\u00c8\7\n\2\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\u00ca\7\13\2\2\u00ca\u00d9")
        buf.write("\5\32\16\2\u00cb\u00cc\7\25\2\2\u00cc\u00ce\5\20\t\2\u00cd")
        buf.write("\u00cf\7\n\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00d2\7\27\2\2\u00d1\u00d3")
        buf.write("\7\n\2\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d5\7\13\2\2\u00d5\u00d6\5\32\16")
        buf.write("\2\u00d6\u00d8\3\2\2\2\u00d7\u00cb\3\2\2\2\u00d8\u00db")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00e6\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00de\7\26\2")
        buf.write("\2\u00dd\u00df\7\n\2\2\u00de\u00dd\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e2\7\27\2\2\u00e1")
        buf.write("\u00e3\7\n\2\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7\13\2\2\u00e5\u00e7")
        buf.write("\5\32\16\2\u00e6\u00dc\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("!\3\2\2\2\u00e8\u00ea\7\35\2\2\u00e9\u00eb\7\n\2\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ee\5\20\t\2\u00ed\u00ef\7\n\2\2\u00ee\u00ed")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f2\7\27\2\2\u00f1\u00f3\7\n\2\2\u00f2\u00f1\3\2\2")
        buf.write("\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5")
        buf.write("\5\32\16\2\u00f5#\3\2\2\2\u00f6\u00f8\7\36\2\2\u00f7\u00f9")
        buf.write("\7\n\2\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00fa\3\2\2\2\u00fa\u00fc\5&\24\2\u00fb\u00fd\7\n\2\2")
        buf.write("\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\3")
        buf.write("\2\2\2\u00fe\u0100\7\27\2\2\u00ff\u0101\7\n\2\2\u0100")
        buf.write("\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0103\5\32\16\2\u0103%\3\2\2\2\u0104\u0105\7\t")
        buf.write("\2\2\u0105\u0106\7\n\2\2\u0106\u0107\7\3\2\2\u0107\u0108")
        buf.write("\7\n\2\2\u0108\u0109\5(\25\2\u0109\'\3\2\2\2\u010a\u0120")
        buf.write("\7\t\2\2\u010b\u0120\5\6\4\2\u010c\u010e\7\4\2\2\u010d")
        buf.write("\u010f\7\n\2\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0110\3\2\2\2\u0110\u0112\5\b\5\2\u0111\u0113\7")
        buf.write("\n\2\2\u0112\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u0114\u0116\7\23\2\2\u0115\u0117\7\n\2\2\u0116")
        buf.write("\u0115\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2")
        buf.write("\u0118\u011a\5\b\5\2\u0119\u011b\7\n\2\2\u011a\u0119\3")
        buf.write("\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d")
        buf.write("\b\25\1\2\u011d\u011e\7\31\2\2\u011e\u0120\3\2\2\2\u011f")
        buf.write("\u010a\3\2\2\2\u011f\u010b\3\2\2\2\u011f\u010c\3\2\2\2")
        buf.write("\u0120)\3\2\2\2\63,\60\66:>BGKOSWZ]luy}\u0082\u0087\u008c")
        buf.write("\u0090\u0095\u0099\u009f\u00a3\u00a9\u00ad\u00b1\u00b9")
        buf.write("\u00bf\u00c3\u00c7\u00ce\u00d2\u00d9\u00de\u00e2\u00e6")
        buf.write("\u00ea\u00ee\u00f2\u00f8\u00fc\u0100\u010e\u0112\u0116")
        buf.write("\u011a\u011f")
        return buf.getvalue()


class fullParser ( Parser ):

    grammarFileName = "full.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'in'", "'range('", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "','", "'if'", 
                     "'elif'", "'else'", "':'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "'not'", "'while'", "'for'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "BOOLEAN", 
                      "STRING", "ESC", "VARIABLE", "WS", "NEWLINE", "WS_SKIPPED", 
                      "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "ASSIGNMENT_OP", 
                      "ARITHMETIC_OP", "LBRACKET", "RBRACKET", "COMMA", 
                      "IF", "ELIF", "ELSE", "COLON", "LPAREN", "RPAREN", 
                      "COMPARISON_OP", "LOGICAL_OP", "NOT_OP", "WHILE", 
                      "FOR" ]

    RULE_assignment = 0
    RULE_expression = 1
    RULE_array = 2
    RULE_count = 3
    RULE_value = 4
    RULE_assignment_operator = 5
    RULE_operator = 6
    RULE_condition = 7
    RULE_logical_condition = 8
    RULE_comparison_condition = 9
    RULE_stat = 10
    RULE_expr = 11
    RULE_block = 12
    RULE_line = 13
    RULE_comment = 14
    RULE_if_block = 15
    RULE_while_block = 16
    RULE_for_block = 17
    RULE_for_condition = 18
    RULE_iterable = 19

    ruleNames =  [ "assignment", "expression", "array", "count", "value", 
                   "assignment_operator", "operator", "condition", "logical_condition", 
                   "comparison_condition", "stat", "expr", "block", "line", 
                   "comment", "if_block", "while_block", "for_block", "for_condition", 
                   "iterable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUMBER=3
    BOOLEAN=4
    STRING=5
    ESC=6
    VARIABLE=7
    WS=8
    NEWLINE=9
    WS_SKIPPED=10
    SINGLE_LINE_COMMENT=11
    MULTI_LINE_COMMENT=12
    ASSIGNMENT_OP=13
    ARITHMETIC_OP=14
    LBRACKET=15
    RBRACKET=16
    COMMA=17
    IF=18
    ELIF=19
    ELSE=20
    COLON=21
    LPAREN=22
    RPAREN=23
    COMPARISON_OP=24
    LOGICAL_OP=25
    NOT_OP=26
    WHILE=27
    FOR=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(fullParser.VARIABLE, 0)

        def assignment_operator(self):
            return self.getTypedRuleContext(fullParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(fullParser.ExpressionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def getRuleIndex(self):
            return fullParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = fullParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(fullParser.VARIABLE)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 41
                self.match(fullParser.WS)


            self.state = 44
            self.assignment_operator()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 45
                self.match(fullParser.WS)


            self.state = 48
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
                return self.getTypedRuleContexts(fullParser.ValueContext)
            else:
                return self.getTypedRuleContext(fullParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fullParser.OperatorContext)
            else:
                return self.getTypedRuleContext(fullParser.OperatorContext,i)


        def getRuleIndex(self):
            return fullParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = fullParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.value()
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 51
                self.match(fullParser.WS)


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fullParser.ARITHMETIC_OP:
                self.state = 54
                self.operator()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 55
                    self.match(fullParser.WS)


                self.state = 58
                self.value()
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 59
                    self.match(fullParser.WS)


                self.state = 66
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
            return self.getToken(fullParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(fullParser.RBRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fullParser.ValueContext)
            else:
                return self.getTypedRuleContext(fullParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.COMMA)
            else:
                return self.getToken(fullParser.COMMA, i)

        def getRuleIndex(self):
            return fullParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = fullParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(fullParser.LBRACKET)
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 68
                    self.match(fullParser.WS)


                self.state = 71
                self.value()
                self.state = 73
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 72
                    self.match(fullParser.WS)


                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fullParser.COMMA:
                    self.state = 75
                    self.match(fullParser.COMMA)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==fullParser.WS:
                        self.state = 76
                        self.match(fullParser.WS)


                    self.state = 79
                    self.value()
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 80
                        self.match(fullParser.WS)


                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 90
                self.match(fullParser.WS)


            self.state = 93
            self.match(fullParser.RBRACKET)
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
            return self.getToken(fullParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(fullParser.VARIABLE, 0)

        def getRuleIndex(self):
            return fullParser.RULE_count

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCount" ):
                listener.enterCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCount" ):
                listener.exitCount(self)




    def count(self):

        localctx = fullParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_count)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not(_la==fullParser.NUMBER or _la==fullParser.VARIABLE):
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
            return self.getToken(fullParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(fullParser.VARIABLE, 0)

        def BOOLEAN(self):
            return self.getToken(fullParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(fullParser.STRING, 0)

        def LPAREN(self):
            return self.getToken(fullParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(fullParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(fullParser.RPAREN, 0)

        def array(self):
            return self.getTypedRuleContext(fullParser.ArrayContext,0)


        def getRuleIndex(self):
            return fullParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = fullParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fullParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(fullParser.NUMBER)
                pass
            elif token in [fullParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(fullParser.VARIABLE)
                pass
            elif token in [fullParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.match(fullParser.BOOLEAN)
                pass
            elif token in [fullParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 100
                self.match(fullParser.STRING)
                pass
            elif token in [fullParser.LPAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.match(fullParser.LPAREN)
                self.state = 102
                self.expression()
                self.state = 103
                self.match(fullParser.RPAREN)
                pass
            elif token in [fullParser.LBRACKET]:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
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
            return self.getToken(fullParser.ASSIGNMENT_OP, 0)

        def getRuleIndex(self):
            return fullParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = fullParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(fullParser.ASSIGNMENT_OP)
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
            return self.getToken(fullParser.ARITHMETIC_OP, 0)

        def getRuleIndex(self):
            return fullParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = fullParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(fullParser.ARITHMETIC_OP)
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

        def logical_condition(self):
            return self.getTypedRuleContext(fullParser.Logical_conditionContext,0)


        def getRuleIndex(self):
            return fullParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = fullParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.logical_condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Logical_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fullParser.Comparison_conditionContext)
            else:
                return self.getTypedRuleContext(fullParser.Comparison_conditionContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.LOGICAL_OP)
            else:
                return self.getToken(fullParser.LOGICAL_OP, i)

        def COMPARISON_OP(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.COMPARISON_OP)
            else:
                return self.getToken(fullParser.COMPARISON_OP, i)

        def getRuleIndex(self):
            return fullParser.RULE_logical_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_condition" ):
                listener.enterLogical_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_condition" ):
                listener.exitLogical_condition(self)




    def logical_condition(self):

        localctx = fullParser.Logical_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logical_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 114
                self.match(fullParser.WS)


            self.state = 117
            self.comparison_condition()
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==fullParser.WS:
                        self.state = 118
                        self.match(fullParser.WS)


                    self.state = 121
                    _la = self._input.LA(1)
                    if not(_la==fullParser.COMPARISON_OP or _la==fullParser.LOGICAL_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==fullParser.WS:
                        self.state = 122
                        self.match(fullParser.WS)


                    self.state = 125
                    self.comparison_condition() 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            return self.getToken(fullParser.NOT_OP, 0)

        def comparison_condition(self):
            return self.getTypedRuleContext(fullParser.Comparison_conditionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def LPAREN(self):
            return self.getToken(fullParser.LPAREN, 0)

        def logical_condition(self):
            return self.getTypedRuleContext(fullParser.Logical_conditionContext,0)


        def RPAREN(self):
            return self.getToken(fullParser.RPAREN, 0)

        def value(self):
            return self.getTypedRuleContext(fullParser.ValueContext,0)


        def getRuleIndex(self):
            return fullParser.RULE_comparison_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_condition" ):
                listener.enterComparison_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_condition" ):
                listener.exitComparison_condition(self)




    def comparison_condition(self):

        localctx = fullParser.Comparison_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparison_condition)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(fullParser.NOT_OP)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 132
                    self.match(fullParser.WS)


                self.state = 135
                self.comparison_condition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(fullParser.LPAREN)
                self.state = 138
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 137
                    self.match(fullParser.WS)


                self.state = 140
                self.logical_condition()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 141
                    self.match(fullParser.WS)


                self.state = 144
                self.match(fullParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.value()
                pass


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
            return self.getTypedRuleContext(fullParser.ExprContext,0)


        def EOF(self):
            return self.getToken(fullParser.EOF, 0)

        def getRuleIndex(self):
            return fullParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = fullParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stat)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(fullParser.EOF)
                pass


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

        def block(self):
            return self.getTypedRuleContext(fullParser.BlockContext,0)


        def EOF(self):
            return self.getToken(fullParser.EOF, 0)

        def getRuleIndex(self):
            return fullParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = fullParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.block()
            self.state = 154
            self.match(fullParser.EOF)
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

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fullParser.LineContext)
            else:
                return self.getTypedRuleContext(fullParser.LineContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.NEWLINE)
            else:
                return self.getToken(fullParser.NEWLINE, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def getRuleIndex(self):
            return fullParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = fullParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 157
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        self.state = 156
                        self.match(fullParser.WS)


                    self.state = 159
                    self.line()
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==fullParser.WS:
                        self.state = 160
                        self.match(fullParser.WS)


                    self.state = 163
                    self.match(fullParser.NEWLINE) 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 170
                self.match(fullParser.WS)


            self.state = 173
            self.line()
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 174
                self.match(fullParser.WS)


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
            return self.getTypedRuleContext(fullParser.AssignmentContext,0)


        def comment(self):
            return self.getTypedRuleContext(fullParser.CommentContext,0)


        def if_block(self):
            return self.getTypedRuleContext(fullParser.If_blockContext,0)


        def while_block(self):
            return self.getTypedRuleContext(fullParser.While_blockContext,0)


        def for_block(self):
            return self.getTypedRuleContext(fullParser.For_blockContext,0)


        def getRuleIndex(self):
            return fullParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = fullParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_line)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fullParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.assignment()
                pass
            elif token in [fullParser.SINGLE_LINE_COMMENT, fullParser.MULTI_LINE_COMMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.comment()
                pass
            elif token in [fullParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.if_block()
                pass
            elif token in [fullParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.while_block()
                pass
            elif token in [fullParser.FOR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 181
                self.for_block()
                pass
            elif token in [fullParser.EOF, fullParser.WS, fullParser.NEWLINE, fullParser.ELIF, fullParser.ELSE]:
                self.enterOuterAlt(localctx, 6)

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
            return self.getToken(fullParser.SINGLE_LINE_COMMENT, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(fullParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return fullParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = fullParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==fullParser.SINGLE_LINE_COMMENT or _la==fullParser.MULTI_LINE_COMMENT):
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
            return self.getToken(fullParser.IF, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fullParser.ConditionContext)
            else:
                return self.getTypedRuleContext(fullParser.ConditionContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.COLON)
            else:
                return self.getToken(fullParser.COLON, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.NEWLINE)
            else:
                return self.getToken(fullParser.NEWLINE, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fullParser.BlockContext)
            else:
                return self.getTypedRuleContext(fullParser.BlockContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.ELIF)
            else:
                return self.getToken(fullParser.ELIF, i)

        def ELSE(self):
            return self.getToken(fullParser.ELSE, 0)

        def getRuleIndex(self):
            return fullParser.RULE_if_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_block" ):
                listener.enterIf_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_block" ):
                listener.exitIf_block(self)




    def if_block(self):

        localctx = fullParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(fullParser.IF)
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 188
                self.match(fullParser.WS)


            self.state = 191
            self.condition()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 192
                self.match(fullParser.WS)


            self.state = 195
            self.match(fullParser.COLON)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 196
                self.match(fullParser.WS)


            self.state = 199
            self.match(fullParser.NEWLINE)
            self.state = 200
            self.block()
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 201
                    self.match(fullParser.ELIF)
                    self.state = 202
                    self.condition()
                    self.state = 204
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==fullParser.WS:
                        self.state = 203
                        self.match(fullParser.WS)


                    self.state = 206
                    self.match(fullParser.COLON)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==fullParser.WS:
                        self.state = 207
                        self.match(fullParser.WS)


                    self.state = 210
                    self.match(fullParser.NEWLINE)
                    self.state = 211
                    self.block() 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 218
                self.match(fullParser.ELSE)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 219
                    self.match(fullParser.WS)


                self.state = 222
                self.match(fullParser.COLON)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 223
                    self.match(fullParser.WS)


                self.state = 226
                self.match(fullParser.NEWLINE)
                self.state = 227
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
            return self.getToken(fullParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(fullParser.ConditionContext,0)


        def COLON(self):
            return self.getToken(fullParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(fullParser.BlockContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def getRuleIndex(self):
            return fullParser.RULE_while_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_block" ):
                listener.enterWhile_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_block" ):
                listener.exitWhile_block(self)




    def while_block(self):

        localctx = fullParser.While_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_while_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(fullParser.WHILE)
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 231
                self.match(fullParser.WS)


            self.state = 234
            self.condition()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 235
                self.match(fullParser.WS)


            self.state = 238
            self.match(fullParser.COLON)
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 239
                self.match(fullParser.WS)


            self.state = 242
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
            return self.getToken(fullParser.FOR, 0)

        def for_condition(self):
            return self.getTypedRuleContext(fullParser.For_conditionContext,0)


        def COLON(self):
            return self.getToken(fullParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(fullParser.BlockContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def getRuleIndex(self):
            return fullParser.RULE_for_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_block" ):
                listener.enterFor_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_block" ):
                listener.exitFor_block(self)




    def for_block(self):

        localctx = fullParser.For_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(fullParser.FOR)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 245
                self.match(fullParser.WS)


            self.state = 248
            self.for_condition()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==fullParser.WS:
                self.state = 249
                self.match(fullParser.WS)


            self.state = 252
            self.match(fullParser.COLON)
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(fullParser.WS)


            self.state = 256
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
            return self.getToken(fullParser.VARIABLE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def iterable(self):
            return self.getTypedRuleContext(fullParser.IterableContext,0)


        def getRuleIndex(self):
            return fullParser.RULE_for_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_condition" ):
                listener.enterFor_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_condition" ):
                listener.exitFor_condition(self)




    def for_condition(self):

        localctx = fullParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(fullParser.VARIABLE)
            self.state = 259
            self.match(fullParser.WS)
            self.state = 260
            self.match(fullParser.T__0)
            self.state = 261
            self.match(fullParser.WS)
            self.state = 262
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
            return self.getToken(fullParser.VARIABLE, 0)

        def array(self):
            return self.getTypedRuleContext(fullParser.ArrayContext,0)


        def count(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fullParser.CountContext)
            else:
                return self.getTypedRuleContext(fullParser.CountContext,i)


        def RPAREN(self):
            return self.getToken(fullParser.RPAREN, 0)

        def COMMA(self):
            return self.getToken(fullParser.COMMA, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(fullParser.WS)
            else:
                return self.getToken(fullParser.WS, i)

        def getRuleIndex(self):
            return fullParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = fullParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_iterable)
        self._la = 0 # Token type
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fullParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(fullParser.VARIABLE)
                pass
            elif token in [fullParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.array()
                pass
            elif token in [fullParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.match(fullParser.T__1)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 267
                    self.match(fullParser.WS)


                self.state = 270
                self.count()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 271
                    self.match(fullParser.WS)


                self.state = 274
                self.match(fullParser.COMMA)
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 275
                    self.match(fullParser.WS)


                self.state = 278
                self.count()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fullParser.WS:
                    self.state = 279
                    self.match(fullParser.WS)


                0,2
                self.state = 283
                self.match(fullParser.RPAREN)
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





