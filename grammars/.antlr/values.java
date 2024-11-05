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
		NUMBER=1, BOOLEAN=2, STRING=3, ESC=4, VARIABLE=5, WS=6, NEWLINE=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS", "NEWLINE"
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
			null, "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS", "NEWLINE"
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
		"\u0004\u0000\u0007Z\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000"+
		"\u0003\u0000\u0011\b\u0000\u0001\u0000\u0004\u0000\u0014\b\u0000\u000b"+
		"\u0000\f\u0000\u0015\u0001\u0000\u0001\u0000\u0004\u0000\u001a\b\u0000"+
		"\u000b\u0000\f\u0000\u001b\u0003\u0000\u001e\b\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0003\u0001)\b\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0005\u0002.\b\u0002\n\u0002\f\u00021\t\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0005\u00027\b\u0002\n\u0002\f\u0002:\t"+
		"\u0002\u0001\u0002\u0003\u0002=\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0005\u0004D\b\u0004\n\u0004\f\u0004G\t"+
		"\u0004\u0001\u0005\u0004\u0005J\b\u0005\u000b\u0005\f\u0005K\u0001\u0006"+
		"\u0003\u0006O\b\u0006\u0001\u0006\u0005\u0006R\b\u0006\n\u0006\f\u0006"+
		"U\t\u0006\u0001\u0006\u0001\u0006\u0003\u0006Y\b\u0006\u0000\u0000\u0007"+
		"\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r"+
		"\u0007\u0001\u0000\u0007\u0001\u000009\u0002\u0000\"\"\\\\\u0002\u0000"+
		"\'\'\\\\\b\u0000\"\"\'\'\\\\bbffnnrrtt\u0003\u0000AZ__az\u0004\u00000"+
		"9AZ__az\u0001\u0000  h\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0001\u0010\u0001\u0000"+
		"\u0000\u0000\u0003(\u0001\u0000\u0000\u0000\u0005<\u0001\u0000\u0000\u0000"+
		"\u0007>\u0001\u0000\u0000\u0000\tA\u0001\u0000\u0000\u0000\u000bI\u0001"+
		"\u0000\u0000\u0000\rX\u0001\u0000\u0000\u0000\u000f\u0011\u0005-\u0000"+
		"\u0000\u0010\u000f\u0001\u0000\u0000\u0000\u0010\u0011\u0001\u0000\u0000"+
		"\u0000\u0011\u0013\u0001\u0000\u0000\u0000\u0012\u0014\u0007\u0000\u0000"+
		"\u0000\u0013\u0012\u0001\u0000\u0000\u0000\u0014\u0015\u0001\u0000\u0000"+
		"\u0000\u0015\u0013\u0001\u0000\u0000\u0000\u0015\u0016\u0001\u0000\u0000"+
		"\u0000\u0016\u001d\u0001\u0000\u0000\u0000\u0017\u0019\u0005.\u0000\u0000"+
		"\u0018\u001a\u0007\u0000\u0000\u0000\u0019\u0018\u0001\u0000\u0000\u0000"+
		"\u001a\u001b\u0001\u0000\u0000\u0000\u001b\u0019\u0001\u0000\u0000\u0000"+
		"\u001b\u001c\u0001\u0000\u0000\u0000\u001c\u001e\u0001\u0000\u0000\u0000"+
		"\u001d\u0017\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000\u0000"+
		"\u001e\u0002\u0001\u0000\u0000\u0000\u001f \u0005T\u0000\u0000 !\u0005"+
		"r\u0000\u0000!\"\u0005u\u0000\u0000\")\u0005e\u0000\u0000#$\u0005F\u0000"+
		"\u0000$%\u0005a\u0000\u0000%&\u0005l\u0000\u0000&\'\u0005s\u0000\u0000"+
		"\')\u0005e\u0000\u0000(\u001f\u0001\u0000\u0000\u0000(#\u0001\u0000\u0000"+
		"\u0000)\u0004\u0001\u0000\u0000\u0000*/\u0005\"\u0000\u0000+.\u0003\u0007"+
		"\u0003\u0000,.\b\u0001\u0000\u0000-+\u0001\u0000\u0000\u0000-,\u0001\u0000"+
		"\u0000\u0000.1\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u0000/0\u0001"+
		"\u0000\u0000\u000002\u0001\u0000\u0000\u00001/\u0001\u0000\u0000\u0000"+
		"2=\u0005\"\u0000\u000038\u0005\'\u0000\u000047\u0003\u0007\u0003\u0000"+
		"57\b\u0002\u0000\u000064\u0001\u0000\u0000\u000065\u0001\u0000\u0000\u0000"+
		"7:\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u000089\u0001\u0000\u0000"+
		"\u00009;\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000;=\u0005\'\u0000"+
		"\u0000<*\u0001\u0000\u0000\u0000<3\u0001\u0000\u0000\u0000=\u0006\u0001"+
		"\u0000\u0000\u0000>?\u0005\\\u0000\u0000?@\u0007\u0003\u0000\u0000@\b"+
		"\u0001\u0000\u0000\u0000AE\u0007\u0004\u0000\u0000BD\u0007\u0005\u0000"+
		"\u0000CB\u0001\u0000\u0000\u0000DG\u0001\u0000\u0000\u0000EC\u0001\u0000"+
		"\u0000\u0000EF\u0001\u0000\u0000\u0000F\n\u0001\u0000\u0000\u0000GE\u0001"+
		"\u0000\u0000\u0000HJ\u0007\u0006\u0000\u0000IH\u0001\u0000\u0000\u0000"+
		"JK\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000"+
		"\u0000L\f\u0001\u0000\u0000\u0000MO\u0005\r\u0000\u0000NM\u0001\u0000"+
		"\u0000\u0000NO\u0001\u0000\u0000\u0000OS\u0001\u0000\u0000\u0000PR\u0007"+
		"\u0006\u0000\u0000QP\u0001\u0000\u0000\u0000RU\u0001\u0000\u0000\u0000"+
		"SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TV\u0001\u0000\u0000"+
		"\u0000US\u0001\u0000\u0000\u0000VY\u0005\n\u0000\u0000WY\u0005\r\u0000"+
		"\u0000XN\u0001\u0000\u0000\u0000XW\u0001\u0000\u0000\u0000Y\u000e\u0001"+
		"\u0000\u0000\u0000\u0010\u0000\u0010\u0015\u001b\u001d(-/68<EKNSX\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}