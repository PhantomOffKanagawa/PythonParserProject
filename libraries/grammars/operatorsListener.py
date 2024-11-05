# Generated from ./grammars/operators.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .operatorsParser import operatorsParser
else:
    from operatorsParser import operatorsParser

# This class defines a complete listener for a parse tree produced by operatorsParser.
class operatorsListener(ParseTreeListener):

    # Enter a parse tree produced by operatorsParser#assignment.
    def enterAssignment(self, ctx:operatorsParser.AssignmentContext):
        pass

    # Exit a parse tree produced by operatorsParser#assignment.
    def exitAssignment(self, ctx:operatorsParser.AssignmentContext):
        pass


    # Enter a parse tree produced by operatorsParser#expression.
    def enterExpression(self, ctx:operatorsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by operatorsParser#expression.
    def exitExpression(self, ctx:operatorsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by operatorsParser#value.
    def enterValue(self, ctx:operatorsParser.ValueContext):
        pass

    # Exit a parse tree produced by operatorsParser#value.
    def exitValue(self, ctx:operatorsParser.ValueContext):
        pass


    # Enter a parse tree produced by operatorsParser#operator.
    def enterOperator(self, ctx:operatorsParser.OperatorContext):
        pass

    # Exit a parse tree produced by operatorsParser#operator.
    def exitOperator(self, ctx:operatorsParser.OperatorContext):
        pass


    # Enter a parse tree produced by operatorsParser#if_block.
    def enterIf_block(self, ctx:operatorsParser.If_blockContext):
        pass

    # Exit a parse tree produced by operatorsParser#if_block.
    def exitIf_block(self, ctx:operatorsParser.If_blockContext):
        pass


    # Enter a parse tree produced by operatorsParser#condition.
    def enterCondition(self, ctx:operatorsParser.ConditionContext):
        pass

    # Exit a parse tree produced by operatorsParser#condition.
    def exitCondition(self, ctx:operatorsParser.ConditionContext):
        pass


    # Enter a parse tree produced by operatorsParser#block.
    def enterBlock(self, ctx:operatorsParser.BlockContext):
        pass

    # Exit a parse tree produced by operatorsParser#block.
    def exitBlock(self, ctx:operatorsParser.BlockContext):
        pass



del operatorsParser