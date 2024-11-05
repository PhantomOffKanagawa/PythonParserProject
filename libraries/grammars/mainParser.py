# Generated from ./grammars/main.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("\u00db\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\7\3&\n")
        buf.write("\3\f\3\16\3)\13\3\3\3\3\3\3\4\3\4\5\4/\n\4\3\5\6\5\62")
        buf.write("\n\5\r\5\16\5\63\3\6\3\6\5\68\n\6\3\7\3\7\5\7<\n\7\3\7")
        buf.write("\3\7\5\7@\n\7\3\7\3\7\3\b\3\b\5\bF\n\b\3\b\3\b\5\bJ\n")
        buf.write("\b\3\b\3\b\5\bN\n\b\7\bP\n\b\f\b\16\bS\13\b\3\t\3\t\5")
        buf.write("\tW\n\t\3\t\3\t\5\t[\n\t\3\t\3\t\5\t_\n\t\3\t\3\t\5\t")
        buf.write("c\n\t\7\te\n\t\f\t\16\th\13\t\5\tj\n\t\3\t\5\tm\n\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nz\n\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\5\16\u0084\n\16\3\16")
        buf.write("\3\16\5\16\u0088\n\16\3\16\3\16\5\16\u008c\n\16\3\16\3")
        buf.write("\16\6\16\u0090\n\16\r\16\16\16\u0091\3\16\3\16\3\16\5")
        buf.write("\16\u0097\n\16\3\16\3\16\5\16\u009b\n\16\3\16\6\16\u009e")
        buf.write("\n\16\r\16\16\16\u009f\7\16\u00a2\n\16\f\16\16\16\u00a5")
        buf.write("\13\16\3\16\3\16\5\16\u00a9\n\16\3\16\3\16\5\16\u00ad")
        buf.write("\n\16\3\16\6\16\u00b0\n\16\r\16\16\16\u00b1\5\16\u00b4")
        buf.write("\n\16\3\17\3\17\3\20\5\20\u00b9\n\20\3\20\3\20\5\20\u00bd")
        buf.write("\n\20\3\20\3\20\5\20\u00c1\n\20\3\20\7\20\u00c4\n\20\f")
        buf.write("\20\16\20\u00c7\13\20\3\21\3\21\5\21\u00cb\n\21\3\21\3")
        buf.write("\21\3\21\5\21\u00d0\n\21\3\21\3\21\5\21\u00d4\n\21\3\21")
        buf.write("\3\21\3\21\5\21\u00d9\n\21\3\21\2\2\22\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \2\4\3\2\32\33\3\2\17\20\2\u00f6")
        buf.write("\2\"\3\2\2\2\4\'\3\2\2\2\6.\3\2\2\2\b\61\3\2\2\2\n\67")
        buf.write("\3\2\2\2\f9\3\2\2\2\16C\3\2\2\2\20T\3\2\2\2\22y\3\2\2")
        buf.write("\2\24{\3\2\2\2\26}\3\2\2\2\30\177\3\2\2\2\32\u0081\3\2")
        buf.write("\2\2\34\u00b5\3\2\2\2\36\u00b8\3\2\2\2 \u00d8\3\2\2\2")
        buf.write("\"#\5\4\3\2#\3\3\2\2\2$&\5\6\4\2%$\3\2\2\2&)\3\2\2\2\'")
        buf.write("%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2\2*+\7\2\2\3+\5")
        buf.write("\3\2\2\2,/\5\b\5\2-/\5\32\16\2.,\3\2\2\2.-\3\2\2\2/\7")
        buf.write("\3\2\2\2\60\62\5\n\6\2\61\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\61\3\2\2\2\63\64\3\2\2\2\64\t\3\2\2\2\658\5\f\7\2\66")
        buf.write("8\5\30\r\2\67\65\3\2\2\2\67\66\3\2\2\28\13\3\2\2\29;\7")
        buf.write("\30\2\2:<\7\31\2\2;:\3\2\2\2;<\3\2\2\2<=\3\2\2\2=?\5\24")
        buf.write("\13\2>@\7\31\2\2?>\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\5\16")
        buf.write("\b\2B\r\3\2\2\2CE\5\22\n\2DF\7\31\2\2ED\3\2\2\2EF\3\2")
        buf.write("\2\2FQ\3\2\2\2GI\5\26\f\2HJ\7\31\2\2IH\3\2\2\2IJ\3\2\2")
        buf.write("\2JK\3\2\2\2KM\5\22\n\2LN\7\31\2\2ML\3\2\2\2MN\3\2\2\2")
        buf.write("NP\3\2\2\2OG\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\17")
        buf.write("\3\2\2\2SQ\3\2\2\2Ti\7\6\2\2UW\7\31\2\2VU\3\2\2\2VW\3")
        buf.write("\2\2\2WX\3\2\2\2XZ\5\22\n\2Y[\7\31\2\2ZY\3\2\2\2Z[\3\2")
        buf.write("\2\2[f\3\2\2\2\\^\7\b\2\2]_\7\31\2\2^]\3\2\2\2^_\3\2\2")
        buf.write("\2_`\3\2\2\2`b\5\22\n\2ac\7\31\2\2ba\3\2\2\2bc\3\2\2\2")
        buf.write("ce\3\2\2\2d\\\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gj")
        buf.write("\3\2\2\2hf\3\2\2\2iV\3\2\2\2ij\3\2\2\2jl\3\2\2\2km\7\31")
        buf.write("\2\2lk\3\2\2\2lm\3\2\2\2mn\3\2\2\2no\7\7\2\2o\21\3\2\2")
        buf.write("\2pz\7\24\2\2qz\7\30\2\2rz\7\25\2\2sz\7\26\2\2tu\7\r\2")
        buf.write("\2uv\5\16\b\2vw\7\16\2\2wz\3\2\2\2xz\5\20\t\2yp\3\2\2")
        buf.write("\2yq\3\2\2\2yr\3\2\2\2ys\3\2\2\2yt\3\2\2\2yx\3\2\2\2z")
        buf.write("\23\3\2\2\2{|\7\4\2\2|\25\3\2\2\2}~\7\5\2\2~\27\3\2\2")
        buf.write("\2\177\u0080\t\2\2\2\u0080\31\3\2\2\2\u0081\u0083\7\t")
        buf.write("\2\2\u0082\u0084\7\31\2\2\u0083\u0082\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0087\5\34\17\2\u0086")
        buf.write("\u0088\7\31\2\2\u0087\u0086\3\2\2\2\u0087\u0088\3\2\2")
        buf.write("\2\u0088\u0089\3\2\2\2\u0089\u008b\7\f\2\2\u008a\u008c")
        buf.write("\7\31\2\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\u008f\3\2\2\2\u008d\u0090\5\b\5\2\u008e\u0090\5\32\16")
        buf.write("\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u00a3\3\2\2\2\u0093\u0094\7\n\2\2\u0094\u0096\5\34\17")
        buf.write("\2\u0095\u0097\7\31\2\2\u0096\u0095\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\7\f\2\2\u0099")
        buf.write("\u009b\7\31\2\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2")
        buf.write("\2\u009b\u009d\3\2\2\2\u009c\u009e\5\b\5\2\u009d\u009c")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u009d\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u0093\3\2\2\2")
        buf.write("\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3")
        buf.write("\2\2\2\u00a4\u00b3\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8")
        buf.write("\7\13\2\2\u00a7\u00a9\7\31\2\2\u00a8\u00a7\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\7\f\2\2")
        buf.write("\u00ab\u00ad\7\31\2\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00b0\5\b\5\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00a6\3")
        buf.write("\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\33\3\2\2\2\u00b5\u00b6")
        buf.write("\5\36\20\2\u00b6\35\3\2\2\2\u00b7\u00b9\7\31\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba\u00c5\5 \21\2\u00bb\u00bd\7\31\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00c0\t\3\2\2\u00bf\u00c1\7\31\2\2\u00c0\u00bf\3\2\2")
        buf.write("\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4")
        buf.write("\5 \21\2\u00c3\u00bc\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\37\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c8\u00ca\7\21\2\2\u00c9\u00cb\7\31\2")
        buf.write("\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00d9\5 \21\2\u00cd\u00cf\7\r\2\2\u00ce")
        buf.write("\u00d0\7\31\2\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0\3\2\2")
        buf.write("\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\5\36\20\2\u00d2\u00d4")
        buf.write("\7\31\2\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d6\7\16\2\2\u00d6\u00d9\3\2\2")
        buf.write("\2\u00d7\u00d9\5\22\n\2\u00d8\u00c8\3\2\2\2\u00d8\u00cd")
        buf.write("\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9!\3\2\2\2)\'.\63\67")
        buf.write(";?EIMQVZ^bfily\u0083\u0087\u008b\u008f\u0091\u0096\u009a")
        buf.write("\u009f\u00a3\u00a8\u00ac\u00b1\u00b3\u00b8\u00bc\u00c0")
        buf.write("\u00c5\u00ca\u00cf\u00d3\u00d8")
        return buf.getvalue()


