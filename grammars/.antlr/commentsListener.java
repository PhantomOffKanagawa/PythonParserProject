// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/comments.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link commentsParser}.
 */
public interface commentsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link commentsParser#comment}.
	 * @param ctx the parse tree
	 */
	void enterComment(commentsParser.CommentContext ctx);
	/**
	 * Exit a parse tree produced by {@link commentsParser#comment}.
	 * @param ctx the parse tree
	 */
	void exitComment(commentsParser.CommentContext ctx);
}