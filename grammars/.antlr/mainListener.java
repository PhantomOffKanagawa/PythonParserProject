// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/main.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link mainParser}.
 */
public interface mainListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link mainParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(mainParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(mainParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(mainParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(mainParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#code}.
	 * @param ctx the parse tree
	 */
	void enterCode(mainParser.CodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#code}.
	 * @param ctx the parse tree
	 */
	void exitCode(mainParser.CodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(mainParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(mainParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(mainParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(mainParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(mainParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(mainParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(mainParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(mainParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_operator(mainParser.Assignment_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_operator(mainParser.Assignment_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(mainParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(mainParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#if_block}.
	 * @param ctx the parse tree
	 */
	void enterIf_block(mainParser.If_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#if_block}.
	 * @param ctx the parse tree
	 */
	void exitIf_block(mainParser.If_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(mainParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(mainParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#logical_condition}.
	 * @param ctx the parse tree
	 */
	void enterLogical_condition(mainParser.Logical_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#logical_condition}.
	 * @param ctx the parse tree
	 */
	void exitLogical_condition(mainParser.Logical_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#comparison_condition}.
	 * @param ctx the parse tree
	 */
	void enterComparison_condition(mainParser.Comparison_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#comparison_condition}.
	 * @param ctx the parse tree
	 */
	void exitComparison_condition(mainParser.Comparison_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(mainParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(mainParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(mainParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(mainParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#comment}.
	 * @param ctx the parse tree
	 */
	void enterComment(mainParser.CommentContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#comment}.
	 * @param ctx the parse tree
	 */
	void exitComment(mainParser.CommentContext ctx);
}