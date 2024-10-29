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


    # Enter a parse tree produced by mainParser#statement.
    def enterStatement(self, ctx:mainParser.StatementContext):
        pass

    # Exit a parse tree produced by mainParser#statement.
    def exitStatement(self, ctx:mainParser.StatementContext):
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


    # Enter a parse tree produced by mainParser#value.
    def enterValue(self, ctx:mainParser.ValueContext):
        pass

    # Exit a parse tree produced by mainParser#value.
    def exitValue(self, ctx:mainParser.ValueContext):
        pass


    # Enter a parse tree produced by mainParser#operator.
    def enterOperator(self, ctx:mainParser.OperatorContext):
        pass

    # Exit a parse tree produced by mainParser#operator.
    def exitOperator(self, ctx:mainParser.OperatorContext):
        pass



del mainParser