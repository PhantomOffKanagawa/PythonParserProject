// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/genericBlocks.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link genericBlocksParser}.
 */
public interface genericBlocksListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(genericBlocksParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(genericBlocksParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(genericBlocksParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(genericBlocksParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(genericBlocksParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(genericBlocksParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(genericBlocksParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(genericBlocksParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(genericBlocksParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(genericBlocksParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(genericBlocksParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(genericBlocksParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_operator(genericBlocksParser.Assignment_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_operator(genericBlocksParser.Assignment_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(genericBlocksParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(genericBlocksParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#comment}.
	 * @param ctx the parse tree
	 */
	void enterComment(genericBlocksParser.CommentContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#comment}.
	 * @param ctx the parse tree
	 */
	void exitComment(genericBlocksParser.CommentContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#if_block}.
	 * @param ctx the parse tree
	 */
	void enterIf_block(genericBlocksParser.If_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#if_block}.
	 * @param ctx the parse tree
	 */
	void exitIf_block(genericBlocksParser.If_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(genericBlocksParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(genericBlocksParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#logical_condition}.
	 * @param ctx the parse tree
	 */
	void enterLogical_condition(genericBlocksParser.Logical_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#logical_condition}.
	 * @param ctx the parse tree
	 */
	void exitLogical_condition(genericBlocksParser.Logical_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link genericBlocksParser#comparison_condition}.
	 * @param ctx the parse tree
	 */
	void enterComparison_condition(genericBlocksParser.Comparison_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link genericBlocksParser#comparison_condition}.
	 * @param ctx the parse tree
	 */
	void exitComparison_condition(genericBlocksParser.Comparison_conditionContext ctx);
}