class mainParser ( Parser ):

    grammarFileName = "main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "','", "'if'", "'elif'", "'else'", "':'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "'not'", "'while'", 
                     "'for'" ]

    symbolicNames = [ "<INVALID>", "WS_SKIPPED", "ASSIGNMENT_OP", "ARITHMETIC_OP", 
                      "LBRACKET", "RBRACKET", "COMMA", "IF", "ELIF", "ELSE", 
                      "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
                      "NOT_OP", "WHILE", "FOR", "NUMBER", "BOOLEAN", "STRING", 
                      "ESC", "VARIABLE", "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

    RULE_stat = 0
    RULE_expr = 1
    RULE_code = 2
    RULE_block = 3
    RULE_line = 4
    RULE_assignment = 5
    RULE_expression = 6
    RULE_array = 7
    RULE_value = 8
    RULE_assignment_operator = 9
    RULE_operator = 10
    RULE_comment = 11
    RULE_if_block = 12
    RULE_condition = 13
    RULE_logical_condition = 14
    RULE_comparison_condition = 15

    ruleNames =  [ "stat", "expr", "code", "block", "line", "assignment", 
                   "expression", "array", "value", "assignment_operator", 
                   "operator", "comment", "if_block", "condition", "logical_condition", 
                   "comparison_condition" ]

    EOF = Token.EOF
    WS_SKIPPED=1
    ASSIGNMENT_OP=2
    ARITHMETIC_OP=3
    LBRACKET=4
    RBRACKET=5
    COMMA=6
    IF=7
    ELIF=8
    ELSE=9
    COLON=10
    LPAREN=11
    RPAREN=12
    COMPARISON_OP=13
    LOGICAL_OP=14
    NOT_OP=15
    WHILE=16
    FOR=17
    NUMBER=18
    BOOLEAN=19
    STRING=20
    ESC=21
    VARIABLE=22
    WS=23
    SINGLE_LINE_COMMENT=24
    MULTI_LINE_COMMENT=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = mainParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
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

        def EOF(self):
            return self.getToken(mainParser.EOF, 0)

        def code(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.CodeContext)
            else:
                return self.getTypedRuleContext(mainParser.CodeContext,i)


        def getRuleIndex(self):
            return mainParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = mainParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mainParser.IF) | (1 << mainParser.VARIABLE) | (1 << mainParser.SINGLE_LINE_COMMENT) | (1 << mainParser.MULTI_LINE_COMMENT))) != 0):
                self.state = 34
                self.code()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(mainParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(mainParser.BlockContext,0)


        def if_block(self):
            return self.getTypedRuleContext(mainParser.If_blockContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode" ):
                listener.enterCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode" ):
                listener.exitCode(self)




    def code(self):

        localctx = mainParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_code)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mainParser.VARIABLE, mainParser.SINGLE_LINE_COMMENT, mainParser.MULTI_LINE_COMMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.block()
                pass
            elif token in [mainParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.if_block()
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

    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.LineContext)
            else:
                return self.getTypedRuleContext(mainParser.LineContext,i)


        def getRuleIndex(self):
            return mainParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = mainParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 46
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 49 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            return self.getTypedRuleContext(mainParser.AssignmentContext,0)


        def comment(self):
            return self.getTypedRuleContext(mainParser.CommentContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = mainParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_line)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mainParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.assignment()
                pass
            elif token in [mainParser.SINGLE_LINE_COMMENT, mainParser.MULTI_LINE_COMMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.comment()
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

    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(mainParser.VARIABLE, 0)

        def assignment_operator(self):
            return self.getTypedRuleContext(mainParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(mainParser.ExpressionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.WS)
            else:
                return self.getToken(mainParser.WS, i)

        def getRuleIndex(self):
            return mainParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = mainParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(mainParser.VARIABLE)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mainParser.WS:
                self.state = 56
                self.match(mainParser.WS)


            self.state = 59
            self.assignment_operator()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mainParser.WS:
                self.state = 60
                self.match(mainParser.WS)


            self.state = 63
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
                return self.getTypedRuleContexts(mainParser.ValueContext)
            else:
                return self.getTypedRuleContext(mainParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.WS)
            else:
                return self.getToken(mainParser.WS, i)

        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.OperatorContext)
            else:
                return self.getTypedRuleContext(mainParser.OperatorContext,i)


        def getRuleIndex(self):
            return mainParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = mainParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.value()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mainParser.WS:
                self.state = 66
                self.match(mainParser.WS)


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mainParser.ARITHMETIC_OP:
                self.state = 69
                self.operator()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==mainParser.WS:
                    self.state = 70
                    self.match(mainParser.WS)


                self.state = 73
                self.value()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==mainParser.WS:
                    self.state = 74
                    self.match(mainParser.WS)


                self.state = 81
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
            return self.getToken(mainParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(mainParser.RBRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.ValueContext)
            else:
                return self.getTypedRuleContext(mainParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.WS)
            else:
                return self.getToken(mainParser.WS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.COMMA)
            else:
                return self.getToken(mainParser.COMMA, i)

        def getRuleIndex(self):
            return mainParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = mainParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(mainParser.LBRACKET)
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==mainParser.WS:
                    self.state = 83
                    self.match(mainParser.WS)


                self.state = 86
                self.value()
                self.state = 88
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 87
                    self.match(mainParser.WS)


                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==mainParser.COMMA:
                    self.state = 90
                    self.match(mainParser.COMMA)
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==mainParser.WS:
                        self.state = 91
                        self.match(mainParser.WS)


                    self.state = 94
                    self.value()
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 95
                        self.match(mainParser.WS)


                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mainParser.WS:
                self.state = 105
                self.match(mainParser.WS)


            self.state = 108
            self.match(mainParser.RBRACKET)
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
            return self.getToken(mainParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(mainParser.VARIABLE, 0)

        def BOOLEAN(self):
            return self.getToken(mainParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(mainParser.STRING, 0)

        def LPAREN(self):
            return self.getToken(mainParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(mainParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(mainParser.RPAREN, 0)

        def array(self):
            return self.getTypedRuleContext(mainParser.ArrayContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = mainParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mainParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(mainParser.NUMBER)
                pass
            elif token in [mainParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(mainParser.VARIABLE)
                pass
            elif token in [mainParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.match(mainParser.BOOLEAN)
                pass
            elif token in [mainParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.match(mainParser.STRING)
                pass
            elif token in [mainParser.LPAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 114
                self.match(mainParser.LPAREN)
                self.state = 115
                self.expression()
                self.state = 116
                self.match(mainParser.RPAREN)
                pass
            elif token in [mainParser.LBRACKET]:
                self.enterOuterAlt(localctx, 6)
                self.state = 118
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
            return self.getToken(mainParser.ASSIGNMENT_OP, 0)

        def getRuleIndex(self):
            return mainParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = mainParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(mainParser.ASSIGNMENT_OP)
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
            return self.getToken(mainParser.ARITHMETIC_OP, 0)

        def getRuleIndex(self):
            return mainParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = mainParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(mainParser.ARITHMETIC_OP)
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
            return self.getToken(mainParser.SINGLE_LINE_COMMENT, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(mainParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return mainParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = mainParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not(_la==mainParser.SINGLE_LINE_COMMENT or _la==mainParser.MULTI_LINE_COMMENT):
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
            return self.getToken(mainParser.IF, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.ConditionContext)
            else:
                return self.getTypedRuleContext(mainParser.ConditionContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.COLON)
            else:
                return self.getToken(mainParser.COLON, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.WS)
            else:
                return self.getToken(mainParser.WS, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.BlockContext)
            else:
                return self.getTypedRuleContext(mainParser.BlockContext,i)


        def if_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.If_blockContext)
            else:
                return self.getTypedRuleContext(mainParser.If_blockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.ELIF)
            else:
                return self.getToken(mainParser.ELIF, i)

        def ELSE(self):
            return self.getToken(mainParser.ELSE, 0)

        def getRuleIndex(self):
            return mainParser.RULE_if_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_block" ):
                listener.enterIf_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_block" ):
                listener.exitIf_block(self)




    def if_block(self):

        localctx = mainParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(mainParser.IF)
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 128
                self.match(mainParser.WS)


            self.state = 131
            self.condition()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mainParser.WS:
                self.state = 132
                self.match(mainParser.WS)


            self.state = 135
            self.match(mainParser.COLON)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mainParser.WS:
                self.state = 136
                self.match(mainParser.WS)


            self.state = 141 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 141
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [mainParser.VARIABLE, mainParser.SINGLE_LINE_COMMENT, mainParser.MULTI_LINE_COMMENT]:
                        self.state = 139
                        self.block()
                        pass
                    elif token in [mainParser.IF]:
                        self.state = 140
                        self.if_block()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 143 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 145
                    self.match(mainParser.ELIF)
                    self.state = 146
                    self.condition()
                    self.state = 148
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==mainParser.WS:
                        self.state = 147
                        self.match(mainParser.WS)


                    self.state = 150
                    self.match(mainParser.COLON)
                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==mainParser.WS:
                        self.state = 151
                        self.match(mainParser.WS)


                    self.state = 155 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 154
                            self.block()

                        else:
                            raise NoViableAltException(self)
                        self.state = 157 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
             
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 164
                self.match(mainParser.ELSE)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==mainParser.WS:
                    self.state = 165
                    self.match(mainParser.WS)


                self.state = 168
                self.match(mainParser.COLON)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==mainParser.WS:
                    self.state = 169
                    self.match(mainParser.WS)


                self.state = 173 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 172
                        self.block()

                    else:
                        raise NoViableAltException(self)
                    self.state = 175 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)



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
            return self.getTypedRuleContext(mainParser.Logical_conditionContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = mainParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
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
                return self.getTypedRuleContexts(mainParser.Comparison_conditionContext)
            else:
                return self.getTypedRuleContext(mainParser.Comparison_conditionContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.WS)
            else:
                return self.getToken(mainParser.WS, i)

        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.LOGICAL_OP)
            else:
                return self.getToken(mainParser.LOGICAL_OP, i)

        def COMPARISON_OP(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.COMPARISON_OP)
            else:
                return self.getToken(mainParser.COMPARISON_OP, i)

        def getRuleIndex(self):
            return mainParser.RULE_logical_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_condition" ):
                listener.enterLogical_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_condition" ):
                listener.exitLogical_condition(self)




    def logical_condition(self):

        localctx = mainParser.Logical_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_logical_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mainParser.WS:
                self.state = 181
                self.match(mainParser.WS)


            self.state = 184
            self.comparison_condition()
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==mainParser.WS:
                        self.state = 185
                        self.match(mainParser.WS)


                    self.state = 188
                    _la = self._input.LA(1)
                    if not(_la==mainParser.COMPARISON_OP or _la==mainParser.LOGICAL_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 190
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==mainParser.WS:
                        self.state = 189
                        self.match(mainParser.WS)


                    self.state = 192
                    self.comparison_condition() 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
            return self.getToken(mainParser.NOT_OP, 0)

        def comparison_condition(self):
            return self.getTypedRuleContext(mainParser.Comparison_conditionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.WS)
            else:
                return self.getToken(mainParser.WS, i)

        def LPAREN(self):
            return self.getToken(mainParser.LPAREN, 0)

        def logical_condition(self):
            return self.getTypedRuleContext(mainParser.Logical_conditionContext,0)


        def RPAREN(self):
            return self.getToken(mainParser.RPAREN, 0)

        def value(self):
            return self.getTypedRuleContext(mainParser.ValueContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_comparison_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_condition" ):
                listener.enterComparison_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_condition" ):
                listener.exitComparison_condition(self)




    def comparison_condition(self):

        localctx = mainParser.Comparison_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparison_condition)
        self._la = 0 # Token type
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(mainParser.NOT_OP)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==mainParser.WS:
                    self.state = 199
                    self.match(mainParser.WS)


                self.state = 202
                self.comparison_condition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(mainParser.LPAREN)
                self.state = 205
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 204
                    self.match(mainParser.WS)


                self.state = 207
                self.logical_condition()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==mainParser.WS:
                    self.state = 208
                    self.match(mainParser.WS)


                self.state = 211
                self.match(mainParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





