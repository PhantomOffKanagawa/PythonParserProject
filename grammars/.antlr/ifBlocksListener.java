// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/ifBlocks.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ifBlocksParser}.
 */
public interface ifBlocksListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#if_block}.
	 * @param ctx the parse tree
	 */
	void enterIf_block(ifBlocksParser.If_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#if_block}.
	 * @param ctx the parse tree
	 */
	void exitIf_block(ifBlocksParser.If_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(ifBlocksParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(ifBlocksParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#logical_condition}.
	 * @param ctx the parse tree
	 */
	void enterLogical_condition(ifBlocksParser.Logical_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#logical_condition}.
	 * @param ctx the parse tree
	 */
	void exitLogical_condition(ifBlocksParser.Logical_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#comparison_condition}.
	 * @param ctx the parse tree
	 */
	void enterComparison_condition(ifBlocksParser.Comparison_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#comparison_condition}.
	 * @param ctx the parse tree
	 */
	void exitComparison_condition(ifBlocksParser.Comparison_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(ifBlocksParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(ifBlocksParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(ifBlocksParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(ifBlocksParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ifBlocksParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ifBlocksParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ifBlocksParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ifBlocksParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(ifBlocksParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(ifBlocksParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(ifBlocksParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(ifBlocksParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_operator(ifBlocksParser.Assignment_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_operator(ifBlocksParser.Assignment_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(ifBlocksParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(ifBlocksParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ifBlocksParser#comment}.
	 * @param ctx the parse tree
	 */
	void enterComment(ifBlocksParser.CommentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ifBlocksParser#comment}.
	 * @param ctx the parse tree
	 */
	void exitComment(ifBlocksParser.CommentContext ctx);
}