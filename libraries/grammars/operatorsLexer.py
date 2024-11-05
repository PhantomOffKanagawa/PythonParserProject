# Generated from ./grammars/operators.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\6\2!\n\2\r\2\16\2\"\3\2\3\2\6\2\'")
        buf.write("\n\2\r\2\16\2(\5\2+\n\2\3\3\3\3\7\3/\n\3\f\3\16\3\62\13")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17i\n\17\2\2\20\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\6")
        buf.write("\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\6\2\'\',-//\61\61\2")
        buf.write("v\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\3 \3\2\2\2\5,\3\2\2\2\7<\3\2\2\2\t>")
        buf.write("\3\2\2\2\13@\3\2\2\2\rC\3\2\2\2\17H\3\2\2\2\21M\3\2\2")
        buf.write("\2\23O\3\2\2\2\25S\3\2\2\2\27V\3\2\2\2\31Z\3\2\2\2\33")
        buf.write("\\\3\2\2\2\35h\3\2\2\2\37!\t\2\2\2 \37\3\2\2\2!\"\3\2")
        buf.write("\2\2\" \3\2\2\2\"#\3\2\2\2#*\3\2\2\2$&\7\60\2\2%\'\t\2")
        buf.write("\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2")
        buf.write("\2*$\3\2\2\2*+\3\2\2\2+\4\3\2\2\2,\60\t\3\2\2-/\t\4\2")
        buf.write("\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\6\3\2\2\2\62\60\3\2\2\2\63=\7?\2\2\64\65\7-\2\2\65=\7")
        buf.write("?\2\2\66\67\7/\2\2\67=\7?\2\289\7,\2\29=\7?\2\2:;\7\61")
        buf.write("\2\2;=\7?\2\2<\63\3\2\2\2<\64\3\2\2\2<\66\3\2\2\2<8\3")
        buf.write("\2\2\2<:\3\2\2\2=\b\3\2\2\2>?\t\5\2\2?\n\3\2\2\2@A\7k")
        buf.write("\2\2AB\7h\2\2B\f\3\2\2\2CD\7g\2\2DE\7n\2\2EF\7k\2\2FG")
        buf.write("\7h\2\2G\16\3\2\2\2HI\7g\2\2IJ\7n\2\2JK\7u\2\2KL\7g\2")
        buf.write("\2L\20\3\2\2\2MN\7<\2\2N\22\3\2\2\2OP\7c\2\2PQ\7p\2\2")
        buf.write("QR\7f\2\2R\24\3\2\2\2ST\7q\2\2TU\7t\2\2U\26\3\2\2\2VW")
        buf.write("\7p\2\2WX\7q\2\2XY\7v\2\2Y\30\3\2\2\2Z[\7*\2\2[\32\3\2")
        buf.write("\2\2\\]\7+\2\2]\34\3\2\2\2^_\7?\2\2_i\7?\2\2`a\7#\2\2")
        buf.write("ai\7?\2\2bi\7>\2\2cd\7>\2\2di\7?\2\2ei\7@\2\2fg\7@\2\2")
        buf.write("gi\7?\2\2h^\3\2\2\2h`\3\2\2\2hb\3\2\2\2hc\3\2\2\2he\3")
        buf.write("\2\2\2hf\3\2\2\2i\36\3\2\2\2\t\2\"(*\60<h\2")
        return buf.getvalue()


class operatorsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    VARIABLE = 2
    ASSIGNMENT_OP = 3
    ARITHMETIC_OP = 4
    IF = 5
    ELIF = 6
    ELSE = 7
    COLON = 8
    AND = 9
    OR = 10
    NOT = 11
    LPAREN = 12
    RPAREN = 13
    COMPARISON_OP = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'elif'", "'else'", "':'", "'and'", "'or'", "'not'", 
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP", "IF", 
            "ELIF", "ELSE", "COLON", "AND", "OR", "NOT", "LPAREN", "RPAREN", 
            "COMPARISON_OP" ]

    ruleNames = [ "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP", 
                  "IF", "ELIF", "ELSE", "COLON", "AND", "OR", "NOT", "LPAREN", 
                  "RPAREN", "COMPARISON_OP" ]

    grammarFileName = "operators.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


