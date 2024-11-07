# Generated from ./grammars/FullParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FullParser import FullParser
else:
    from FullParser import FullParser

# This class defines a complete listener for a parse tree produced by FullParser.
class FullParserListener(ParseTreeListener):

    # Enter a parse tree produced by FullParser#first_block.
    def enterFirst_block(self, ctx:FullParser.First_blockContext):
        pass

    # Exit a parse tree produced by FullParser#first_block.
    def exitFirst_block(self, ctx:FullParser.First_blockContext):
        pass


    # Enter a parse tree produced by FullParser#block.
    def enterBlock(self, ctx:FullParser.BlockContext):
        pass

    # Exit a parse tree produced by FullParser#block.
    def exitBlock(self, ctx:FullParser.BlockContext):
        pass


    # Enter a parse tree produced by FullParser#line.
    def enterLine(self, ctx:FullParser.LineContext):
        pass

    # Exit a parse tree produced by FullParser#line.
    def exitLine(self, ctx:FullParser.LineContext):
        pass


    # Enter a parse tree produced by FullParser#comment.
    def enterComment(self, ctx:FullParser.CommentContext):
        pass

    # Exit a parse tree produced by FullParser#comment.
    def exitComment(self, ctx:FullParser.CommentContext):
        pass


    # Enter a parse tree produced by FullParser#if_block.
    def enterIf_block(self, ctx:FullParser.If_blockContext):
        pass

    # Exit a parse tree produced by FullParser#if_block.
    def exitIf_block(self, ctx:FullParser.If_blockContext):
        pass


    # Enter a parse tree produced by FullParser#elif_block.
    def enterElif_block(self, ctx:FullParser.Elif_blockContext):
        pass

    # Exit a parse tree produced by FullParser#elif_block.
    def exitElif_block(self, ctx:FullParser.Elif_blockContext):
        pass


    # Enter a parse tree produced by FullParser#else_block.
    def enterElse_block(self, ctx:FullParser.Else_blockContext):
        pass

    # Exit a parse tree produced by FullParser#else_block.
    def exitElse_block(self, ctx:FullParser.Else_blockContext):
        pass


    # Enter a parse tree produced by FullParser#while_block.
    def enterWhile_block(self, ctx:FullParser.While_blockContext):
        pass

    # Exit a parse tree produced by FullParser#while_block.
    def exitWhile_block(self, ctx:FullParser.While_blockContext):
        pass


    # Enter a parse tree produced by FullParser#for_block.
    def enterFor_block(self, ctx:FullParser.For_blockContext):
        pass

    # Exit a parse tree produced by FullParser#for_block.
    def exitFor_block(self, ctx:FullParser.For_blockContext):
        pass


    # Enter a parse tree produced by FullParser#for_condition.
    def enterFor_condition(self, ctx:FullParser.For_conditionContext):
        pass

    # Exit a parse tree produced by FullParser#for_condition.
    def exitFor_condition(self, ctx:FullParser.For_conditionContext):
        pass


    # Enter a parse tree produced by FullParser#iterable.
    def enterIterable(self, ctx:FullParser.IterableContext):
        pass

    # Exit a parse tree produced by FullParser#iterable.
    def exitIterable(self, ctx:FullParser.IterableContext):
        pass


    # Enter a parse tree produced by FullParser#stat.
    def enterStat(self, ctx:FullParser.StatContext):
        pass

    # Exit a parse tree produced by FullParser#stat.
    def exitStat(self, ctx:FullParser.StatContext):
        pass


    # Enter a parse tree produced by FullParser#expr.
    def enterExpr(self, ctx:FullParser.ExprContext):
        pass

    # Exit a parse tree produced by FullParser#expr.
    def exitExpr(self, ctx:FullParser.ExprContext):
        pass


    # Enter a parse tree produced by FullParser#assignment.
    def enterAssignment(self, ctx:FullParser.AssignmentContext):
        pass

    # Exit a parse tree produced by FullParser#assignment.
    def exitAssignment(self, ctx:FullParser.AssignmentContext):
        pass


    # Enter a parse tree produced by FullParser#expression.
    def enterExpression(self, ctx:FullParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FullParser#expression.
    def exitExpression(self, ctx:FullParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FullParser#array.
    def enterArray(self, ctx:FullParser.ArrayContext):
        pass

    # Exit a parse tree produced by FullParser#array.
    def exitArray(self, ctx:FullParser.ArrayContext):
        pass


    # Enter a parse tree produced by FullParser#count.
    def enterCount(self, ctx:FullParser.CountContext):
        pass

    # Exit a parse tree produced by FullParser#count.
    def exitCount(self, ctx:FullParser.CountContext):
        pass


    # Enter a parse tree produced by FullParser#value.
    def enterValue(self, ctx:FullParser.ValueContext):
        pass

    # Exit a parse tree produced by FullParser#value.
    def exitValue(self, ctx:FullParser.ValueContext):
        pass


    # Enter a parse tree produced by FullParser#assignment_operator.
    def enterAssignment_operator(self, ctx:FullParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by FullParser#assignment_operator.
    def exitAssignment_operator(self, ctx:FullParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by FullParser#operator.
    def enterOperator(self, ctx:FullParser.OperatorContext):
        pass

    # Exit a parse tree produced by FullParser#operator.
    def exitOperator(self, ctx:FullParser.OperatorContext):
        pass


    # Enter a parse tree produced by FullParser#condition.
    def enterCondition(self, ctx:FullParser.ConditionContext):
        pass

    # Exit a parse tree produced by FullParser#condition.
    def exitCondition(self, ctx:FullParser.ConditionContext):
        pass


    # Enter a parse tree produced by FullParser#comparison_condition.
    def enterComparison_condition(self, ctx:FullParser.Comparison_conditionContext):
        pass

    # Exit a parse tree produced by FullParser#comparison_condition.
    def exitComparison_condition(self, ctx:FullParser.Comparison_conditionContext):
        pass



del FullParser