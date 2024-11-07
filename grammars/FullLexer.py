# Generated from ./grammars/FullLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr4 import *
from antlr4.Token import CommonToken
from collections import deque


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2!")
        buf.write("\u0116\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\3\2\3\2\3\2\5\2A\n\2\3\2\3\2\5\2E\n\2\3\2\5\2H\n")
        buf.write("\2\5\2J\n\2\3\2\3\2\3\3\6\3O\n\3\r\3\16\3P\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4^\n\4\3\5\3\5\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0085")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u008c\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\7\26\u00a7\n\26\f\26\16\26\u00aa\13\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\7\27\u00b1\n\27\f\27\16\27\u00b4")
        buf.write("\13\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00be")
        buf.write("\n\27\f\27\16\27\u00c1\13\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\7\27\u00cb\n\27\f\27\16\27\u00ce\13\27")
        buf.write("\3\27\3\27\3\27\5\27\u00d3\n\27\3\30\5\30\u00d6\n\30\3")
        buf.write("\30\6\30\u00d9\n\30\r\30\16\30\u00da\3\30\3\30\6\30\u00df")
        buf.write("\n\30\r\30\16\30\u00e0\5\30\u00e3\n\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00ee\n\31\3\32\3")
        buf.write("\32\3\32\7\32\u00f3\n\32\f\32\16\32\u00f6\13\32\3\32\3")
        buf.write("\32\3\32\3\32\7\32\u00fc\n\32\f\32\16\32\u00ff\13\32\3")
        buf.write("\32\5\32\u0102\n\32\3\33\3\33\3\33\3\34\3\34\7\34\u0109")
        buf.write("\n\34\f\34\16\34\u010c\13\34\3\35\6\35\u010f\n\35\r\35")
        buf.write("\16\35\u0110\3\36\3\36\3\36\3\36\5\u00b2\u00bf\u00cc\2")
        buf.write("\37\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27")
        buf.write("\17\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-")
        buf.write("\32/\33\61\34\63\35\65\36\67\379 ;!\3\2\r\3\2\13\13\6")
        buf.write("\2\'\',-//\61\61\4\2\f\f\17\17\3\2\62;\4\2$$^^\4\2))^")
        buf.write("^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\3\2\"")
        buf.write("\"\4\2\13\13\"\"\2\u0136\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\3I\3\2\2\2\5N\3\2\2\2\7]\3\2\2\2\t_\3\2\2\2\13a\3\2\2")
        buf.write("\2\rc\3\2\2\2\17e\3\2\2\2\21g\3\2\2\2\23j\3\2\2\2\25o")
        buf.write("\3\2\2\2\27t\3\2\2\2\31v\3\2\2\2\33x\3\2\2\2\35\u0084")
        buf.write("\3\2\2\2\37\u008b\3\2\2\2!\u008d\3\2\2\2#\u0091\3\2\2")
        buf.write("\2%\u0097\3\2\2\2\'\u009b\3\2\2\2)\u00a1\3\2\2\2+\u00a4")
        buf.write("\3\2\2\2-\u00d2\3\2\2\2/\u00d5\3\2\2\2\61\u00ed\3\2\2")
        buf.write("\2\63\u0101\3\2\2\2\65\u0103\3\2\2\2\67\u0106\3\2\2\2")
        buf.write("9\u010e\3\2\2\2;\u0112\3\2\2\2=>\6\2\2\2>J\5\5\3\2?A\7")
        buf.write("\17\2\2@?\3\2\2\2@A\3\2\2\2AB\3\2\2\2BE\7\f\2\2CE\7\17")
        buf.write("\2\2D@\3\2\2\2DC\3\2\2\2EG\3\2\2\2FH\5\5\3\2GF\3\2\2\2")
        buf.write("GH\3\2\2\2HJ\3\2\2\2I=\3\2\2\2ID\3\2\2\2JK\3\2\2\2KL\b")
        buf.write("\2\2\2L\4\3\2\2\2MO\t\2\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2")
        buf.write("\2\2PQ\3\2\2\2QR\3\2\2\2RS\b\3\3\2S\6\3\2\2\2T^\7?\2\2")
        buf.write("UV\7-\2\2V^\7?\2\2WX\7/\2\2X^\7?\2\2YZ\7,\2\2Z^\7?\2\2")
        buf.write("[\\\7\61\2\2\\^\7?\2\2]T\3\2\2\2]U\3\2\2\2]W\3\2\2\2]")
        buf.write("Y\3\2\2\2][\3\2\2\2^\b\3\2\2\2_`\t\3\2\2`\n\3\2\2\2ab")
        buf.write("\7]\2\2b\f\3\2\2\2cd\7_\2\2d\16\3\2\2\2ef\7.\2\2f\20\3")
        buf.write("\2\2\2gh\7k\2\2hi\7h\2\2i\22\3\2\2\2jk\7g\2\2kl\7n\2\2")
        buf.write("lm\7k\2\2mn\7h\2\2n\24\3\2\2\2op\7g\2\2pq\7n\2\2qr\7u")
        buf.write("\2\2rs\7g\2\2s\26\3\2\2\2tu\7<\2\2u\30\3\2\2\2vw\7*\2")
        buf.write("\2w\32\3\2\2\2xy\7+\2\2y\34\3\2\2\2z{\7?\2\2{\u0085\7")
        buf.write("?\2\2|}\7#\2\2}\u0085\7?\2\2~\u0085\7>\2\2\177\u0080\7")
        buf.write(">\2\2\u0080\u0085\7?\2\2\u0081\u0085\7@\2\2\u0082\u0083")
        buf.write("\7@\2\2\u0083\u0085\7?\2\2\u0084z\3\2\2\2\u0084|\3\2\2")
        buf.write("\2\u0084~\3\2\2\2\u0084\177\3\2\2\2\u0084\u0081\3\2\2")
        buf.write("\2\u0084\u0082\3\2\2\2\u0085\36\3\2\2\2\u0086\u0087\7")
        buf.write("c\2\2\u0087\u0088\7p\2\2\u0088\u008c\7f\2\2\u0089\u008a")
        buf.write("\7q\2\2\u008a\u008c\7t\2\2\u008b\u0086\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008c \3\2\2\2\u008d\u008e\7p\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7v\2\2\u0090\"\3\2\2\2\u0091\u0092")
        buf.write("\7y\2\2\u0092\u0093\7j\2\2\u0093\u0094\7k\2\2\u0094\u0095")
        buf.write("\7n\2\2\u0095\u0096\7g\2\2\u0096$\3\2\2\2\u0097\u0098")
        buf.write("\7h\2\2\u0098\u0099\7q\2\2\u0099\u009a\7t\2\2\u009a&\3")
        buf.write("\2\2\2\u009b\u009c\7t\2\2\u009c\u009d\7c\2\2\u009d\u009e")
        buf.write("\7p\2\2\u009e\u009f\7i\2\2\u009f\u00a0\7g\2\2\u00a0(\3")
        buf.write("\2\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7p\2\2\u00a3*\3")
        buf.write("\2\2\2\u00a4\u00a8\7%\2\2\u00a5\u00a7\n\4\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9,\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab")
        buf.write("\u00ac\7$\2\2\u00ac\u00ad\7$\2\2\u00ad\u00ae\7$\2\2\u00ae")
        buf.write("\u00b2\3\2\2\2\u00af\u00b1\13\2\2\2\u00b0\u00af\3\2\2")
        buf.write("\2\u00b1\u00b4\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5")
        buf.write("\u00b6\7$\2\2\u00b6\u00b7\7$\2\2\u00b7\u00d3\7$\2\2\u00b8")
        buf.write("\u00b9\7)\2\2\u00b9\u00ba\7)\2\2\u00ba\u00bb\7)\2\2\u00bb")
        buf.write("\u00bf\3\2\2\2\u00bc\u00be\13\2\2\2\u00bd\u00bc\3\2\2")
        buf.write("\2\u00be\u00c1\3\2\2\2\u00bf\u00c0\3\2\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2")
        buf.write("\u00c3\7)\2\2\u00c3\u00c4\7)\2\2\u00c4\u00d3\7)\2\2\u00c5")
        buf.write("\u00c6\7b\2\2\u00c6\u00c7\7b\2\2\u00c7\u00c8\7b\2\2\u00c8")
        buf.write("\u00cc\3\2\2\2\u00c9\u00cb\13\2\2\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb\u00ce\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cc\u00ca")
        buf.write("\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf")
        buf.write("\u00d0\7b\2\2\u00d0\u00d1\7b\2\2\u00d1\u00d3\7b\2\2\u00d2")
        buf.write("\u00ab\3\2\2\2\u00d2\u00b8\3\2\2\2\u00d2\u00c5\3\2\2\2")
        buf.write("\u00d3.\3\2\2\2\u00d4\u00d6\7/\2\2\u00d5\u00d4\3\2\2\2")
        buf.write("\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d9\t")
        buf.write("\5\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00e2\3\2\2\2\u00dc")
        buf.write("\u00de\7\60\2\2\u00dd\u00df\t\5\2\2\u00de\u00dd\3\2\2")
        buf.write("\2\u00df\u00e0\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00dc\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\60\3\2\2\2\u00e4\u00e5\7V\2\2\u00e5")
        buf.write("\u00e6\7t\2\2\u00e6\u00e7\7w\2\2\u00e7\u00ee\7g\2\2\u00e8")
        buf.write("\u00e9\7H\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7n\2\2\u00eb")
        buf.write("\u00ec\7u\2\2\u00ec\u00ee\7g\2\2\u00ed\u00e4\3\2\2\2\u00ed")
        buf.write("\u00e8\3\2\2\2\u00ee\62\3\2\2\2\u00ef\u00f4\7$\2\2\u00f0")
        buf.write("\u00f3\5\65\33\2\u00f1\u00f3\n\6\2\2\u00f2\u00f0\3\2\2")
        buf.write("\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f7\u0102\7$\2\2\u00f8\u00fd\7)\2\2\u00f9")
        buf.write("\u00fc\5\65\33\2\u00fa\u00fc\n\7\2\2\u00fb\u00f9\3\2\2")
        buf.write("\2\u00fb\u00fa\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u0100\u0102\7)\2\2\u0101\u00ef\3\2\2\2")
        buf.write("\u0101\u00f8\3\2\2\2\u0102\64\3\2\2\2\u0103\u0104\7^\2")
        buf.write("\2\u0104\u0105\t\b\2\2\u0105\66\3\2\2\2\u0106\u010a\t")
        buf.write("\t\2\2\u0107\u0109\t\n\2\2\u0108\u0107\3\2\2\2\u0109\u010c")
        buf.write("\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("8\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010f\t\13\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111:\3\2\2\2\u0112\u0113\t\f\2")
        buf.write("\2\u0113\u0114\3\2\2\2\u0114\u0115\b\36\3\2\u0115<\3\2")
        buf.write("\2\2\34\2@DGIP]\u0084\u008b\u00a8\u00b2\u00bf\u00cc\u00d2")
        buf.write("\u00d5\u00da\u00e0\u00e2\u00ed\u00f2\u00f4\u00fb\u00fd")
        buf.write("\u0101\u010a\u0110\4\3\2\2\b\2\2")
        return buf.getvalue()


class FullLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    NEWLINE = 3
    SPACES = 4
    ASSIGNMENT_OP = 5
    ARITHMETIC_OP = 6
    LBRACKET = 7
    RBRACKET = 8
    COMMA = 9
    IF = 10
    ELIF = 11
    ELSE = 12
    COLON = 13
    LPAREN = 14
    RPAREN = 15
    COMPARISON_OP = 16
    LOGICAL_OP = 17
    NOT_OP = 18
    WHILE = 19
    FOR = 20
    RANGE = 21
    IN = 22
    SINGLE_LINE_COMMENT = 23
    MULTI_LINE_COMMENT = 24
    NUMBER = 25
    BOOLEAN = 26
    STRING = 27
    ESC = 28
    VARIABLE = 29
    WS = 30
    WS_SKIPPED = 31

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "','", "'if'", "'elif'", "'else'", "':'", "'('", 
            "')'", "'not'", "'while'", "'for'", "'range'", "'in'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NEWLINE", "SPACES", "ASSIGNMENT_OP", "ARITHMETIC_OP", 
            "LBRACKET", "RBRACKET", "COMMA", "IF", "ELIF", "ELSE", "COLON", 
            "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", "NOT_OP", 
            "WHILE", "FOR", "RANGE", "IN", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
            "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS", "WS_SKIPPED" ]

    ruleNames = [ "NEWLINE", "SPACES", "ASSIGNMENT_OP", "ARITHMETIC_OP", 
                  "LBRACKET", "RBRACKET", "COMMA", "IF", "ELIF", "ELSE", 
                  "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
                  "NOT_OP", "WHILE", "FOR", "RANGE", "IN", "SINGLE_LINE_COMMENT", 
                  "MULTI_LINE_COMMENT", "NUMBER", "BOOLEAN", "STRING", "ESC", 
                  "VARIABLE", "WS", "WS_SKIPPED" ]

    grammarFileName = "FullLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    # Deques to manage tokens and indentation levels
    tokens = deque()
    indents = deque()
    mIndent = -1
    lastToken = None

    # Emit a token and add it to the token queue
    def emit(self, token=None):
        if token is None:
            token = self._factory.create(self._tokenFactorySourcePair, 
                                        self._type, 
                                        self._text, 
                                        self._channel, 
                                        self._tokenStartCharIndex, 
                                        self.getCharIndex()-1,
                                        self._tokenStartLine, 
                                        self._tokenStartColumn)

        self._token = token
        self.tokens.append(token)  # Add token to the queue
        return token

    # Override nextToken to handle EOF and manage indentation tokens
    def nextToken(self):
        if (self._input.LA(1) == Token.EOF and len(self.indents) > 0):
            for i in range(len(self.tokens) - 1, -1, -1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop()

            self.emit(self.commonToken(self.NEWLINE, ""))

            while (len(self.indents) > 0):
                self.emit(self.createDedent())
                self.indents.pop()

            self.emit(self.commonToken(Token.EOF, "<EOF>"))

        next_token = super().nextToken()

        if next_token.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next_token

        return next_token if len(self.tokens) == 0 else self.tokens.popleft()

    # Create a DEDENT token
    def createDedent(self):
        dedent = CommonToken(
            self._tokenFactorySourcePair,
            self.DEDENT,
            self.DEFAULT_TOKEN_CHANNEL,
            self.getCharIndex()-1,
            self.getCharIndex()-1
        )
        dedent.line = self.lastToken.line
        dedent.text = "<DEDENT>"  # Custom text representation
        return dedent

    # Create an INDENT token
    def createIndent(self):
        indent = CommonToken(
            self._tokenFactorySourcePair,
            self.INDENT,
            self.DEFAULT_TOKEN_CHANNEL,
            self.getCharIndex()-1,
            self.getCharIndex()-1
        )
        indent.line = self.lastToken.line
        indent.text = "<INDENT>"  # Custom text representation
        return indent

    # Create a common token with specified type and text
    def commonToken(self, type, text):
        stop = self.getCharIndex() - 1
        start = stop if len(text) == 0 else stop - len(text) + 1

        return CommonToken(self._tokenFactorySourcePair, type, self.DEFAULT_TOKEN_CHANNEL, start, stop)

    # Static method to count indentation levels
    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 4 - count % 4
            else:
                count += 1

        return count

    # Check if at the start of input
    def atStartOfInput(self):
        return self.column == 0 and super().line == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            newLine = self.text.replace("[^\r\n]+", "")
            spaces = self.text.replace("[\r\n]+", "")
            if next == '\r' or next == '\n' or next == '\f' or next == '#':
                self.skip()
            else:
                self.emit(self.commonToken(self.NEWLINE, ""))
                indent = self.getIndentationCount(spaces)
                if self.mIndent == -1:
                    self.mIndent = indent
                    self.indents.append(indent)
                previous = 0 if len(self.indents) == 0 else self.indents[-1]
                if (indent == previous):
                    self.skip()
                elif (indent > previous):
                    self.indents.append(indent)
                    self.emit(self.createIndent())
                else:
                    while (len(self.indents) > 0 and self.indents[-1] > indent):
                        self.emit(self.createDedent())
                        self.indents.pop()
                
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[0] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


