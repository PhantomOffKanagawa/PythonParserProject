// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/keywordsLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class keywordsLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSIGNMENT_OP=1, ARITHMETIC_OP=2, LBRACKET=3, RBRACKET=4, COMMA=5, IF=6, 
		ELIF=7, ELSE=8, COLON=9, LPAREN=10, RPAREN=11, COMPARISON_OP=12, LOGICAL_OP=13, 
		NOT_OP=14, INDENT=15, DEDENT=16, WHILE=17, FOR=18;
	public static final int
		INDENT_MODE=1;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "INDENT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", "RBRACKET", "COMMA", "IF", 
			"ELIF", "ELSE", "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
			"NOT_OP", "INDENT", "DEDENT", "WHILE", "FOR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'['", "']'", "','", "'if'", "'elif'", "'else'", "':'", 
			"'('", "')'", null, null, "'not'", "'\\t'", "'\\n'", "'while'", "'for'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASSIGNMENT_OP", "ARITHMETIC_OP", "LBRACKET", "RBRACKET", "COMMA", 
			"IF", "ELIF", "ELSE", "COLON", "LPAREN", "RPAREN", "COMPARISON_OP", "LOGICAL_OP", 
			"NOT_OP", "INDENT", "DEDENT", "WHILE", "FOR"
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


	public keywordsLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "keywordsLexer.g4"; }

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
		"\u0004\u0000\u0012u\u0006\uffff\uffff\u0006\uffff\uffff\u0002\u0000\u0007"+
		"\u0000\u0002\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007"+
		"\u0003\u0002\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007"+
		"\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n"+
		"\u0007\n\u0002\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002"+
		"\u000e\u0007\u000e\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002"+
		"\u0011\u0007\u0011\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u00000\b"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003"+
		"\u000bW\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f^\b\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0000\u0000\u0012\u0002\u0001\u0004\u0002\u0006"+
		"\u0003\b\u0004\n\u0005\f\u0006\u000e\u0007\u0010\b\u0012\t\u0014\n\u0016"+
		"\u000b\u0018\f\u001a\r\u001c\u000e\u001e\u000f \u0010\"\u0011$\u0012\u0002"+
		"\u0000\u0001\u0001\u0004\u0000%%*+--//}\u0000\u0002\u0001\u0000\u0000"+
		"\u0000\u0000\u0004\u0001\u0000\u0000\u0000\u0000\u0006\u0001\u0000\u0000"+
		"\u0000\u0000\b\u0001\u0000\u0000\u0000\u0000\n\u0001\u0000\u0000\u0000"+
		"\u0000\f\u0001\u0000\u0000\u0000\u0000\u000e\u0001\u0000\u0000\u0000\u0000"+
		"\u0010\u0001\u0000\u0000\u0000\u0000\u0012\u0001\u0000\u0000\u0000\u0000"+
		"\u0014\u0001\u0000\u0000\u0000\u0000\u0016\u0001\u0000\u0000\u0000\u0000"+
		"\u0018\u0001\u0000\u0000\u0000\u0000\u001a\u0001\u0000\u0000\u0000\u0000"+
		"\u001c\u0001\u0000\u0000\u0000\u0000\u001e\u0001\u0000\u0000\u0000\u0000"+
		" \u0001\u0000\u0000\u0000\u0001\"\u0001\u0000\u0000\u0000\u0001$\u0001"+
		"\u0000\u0000\u0000\u0002/\u0001\u0000\u0000\u0000\u00041\u0001\u0000\u0000"+
		"\u0000\u00063\u0001\u0000\u0000\u0000\b5\u0001\u0000\u0000\u0000\n7\u0001"+
		"\u0000\u0000\u0000\f9\u0001\u0000\u0000\u0000\u000e<\u0001\u0000\u0000"+
		"\u0000\u0010A\u0001\u0000\u0000\u0000\u0012F\u0001\u0000\u0000\u0000\u0014"+
		"H\u0001\u0000\u0000\u0000\u0016J\u0001\u0000\u0000\u0000\u0018V\u0001"+
		"\u0000\u0000\u0000\u001a]\u0001\u0000\u0000\u0000\u001c_\u0001\u0000\u0000"+
		"\u0000\u001ec\u0001\u0000\u0000\u0000 g\u0001\u0000\u0000\u0000\"k\u0001"+
		"\u0000\u0000\u0000$q\u0001\u0000\u0000\u0000&0\u0005=\u0000\u0000\'(\u0005"+
		"+\u0000\u0000(0\u0005=\u0000\u0000)*\u0005-\u0000\u0000*0\u0005=\u0000"+
		"\u0000+,\u0005*\u0000\u0000,0\u0005=\u0000\u0000-.\u0005/\u0000\u0000"+
		".0\u0005=\u0000\u0000/&\u0001\u0000\u0000\u0000/\'\u0001\u0000\u0000\u0000"+
		"/)\u0001\u0000\u0000\u0000/+\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000"+
		"\u00000\u0003\u0001\u0000\u0000\u000012\u0007\u0000\u0000\u00002\u0005"+
		"\u0001\u0000\u0000\u000034\u0005[\u0000\u00004\u0007\u0001\u0000\u0000"+
		"\u000056\u0005]\u0000\u00006\t\u0001\u0000\u0000\u000078\u0005,\u0000"+
		"\u00008\u000b\u0001\u0000\u0000\u00009:\u0005i\u0000\u0000:;\u0005f\u0000"+
		"\u0000;\r\u0001\u0000\u0000\u0000<=\u0005e\u0000\u0000=>\u0005l\u0000"+
		"\u0000>?\u0005i\u0000\u0000?@\u0005f\u0000\u0000@\u000f\u0001\u0000\u0000"+
		"\u0000AB\u0005e\u0000\u0000BC\u0005l\u0000\u0000CD\u0005s\u0000\u0000"+
		"DE\u0005e\u0000\u0000E\u0011\u0001\u0000\u0000\u0000FG\u0005:\u0000\u0000"+
		"G\u0013\u0001\u0000\u0000\u0000HI\u0005(\u0000\u0000I\u0015\u0001\u0000"+
		"\u0000\u0000JK\u0005)\u0000\u0000K\u0017\u0001\u0000\u0000\u0000LM\u0005"+
		"=\u0000\u0000MW\u0005=\u0000\u0000NO\u0005!\u0000\u0000OW\u0005=\u0000"+
		"\u0000PW\u0005<\u0000\u0000QR\u0005<\u0000\u0000RW\u0005=\u0000\u0000"+
		"SW\u0005>\u0000\u0000TU\u0005>\u0000\u0000UW\u0005=\u0000\u0000VL\u0001"+
		"\u0000\u0000\u0000VN\u0001\u0000\u0000\u0000VP\u0001\u0000\u0000\u0000"+
		"VQ\u0001\u0000\u0000\u0000VS\u0001\u0000\u0000\u0000VT\u0001\u0000\u0000"+
		"\u0000W\u0019\u0001\u0000\u0000\u0000XY\u0005a\u0000\u0000YZ\u0005n\u0000"+
		"\u0000Z^\u0005d\u0000\u0000[\\\u0005o\u0000\u0000\\^\u0005r\u0000\u0000"+
		"]X\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000^\u001b\u0001\u0000"+
		"\u0000\u0000_`\u0005n\u0000\u0000`a\u0005o\u0000\u0000ab\u0005t\u0000"+
		"\u0000b\u001d\u0001\u0000\u0000\u0000cd\u0005\t\u0000\u0000de\u0001\u0000"+
		"\u0000\u0000ef\u0006\u000e\u0000\u0000f\u001f\u0001\u0000\u0000\u0000"+
		"gh\u0005\n\u0000\u0000hi\u0001\u0000\u0000\u0000ij\u0006\u000f\u0001\u0000"+
		"j!\u0001\u0000\u0000\u0000kl\u0005w\u0000\u0000lm\u0005h\u0000\u0000m"+
		"n\u0005i\u0000\u0000no\u0005l\u0000\u0000op\u0005e\u0000\u0000p#\u0001"+
		"\u0000\u0000\u0000qr\u0005f\u0000\u0000rs\u0005o\u0000\u0000st\u0005r"+
		"\u0000\u0000t%\u0001\u0000\u0000\u0000\u0005\u0000\u0001/V]\u0002\u0005"+
		"\u0001\u0000\u0004\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}