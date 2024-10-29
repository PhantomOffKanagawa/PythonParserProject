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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\3\2\3\2\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\3\3\3")
        buf.write("\3\4\3\4\5\4\35\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7")
        buf.write("\6\'\n\6\f\6\16\6*\13\6\3\7\3\7\3\7\5\7/\n\7\3\b\3\b\3")
        buf.write("\b\2\2\t\2\4\6\b\n\f\16\2\2\2/\2\20\3\2\2\2\4\25\3\2\2")
        buf.write("\2\6\34\3\2\2\2\b\36\3\2\2\2\n\"\3\2\2\2\f.\3\2\2\2\16")
        buf.write("\60\3\2\2\2\20\21\5\4\3\2\21\3\3\2\2\2\22\24\5\6\4\2\23")
        buf.write("\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\30\3\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3\31\5\3\2\2")
        buf.write("\2\32\35\5\b\5\2\33\35\5\n\6\2\34\32\3\2\2\2\34\33\3\2")
        buf.write("\2\2\35\7\3\2\2\2\36\37\7\6\2\2\37 \7\7\2\2 !\5\n\6\2")
        buf.write("!\t\3\2\2\2\"(\5\f\7\2#$\5\16\b\2$%\5\f\7\2%\'\3\2\2\2")
        buf.write("&#\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\13\3\2\2\2")
        buf.write("*(\3\2\2\2+/\7\5\2\2,-\7\6\2\2-/\b\7\1\2.+\3\2\2\2.,\3")
        buf.write("\2\2\2/\r\3\2\2\2\60\61\7\b\2\2\61\17\3\2\2\2\6\25\34")
        buf.write("(.")
        return buf.getvalue()


class mainParser ( Parser ):

    grammarFileName = "main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "NUMBER", "VARIABLE", 
                      "ASSIGNMENT_OP", "ARITHMETIC_OP" ]

    RULE_stat = 0
    RULE_expr = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_expression = 4
    RULE_value = 5
    RULE_operator = 6

    ruleNames =  [ "stat", "expr", "statement", "assignment", "expression", 
                   "value", "operator" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    NUMBER=3
    VARIABLE=4
    ASSIGNMENT_OP=5
    ARITHMETIC_OP=6

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
            self.state = 14
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.StatementContext)
            else:
                return self.getTypedRuleContext(mainParser.StatementContext,i)


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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mainParser.NUMBER or _la==mainParser.VARIABLE:
                self.state = 16
                self.statement()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(mainParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(mainParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(mainParser.ExpressionContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = mainParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.expression()
                pass


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

        def ASSIGNMENT_OP(self):
            return self.getToken(mainParser.ASSIGNMENT_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(mainParser.ExpressionContext,0)


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
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(mainParser.VARIABLE)
            self.state = 29
            self.match(mainParser.ASSIGNMENT_OP)
            self.state = 30
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
        self.enterRule(localctx, 8, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.value()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mainParser.ARITHMETIC_OP:
                self.state = 33
                self.operator()
                self.state = 34
                self.value()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mainParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(mainParser.NUMBER)
                pass
            elif token in [mainParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(mainParser.VARIABLE)

                    
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
        self.enterRule(localctx, 12, self.RULE_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(mainParser.ARITHMETIC_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





