# Generated from ./grammars/main.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete listener for a parse tree produced by mainParser.
class mainListener(ParseTreeListener):

    # Enter a parse tree produced by mainParser#stat.
    def enterStat(self, ctx:mainParser.StatContext):
        pass

    # Exit a parse tree produced by mainParser#stat.
    def exitStat(self, ctx:mainParser.StatContext):
        pass


    # Enter a parse tree produced by mainParser#expr.
    def enterExpr(self, ctx:mainParser.ExprContext):
        pass

    # Exit a parse tree produced by mainParser#expr.
    def exitExpr(self, ctx:mainParser.ExprContext):
        pass


    # Enter a parse tree produced by mainParser#code.
    def enterCode(self, ctx:mainParser.CodeContext):
        pass

    # Exit a parse tree produced by mainParser#code.
    def exitCode(self, ctx:mainParser.CodeContext):
        pass


    # Enter a parse tree produced by mainParser#block.
    def enterBlock(self, ctx:mainParser.BlockContext):
        pass

    # Exit a parse tree produced by mainParser#block.
    def exitBlock(self, ctx:mainParser.BlockContext):
        pass


    # Enter a parse tree produced by mainParser#line.
    def enterLine(self, ctx:mainParser.LineContext):
        pass

    # Exit a parse tree produced by mainParser#line.
    def exitLine(self, ctx:mainParser.LineContext):
        pass


    # Enter a parse tree produced by mainParser#assignment.
    def enterAssignment(self, ctx:mainParser.AssignmentContext):
        pass

    # Exit a parse tree produced by mainParser#assignment.
    def exitAssignment(self, ctx:mainParser.AssignmentContext):
        pass


    # Enter a parse tree produced by mainParser#expression.
    def enterExpression(self, ctx:mainParser.ExpressionContext):
        pass

    # Exit a parse tree produced by mainParser#expression.
    def exitExpression(self, ctx:mainParser.ExpressionContext):
        pass


    # Enter a parse tree produced by mainParser#array.
    def enterArray(self, ctx:mainParser.ArrayContext):
        pass

    # Exit a parse tree produced by mainParser#array.
    def exitArray(self, ctx:mainParser.ArrayContext):
        pass


    # Enter a parse tree produced by mainParser#value.
    def enterValue(self, ctx:mainParser.ValueContext):
        pass

    # Exit a parse tree produced by mainParser#value.
    def exitValue(self, ctx:mainParser.ValueContext):
        pass


    # Enter a parse tree produced by mainParser#assignment_operator.
    def enterAssignment_operator(self, ctx:mainParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by mainParser#assignment_operator.
    def exitAssignment_operator(self, ctx:mainParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by mainParser#operator.
    def enterOperator(self, ctx:mainParser.OperatorContext):
        pass

    # Exit a parse tree produced by mainParser#operator.
    def exitOperator(self, ctx:mainParser.OperatorContext):
        pass


    # Enter a parse tree produced by mainParser#comment.
    def enterComment(self, ctx:mainParser.CommentContext):
        pass

    # Exit a parse tree produced by mainParser#comment.
    def exitComment(self, ctx:mainParser.CommentContext):
        pass


    # Enter a parse tree produced by mainParser#if_block.
    def enterIf_block(self, ctx:mainParser.If_blockContext):
        pass

    # Exit a parse tree produced by mainParser#if_block.
    def exitIf_block(self, ctx:mainParser.If_blockContext):
        pass


    # Enter a parse tree produced by mainParser#condition.
    def enterCondition(self, ctx:mainParser.ConditionContext):
        pass

    # Exit a parse tree produced by mainParser#condition.
    def exitCondition(self, ctx:mainParser.ConditionContext):
        pass


    # Enter a parse tree produced by mainParser#logical_condition.
    def enterLogical_condition(self, ctx:mainParser.Logical_conditionContext):
        pass

    # Exit a parse tree produced by mainParser#logical_condition.
    def exitLogical_condition(self, ctx:mainParser.Logical_conditionContext):
        pass


    # Enter a parse tree produced by mainParser#comparison_condition.
    def enterComparison_condition(self, ctx:mainParser.Comparison_conditionContext):
        pass

    # Exit a parse tree produced by mainParser#comparison_condition.
    def exitComparison_condition(self, ctx:mainParser.Comparison_conditionContext):
        pass



del mainParser