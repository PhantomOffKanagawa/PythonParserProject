// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/loopBlocks.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class loopBlocksLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSIGNMENT_OP=1, ARITHMETIC_OP=2, LBRACKET=3, RBRACKET=4, COMMA=5, IF=6, 
		ELIF=7, ELSE=8, COLON=9, LPAREN=10, RPAREN=11, COMPARISON_OP=12, LOGICAL_OP=13, 
		NOT_OP=14, NUMBER=15, BOOLEAN=16, STRING=17, ESC=18, VARIABLE=19, WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", "RBRACKET", "COMMA", "IF", 
			"ELIF", "ELSE", "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
			"NOT_OP", "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'['", "']'", "','", "'if'", "'elif'", "'else'", "':'", 
			"'('", "')'", null, null, "'not'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", "RBRACKET", "COMMA", 
			"IF", "ELIF", "ELSE", "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
			"NOT_OP", "NUMBER", "BOOLEAN", "STRING", "ESC", "VARIABLE", "WS"
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


	public loopBlocksLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "loopBlocks.g4"; }

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
		"\u0004\u0000\u0014\u00a4\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0003\u00003\b\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0003\u000bZ\b\u000b\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0003\fa\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e"+
		"\u0003\u000eh\b\u000e\u0001\u000e\u0004\u000ek\b\u000e\u000b\u000e\f\u000e"+
		"l\u0001\u000e\u0001\u000e\u0004\u000eq\b\u000e\u000b\u000e\f\u000er\u0003"+
		"\u000eu\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0080"+
		"\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u0085\b\u0010"+
		"\n\u0010\f\u0010\u0088\t\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0005\u0010\u008e\b\u0010\n\u0010\f\u0010\u0091\t\u0010\u0001\u0010"+
		"\u0003\u0010\u0094\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0005\u0012\u009b\b\u0012\n\u0012\f\u0012\u009e\t\u0012\u0001"+
		"\u0013\u0004\u0013\u00a1\b\u0013\u000b\u0013\f\u0013\u00a2\u0000\u0000"+
		"\u0014\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014\u0001\u0000\b\u0004"+
		"\u0000%%*+--//\u0001\u000009\u0002\u0000\"\"\\\\\u0002\u0000\'\'\\\\\b"+
		"\u0000\"\"\'\'\\\\bbffnnrrtt\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001"+
		"\u0000  \u00b9\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u00012\u0001"+
		"\u0000\u0000\u0000\u00034\u0001\u0000\u0000\u0000\u00056\u0001\u0000\u0000"+
		"\u0000\u00078\u0001\u0000\u0000\u0000\t:\u0001\u0000\u0000\u0000\u000b"+
		"<\u0001\u0000\u0000\u0000\r?\u0001\u0000\u0000\u0000\u000fD\u0001\u0000"+
		"\u0000\u0000\u0011I\u0001\u0000\u0000\u0000\u0013K\u0001\u0000\u0000\u0000"+
		"\u0015M\u0001\u0000\u0000\u0000\u0017Y\u0001\u0000\u0000\u0000\u0019`"+
		"\u0001\u0000\u0000\u0000\u001bb\u0001\u0000\u0000\u0000\u001dg\u0001\u0000"+
		"\u0000\u0000\u001f\u007f\u0001\u0000\u0000\u0000!\u0093\u0001\u0000\u0000"+
		"\u0000#\u0095\u0001\u0000\u0000\u0000%\u0098\u0001\u0000\u0000\u0000\'"+
		"\u00a0\u0001\u0000\u0000\u0000)3\u0005=\u0000\u0000*+\u0005+\u0000\u0000"+
		"+3\u0005=\u0000\u0000,-\u0005-\u0000\u0000-3\u0005=\u0000\u0000./\u0005"+
		"*\u0000\u0000/3\u0005=\u0000\u000001\u0005/\u0000\u000013\u0005=\u0000"+
		"\u00002)\u0001\u0000\u0000\u00002*\u0001\u0000\u0000\u00002,\u0001\u0000"+
		"\u0000\u00002.\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u00003\u0002"+
		"\u0001\u0000\u0000\u000045\u0007\u0000\u0000\u00005\u0004\u0001\u0000"+
		"\u0000\u000067\u0005[\u0000\u00007\u0006\u0001\u0000\u0000\u000089\u0005"+
		"]\u0000\u00009\b\u0001\u0000\u0000\u0000:;\u0005,\u0000\u0000;\n\u0001"+
		"\u0000\u0000\u0000<=\u0005i\u0000\u0000=>\u0005f\u0000\u0000>\f\u0001"+
		"\u0000\u0000\u0000?@\u0005e\u0000\u0000@A\u0005l\u0000\u0000AB\u0005i"+
		"\u0000\u0000BC\u0005f\u0000\u0000C\u000e\u0001\u0000\u0000\u0000DE\u0005"+
		"e\u0000\u0000EF\u0005l\u0000\u0000FG\u0005s\u0000\u0000GH\u0005e\u0000"+
		"\u0000H\u0010\u0001\u0000\u0000\u0000IJ\u0005:\u0000\u0000J\u0012\u0001"+
		"\u0000\u0000\u0000KL\u0005(\u0000\u0000L\u0014\u0001\u0000\u0000\u0000"+
		"MN\u0005)\u0000\u0000N\u0016\u0001\u0000\u0000\u0000OP\u0005=\u0000\u0000"+
		"PZ\u0005=\u0000\u0000QR\u0005!\u0000\u0000RZ\u0005=\u0000\u0000SZ\u0005"+
		"<\u0000\u0000TU\u0005<\u0000\u0000UZ\u0005=\u0000\u0000VZ\u0005>\u0000"+
		"\u0000WX\u0005>\u0000\u0000XZ\u0005=\u0000\u0000YO\u0001\u0000\u0000\u0000"+
		"YQ\u0001\u0000\u0000\u0000YS\u0001\u0000\u0000\u0000YT\u0001\u0000\u0000"+
		"\u0000YV\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000Z\u0018\u0001"+
		"\u0000\u0000\u0000[\\\u0005a\u0000\u0000\\]\u0005n\u0000\u0000]a\u0005"+
		"d\u0000\u0000^_\u0005o\u0000\u0000_a\u0005r\u0000\u0000`[\u0001\u0000"+
		"\u0000\u0000`^\u0001\u0000\u0000\u0000a\u001a\u0001\u0000\u0000\u0000"+
		"bc\u0005n\u0000\u0000cd\u0005o\u0000\u0000de\u0005t\u0000\u0000e\u001c"+
		"\u0001\u0000\u0000\u0000fh\u0005-\u0000\u0000gf\u0001\u0000\u0000\u0000"+
		"gh\u0001\u0000\u0000\u0000hj\u0001\u0000\u0000\u0000ik\u0007\u0001\u0000"+
		"\u0000ji\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000lj\u0001\u0000"+
		"\u0000\u0000lm\u0001\u0000\u0000\u0000mt\u0001\u0000\u0000\u0000np\u0005"+
		".\u0000\u0000oq\u0007\u0001\u0000\u0000po\u0001\u0000\u0000\u0000qr\u0001"+
		"\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000"+
		"su\u0001\u0000\u0000\u0000tn\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000"+
		"\u0000u\u001e\u0001\u0000\u0000\u0000vw\u0005T\u0000\u0000wx\u0005r\u0000"+
		"\u0000xy\u0005u\u0000\u0000y\u0080\u0005e\u0000\u0000z{\u0005F\u0000\u0000"+
		"{|\u0005a\u0000\u0000|}\u0005l\u0000\u0000}~\u0005s\u0000\u0000~\u0080"+
		"\u0005e\u0000\u0000\u007fv\u0001\u0000\u0000\u0000\u007fz\u0001\u0000"+
		"\u0000\u0000\u0080 \u0001\u0000\u0000\u0000\u0081\u0086\u0005\"\u0000"+
		"\u0000\u0082\u0085\u0003#\u0011\u0000\u0083\u0085\b\u0002\u0000\u0000"+
		"\u0084\u0082\u0001\u0000\u0000\u0000\u0084\u0083\u0001\u0000\u0000\u0000"+
		"\u0085\u0088\u0001\u0000\u0000\u0000\u0086\u0084\u0001\u0000\u0000\u0000"+
		"\u0086\u0087\u0001\u0000\u0000\u0000\u0087\u0089\u0001\u0000\u0000\u0000"+
		"\u0088\u0086\u0001\u0000\u0000\u0000\u0089\u0094\u0005\"\u0000\u0000\u008a"+
		"\u008f\u0005\'\u0000\u0000\u008b\u008e\u0003#\u0011\u0000\u008c\u008e"+
		"\b\u0003\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008d\u008c\u0001"+
		"\u0000\u0000\u0000\u008e\u0091\u0001\u0000\u0000\u0000\u008f\u008d\u0001"+
		"\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0092\u0001"+
		"\u0000\u0000\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0092\u0094\u0005"+
		"\'\u0000\u0000\u0093\u0081\u0001\u0000\u0000\u0000\u0093\u008a\u0001\u0000"+
		"\u0000\u0000\u0094\"\u0001\u0000\u0000\u0000\u0095\u0096\u0005\\\u0000"+
		"\u0000\u0096\u0097\u0007\u0004\u0000\u0000\u0097$\u0001\u0000\u0000\u0000"+
		"\u0098\u009c\u0007\u0005\u0000\u0000\u0099\u009b\u0007\u0006\u0000\u0000"+
		"\u009a\u0099\u0001\u0000\u0000\u0000\u009b\u009e\u0001\u0000\u0000\u0000"+
		"\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000"+
		"\u009d&\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000\u009f"+
		"\u00a1\u0007\u0007\u0000\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1"+
		"\u00a2\u0001\u0000\u0000\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a3\u0001\u0000\u0000\u0000\u00a3(\u0001\u0000\u0000\u0000\u0010\u0000"+
		"2Y`glrt\u007f\u0084\u0086\u008d\u008f\u0093\u009c\u00a2\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}