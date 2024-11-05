# Generated from ./grammars/operators.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\31\n\3\f\3\16")
        buf.write("\3\34\13\3\3\4\3\4\3\4\5\4!\n\4\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\7\6.\n\6\f\6\16\6\61\13\6\3\6\3")
        buf.write("\6\3\6\5\6\66\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7D\n\7\3\7\3\7\3\7\7\7I\n\7\f\7\16\7L\13")
        buf.write("\7\3\b\3\b\5\bP\n\b\3\b\2\3\f\t\2\4\6\b\n\f\16\2\3\3\2")
        buf.write("\13\f\2S\2\20\3\2\2\2\4\24\3\2\2\2\6 \3\2\2\2\b\"\3\2")
        buf.write("\2\2\n$\3\2\2\2\fC\3\2\2\2\16O\3\2\2\2\20\21\7\4\2\2\21")
        buf.write("\22\7\5\2\2\22\23\5\4\3\2\23\3\3\2\2\2\24\32\5\6\4\2\25")
        buf.write("\26\5\b\5\2\26\27\5\6\4\2\27\31\3\2\2\2\30\25\3\2\2\2")
        buf.write("\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\5\3\2\2")
        buf.write("\2\34\32\3\2\2\2\35!\7\3\2\2\36\37\7\4\2\2\37!\b\4\1\2")
        buf.write(" \35\3\2\2\2 \36\3\2\2\2!\7\3\2\2\2\"#\7\6\2\2#\t\3\2")
        buf.write("\2\2$%\7\7\2\2%&\5\f\7\2&\'\7\n\2\2\'/\5\16\b\2()\7\b")
        buf.write("\2\2)*\5\f\7\2*+\7\n\2\2+,\5\16\b\2,.\3\2\2\2-(\3\2\2")
        buf.write("\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\65\3\2\2\2\61")
        buf.write("/\3\2\2\2\62\63\7\t\2\2\63\64\7\n\2\2\64\66\5\16\b\2\65")
        buf.write("\62\3\2\2\2\65\66\3\2\2\2\66\13\3\2\2\2\678\b\7\1\289")
        buf.write("\5\6\4\29:\7\20\2\2:;\5\6\4\2;D\3\2\2\2<D\5\6\4\2=>\7")
        buf.write("\r\2\2>D\5\f\7\5?@\7\16\2\2@A\5\f\7\2AB\7\17\2\2BD\3\2")
        buf.write("\2\2C\67\3\2\2\2C<\3\2\2\2C=\3\2\2\2C?\3\2\2\2DJ\3\2\2")
        buf.write("\2EF\f\4\2\2FG\t\2\2\2GI\5\f\7\5HE\3\2\2\2IL\3\2\2\2J")
        buf.write("H\3\2\2\2JK\3\2\2\2K\r\3\2\2\2LJ\3\2\2\2MP\5\2\2\2NP\5")
        buf.write("\4\3\2OM\3\2\2\2ON\3\2\2\2P\17\3\2\2\2\t\32 /\65CJO")
        return buf.getvalue()


