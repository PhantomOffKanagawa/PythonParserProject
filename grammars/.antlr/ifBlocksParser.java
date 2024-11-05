// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/ifBlocks.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ifBlocksParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSIGNMENT_OP=1, ARITHMETIC_OP=2, LBRACKET=3, RBRACKET=4, COMMA=5, IF=6, 
		ELIF=7, ELSE=8, COLON=9, LPAREN=10, RPAREN=11, COMPARISON_OP=12, LOGICAL_OP=13, 
		NOT_OP=14, WHILE=15, FOR=16, NUMBER=17, BOOLEAN=18, STRING=19, ESC=20, 
		VARIABLE=21, WS=22, SINGLE_LINE_COMMENT=23, MULTI_LINE_COMMENT=24;
	public static final int
		RULE_if_block = 0, RULE_condition = 1, RULE_logical_condition = 2, RULE_comparison_condition = 3, 
		RULE_block = 4, RULE_assignment = 5, RULE_expression = 6, RULE_array = 7, 
		RULE_value = 8, RULE_assignment_operator = 9, RULE_operator = 10, RULE_line = 11, 
		RULE_comment = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"if_block", "condition", "logical_condition", "comparison_condition", 
			"block", "assignment", "expression", "array", "value", "assignment_operator", 
			"operator", "line", "comment"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'['", "']'", "','", "'if'", "'elif'", "'else'", "':'", 
			"'('", "')'", null, null, "'not'", "'while'", "'for'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", "RBRACKET", "COMMA", 
			"IF", "ELIF", "ELSE", "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
			"NOT_OP", "WHILE", "FOR", "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", 
			"WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT"
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
	public String getGrammarFileName() { return "ifBlocks.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ifBlocksParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_blockContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(ifBlocksParser.IF, 0); }
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(ifBlocksParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(ifBlocksParser.COLON, i);
		}
		public List<TerminalNode> WS() { return getTokens(ifBlocksParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(ifBlocksParser.WS, i);
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
		public List<TerminalNode> ELIF() { return getTokens(ifBlocksParser.ELIF); }
		public TerminalNode ELIF(int i) {
			return getToken(ifBlocksParser.ELIF, i);
		}
		public TerminalNode ELSE() { return getToken(ifBlocksParser.ELSE, 0); }
		public If_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_block; }
	}

	public final If_blockContext if_block() throws RecognitionException {
		If_blockContext _localctx = new If_blockContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_if_block);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			match(IF);
			setState(28);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(27);
				match(WS);
				}
				break;
			}
			setState(30);
			condition();
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(31);
				match(WS);
				}
			}

			setState(34);
			match(COLON);
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(35);
				match(WS);
				}
			}

			setState(40); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(40);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LBRACKET:
					case LPAREN:
					case NUMBER:
					case BOOLEAN:
					case STRING:
					case VARIABLE:
						{
						setState(38);
						block();
						}
						break;
					case IF:
						{
						setState(39);
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
				setState(42); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(60);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(44);
					match(ELIF);
					setState(45);
					condition();
					setState(47);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(46);
						match(WS);
						}
					}

					setState(49);
					match(COLON);
					setState(51);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(50);
						match(WS);
						}
					}

					setState(54); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(53);
							block();
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(56); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					} 
				}
				setState(62);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(76);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(63);
				match(ELSE);
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(64);
					match(WS);
					}
				}

				setState(67);
				match(COLON);
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(68);
					match(WS);
					}
				}

				setState(72); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(71);
						block();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(74); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
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
		enterRule(_localctx, 2, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
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
		public List<TerminalNode> WS() { return getTokens(ifBlocksParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(ifBlocksParser.WS, i);
		}
		public List<TerminalNode> LOGICAL_OP() { return getTokens(ifBlocksParser.LOGICAL_OP); }
		public TerminalNode LOGICAL_OP(int i) {
			return getToken(ifBlocksParser.LOGICAL_OP, i);
		}
		public List<TerminalNode> COMPARISON_OP() { return getTokens(ifBlocksParser.COMPARISON_OP); }
		public TerminalNode COMPARISON_OP(int i) {
			return getToken(ifBlocksParser.COMPARISON_OP, i);
		}
		public Logical_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_condition; }
	}

	public final Logical_conditionContext logical_condition() throws RecognitionException {
		Logical_conditionContext _localctx = new Logical_conditionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_logical_condition);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(80);
				match(WS);
				}
			}

			setState(83);
			comparison_condition();
			setState(94);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(85);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(84);
						match(WS);
						}
					}

					setState(87);
					_la = _input.LA(1);
					if ( !(_la==COMPARISON_OP || _la==LOGICAL_OP) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(89);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(88);
						match(WS);
						}
					}

					setState(91);
					comparison_condition();
					}
					} 
				}
				setState(96);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
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
		public TerminalNode NOT_OP() { return getToken(ifBlocksParser.NOT_OP, 0); }
		public Comparison_conditionContext comparison_condition() {
			return getRuleContext(Comparison_conditionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(ifBlocksParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(ifBlocksParser.WS, i);
		}
		public TerminalNode LPAREN() { return getToken(ifBlocksParser.LPAREN, 0); }
		public Logical_conditionContext logical_condition() {
			return getRuleContext(Logical_conditionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ifBlocksParser.RPAREN, 0); }
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
		enterRule(_localctx, 6, RULE_comparison_condition);
		int _la;
		try {
			setState(113);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(97);
				match(NOT_OP);
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(98);
					match(WS);
					}
				}

				setState(101);
				comparison_condition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(102);
				match(LPAREN);
				setState(104);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
				case 1:
					{
					setState(103);
					match(WS);
					}
					break;
				}
				setState(106);
				logical_condition();
				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(107);
					match(WS);
					}
				}

				setState(110);
				match(RPAREN);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(112);
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

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_block);
		try {
			setState(117);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(115);
				assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(116);
				expression();
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

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode VARIABLE() { return getToken(ifBlocksParser.VARIABLE, 0); }
		public Assignment_operatorContext assignment_operator() {
			return getRuleContext(Assignment_operatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(ifBlocksParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(ifBlocksParser.WS, i);
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
			setState(119);
			match(VARIABLE);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(120);
				match(WS);
				}
			}

			setState(123);
			assignment_operator();
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(124);
				match(WS);
				}
			}

			setState(127);
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
		public List<TerminalNode> WS() { return getTokens(ifBlocksParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(ifBlocksParser.WS, i);
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
			setState(129);
			value();
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(130);
				match(WS);
				}
			}

			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ARITHMETIC_OP) {
				{
				{
				setState(133);
				operator();
				setState(135);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(134);
					match(WS);
					}
				}

				setState(137);
				value();
				setState(139);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(138);
					match(WS);
					}
				}

				}
				}
				setState(145);
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
		public TerminalNode LBRACKET() { return getToken(ifBlocksParser.LBRACKET, 0); }
		public TerminalNode RBRACKET() { return getToken(ifBlocksParser.RBRACKET, 0); }
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(ifBlocksParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(ifBlocksParser.WS, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ifBlocksParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ifBlocksParser.COMMA, i);
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
			setState(146);
			match(LBRACKET);
			setState(167);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				{
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
				value();
				setState(152);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
				case 1:
					{
					setState(151);
					match(WS);
					}
					break;
				}
				setState(164);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(154);
					match(COMMA);
					setState(156);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(155);
						match(WS);
						}
					}

					setState(158);
					value();
					setState(160);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
					case 1:
						{
						setState(159);
						match(WS);
						}
						break;
					}
					}
					}
					setState(166);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(169);
				match(WS);
				}
			}

			setState(172);
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
		public TerminalNode NUMBER() { return getToken(ifBlocksParser.NUMBER, 0); }
		public TerminalNode VARIABLE() { return getToken(ifBlocksParser.VARIABLE, 0); }
		public TerminalNode BOOLEAN() { return getToken(ifBlocksParser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(ifBlocksParser.STRING, 0); }
		public TerminalNode LPAREN() { return getToken(ifBlocksParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ifBlocksParser.RPAREN, 0); }
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
			setState(183);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(174);
				match(NUMBER);
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(175);
				match(VARIABLE);
				}
				break;
			case BOOLEAN:
				enterOuterAlt(_localctx, 3);
				{
				setState(176);
				match(BOOLEAN);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(177);
				match(STRING);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 5);
				{
				setState(178);
				match(LPAREN);
				setState(179);
				expression();
				setState(180);
				match(RPAREN);
				}
				break;
			case LBRACKET:
				enterOuterAlt(_localctx, 6);
				{
				setState(182);
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
		public TerminalNode ASSIGNMENT_OP() { return getToken(ifBlocksParser.ASSIGNMENT_OP, 0); }
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
			setState(185);
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
		public TerminalNode ARITHMETIC_OP() { return getToken(ifBlocksParser.ARITHMETIC_OP, 0); }
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
			setState(187);
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
		enterRule(_localctx, 22, RULE_line);
		try {
			setState(191);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARIABLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(189);
				assignment();
				}
				break;
			case SINGLE_LINE_COMMENT:
			case MULTI_LINE_COMMENT:
				enterOuterAlt(_localctx, 2);
				{
				setState(190);
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
	public static class CommentContext extends ParserRuleContext {
		public TerminalNode SINGLE_LINE_COMMENT() { return getToken(ifBlocksParser.SINGLE_LINE_COMMENT, 0); }
		public TerminalNode MULTI_LINE_COMMENT() { return getToken(ifBlocksParser.MULTI_LINE_COMMENT, 0); }
		public CommentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comment; }
	}

	public final CommentContext comment() throws RecognitionException {
		CommentContext _localctx = new CommentContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_comment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
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

	public static final String _serializedATN =
		"\u0004\u0001\u0018\u00c4\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0001\u0000\u0001\u0000\u0003\u0000\u001d\b\u0000\u0001"+
		"\u0000\u0001\u0000\u0003\u0000!\b\u0000\u0001\u0000\u0001\u0000\u0003"+
		"\u0000%\b\u0000\u0001\u0000\u0001\u0000\u0004\u0000)\b\u0000\u000b\u0000"+
		"\f\u0000*\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u00000\b\u0000\u0001"+
		"\u0000\u0001\u0000\u0003\u00004\b\u0000\u0001\u0000\u0004\u00007\b\u0000"+
		"\u000b\u0000\f\u00008\u0005\u0000;\b\u0000\n\u0000\f\u0000>\t\u0000\u0001"+
		"\u0000\u0001\u0000\u0003\u0000B\b\u0000\u0001\u0000\u0001\u0000\u0003"+
		"\u0000F\b\u0000\u0001\u0000\u0004\u0000I\b\u0000\u000b\u0000\f\u0000J"+
		"\u0003\u0000M\b\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0003\u0002"+
		"R\b\u0002\u0001\u0002\u0001\u0002\u0003\u0002V\b\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002Z\b\u0002\u0001\u0002\u0005\u0002]\b\u0002\n\u0002\f"+
		"\u0002`\t\u0002\u0001\u0003\u0001\u0003\u0003\u0003d\b\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003i\b\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003m\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003"+
		"r\b\u0003\u0001\u0004\u0001\u0004\u0003\u0004v\b\u0004\u0001\u0005\u0001"+
		"\u0005\u0003\u0005z\b\u0005\u0001\u0005\u0001\u0005\u0003\u0005~\b\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0003\u0006\u0084\b\u0006"+
		"\u0001\u0006\u0001\u0006\u0003\u0006\u0088\b\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u008c\b\u0006\u0005\u0006\u008e\b\u0006\n\u0006\f\u0006\u0091"+
		"\t\u0006\u0001\u0007\u0001\u0007\u0003\u0007\u0095\b\u0007\u0001\u0007"+
		"\u0001\u0007\u0003\u0007\u0099\b\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"\u009d\b\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u00a1\b\u0007\u0005"+
		"\u0007\u00a3\b\u0007\n\u0007\f\u0007\u00a6\t\u0007\u0003\u0007\u00a8\b"+
		"\u0007\u0001\u0007\u0003\u0007\u00ab\b\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003"+
		"\b\u00b8\b\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0003"+
		"\u000b\u00c0\b\u000b\u0001\f\u0001\f\u0001\f\u0000\u0000\r\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0002\u0001"+
		"\u0000\f\r\u0001\u0000\u0017\u0018\u00e0\u0000\u001a\u0001\u0000\u0000"+
		"\u0000\u0002N\u0001\u0000\u0000\u0000\u0004Q\u0001\u0000\u0000\u0000\u0006"+
		"q\u0001\u0000\u0000\u0000\bu\u0001\u0000\u0000\u0000\nw\u0001\u0000\u0000"+
		"\u0000\f\u0081\u0001\u0000\u0000\u0000\u000e\u0092\u0001\u0000\u0000\u0000"+
		"\u0010\u00b7\u0001\u0000\u0000\u0000\u0012\u00b9\u0001\u0000\u0000\u0000"+
		"\u0014\u00bb\u0001\u0000\u0000\u0000\u0016\u00bf\u0001\u0000\u0000\u0000"+
		"\u0018\u00c1\u0001\u0000\u0000\u0000\u001a\u001c\u0005\u0006\u0000\u0000"+
		"\u001b\u001d\u0005\u0016\u0000\u0000\u001c\u001b\u0001\u0000\u0000\u0000"+
		"\u001c\u001d\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000\u0000"+
		"\u001e \u0003\u0002\u0001\u0000\u001f!\u0005\u0016\u0000\u0000 \u001f"+
		"\u0001\u0000\u0000\u0000 !\u0001\u0000\u0000\u0000!\"\u0001\u0000\u0000"+
		"\u0000\"$\u0005\t\u0000\u0000#%\u0005\u0016\u0000\u0000$#\u0001\u0000"+
		"\u0000\u0000$%\u0001\u0000\u0000\u0000%(\u0001\u0000\u0000\u0000&)\u0003"+
		"\b\u0004\u0000\')\u0003\u0000\u0000\u0000(&\u0001\u0000\u0000\u0000(\'"+
		"\u0001\u0000\u0000\u0000)*\u0001\u0000\u0000\u0000*(\u0001\u0000\u0000"+
		"\u0000*+\u0001\u0000\u0000\u0000+<\u0001\u0000\u0000\u0000,-\u0005\u0007"+
		"\u0000\u0000-/\u0003\u0002\u0001\u0000.0\u0005\u0016\u0000\u0000/.\u0001"+
		"\u0000\u0000\u0000/0\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u0000"+
		"13\u0005\t\u0000\u000024\u0005\u0016\u0000\u000032\u0001\u0000\u0000\u0000"+
		"34\u0001\u0000\u0000\u000046\u0001\u0000\u0000\u000057\u0003\b\u0004\u0000"+
		"65\u0001\u0000\u0000\u000078\u0001\u0000\u0000\u000086\u0001\u0000\u0000"+
		"\u000089\u0001\u0000\u0000\u00009;\u0001\u0000\u0000\u0000:,\u0001\u0000"+
		"\u0000\u0000;>\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000<=\u0001"+
		"\u0000\u0000\u0000=L\u0001\u0000\u0000\u0000><\u0001\u0000\u0000\u0000"+
		"?A\u0005\b\u0000\u0000@B\u0005\u0016\u0000\u0000A@\u0001\u0000\u0000\u0000"+
		"AB\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CE\u0005\t\u0000\u0000"+
		"DF\u0005\u0016\u0000\u0000ED\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000"+
		"\u0000FH\u0001\u0000\u0000\u0000GI\u0003\b\u0004\u0000HG\u0001\u0000\u0000"+
		"\u0000IJ\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001\u0000"+
		"\u0000\u0000KM\u0001\u0000\u0000\u0000L?\u0001\u0000\u0000\u0000LM\u0001"+
		"\u0000\u0000\u0000M\u0001\u0001\u0000\u0000\u0000NO\u0003\u0004\u0002"+
		"\u0000O\u0003\u0001\u0000\u0000\u0000PR\u0005\u0016\u0000\u0000QP\u0001"+
		"\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000"+
		"S^\u0003\u0006\u0003\u0000TV\u0005\u0016\u0000\u0000UT\u0001\u0000\u0000"+
		"\u0000UV\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WY\u0007\u0000"+
		"\u0000\u0000XZ\u0005\u0016\u0000\u0000YX\u0001\u0000\u0000\u0000YZ\u0001"+
		"\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000[]\u0003\u0006\u0003\u0000"+
		"\\U\u0001\u0000\u0000\u0000]`\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000"+
		"\u0000^_\u0001\u0000\u0000\u0000_\u0005\u0001\u0000\u0000\u0000`^\u0001"+
		"\u0000\u0000\u0000ac\u0005\u000e\u0000\u0000bd\u0005\u0016\u0000\u0000"+
		"cb\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000de\u0001\u0000\u0000"+
		"\u0000er\u0003\u0006\u0003\u0000fh\u0005\n\u0000\u0000gi\u0005\u0016\u0000"+
		"\u0000hg\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ij\u0001\u0000"+
		"\u0000\u0000jl\u0003\u0004\u0002\u0000km\u0005\u0016\u0000\u0000lk\u0001"+
		"\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000"+
		"no\u0005\u000b\u0000\u0000or\u0001\u0000\u0000\u0000pr\u0003\u0010\b\u0000"+
		"qa\u0001\u0000\u0000\u0000qf\u0001\u0000\u0000\u0000qp\u0001\u0000\u0000"+
		"\u0000r\u0007\u0001\u0000\u0000\u0000sv\u0003\n\u0005\u0000tv\u0003\f"+
		"\u0006\u0000us\u0001\u0000\u0000\u0000ut\u0001\u0000\u0000\u0000v\t\u0001"+
		"\u0000\u0000\u0000wy\u0005\u0015\u0000\u0000xz\u0005\u0016\u0000\u0000"+
		"yx\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000"+
		"\u0000{}\u0003\u0012\t\u0000|~\u0005\u0016\u0000\u0000}|\u0001\u0000\u0000"+
		"\u0000}~\u0001\u0000\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f"+
		"\u0080\u0003\f\u0006\u0000\u0080\u000b\u0001\u0000\u0000\u0000\u0081\u0083"+
		"\u0003\u0010\b\u0000\u0082\u0084\u0005\u0016\u0000\u0000\u0083\u0082\u0001"+
		"\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u008f\u0001"+
		"\u0000\u0000\u0000\u0085\u0087\u0003\u0014\n\u0000\u0086\u0088\u0005\u0016"+
		"\u0000\u0000\u0087\u0086\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000"+
		"\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0089\u008b\u0003\u0010"+
		"\b\u0000\u008a\u008c\u0005\u0016\u0000\u0000\u008b\u008a\u0001\u0000\u0000"+
		"\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u008e\u0001\u0000\u0000"+
		"\u0000\u008d\u0085\u0001\u0000\u0000\u0000\u008e\u0091\u0001\u0000\u0000"+
		"\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000"+
		"\u0000\u0090\r\u0001\u0000\u0000\u0000\u0091\u008f\u0001\u0000\u0000\u0000"+
		"\u0092\u00a7\u0005\u0003\u0000\u0000\u0093\u0095\u0005\u0016\u0000\u0000"+
		"\u0094\u0093\u0001\u0000\u0000\u0000\u0094\u0095\u0001\u0000\u0000\u0000"+
		"\u0095\u0096\u0001\u0000\u0000\u0000\u0096\u0098\u0003\u0010\b\u0000\u0097"+
		"\u0099\u0005\u0016\u0000\u0000\u0098\u0097\u0001\u0000\u0000\u0000\u0098"+
		"\u0099\u0001\u0000\u0000\u0000\u0099\u00a4\u0001\u0000\u0000\u0000\u009a"+
		"\u009c\u0005\u0005\u0000\u0000\u009b\u009d\u0005\u0016\u0000\u0000\u009c"+
		"\u009b\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0001\u0000\u0000\u0000\u009e\u00a0\u0003\u0010\b\u0000\u009f\u00a1"+
		"\u0005\u0016\u0000\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a0\u00a1"+
		"\u0001\u0000\u0000\u0000\u00a1\u00a3\u0001\u0000\u0000\u0000\u00a2\u009a"+
		"\u0001\u0000\u0000\u0000\u00a3\u00a6\u0001\u0000\u0000\u0000\u00a4\u00a2"+
		"\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5\u00a8"+
		"\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000\u0000\u00a7\u0094"+
		"\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u00aa"+
		"\u0001\u0000\u0000\u0000\u00a9\u00ab\u0005\u0016\u0000\u0000\u00aa\u00a9"+
		"\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ac"+
		"\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005\u0004\u0000\u0000\u00ad\u000f"+
		"\u0001\u0000\u0000\u0000\u00ae\u00b8\u0005\u0011\u0000\u0000\u00af\u00b8"+
		"\u0005\u0015\u0000\u0000\u00b0\u00b8\u0005\u0012\u0000\u0000\u00b1\u00b8"+
		"\u0005\u0013\u0000\u0000\u00b2\u00b3\u0005\n\u0000\u0000\u00b3\u00b4\u0003"+
		"\f\u0006\u0000\u00b4\u00b5\u0005\u000b\u0000\u0000\u00b5\u00b8\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b8\u0003\u000e\u0007\u0000\u00b7\u00ae\u0001\u0000"+
		"\u0000\u0000\u00b7\u00af\u0001\u0000\u0000\u0000\u00b7\u00b0\u0001\u0000"+
		"\u0000\u0000\u00b7\u00b1\u0001\u0000\u0000\u0000\u00b7\u00b2\u0001\u0000"+
		"\u0000\u0000\u00b7\u00b6\u0001\u0000\u0000\u0000\u00b8\u0011\u0001\u0000"+
		"\u0000\u0000\u00b9\u00ba\u0005\u0001\u0000\u0000\u00ba\u0013\u0001\u0000"+
		"\u0000\u0000\u00bb\u00bc\u0005\u0002\u0000\u0000\u00bc\u0015\u0001\u0000"+
		"\u0000\u0000\u00bd\u00c0\u0003\n\u0005\u0000\u00be\u00c0\u0003\u0018\f"+
		"\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00bf\u00be\u0001\u0000\u0000"+
		"\u0000\u00c0\u0017\u0001\u0000\u0000\u0000\u00c1\u00c2\u0007\u0001\u0000"+
		"\u0000\u00c2\u0019\u0001\u0000\u0000\u0000%\u001c $(*/38<AEJLQUY^chlq"+
		"uy}\u0083\u0087\u008b\u008f\u0094\u0098\u009c\u00a0\u00a4\u00a7\u00aa"+
		"\u00b7\u00bf";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}