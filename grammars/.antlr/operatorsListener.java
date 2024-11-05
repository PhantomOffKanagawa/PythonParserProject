// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/operators.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link operatorsParser}.
 */
public interface operatorsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link operatorsParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(operatorsParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link operatorsParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(operatorsParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link operatorsParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(operatorsParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link operatorsParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(operatorsParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link operatorsParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(operatorsParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link operatorsParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(operatorsParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link operatorsParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(operatorsParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link operatorsParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(operatorsParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link operatorsParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_operator(operatorsParser.Assignment_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link operatorsParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_operator(operatorsParser.Assignment_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link operatorsParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(operatorsParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link operatorsParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(operatorsParser.OperatorContext ctx);
}