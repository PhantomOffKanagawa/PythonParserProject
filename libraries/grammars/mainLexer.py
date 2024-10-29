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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\6\2\21\n\2\r\2\16\2\22\3\2\3\2\3\3\3\3\7\3\31\n\3")
        buf.write("\f\3\16\3\34\13\3\3\3\3\3\3\4\6\4!\n\4\r\4\16\4\"\3\4")
        buf.write("\3\4\6\4\'\n\4\r\4\16\4(\5\4+\n\4\3\5\3\5\7\5/\n\5\f\5")
        buf.write("\16\5\62\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("=\n\6\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\b\5\2")
        buf.write("\13\f\17\17\"\"\4\2\f\f\17\17\3\2\62;\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\6\2\'\',-//\61\61\2I\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\20")
        buf.write("\3\2\2\2\5\26\3\2\2\2\7 \3\2\2\2\t,\3\2\2\2\13<\3\2\2")
        buf.write("\2\r>\3\2\2\2\17\21\t\2\2\2\20\17\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\20\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\25\b\2")
        buf.write("\2\2\25\4\3\2\2\2\26\32\7%\2\2\27\31\n\3\2\2\30\27\3\2")
        buf.write("\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\35\3")
        buf.write("\2\2\2\34\32\3\2\2\2\35\36\b\3\2\2\36\6\3\2\2\2\37!\t")
        buf.write("\4\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#*")
        buf.write("\3\2\2\2$&\7\60\2\2%\'\t\4\2\2&%\3\2\2\2\'(\3\2\2\2(&")
        buf.write("\3\2\2\2()\3\2\2\2)+\3\2\2\2*$\3\2\2\2*+\3\2\2\2+\b\3")
        buf.write("\2\2\2,\60\t\5\2\2-/\t\6\2\2.-\3\2\2\2/\62\3\2\2\2\60")
        buf.write(".\3\2\2\2\60\61\3\2\2\2\61\n\3\2\2\2\62\60\3\2\2\2\63")
        buf.write("=\7?\2\2\64\65\7-\2\2\65=\7?\2\2\66\67\7/\2\2\67=\7?\2")
        buf.write("\289\7,\2\29=\7?\2\2:;\7\61\2\2;=\7?\2\2<\63\3\2\2\2<")
        buf.write("\64\3\2\2\2<\66\3\2\2\2<8\3\2\2\2<:\3\2\2\2=\f\3\2\2\2")
        buf.write(">?\t\7\2\2?\16\3\2\2\2\n\2\22\32\"(*\60<\3\b\2\2")
        return buf.getvalue()


class mainLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT = 2
    NUMBER = 3
    VARIABLE = 4
    ASSIGNMENT_OP = 5
    ARITHMETIC_OP = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP" ]

    ruleNames = [ "WS", "COMMENT", "NUMBER", "VARIABLE", "ASSIGNMENT_OP", 
                  "ARITHMETIC_OP" ]

    grammarFileName = "main.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


