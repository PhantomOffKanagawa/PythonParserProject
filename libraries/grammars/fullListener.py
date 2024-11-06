# Generated from ./grammars/full.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fullParser import fullParser
else:
    from fullParser import fullParser

# This class defines a complete listener for a parse tree produced by fullParser.
class fullListener(ParseTreeListener):

    # Enter a parse tree produced by fullParser#assignment.
    def enterAssignment(self, ctx:fullParser.AssignmentContext):
        pass

    # Exit a parse tree produced by fullParser#assignment.
    def exitAssignment(self, ctx:fullParser.AssignmentContext):
        pass


    # Enter a parse tree produced by fullParser#expression.
    def enterExpression(self, ctx:fullParser.ExpressionContext):
        pass

    # Exit a parse tree produced by fullParser#expression.
    def exitExpression(self, ctx:fullParser.ExpressionContext):
        pass


    # Enter a parse tree produced by fullParser#array.
    def enterArray(self, ctx:fullParser.ArrayContext):
        pass

    # Exit a parse tree produced by fullParser#array.
    def exitArray(self, ctx:fullParser.ArrayContext):
        pass


    # Enter a parse tree produced by fullParser#count.
    def enterCount(self, ctx:fullParser.CountContext):
        pass

    # Exit a parse tree produced by fullParser#count.
    def exitCount(self, ctx:fullParser.CountContext):
        pass


    # Enter a parse tree produced by fullParser#value.
    def enterValue(self, ctx:fullParser.ValueContext):
        pass

    # Exit a parse tree produced by fullParser#value.
    def exitValue(self, ctx:fullParser.ValueContext):
        pass


    # Enter a parse tree produced by fullParser#assignment_operator.
    def enterAssignment_operator(self, ctx:fullParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by fullParser#assignment_operator.
    def exitAssignment_operator(self, ctx:fullParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by fullParser#operator.
    def enterOperator(self, ctx:fullParser.OperatorContext):
        pass

    # Exit a parse tree produced by fullParser#operator.
    def exitOperator(self, ctx:fullParser.OperatorContext):
        pass


    # Enter a parse tree produced by fullParser#condition.
    def enterCondition(self, ctx:fullParser.ConditionContext):
        pass

    # Exit a parse tree produced by fullParser#condition.
    def exitCondition(self, ctx:fullParser.ConditionContext):
        pass


    # Enter a parse tree produced by fullParser#logical_condition.
    def enterLogical_condition(self, ctx:fullParser.Logical_conditionContext):
        pass

    # Exit a parse tree produced by fullParser#logical_condition.
    def exitLogical_condition(self, ctx:fullParser.Logical_conditionContext):
        pass


    # Enter a parse tree produced by fullParser#comparison_condition.
    def enterComparison_condition(self, ctx:fullParser.Comparison_conditionContext):
        pass

    # Exit a parse tree produced by fullParser#comparison_condition.
    def exitComparison_condition(self, ctx:fullParser.Comparison_conditionContext):
        pass


    # Enter a parse tree produced by fullParser#stat.
    def enterStat(self, ctx:fullParser.StatContext):
        pass

    # Exit a parse tree produced by fullParser#stat.
    def exitStat(self, ctx:fullParser.StatContext):
        pass


    # Enter a parse tree produced by fullParser#expr.
    def enterExpr(self, ctx:fullParser.ExprContext):
        pass

    # Exit a parse tree produced by fullParser#expr.
    def exitExpr(self, ctx:fullParser.ExprContext):
        pass


    # Enter a parse tree produced by fullParser#block.
    def enterBlock(self, ctx:fullParser.BlockContext):
        pass

    # Exit a parse tree produced by fullParser#block.
    def exitBlock(self, ctx:fullParser.BlockContext):
        pass


    # Enter a parse tree produced by fullParser#line.
    def enterLine(self, ctx:fullParser.LineContext):
        pass

    # Exit a parse tree produced by fullParser#line.
    def exitLine(self, ctx:fullParser.LineContext):
        pass


    # Enter a parse tree produced by fullParser#comment.
    def enterComment(self, ctx:fullParser.CommentContext):
        pass

    # Exit a parse tree produced by fullParser#comment.
    def exitComment(self, ctx:fullParser.CommentContext):
        pass


    # Enter a parse tree produced by fullParser#if_block.
    def enterIf_block(self, ctx:fullParser.If_blockContext):
        pass

    # Exit a parse tree produced by fullParser#if_block.
    def exitIf_block(self, ctx:fullParser.If_blockContext):
        pass


    # Enter a parse tree produced by fullParser#while_block.
    def enterWhile_block(self, ctx:fullParser.While_blockContext):
        pass

    # Exit a parse tree produced by fullParser#while_block.
    def exitWhile_block(self, ctx:fullParser.While_blockContext):
        pass


    # Enter a parse tree produced by fullParser#for_block.
    def enterFor_block(self, ctx:fullParser.For_blockContext):
        pass

    # Exit a parse tree produced by fullParser#for_block.
    def exitFor_block(self, ctx:fullParser.For_blockContext):
        pass


    # Enter a parse tree produced by fullParser#for_condition.
    def enterFor_condition(self, ctx:fullParser.For_conditionContext):
        pass

    # Exit a parse tree produced by fullParser#for_condition.
    def exitFor_condition(self, ctx:fullParser.For_conditionContext):
        pass


    # Enter a parse tree produced by fullParser#iterable.
    def enterIterable(self, ctx:fullParser.IterableContext):
        pass

    # Exit a parse tree produced by fullParser#iterable.
    def exitIterable(self, ctx:fullParser.IterableContext):
        pass



del fullParser