// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/operators.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class operatorsLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, NUMBER=2, VARIABLE=3, ASSIGNMENT_OP=4, ARITHMETIC_OP=5, IF=6, 
		ELIF=7, ELSE=8, COLON=9, AND=10, OR=11, NOT=12, LPAREN=13, RPAREN=14, 
		COMPARISON_OP=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP", "IF", 
			"ELIF", "ELSE", "COLON", "AND", "OR", "NOT", "LPAREN", "RPAREN", "COMPARISON_OP"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'statement'", null, null, null, null, "'if'", "'elif'", "'else'", 
			"':'", "'and'", "'or'", "'not'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP", "IF", 
			"ELIF", "ELSE", "COLON", "AND", "OR", "NOT", "LPAREN", "RPAREN", "COMPARISON_OP"
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


	public operatorsLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "operators.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000ft\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0004\u0001+\b"+
		"\u0001\u000b\u0001\f\u0001,\u0001\u0001\u0001\u0001\u0004\u00011\b\u0001"+
		"\u000b\u0001\f\u00012\u0003\u00015\b\u0001\u0001\u0002\u0001\u0002\u0005"+
		"\u00029\b\u0002\n\u0002\f\u0002<\t\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u0003G\b\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000es\b\u000e"+
		"\u0000\u0000\u000f\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u0001\u0000\u0004\u0001\u000009\u0003\u0000"+
		"AZ__az\u0004\u000009AZ__az\u0004\u0000%%*+--//\u0080\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000"+
		"\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000"+
		"\u0000\u0001\u001f\u0001\u0000\u0000\u0000\u0003*\u0001\u0000\u0000\u0000"+
		"\u00056\u0001\u0000\u0000\u0000\u0007F\u0001\u0000\u0000\u0000\tH\u0001"+
		"\u0000\u0000\u0000\u000bJ\u0001\u0000\u0000\u0000\rM\u0001\u0000\u0000"+
		"\u0000\u000fR\u0001\u0000\u0000\u0000\u0011W\u0001\u0000\u0000\u0000\u0013"+
		"Y\u0001\u0000\u0000\u0000\u0015]\u0001\u0000\u0000\u0000\u0017`\u0001"+
		"\u0000\u0000\u0000\u0019d\u0001\u0000\u0000\u0000\u001bf\u0001\u0000\u0000"+
		"\u0000\u001dr\u0001\u0000\u0000\u0000\u001f \u0005s\u0000\u0000 !\u0005"+
		"t\u0000\u0000!\"\u0005a\u0000\u0000\"#\u0005t\u0000\u0000#$\u0005e\u0000"+
		"\u0000$%\u0005m\u0000\u0000%&\u0005e\u0000\u0000&\'\u0005n\u0000\u0000"+
		"\'(\u0005t\u0000\u0000(\u0002\u0001\u0000\u0000\u0000)+\u0007\u0000\u0000"+
		"\u0000*)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000,*\u0001\u0000"+
		"\u0000\u0000,-\u0001\u0000\u0000\u0000-4\u0001\u0000\u0000\u0000.0\u0005"+
		".\u0000\u0000/1\u0007\u0000\u0000\u00000/\u0001\u0000\u0000\u000012\u0001"+
		"\u0000\u0000\u000020\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u0000"+
		"35\u0001\u0000\u0000\u00004.\u0001\u0000\u0000\u000045\u0001\u0000\u0000"+
		"\u00005\u0004\u0001\u0000\u0000\u00006:\u0007\u0001\u0000\u000079\u0007"+
		"\u0002\u0000\u000087\u0001\u0000\u0000\u00009<\u0001\u0000\u0000\u0000"+
		":8\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;\u0006\u0001\u0000"+
		"\u0000\u0000<:\u0001\u0000\u0000\u0000=G\u0005=\u0000\u0000>?\u0005+\u0000"+
		"\u0000?G\u0005=\u0000\u0000@A\u0005-\u0000\u0000AG\u0005=\u0000\u0000"+
		"BC\u0005*\u0000\u0000CG\u0005=\u0000\u0000DE\u0005/\u0000\u0000EG\u0005"+
		"=\u0000\u0000F=\u0001\u0000\u0000\u0000F>\u0001\u0000\u0000\u0000F@\u0001"+
		"\u0000\u0000\u0000FB\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000"+
		"G\b\u0001\u0000\u0000\u0000HI\u0007\u0003\u0000\u0000I\n\u0001\u0000\u0000"+
		"\u0000JK\u0005i\u0000\u0000KL\u0005f\u0000\u0000L\f\u0001\u0000\u0000"+
		"\u0000MN\u0005e\u0000\u0000NO\u0005l\u0000\u0000OP\u0005i\u0000\u0000"+
		"PQ\u0005f\u0000\u0000Q\u000e\u0001\u0000\u0000\u0000RS\u0005e\u0000\u0000"+
		"ST\u0005l\u0000\u0000TU\u0005s\u0000\u0000UV\u0005e\u0000\u0000V\u0010"+
		"\u0001\u0000\u0000\u0000WX\u0005:\u0000\u0000X\u0012\u0001\u0000\u0000"+
		"\u0000YZ\u0005a\u0000\u0000Z[\u0005n\u0000\u0000[\\\u0005d\u0000\u0000"+
		"\\\u0014\u0001\u0000\u0000\u0000]^\u0005o\u0000\u0000^_\u0005r\u0000\u0000"+
		"_\u0016\u0001\u0000\u0000\u0000`a\u0005n\u0000\u0000ab\u0005o\u0000\u0000"+
		"bc\u0005t\u0000\u0000c\u0018\u0001\u0000\u0000\u0000de\u0005(\u0000\u0000"+
		"e\u001a\u0001\u0000\u0000\u0000fg\u0005)\u0000\u0000g\u001c\u0001\u0000"+
		"\u0000\u0000hi\u0005=\u0000\u0000is\u0005=\u0000\u0000jk\u0005!\u0000"+
		"\u0000ks\u0005=\u0000\u0000ls\u0005<\u0000\u0000mn\u0005<\u0000\u0000"+
		"ns\u0005=\u0000\u0000os\u0005>\u0000\u0000pq\u0005>\u0000\u0000qs\u0005"+
		"=\u0000\u0000rh\u0001\u0000\u0000\u0000rj\u0001\u0000\u0000\u0000rl\u0001"+
		"\u0000\u0000\u0000rm\u0001\u0000\u0000\u0000ro\u0001\u0000\u0000\u0000"+
		"rp\u0001\u0000\u0000\u0000s\u001e\u0001\u0000\u0000\u0000\u0007\u0000"+
		",24:Fr\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}