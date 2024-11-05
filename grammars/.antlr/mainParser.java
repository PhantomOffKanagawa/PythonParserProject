// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/main.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class mainParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WS_SKIPPED=1, ASSIGNMENT_OP=2, ARITHMETIC_OP=3, LBRACKET=4, RBRACKET=5, 
		COMMA=6, IF=7, ELIF=8, ELSE=9, COLON=10, LPAREN=11, RPAREN=12, COMPARISON_OP=13, 
		LOGICAL_OP=14, NOT_OP=15, WHILE=16, FOR=17, NUMBER=18, BOOLEAN=19, STRING=20, 
		ESC=21, VARIABLE=22, WS=23, SINGLE_LINE_COMMENT=24, MULTI_LINE_COMMENT=25;
	public static final int
		RULE_stat = 0, RULE_expr = 1, RULE_code = 2, RULE_block = 3, RULE_line = 4, 
		RULE_assignment = 5, RULE_expression = 6, RULE_array = 7, RULE_value = 8, 
		RULE_assignment_operator = 9, RULE_operator = 10, RULE_comment = 11, RULE_if_block = 12, 
		RULE_condition = 13, RULE_logical_condition = 14, RULE_comparison_condition = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"stat", "expr", "code", "block", "line", "assignment", "expression", 
			"array", "value", "assignment_operator", "operator", "comment", "if_block", 
			"condition", "logical_condition", "comparison_condition"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "'['", "']'", "','", "'if'", "'elif'", "'else'", 
			"':'", "'('", "')'", null, null, "'not'", "'while'", "'for'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WS_SKIPPED", "ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", "RBRACKET", 
			"COMMA", "IF", "ELIF", "ELSE", "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", 
			"LOGICAL_OP", "NOT_OP", "WHILE", "FOR", "NUMBER", "BOOLEAN", "STRING", 
			"ESC", "VARIABLE", "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "main.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public mainParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(mainParser.EOF, 0); }
		public List<CodeContext> code() {
			return getRuleContexts(CodeContext.class);
		}
		public CodeContext code(int i) {
			return getRuleContext(CodeContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 54526080L) != 0)) {
				{
				{
				setState(34);
				code();
				}
				}
				setState(39);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(40);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CodeContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public If_blockContext if_block() {
			return getRuleContext(If_blockContext.class,0);
		}
		public CodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_code; }
	}

	public final CodeContext code() throws RecognitionException {
		CodeContext _localctx = new CodeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_code);
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARIABLE:
			case SINGLE_LINE_COMMENT:
			case MULTI_LINE_COMMENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(42);
				block();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(43);
				if_block();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(47); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(46);
					line();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(49); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public CommentContext comment() {
			return getRuleContext(CommentContext.class,0);
		}
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_line);
		try {
			setState(53);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARIABLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				assignment();
				}
				break;
			case SINGLE_LINE_COMMENT:
			case MULTI_LINE_COMMENT:
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
				comment();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode VARIABLE() { return getToken(mainParser.VARIABLE, 0); }
		public Assignment_operatorContext assignment_operator() {
			return getRuleContext(Assignment_operatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(mainParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(mainParser.WS, i);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(VARIABLE);
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(56);
				match(WS);
				}
			}

			setState(59);
			assignment_operator();
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(60);
				match(WS);
				}
			}

			setState(63);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(mainParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(mainParser.WS, i);
		}
		public List<OperatorContext> operator() {
			return getRuleContexts(OperatorContext.class);
		}
		public OperatorContext operator(int i) {
			return getRuleContext(OperatorContext.class,i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			value();
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(66);
				match(WS);
				}
			}

			setState(79);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ARITHMETIC_OP) {
				{
				{
				setState(69);
				operator();
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(70);
					match(WS);
					}
				}

				setState(73);
				value();
				setState(75);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(74);
					match(WS);
					}
				}

				}
				}
				setState(81);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(mainParser.LBRACKET, 0); }
		public TerminalNode RBRACKET() { return getToken(mainParser.RBRACKET, 0); }
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(mainParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(mainParser.WS, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(mainParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(mainParser.COMMA, i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(LBRACKET);
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(83);
					match(WS);
					}
				}

				setState(86);
				value();
				setState(88);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
				case 1:
					{
					setState(87);
					match(WS);
					}
					break;
				}
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(90);
					match(COMMA);
					setState(92);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(91);
						match(WS);
						}
					}

					setState(94);
					value();
					setState(96);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
					case 1:
						{
						setState(95);
						match(WS);
						}
						break;
					}
					}
					}
					setState(102);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(105);
				match(WS);
				}
			}

			setState(108);
			match(RBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(mainParser.NUMBER, 0); }
		public TerminalNode VARIABLE() { return getToken(mainParser.VARIABLE, 0); }
		public TerminalNode BOOLEAN() { return getToken(mainParser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(mainParser.STRING, 0); }
		public TerminalNode LPAREN() { return getToken(mainParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(mainParser.RPAREN, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_value);
		try {
			setState(119);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				match(NUMBER);
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(111);
				match(VARIABLE);
				}
				break;
			case BOOLEAN:
				enterOuterAlt(_localctx, 3);
				{
				setState(112);
				match(BOOLEAN);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(113);
				match(STRING);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 5);
				{
				setState(114);
				match(LPAREN);
				setState(115);
				expression();
				setState(116);
				match(RPAREN);
				}
				break;
			case LBRACKET:
				enterOuterAlt(_localctx, 6);
				{
				setState(118);
				array();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assignment_operatorContext extends ParserRuleContext {
		public TerminalNode ASSIGNMENT_OP() { return getToken(mainParser.ASSIGNMENT_OP, 0); }
		public Assignment_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment_operator; }
	}

	public final Assignment_operatorContext assignment_operator() throws RecognitionException {
		Assignment_operatorContext _localctx = new Assignment_operatorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_assignment_operator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(ASSIGNMENT_OP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperatorContext extends ParserRuleContext {
		public TerminalNode ARITHMETIC_OP() { return getToken(mainParser.ARITHMETIC_OP, 0); }
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_operator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(ARITHMETIC_OP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommentContext extends ParserRuleContext {
		public TerminalNode SINGLE_LINE_COMMENT() { return getToken(mainParser.SINGLE_LINE_COMMENT, 0); }
		public TerminalNode MULTI_LINE_COMMENT() { return getToken(mainParser.MULTI_LINE_COMMENT, 0); }
		public CommentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comment; }
	}

	public final CommentContext comment() throws RecognitionException {
		CommentContext _localctx = new CommentContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_comment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_la = _input.LA(1);
			if ( !(_la==SINGLE_LINE_COMMENT || _la==MULTI_LINE_COMMENT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_blockContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(mainParser.IF, 0); }
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(mainParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(mainParser.COLON, i);
		}
		public List<TerminalNode> WS() { return getTokens(mainParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(mainParser.WS, i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<If_blockContext> if_block() {
			return getRuleContexts(If_blockContext.class);
		}
		public If_blockContext if_block(int i) {
			return getRuleContext(If_blockContext.class,i);
		}
		public List<TerminalNode> ELIF() { return getTokens(mainParser.ELIF); }
		public TerminalNode ELIF(int i) {
			return getToken(mainParser.ELIF, i);
		}
		public TerminalNode ELSE() { return getToken(mainParser.ELSE, 0); }
		public If_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_block; }
	}

	public final If_blockContext if_block() throws RecognitionException {
		If_blockContext _localctx = new If_blockContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_if_block);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(IF);
			setState(129);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(128);
				match(WS);
				}
				break;
			}
			setState(131);
			condition();
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(132);
				match(WS);
				}
			}

			setState(135);
			match(COLON);
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(136);
				match(WS);
				}
			}

			setState(141); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(141);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case VARIABLE:
					case SINGLE_LINE_COMMENT:
					case MULTI_LINE_COMMENT:
						{
						setState(139);
						block();
						}
						break;
					case IF:
						{
						setState(140);
						if_block();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(143); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(161);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(145);
					match(ELIF);
					setState(146);
					condition();
					setState(148);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(147);
						match(WS);
						}
					}

					setState(150);
					match(COLON);
					setState(152);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(151);
						match(WS);
						}
					}

					setState(155); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(154);
							block();
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(157); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					} 
				}
				setState(163);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			setState(177);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				{
				setState(164);
				match(ELSE);
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(165);
					match(WS);
					}
				}

				setState(168);
				match(COLON);
				setState(170);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(169);
					match(WS);
					}
				}

				setState(173); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(172);
						block();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(175); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public Logical_conditionContext logical_condition() {
			return getRuleContext(Logical_conditionContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			logical_condition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logical_conditionContext extends ParserRuleContext {
		public List<Comparison_conditionContext> comparison_condition() {
			return getRuleContexts(Comparison_conditionContext.class);
		}
		public Comparison_conditionContext comparison_condition(int i) {
			return getRuleContext(Comparison_conditionContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(mainParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(mainParser.WS, i);
		}
		public List<TerminalNode> LOGICAL_OP() { return getTokens(mainParser.LOGICAL_OP); }
		public TerminalNode LOGICAL_OP(int i) {
			return getToken(mainParser.LOGICAL_OP, i);
		}
		public List<TerminalNode> COMPARISON_OP() { return getTokens(mainParser.COMPARISON_OP); }
		public TerminalNode COMPARISON_OP(int i) {
			return getToken(mainParser.COMPARISON_OP, i);
		}
		public Logical_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_condition; }
	}

	public final Logical_conditionContext logical_condition() throws RecognitionException {
		Logical_conditionContext _localctx = new Logical_conditionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_logical_condition);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(181);
				match(WS);
				}
			}

			setState(184);
			comparison_condition();
			setState(195);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,34,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(186);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(185);
						match(WS);
						}
					}

					setState(188);
					_la = _input.LA(1);
					if ( !(_la==COMPARISON_OP || _la==LOGICAL_OP) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(190);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(189);
						match(WS);
						}
					}

					setState(192);
					comparison_condition();
					}
					} 
				}
				setState(197);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,34,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Comparison_conditionContext extends ParserRuleContext {
		public TerminalNode NOT_OP() { return getToken(mainParser.NOT_OP, 0); }
		public Comparison_conditionContext comparison_condition() {
			return getRuleContext(Comparison_conditionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(mainParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(mainParser.WS, i);
		}
		public TerminalNode LPAREN() { return getToken(mainParser.LPAREN, 0); }
		public Logical_conditionContext logical_condition() {
			return getRuleContext(Logical_conditionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(mainParser.RPAREN, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Comparison_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison_condition; }
	}

	public final Comparison_conditionContext comparison_condition() throws RecognitionException {
		Comparison_conditionContext _localctx = new Comparison_conditionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_comparison_condition);
		int _la;
		try {
			setState(214);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(198);
				match(NOT_OP);
				setState(200);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(199);
					match(WS);
					}
				}

				setState(202);
				comparison_condition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(203);
				match(LPAREN);
				setState(205);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
				case 1:
					{
					setState(204);
					match(WS);
					}
					break;
				}
				setState(207);
				logical_condition();
				setState(209);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(208);
					match(WS);
					}
				}

				setState(211);
				match(RPAREN);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(213);
				value();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0019\u00d9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0001\u0000\u0001\u0000\u0001\u0001\u0005\u0001$\b\u0001\n\u0001"+
		"\f\u0001\'\t\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0003"+
		"\u0002-\b\u0002\u0001\u0003\u0004\u00030\b\u0003\u000b\u0003\f\u00031"+
		"\u0001\u0004\u0001\u0004\u0003\u00046\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0003\u0005:\b\u0005\u0001\u0005\u0001\u0005\u0003\u0005>\b\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0003\u0006D\b\u0006\u0001"+
		"\u0006\u0001\u0006\u0003\u0006H\b\u0006\u0001\u0006\u0001\u0006\u0003"+
		"\u0006L\b\u0006\u0005\u0006N\b\u0006\n\u0006\f\u0006Q\t\u0006\u0001\u0007"+
		"\u0001\u0007\u0003\u0007U\b\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"Y\b\u0007\u0001\u0007\u0001\u0007\u0003\u0007]\b\u0007\u0001\u0007\u0001"+
		"\u0007\u0003\u0007a\b\u0007\u0005\u0007c\b\u0007\n\u0007\f\u0007f\t\u0007"+
		"\u0003\u0007h\b\u0007\u0001\u0007\u0003\u0007k\b\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0003\bx\b\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0003\f\u0082\b\f\u0001\f\u0001\f\u0003\f\u0086"+
		"\b\f\u0001\f\u0001\f\u0003\f\u008a\b\f\u0001\f\u0001\f\u0004\f\u008e\b"+
		"\f\u000b\f\f\f\u008f\u0001\f\u0001\f\u0001\f\u0003\f\u0095\b\f\u0001\f"+
		"\u0001\f\u0003\f\u0099\b\f\u0001\f\u0004\f\u009c\b\f\u000b\f\f\f\u009d"+
		"\u0005\f\u00a0\b\f\n\f\f\f\u00a3\t\f\u0001\f\u0001\f\u0003\f\u00a7\b\f"+
		"\u0001\f\u0001\f\u0003\f\u00ab\b\f\u0001\f\u0004\f\u00ae\b\f\u000b\f\f"+
		"\f\u00af\u0003\f\u00b2\b\f\u0001\r\u0001\r\u0001\u000e\u0003\u000e\u00b7"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00bb\b\u000e\u0001\u000e"+
		"\u0001\u000e\u0003\u000e\u00bf\b\u000e\u0001\u000e\u0005\u000e\u00c2\b"+
		"\u000e\n\u000e\f\u000e\u00c5\t\u000e\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u00c9\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00ce\b"+
		"\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00d2\b\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u00d7\b\u000f\u0001\u000f\u0000\u0000\u0010"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e\u0000\u0002\u0001\u0000\u0018\u0019\u0001\u0000\r\u000e\u00f4"+
		"\u0000 \u0001\u0000\u0000\u0000\u0002%\u0001\u0000\u0000\u0000\u0004,"+
		"\u0001\u0000\u0000\u0000\u0006/\u0001\u0000\u0000\u0000\b5\u0001\u0000"+
		"\u0000\u0000\n7\u0001\u0000\u0000\u0000\fA\u0001\u0000\u0000\u0000\u000e"+
		"R\u0001\u0000\u0000\u0000\u0010w\u0001\u0000\u0000\u0000\u0012y\u0001"+
		"\u0000\u0000\u0000\u0014{\u0001\u0000\u0000\u0000\u0016}\u0001\u0000\u0000"+
		"\u0000\u0018\u007f\u0001\u0000\u0000\u0000\u001a\u00b3\u0001\u0000\u0000"+
		"\u0000\u001c\u00b6\u0001\u0000\u0000\u0000\u001e\u00d6\u0001\u0000\u0000"+
		"\u0000 !\u0003\u0002\u0001\u0000!\u0001\u0001\u0000\u0000\u0000\"$\u0003"+
		"\u0004\u0002\u0000#\"\u0001\u0000\u0000\u0000$\'\u0001\u0000\u0000\u0000"+
		"%#\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&(\u0001\u0000\u0000"+
		"\u0000\'%\u0001\u0000\u0000\u0000()\u0005\u0000\u0000\u0001)\u0003\u0001"+
		"\u0000\u0000\u0000*-\u0003\u0006\u0003\u0000+-\u0003\u0018\f\u0000,*\u0001"+
		"\u0000\u0000\u0000,+\u0001\u0000\u0000\u0000-\u0005\u0001\u0000\u0000"+
		"\u0000.0\u0003\b\u0004\u0000/.\u0001\u0000\u0000\u000001\u0001\u0000\u0000"+
		"\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u00002\u0007\u0001"+
		"\u0000\u0000\u000036\u0003\n\u0005\u000046\u0003\u0016\u000b\u000053\u0001"+
		"\u0000\u0000\u000054\u0001\u0000\u0000\u00006\t\u0001\u0000\u0000\u0000"+
		"79\u0005\u0016\u0000\u00008:\u0005\u0017\u0000\u000098\u0001\u0000\u0000"+
		"\u00009:\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;=\u0003\u0012"+
		"\t\u0000<>\u0005\u0017\u0000\u0000=<\u0001\u0000\u0000\u0000=>\u0001\u0000"+
		"\u0000\u0000>?\u0001\u0000\u0000\u0000?@\u0003\f\u0006\u0000@\u000b\u0001"+
		"\u0000\u0000\u0000AC\u0003\u0010\b\u0000BD\u0005\u0017\u0000\u0000CB\u0001"+
		"\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000DO\u0001\u0000\u0000\u0000"+
		"EG\u0003\u0014\n\u0000FH\u0005\u0017\u0000\u0000GF\u0001\u0000\u0000\u0000"+
		"GH\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IK\u0003\u0010\b\u0000"+
		"JL\u0005\u0017\u0000\u0000KJ\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000"+
		"\u0000LN\u0001\u0000\u0000\u0000ME\u0001\u0000\u0000\u0000NQ\u0001\u0000"+
		"\u0000\u0000OM\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000P\r\u0001"+
		"\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000Rg\u0005\u0004\u0000\u0000"+
		"SU\u0005\u0017\u0000\u0000TS\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000"+
		"\u0000UV\u0001\u0000\u0000\u0000VX\u0003\u0010\b\u0000WY\u0005\u0017\u0000"+
		"\u0000XW\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Yd\u0001\u0000"+
		"\u0000\u0000Z\\\u0005\u0006\u0000\u0000[]\u0005\u0017\u0000\u0000\\[\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000"+
		"^`\u0003\u0010\b\u0000_a\u0005\u0017\u0000\u0000`_\u0001\u0000\u0000\u0000"+
		"`a\u0001\u0000\u0000\u0000ac\u0001\u0000\u0000\u0000bZ\u0001\u0000\u0000"+
		"\u0000cf\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000de\u0001\u0000"+
		"\u0000\u0000eh\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000gT\u0001"+
		"\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hj\u0001\u0000\u0000\u0000"+
		"ik\u0005\u0017\u0000\u0000ji\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000"+
		"\u0000kl\u0001\u0000\u0000\u0000lm\u0005\u0005\u0000\u0000m\u000f\u0001"+
		"\u0000\u0000\u0000nx\u0005\u0012\u0000\u0000ox\u0005\u0016\u0000\u0000"+
		"px\u0005\u0013\u0000\u0000qx\u0005\u0014\u0000\u0000rs\u0005\u000b\u0000"+
		"\u0000st\u0003\f\u0006\u0000tu\u0005\f\u0000\u0000ux\u0001\u0000\u0000"+
		"\u0000vx\u0003\u000e\u0007\u0000wn\u0001\u0000\u0000\u0000wo\u0001\u0000"+
		"\u0000\u0000wp\u0001\u0000\u0000\u0000wq\u0001\u0000\u0000\u0000wr\u0001"+
		"\u0000\u0000\u0000wv\u0001\u0000\u0000\u0000x\u0011\u0001\u0000\u0000"+
		"\u0000yz\u0005\u0002\u0000\u0000z\u0013\u0001\u0000\u0000\u0000{|\u0005"+
		"\u0003\u0000\u0000|\u0015\u0001\u0000\u0000\u0000}~\u0007\u0000\u0000"+
		"\u0000~\u0017\u0001\u0000\u0000\u0000\u007f\u0081\u0005\u0007\u0000\u0000"+
		"\u0080\u0082\u0005\u0017\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000"+
		"\u0081\u0082\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000"+
		"\u0083\u0085\u0003\u001a\r\u0000\u0084\u0086\u0005\u0017\u0000\u0000\u0085"+
		"\u0084\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086"+
		"\u0087\u0001\u0000\u0000\u0000\u0087\u0089\u0005\n\u0000\u0000\u0088\u008a"+
		"\u0005\u0017\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0001\u0000\u0000\u0000\u008a\u008d\u0001\u0000\u0000\u0000\u008b\u008e"+
		"\u0003\u0006\u0003\u0000\u008c\u008e\u0003\u0018\f\u0000\u008d\u008b\u0001"+
		"\u0000\u0000\u0000\u008d\u008c\u0001\u0000\u0000\u0000\u008e\u008f\u0001"+
		"\u0000\u0000\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u008f\u0090\u0001"+
		"\u0000\u0000\u0000\u0090\u00a1\u0001\u0000\u0000\u0000\u0091\u0092\u0005"+
		"\b\u0000\u0000\u0092\u0094\u0003\u001a\r\u0000\u0093\u0095\u0005\u0017"+
		"\u0000\u0000\u0094\u0093\u0001\u0000\u0000\u0000\u0094\u0095\u0001\u0000"+
		"\u0000\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096\u0098\u0005\n\u0000"+
		"\u0000\u0097\u0099\u0005\u0017\u0000\u0000\u0098\u0097\u0001\u0000\u0000"+
		"\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099\u009b\u0001\u0000\u0000"+
		"\u0000\u009a\u009c\u0003\u0006\u0003\u0000\u009b\u009a\u0001\u0000\u0000"+
		"\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d\u009b\u0001\u0000\u0000"+
		"\u0000\u009d\u009e\u0001\u0000\u0000\u0000\u009e\u00a0\u0001\u0000\u0000"+
		"\u0000\u009f\u0091\u0001\u0000\u0000\u0000\u00a0\u00a3\u0001\u0000\u0000"+
		"\u0000\u00a1\u009f\u0001\u0000\u0000\u0000\u00a1\u00a2\u0001\u0000\u0000"+
		"\u0000\u00a2\u00b1\u0001\u0000\u0000\u0000\u00a3\u00a1\u0001\u0000\u0000"+
		"\u0000\u00a4\u00a6\u0005\t\u0000\u0000\u00a5\u00a7\u0005\u0017\u0000\u0000"+
		"\u00a6\u00a5\u0001\u0000\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000"+
		"\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u00aa\u0005\n\u0000\u0000\u00a9"+
		"\u00ab\u0005\u0017\u0000\u0000\u00aa\u00a9\u0001\u0000\u0000\u0000\u00aa"+
		"\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ad\u0001\u0000\u0000\u0000\u00ac"+
		"\u00ae\u0003\u0006\u0003\u0000\u00ad\u00ac\u0001\u0000\u0000\u0000\u00ae"+
		"\u00af\u0001\u0000\u0000\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00af"+
		"\u00b0\u0001\u0000\u0000\u0000\u00b0\u00b2\u0001\u0000\u0000\u0000\u00b1"+
		"\u00a4\u0001\u0000\u0000\u0000\u00b1\u00b2\u0001\u0000\u0000\u0000\u00b2"+
		"\u0019\u0001\u0000\u0000\u0000\u00b3\u00b4\u0003\u001c\u000e\u0000\u00b4"+
		"\u001b\u0001\u0000\u0000\u0000\u00b5\u00b7\u0005\u0017\u0000\u0000\u00b6"+
		"\u00b5\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7"+
		"\u00b8\u0001\u0000\u0000\u0000\u00b8\u00c3\u0003\u001e\u000f\u0000\u00b9"+
		"\u00bb\u0005\u0017\u0000\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00ba"+
		"\u00bb\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc"+
		"\u00be\u0007\u0001\u0000\u0000\u00bd\u00bf\u0005\u0017\u0000\u0000\u00be"+
		"\u00bd\u0001\u0000\u0000\u0000\u00be\u00bf\u0001\u0000\u0000\u0000\u00bf"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c0\u00c2\u0003\u001e\u000f\u0000\u00c1"+
		"\u00ba\u0001\u0000\u0000\u0000\u00c2\u00c5\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c1\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000\u00c4"+
		"\u001d\u0001\u0000\u0000\u0000\u00c5\u00c3\u0001\u0000\u0000\u0000\u00c6"+
		"\u00c8\u0005\u000f\u0000\u0000\u00c7\u00c9\u0005\u0017\u0000\u0000\u00c8"+
		"\u00c7\u0001\u0000\u0000\u0000\u00c8\u00c9\u0001\u0000\u0000\u0000\u00c9"+
		"\u00ca\u0001\u0000\u0000\u0000\u00ca\u00d7\u0003\u001e\u000f\u0000\u00cb"+
		"\u00cd\u0005\u000b\u0000\u0000\u00cc\u00ce\u0005\u0017\u0000\u0000\u00cd"+
		"\u00cc\u0001\u0000\u0000\u0000\u00cd\u00ce\u0001\u0000\u0000\u0000\u00ce"+
		"\u00cf\u0001\u0000\u0000\u0000\u00cf\u00d1\u0003\u001c\u000e\u0000\u00d0"+
		"\u00d2\u0005\u0017\u0000\u0000\u00d1\u00d0\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d4\u0005\f\u0000\u0000\u00d4\u00d7\u0001\u0000\u0000\u0000\u00d5\u00d7"+
		"\u0003\u0010\b\u0000\u00d6\u00c6\u0001\u0000\u0000\u0000\u00d6\u00cb\u0001"+
		"\u0000\u0000\u0000\u00d6\u00d5\u0001\u0000\u0000\u0000\u00d7\u001f\u0001"+
		"\u0000\u0000\u0000\'%,159=CGKOTX\\`dgjw\u0081\u0085\u0089\u008d\u008f"+
		"\u0094\u0098\u009d\u00a1\u00a6\u00aa\u00af\u00b1\u00b6\u00ba\u00be\u00c3"+
		"\u00c8\u00cd\u00d1\u00d6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}