class operatorsParser ( Parser ):

    grammarFileName = "operators.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'elif'", "'else'", "':'", "'and'", 
                     "'or'", "'not'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "VARIABLE", "ASSIGNMENT_OP", 
                      "ARITHMETIC_OP", "IF", "ELIF", "ELSE", "COLON", "AND", 
                      "OR", "NOT", "LPAREN", "RPAREN", "COMPARISON_OP" ]

    RULE_assignment = 0
    RULE_expression = 1
    RULE_value = 2
    RULE_operator = 3
    RULE_if_block = 4
    RULE_condition = 5
    RULE_block = 6

    ruleNames =  [ "assignment", "expression", "value", "operator", "if_block", 
                   "condition", "block" ]

    EOF = Token.EOF
    NUMBER=1
    VARIABLE=2
    ASSIGNMENT_OP=3
    ARITHMETIC_OP=4
    IF=5
    ELIF=6
    ELSE=7
    COLON=8
    AND=9
    OR=10
    NOT=11
    LPAREN=12
    RPAREN=13
    COMPARISON_OP=14

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
            return self.getToken(operatorsParser.VARIABLE, 0)

        def ASSIGNMENT_OP(self):
            return self.getToken(operatorsParser.ASSIGNMENT_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(operatorsParser.ExpressionContext,0)


        def getRuleIndex(self):
            return operatorsParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = operatorsParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(operatorsParser.VARIABLE)
            self.state = 15
            self.match(operatorsParser.ASSIGNMENT_OP)
            self.state = 16
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
                return self.getTypedRuleContexts(operatorsParser.ValueContext)
            else:
                return self.getTypedRuleContext(operatorsParser.ValueContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(operatorsParser.OperatorContext)
            else:
                return self.getTypedRuleContext(operatorsParser.OperatorContext,i)


        def getRuleIndex(self):
            return operatorsParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = operatorsParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.value()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==operatorsParser.ARITHMETIC_OP:
                self.state = 19
                self.operator()
                self.state = 20
                self.value()
                self.state = 26
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
            return self.getToken(operatorsParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(operatorsParser.VARIABLE, 0)

        def getRuleIndex(self):
            return operatorsParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = operatorsParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_value)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [operatorsParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(operatorsParser.NUMBER)
                pass
            elif token in [operatorsParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(operatorsParser.VARIABLE)

                    
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
            return self.getToken(operatorsParser.ARITHMETIC_OP, 0)

        def getRuleIndex(self):
            return operatorsParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = operatorsParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(operatorsParser.ARITHMETIC_OP)
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
            return self.getToken(operatorsParser.IF, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(operatorsParser.ConditionContext)
            else:
                return self.getTypedRuleContext(operatorsParser.ConditionContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(operatorsParser.COLON)
            else:
                return self.getToken(operatorsParser.COLON, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(operatorsParser.BlockContext)
            else:
                return self.getTypedRuleContext(operatorsParser.BlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(operatorsParser.ELIF)
            else:
                return self.getToken(operatorsParser.ELIF, i)

        def ELSE(self):
            return self.getToken(operatorsParser.ELSE, 0)

        def getRuleIndex(self):
            return operatorsParser.RULE_if_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_block" ):
                listener.enterIf_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_block" ):
                listener.exitIf_block(self)




    def if_block(self):

        localctx = operatorsParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(operatorsParser.IF)
            self.state = 35
            self.condition(0)
            self.state = 36
            self.match(operatorsParser.COLON)
            self.state = 37
            self.block()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==operatorsParser.ELIF:
                self.state = 38
                self.match(operatorsParser.ELIF)
                self.state = 39
                self.condition(0)
                self.state = 40
                self.match(operatorsParser.COLON)
                self.state = 41
                self.block()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==operatorsParser.ELSE:
                self.state = 48
                self.match(operatorsParser.ELSE)
                self.state = 49
                self.match(operatorsParser.COLON)
                self.state = 50
                self.block()


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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(operatorsParser.ValueContext)
            else:
                return self.getTypedRuleContext(operatorsParser.ValueContext,i)


        def COMPARISON_OP(self):
            return self.getToken(operatorsParser.COMPARISON_OP, 0)

        def NOT(self):
            return self.getToken(operatorsParser.NOT, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(operatorsParser.ConditionContext)
            else:
                return self.getTypedRuleContext(operatorsParser.ConditionContext,i)


        def LPAREN(self):
            return self.getToken(operatorsParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(operatorsParser.RPAREN, 0)

        def AND(self):
            return self.getToken(operatorsParser.AND, 0)

        def OR(self):
            return self.getToken(operatorsParser.OR, 0)

        def getRuleIndex(self):
            return operatorsParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = operatorsParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 54
                self.value()
                self.state = 55
                self.match(operatorsParser.COMPARISON_OP)
                self.state = 56
                self.value()
                pass

            elif la_ == 2:
                self.state = 58
                self.value()
                pass

            elif la_ == 3:
                self.state = 59
                self.match(operatorsParser.NOT)
                self.state = 60
                self.condition(3)
                pass

            elif la_ == 4:
                self.state = 61
                self.match(operatorsParser.LPAREN)
                self.state = 62
                self.condition(0)
                self.state = 63
                self.match(operatorsParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = operatorsParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 67
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 68
                    _la = self._input.LA(1)
                    if not(_la==operatorsParser.AND or _la==operatorsParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 69
                    self.condition(3) 
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(operatorsParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(operatorsParser.ExpressionContext,0)


        def getRuleIndex(self):
            return operatorsParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = operatorsParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




