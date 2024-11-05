// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/operators.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class operatorsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSIGNMENT_OP=1, ARITHMETIC_OP=2, LBRACKET=3, RBRACKET=4, COMMA=5, IF=6, 
		ELIF=7, ELSE=8, COLON=9, LPAREN=10, RPAREN=11, COMPARISON_OP=12, LOGICAL_OP=13, 
		NOT_OP=14, WHILE=15, FOR=16, NUMBER=17, BOOLEAN=18, STRING=19, ESC=20, 
		VARIABLE=21, WS=22, NEWLINE=23;
	public static final int
		RULE_assignment = 0, RULE_expression = 1, RULE_array = 2, RULE_count = 3, 
		RULE_value = 4, RULE_assignment_operator = 5, RULE_operator = 6, RULE_condition = 7, 
		RULE_logical_condition = 8, RULE_comparison_condition = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"assignment", "expression", "array", "count", "value", "assignment_operator", 
			"operator", "condition", "logical_condition", "comparison_condition"
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
			"WS", "NEWLINE"
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
	public String getGrammarFileName() { return "operators.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public operatorsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode VARIABLE() { return getToken(operatorsParser.VARIABLE, 0); }
		public Assignment_operatorContext assignment_operator() {
			return getRuleContext(Assignment_operatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(operatorsParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(operatorsParser.WS, i);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			match(VARIABLE);
			setState(22);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(21);
				match(WS);
				}
			}

			setState(24);
			assignment_operator();
			setState(26);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(25);
				match(WS);
				}
			}

			setState(28);
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
		public List<TerminalNode> WS() { return getTokens(operatorsParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(operatorsParser.WS, i);
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
		enterRule(_localctx, 2, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			value();
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(31);
				match(WS);
				}
			}

			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ARITHMETIC_OP) {
				{
				{
				setState(34);
				operator();
				setState(36);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(35);
					match(WS);
					}
				}

				setState(38);
				value();
				setState(40);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(39);
					match(WS);
					}
				}

				}
				}
				setState(46);
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
		public TerminalNode LBRACKET() { return getToken(operatorsParser.LBRACKET, 0); }
		public TerminalNode RBRACKET() { return getToken(operatorsParser.RBRACKET, 0); }
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(operatorsParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(operatorsParser.WS, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(operatorsParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(operatorsParser.COMMA, i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(LBRACKET);
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(48);
					match(WS);
					}
				}

				setState(51);
				value();
				setState(53);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
				case 1:
					{
					setState(52);
					match(WS);
					}
					break;
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(55);
					match(COMMA);
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
					value();
					setState(61);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						setState(60);
						match(WS);
						}
						break;
					}
					}
					}
					setState(67);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
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
	public static class CountContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(operatorsParser.NUMBER, 0); }
		public TerminalNode VARIABLE() { return getToken(operatorsParser.VARIABLE, 0); }
		public CountContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_count; }
	}

	public final CountContext count() throws RecognitionException {
		CountContext _localctx = new CountContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_count);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			_la = _input.LA(1);
			if ( !(_la==NUMBER || _la==VARIABLE) ) {
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
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(operatorsParser.NUMBER, 0); }
		public TerminalNode VARIABLE() { return getToken(operatorsParser.VARIABLE, 0); }
		public TerminalNode BOOLEAN() { return getToken(operatorsParser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(operatorsParser.STRING, 0); }
		public TerminalNode LPAREN() { return getToken(operatorsParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(operatorsParser.RPAREN, 0); }
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
		enterRule(_localctx, 8, RULE_value);
		try {
			setState(86);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(NUMBER);
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				match(VARIABLE);
				}
				break;
			case BOOLEAN:
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				match(BOOLEAN);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(80);
				match(STRING);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 5);
				{
				setState(81);
				match(LPAREN);
				setState(82);
				expression();
				setState(83);
				match(RPAREN);
				}
				break;
			case LBRACKET:
				enterOuterAlt(_localctx, 6);
				{
				setState(85);
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
		public TerminalNode ASSIGNMENT_OP() { return getToken(operatorsParser.ASSIGNMENT_OP, 0); }
		public Assignment_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment_operator; }
	}

	public final Assignment_operatorContext assignment_operator() throws RecognitionException {
		Assignment_operatorContext _localctx = new Assignment_operatorContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assignment_operator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
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
		public TerminalNode ARITHMETIC_OP() { return getToken(operatorsParser.ARITHMETIC_OP, 0); }
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_operator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
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
		enterRule(_localctx, 14, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
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
		public List<TerminalNode> WS() { return getTokens(operatorsParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(operatorsParser.WS, i);
		}
		public List<TerminalNode> LOGICAL_OP() { return getTokens(operatorsParser.LOGICAL_OP); }
		public TerminalNode LOGICAL_OP(int i) {
			return getToken(operatorsParser.LOGICAL_OP, i);
		}
		public List<TerminalNode> COMPARISON_OP() { return getTokens(operatorsParser.COMPARISON_OP); }
		public TerminalNode COMPARISON_OP(int i) {
			return getToken(operatorsParser.COMPARISON_OP, i);
		}
		public Logical_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_condition; }
	}

	public final Logical_conditionContext logical_condition() throws RecognitionException {
		Logical_conditionContext _localctx = new Logical_conditionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_logical_condition);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(94);
				match(WS);
				}
			}

			setState(97);
			comparison_condition();
			setState(108);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
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
					_la = _input.LA(1);
					if ( !(_la==COMPARISON_OP || _la==LOGICAL_OP) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(103);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(102);
						match(WS);
						}
					}

					setState(105);
					comparison_condition();
					}
					} 
				}
				setState(110);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
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
		public TerminalNode NOT_OP() { return getToken(operatorsParser.NOT_OP, 0); }
		public Comparison_conditionContext comparison_condition() {
			return getRuleContext(Comparison_conditionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(operatorsParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(operatorsParser.WS, i);
		}
		public TerminalNode LPAREN() { return getToken(operatorsParser.LPAREN, 0); }
		public Logical_conditionContext logical_condition() {
			return getRuleContext(Logical_conditionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(operatorsParser.RPAREN, 0); }
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
		enterRule(_localctx, 18, RULE_comparison_condition);
		int _la;
		try {
			setState(127);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(111);
				match(NOT_OP);
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(112);
					match(WS);
					}
				}

				setState(115);
				comparison_condition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(116);
				match(LPAREN);
				setState(118);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
				case 1:
					{
					setState(117);
					match(WS);
					}
					break;
				}
				setState(120);
				logical_condition();
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(121);
					match(WS);
					}
				}

				setState(124);
				match(RPAREN);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(126);
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
		"\u0004\u0001\u0017\u0082\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0003\u0000\u0017"+
		"\b\u0000\u0001\u0000\u0001\u0000\u0003\u0000\u001b\b\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001!\b\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001%\b\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		")\b\u0001\u0005\u0001+\b\u0001\n\u0001\f\u0001.\t\u0001\u0001\u0002\u0001"+
		"\u0002\u0003\u00022\b\u0002\u0001\u0002\u0001\u0002\u0003\u00026\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002:\b\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002>\b\u0002\u0005\u0002@\b\u0002\n\u0002\f\u0002C\t\u0002\u0003"+
		"\u0002E\b\u0002\u0001\u0002\u0003\u0002H\b\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004"+
		"W\b\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0003\b`\b\b\u0001\b\u0001\b\u0003\bd\b\b\u0001\b"+
		"\u0001\b\u0003\bh\b\b\u0001\b\u0005\bk\b\b\n\b\f\bn\t\b\u0001\t\u0001"+
		"\t\u0003\tr\b\t\u0001\t\u0001\t\u0001\t\u0003\tw\b\t\u0001\t\u0001\t\u0003"+
		"\t{\b\t\u0001\t\u0001\t\u0001\t\u0003\t\u0080\b\t\u0001\t\u0000\u0000"+
		"\n\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0000\u0002\u0002\u0000"+
		"\u0011\u0011\u0015\u0015\u0001\u0000\f\r\u0092\u0000\u0014\u0001\u0000"+
		"\u0000\u0000\u0002\u001e\u0001\u0000\u0000\u0000\u0004/\u0001\u0000\u0000"+
		"\u0000\u0006K\u0001\u0000\u0000\u0000\bV\u0001\u0000\u0000\u0000\nX\u0001"+
		"\u0000\u0000\u0000\fZ\u0001\u0000\u0000\u0000\u000e\\\u0001\u0000\u0000"+
		"\u0000\u0010_\u0001\u0000\u0000\u0000\u0012\u007f\u0001\u0000\u0000\u0000"+
		"\u0014\u0016\u0005\u0015\u0000\u0000\u0015\u0017\u0005\u0016\u0000\u0000"+
		"\u0016\u0015\u0001\u0000\u0000\u0000\u0016\u0017\u0001\u0000\u0000\u0000"+
		"\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u001a\u0003\n\u0005\u0000\u0019"+
		"\u001b\u0005\u0016\u0000\u0000\u001a\u0019\u0001\u0000\u0000\u0000\u001a"+
		"\u001b\u0001\u0000\u0000\u0000\u001b\u001c\u0001\u0000\u0000\u0000\u001c"+
		"\u001d\u0003\u0002\u0001\u0000\u001d\u0001\u0001\u0000\u0000\u0000\u001e"+
		" \u0003\b\u0004\u0000\u001f!\u0005\u0016\u0000\u0000 \u001f\u0001\u0000"+
		"\u0000\u0000 !\u0001\u0000\u0000\u0000!,\u0001\u0000\u0000\u0000\"$\u0003"+
		"\f\u0006\u0000#%\u0005\u0016\u0000\u0000$#\u0001\u0000\u0000\u0000$%\u0001"+
		"\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&(\u0003\b\u0004\u0000\')"+
		"\u0005\u0016\u0000\u0000(\'\u0001\u0000\u0000\u0000()\u0001\u0000\u0000"+
		"\u0000)+\u0001\u0000\u0000\u0000*\"\u0001\u0000\u0000\u0000+.\u0001\u0000"+
		"\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-\u0003"+
		"\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000/D\u0005\u0003\u0000"+
		"\u000002\u0005\u0016\u0000\u000010\u0001\u0000\u0000\u000012\u0001\u0000"+
		"\u0000\u000023\u0001\u0000\u0000\u000035\u0003\b\u0004\u000046\u0005\u0016"+
		"\u0000\u000054\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u00006A\u0001"+
		"\u0000\u0000\u000079\u0005\u0005\u0000\u00008:\u0005\u0016\u0000\u0000"+
		"98\u0001\u0000\u0000\u00009:\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000"+
		"\u0000;=\u0003\b\u0004\u0000<>\u0005\u0016\u0000\u0000=<\u0001\u0000\u0000"+
		"\u0000=>\u0001\u0000\u0000\u0000>@\u0001\u0000\u0000\u0000?7\u0001\u0000"+
		"\u0000\u0000@C\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000AB\u0001"+
		"\u0000\u0000\u0000BE\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000"+
		"D1\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EG\u0001\u0000\u0000"+
		"\u0000FH\u0005\u0016\u0000\u0000GF\u0001\u0000\u0000\u0000GH\u0001\u0000"+
		"\u0000\u0000HI\u0001\u0000\u0000\u0000IJ\u0005\u0004\u0000\u0000J\u0005"+
		"\u0001\u0000\u0000\u0000KL\u0007\u0000\u0000\u0000L\u0007\u0001\u0000"+
		"\u0000\u0000MW\u0005\u0011\u0000\u0000NW\u0005\u0015\u0000\u0000OW\u0005"+
		"\u0012\u0000\u0000PW\u0005\u0013\u0000\u0000QR\u0005\n\u0000\u0000RS\u0003"+
		"\u0002\u0001\u0000ST\u0005\u000b\u0000\u0000TW\u0001\u0000\u0000\u0000"+
		"UW\u0003\u0004\u0002\u0000VM\u0001\u0000\u0000\u0000VN\u0001\u0000\u0000"+
		"\u0000VO\u0001\u0000\u0000\u0000VP\u0001\u0000\u0000\u0000VQ\u0001\u0000"+
		"\u0000\u0000VU\u0001\u0000\u0000\u0000W\t\u0001\u0000\u0000\u0000XY\u0005"+
		"\u0001\u0000\u0000Y\u000b\u0001\u0000\u0000\u0000Z[\u0005\u0002\u0000"+
		"\u0000[\r\u0001\u0000\u0000\u0000\\]\u0003\u0010\b\u0000]\u000f\u0001"+
		"\u0000\u0000\u0000^`\u0005\u0016\u0000\u0000_^\u0001\u0000\u0000\u0000"+
		"_`\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000al\u0003\u0012\t\u0000"+
		"bd\u0005\u0016\u0000\u0000cb\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000"+
		"\u0000de\u0001\u0000\u0000\u0000eg\u0007\u0001\u0000\u0000fh\u0005\u0016"+
		"\u0000\u0000gf\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hi\u0001"+
		"\u0000\u0000\u0000ik\u0003\u0012\t\u0000jc\u0001\u0000\u0000\u0000kn\u0001"+
		"\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000"+
		"m\u0011\u0001\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000oq\u0005\u000e"+
		"\u0000\u0000pr\u0005\u0016\u0000\u0000qp\u0001\u0000\u0000\u0000qr\u0001"+
		"\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000s\u0080\u0003\u0012\t\u0000"+
		"tv\u0005\n\u0000\u0000uw\u0005\u0016\u0000\u0000vu\u0001\u0000\u0000\u0000"+
		"vw\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000xz\u0003\u0010\b\u0000"+
		"y{\u0005\u0016\u0000\u0000zy\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000"+
		"\u0000{|\u0001\u0000\u0000\u0000|}\u0005\u000b\u0000\u0000}\u0080\u0001"+
		"\u0000\u0000\u0000~\u0080\u0003\b\u0004\u0000\u007fo\u0001\u0000\u0000"+
		"\u0000\u007ft\u0001\u0000\u0000\u0000\u007f~\u0001\u0000\u0000\u0000\u0080"+
		"\u0013\u0001\u0000\u0000\u0000\u0016\u0016\u001a $(,159=ADGV_cglqvz\u007f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}