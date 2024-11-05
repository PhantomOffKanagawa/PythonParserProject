// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/main.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class mainLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, WS=2, COMMENT=3, NUMBER=4, VARIABLE=5, ASSIGNMENT_OP=6, ARITHMETIC_OP=7, 
		IF=8, ELIF=9, ELSE=10, COLON=11, AND=12, OR=13, NOT=14, LPAREN=15, RPAREN=16, 
		COMPARISON_OP=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "WS", "COMMENT", "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP", 
			"IF", "ELIF", "ELSE", "COLON", "AND", "OR", "NOT", "LPAREN", "RPAREN", 
			"COMPARISON_OP"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'statement'", null, null, null, null, null, null, "'if'", "'elif'", 
			"'else'", "':'", "'and'", "'or'", "'not'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "WS", "COMMENT", "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP", 
			"IF", "ELIF", "ELSE", "COLON", "AND", "OR", "NOT", "LPAREN", "RPAREN", 
			"COMPARISON_OP"
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


	public mainLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "main.g4"; }

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
		"\u0004\u0000\u0011\u0088\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0004\u0001/\b\u0001\u000b\u0001"+
		"\f\u00010\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0005\u0002"+
		"7\b\u0002\n\u0002\f\u0002:\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0004\u0003?\b\u0003\u000b\u0003\f\u0003@\u0001\u0003\u0001\u0003\u0004"+
		"\u0003E\b\u0003\u000b\u0003\f\u0003F\u0003\u0003I\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0005\u0004M\b\u0004\n\u0004\f\u0004P\t\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005[\b\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u0087\b\u0010\u0000"+
		"\u0000\u0011\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b"+
		"\u000e\u001d\u000f\u001f\u0010!\u0011\u0001\u0000\u0006\u0003\u0000\t"+
		"\n\r\r  \u0002\u0000\n\n\r\r\u0001\u000009\u0003\u0000AZ__az\u0004\u0000"+
		"09AZ__az\u0004\u0000%%*+--//\u0096\u0000\u0001\u0001\u0000\u0000\u0000"+
		"\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000"+
		"\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f"+
		"\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013"+
		"\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017"+
		"\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b"+
		"\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f"+
		"\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0001#\u0001\u0000"+
		"\u0000\u0000\u0003.\u0001\u0000\u0000\u0000\u00054\u0001\u0000\u0000\u0000"+
		"\u0007>\u0001\u0000\u0000\u0000\tJ\u0001\u0000\u0000\u0000\u000bZ\u0001"+
		"\u0000\u0000\u0000\r\\\u0001\u0000\u0000\u0000\u000f^\u0001\u0000\u0000"+
		"\u0000\u0011a\u0001\u0000\u0000\u0000\u0013f\u0001\u0000\u0000\u0000\u0015"+
		"k\u0001\u0000\u0000\u0000\u0017m\u0001\u0000\u0000\u0000\u0019q\u0001"+
		"\u0000\u0000\u0000\u001bt\u0001\u0000\u0000\u0000\u001dx\u0001\u0000\u0000"+
		"\u0000\u001fz\u0001\u0000\u0000\u0000!\u0086\u0001\u0000\u0000\u0000#"+
		"$\u0005s\u0000\u0000$%\u0005t\u0000\u0000%&\u0005a\u0000\u0000&\'\u0005"+
		"t\u0000\u0000\'(\u0005e\u0000\u0000()\u0005m\u0000\u0000)*\u0005e\u0000"+
		"\u0000*+\u0005n\u0000\u0000+,\u0005t\u0000\u0000,\u0002\u0001\u0000\u0000"+
		"\u0000-/\u0007\u0000\u0000\u0000.-\u0001\u0000\u0000\u0000/0\u0001\u0000"+
		"\u0000\u00000.\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u000012\u0001"+
		"\u0000\u0000\u000023\u0006\u0001\u0000\u00003\u0004\u0001\u0000\u0000"+
		"\u000048\u0005#\u0000\u000057\b\u0001\u0000\u000065\u0001\u0000\u0000"+
		"\u00007:\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u000089\u0001\u0000"+
		"\u0000\u00009;\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000;<\u0006"+
		"\u0002\u0000\u0000<\u0006\u0001\u0000\u0000\u0000=?\u0007\u0002\u0000"+
		"\u0000>=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@>\u0001\u0000"+
		"\u0000\u0000@A\u0001\u0000\u0000\u0000AH\u0001\u0000\u0000\u0000BD\u0005"+
		".\u0000\u0000CE\u0007\u0002\u0000\u0000DC\u0001\u0000\u0000\u0000EF\u0001"+
		"\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000"+
		"GI\u0001\u0000\u0000\u0000HB\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000"+
		"\u0000I\b\u0001\u0000\u0000\u0000JN\u0007\u0003\u0000\u0000KM\u0007\u0004"+
		"\u0000\u0000LK\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001"+
		"\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000O\n\u0001\u0000\u0000\u0000"+
		"PN\u0001\u0000\u0000\u0000Q[\u0005=\u0000\u0000RS\u0005+\u0000\u0000S"+
		"[\u0005=\u0000\u0000TU\u0005-\u0000\u0000U[\u0005=\u0000\u0000VW\u0005"+
		"*\u0000\u0000W[\u0005=\u0000\u0000XY\u0005/\u0000\u0000Y[\u0005=\u0000"+
		"\u0000ZQ\u0001\u0000\u0000\u0000ZR\u0001\u0000\u0000\u0000ZT\u0001\u0000"+
		"\u0000\u0000ZV\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000[\f\u0001"+
		"\u0000\u0000\u0000\\]\u0007\u0005\u0000\u0000]\u000e\u0001\u0000\u0000"+
		"\u0000^_\u0005i\u0000\u0000_`\u0005f\u0000\u0000`\u0010\u0001\u0000\u0000"+
		"\u0000ab\u0005e\u0000\u0000bc\u0005l\u0000\u0000cd\u0005i\u0000\u0000"+
		"de\u0005f\u0000\u0000e\u0012\u0001\u0000\u0000\u0000fg\u0005e\u0000\u0000"+
		"gh\u0005l\u0000\u0000hi\u0005s\u0000\u0000ij\u0005e\u0000\u0000j\u0014"+
		"\u0001\u0000\u0000\u0000kl\u0005:\u0000\u0000l\u0016\u0001\u0000\u0000"+
		"\u0000mn\u0005a\u0000\u0000no\u0005n\u0000\u0000op\u0005d\u0000\u0000"+
		"p\u0018\u0001\u0000\u0000\u0000qr\u0005o\u0000\u0000rs\u0005r\u0000\u0000"+
		"s\u001a\u0001\u0000\u0000\u0000tu\u0005n\u0000\u0000uv\u0005o\u0000\u0000"+
		"vw\u0005t\u0000\u0000w\u001c\u0001\u0000\u0000\u0000xy\u0005(\u0000\u0000"+
		"y\u001e\u0001\u0000\u0000\u0000z{\u0005)\u0000\u0000{ \u0001\u0000\u0000"+
		"\u0000|}\u0005=\u0000\u0000}\u0087\u0005=\u0000\u0000~\u007f\u0005!\u0000"+
		"\u0000\u007f\u0087\u0005=\u0000\u0000\u0080\u0087\u0005<\u0000\u0000\u0081"+
		"\u0082\u0005<\u0000\u0000\u0082\u0087\u0005=\u0000\u0000\u0083\u0087\u0005"+
		">\u0000\u0000\u0084\u0085\u0005>\u0000\u0000\u0085\u0087\u0005=\u0000"+
		"\u0000\u0086|\u0001\u0000\u0000\u0000\u0086~\u0001\u0000\u0000\u0000\u0086"+
		"\u0080\u0001\u0000\u0000\u0000\u0086\u0081\u0001\u0000\u0000\u0000\u0086"+
		"\u0083\u0001\u0000\u0000\u0000\u0086\u0084\u0001\u0000\u0000\u0000\u0087"+
		"\"\u0001\u0000\u0000\u0000\t\u000008@FHNZ\u0086\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}