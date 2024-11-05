// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/values.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class values extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUMBER=1, BOOLEAN=2, STRING=3, ESC=4, VARIABLE=5, WS=6;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS"
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


	public values(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "values.g4"; }

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
		"\u0004\u0000\u0006K\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0001\u0000\u0003\u0000\u000f\b\u0000"+
		"\u0001\u0000\u0004\u0000\u0012\b\u0000\u000b\u0000\f\u0000\u0013\u0001"+
		"\u0000\u0001\u0000\u0004\u0000\u0018\b\u0000\u000b\u0000\f\u0000\u0019"+
		"\u0003\u0000\u001c\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\'\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002,\b\u0002\n"+
		"\u0002\f\u0002/\t\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0005\u00025\b\u0002\n\u0002\f\u00028\t\u0002\u0001\u0002\u0003\u0002"+
		";\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0005\u0004B\b\u0004\n\u0004\f\u0004E\t\u0004\u0001\u0005\u0004\u0005"+
		"H\b\u0005\u000b\u0005\f\u0005I\u0000\u0000\u0006\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\u0001\u0000\u0007\u0001\u0000"+
		"09\u0002\u0000\"\"\\\\\u0002\u0000\'\'\\\\\b\u0000\"\"\'\'\\\\bbffnnr"+
		"rtt\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001\u0000  V\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0001\u000e\u0001\u0000"+
		"\u0000\u0000\u0003&\u0001\u0000\u0000\u0000\u0005:\u0001\u0000\u0000\u0000"+
		"\u0007<\u0001\u0000\u0000\u0000\t?\u0001\u0000\u0000\u0000\u000bG\u0001"+
		"\u0000\u0000\u0000\r\u000f\u0005-\u0000\u0000\u000e\r\u0001\u0000\u0000"+
		"\u0000\u000e\u000f\u0001\u0000\u0000\u0000\u000f\u0011\u0001\u0000\u0000"+
		"\u0000\u0010\u0012\u0007\u0000\u0000\u0000\u0011\u0010\u0001\u0000\u0000"+
		"\u0000\u0012\u0013\u0001\u0000\u0000\u0000\u0013\u0011\u0001\u0000\u0000"+
		"\u0000\u0013\u0014\u0001\u0000\u0000\u0000\u0014\u001b\u0001\u0000\u0000"+
		"\u0000\u0015\u0017\u0005.\u0000\u0000\u0016\u0018\u0007\u0000\u0000\u0000"+
		"\u0017\u0016\u0001\u0000\u0000\u0000\u0018\u0019\u0001\u0000\u0000\u0000"+
		"\u0019\u0017\u0001\u0000\u0000\u0000\u0019\u001a\u0001\u0000\u0000\u0000"+
		"\u001a\u001c\u0001\u0000\u0000\u0000\u001b\u0015\u0001\u0000\u0000\u0000"+
		"\u001b\u001c\u0001\u0000\u0000\u0000\u001c\u0002\u0001\u0000\u0000\u0000"+
		"\u001d\u001e\u0005T\u0000\u0000\u001e\u001f\u0005r\u0000\u0000\u001f "+
		"\u0005u\u0000\u0000 \'\u0005e\u0000\u0000!\"\u0005F\u0000\u0000\"#\u0005"+
		"a\u0000\u0000#$\u0005l\u0000\u0000$%\u0005s\u0000\u0000%\'\u0005e\u0000"+
		"\u0000&\u001d\u0001\u0000\u0000\u0000&!\u0001\u0000\u0000\u0000\'\u0004"+
		"\u0001\u0000\u0000\u0000(-\u0005\"\u0000\u0000),\u0003\u0007\u0003\u0000"+
		"*,\b\u0001\u0000\u0000+)\u0001\u0000\u0000\u0000+*\u0001\u0000\u0000\u0000"+
		",/\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000"+
		"\u0000.0\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u00000;\u0005\"\u0000"+
		"\u000016\u0005\'\u0000\u000025\u0003\u0007\u0003\u000035\b\u0002\u0000"+
		"\u000042\u0001\u0000\u0000\u000043\u0001\u0000\u0000\u000058\u0001\u0000"+
		"\u0000\u000064\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u000079\u0001"+
		"\u0000\u0000\u000086\u0001\u0000\u0000\u00009;\u0005\'\u0000\u0000:(\u0001"+
		"\u0000\u0000\u0000:1\u0001\u0000\u0000\u0000;\u0006\u0001\u0000\u0000"+
		"\u0000<=\u0005\\\u0000\u0000=>\u0007\u0003\u0000\u0000>\b\u0001\u0000"+
		"\u0000\u0000?C\u0007\u0004\u0000\u0000@B\u0007\u0005\u0000\u0000A@\u0001"+
		"\u0000\u0000\u0000BE\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000"+
		"CD\u0001\u0000\u0000\u0000D\n\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000"+
		"\u0000FH\u0007\u0006\u0000\u0000GF\u0001\u0000\u0000\u0000HI\u0001\u0000"+
		"\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000J\f\u0001"+
		"\u0000\u0000\u0000\r\u0000\u000e\u0013\u0019\u001b&+-46:CI\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}