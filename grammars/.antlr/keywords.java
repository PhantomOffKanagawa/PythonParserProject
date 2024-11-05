// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/keywords.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class keywords extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSIGNMENT_OP=1, ARITHMETIC_OP=2, LBRACKET=3, RBRACKET=4, COMMA=5, IF=6, 
		ELIF=7, ELSE=8, COLON=9, LPAREN=10, RPAREN=11, COMPARISON_OP=12, LOGICAL_OP=13, 
		NOT_OP=14, WHILE=15, FOR=16;
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
			"NOT_OP", "WHILE", "FOR"
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
			"NOT_OP", "WHILE", "FOR"
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


	public keywords(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "keywords.g4"; }

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
		"\u0004\u0000\u0010h\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000+\b"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003"+
		"\u000bR\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\fY\b\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0000\u0000\u0010\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010\u0001\u0000\u0001\u0004\u0000%"+
		"%*+--//q\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0001"+
		"*\u0001\u0000\u0000\u0000\u0003,\u0001\u0000\u0000\u0000\u0005.\u0001"+
		"\u0000\u0000\u0000\u00070\u0001\u0000\u0000\u0000\t2\u0001\u0000\u0000"+
		"\u0000\u000b4\u0001\u0000\u0000\u0000\r7\u0001\u0000\u0000\u0000\u000f"+
		"<\u0001\u0000\u0000\u0000\u0011A\u0001\u0000\u0000\u0000\u0013C\u0001"+
		"\u0000\u0000\u0000\u0015E\u0001\u0000\u0000\u0000\u0017Q\u0001\u0000\u0000"+
		"\u0000\u0019X\u0001\u0000\u0000\u0000\u001bZ\u0001\u0000\u0000\u0000\u001d"+
		"^\u0001\u0000\u0000\u0000\u001fd\u0001\u0000\u0000\u0000!+\u0005=\u0000"+
		"\u0000\"#\u0005+\u0000\u0000#+\u0005=\u0000\u0000$%\u0005-\u0000\u0000"+
		"%+\u0005=\u0000\u0000&\'\u0005*\u0000\u0000\'+\u0005=\u0000\u0000()\u0005"+
		"/\u0000\u0000)+\u0005=\u0000\u0000*!\u0001\u0000\u0000\u0000*\"\u0001"+
		"\u0000\u0000\u0000*$\u0001\u0000\u0000\u0000*&\u0001\u0000\u0000\u0000"+
		"*(\u0001\u0000\u0000\u0000+\u0002\u0001\u0000\u0000\u0000,-\u0007\u0000"+
		"\u0000\u0000-\u0004\u0001\u0000\u0000\u0000./\u0005[\u0000\u0000/\u0006"+
		"\u0001\u0000\u0000\u000001\u0005]\u0000\u00001\b\u0001\u0000\u0000\u0000"+
		"23\u0005,\u0000\u00003\n\u0001\u0000\u0000\u000045\u0005i\u0000\u0000"+
		"56\u0005f\u0000\u00006\f\u0001\u0000\u0000\u000078\u0005e\u0000\u0000"+
		"89\u0005l\u0000\u00009:\u0005i\u0000\u0000:;\u0005f\u0000\u0000;\u000e"+
		"\u0001\u0000\u0000\u0000<=\u0005e\u0000\u0000=>\u0005l\u0000\u0000>?\u0005"+
		"s\u0000\u0000?@\u0005e\u0000\u0000@\u0010\u0001\u0000\u0000\u0000AB\u0005"+
		":\u0000\u0000B\u0012\u0001\u0000\u0000\u0000CD\u0005(\u0000\u0000D\u0014"+
		"\u0001\u0000\u0000\u0000EF\u0005)\u0000\u0000F\u0016\u0001\u0000\u0000"+
		"\u0000GH\u0005=\u0000\u0000HR\u0005=\u0000\u0000IJ\u0005!\u0000\u0000"+
		"JR\u0005=\u0000\u0000KR\u0005<\u0000\u0000LM\u0005<\u0000\u0000MR\u0005"+
		"=\u0000\u0000NR\u0005>\u0000\u0000OP\u0005>\u0000\u0000PR\u0005=\u0000"+
		"\u0000QG\u0001\u0000\u0000\u0000QI\u0001\u0000\u0000\u0000QK\u0001\u0000"+
		"\u0000\u0000QL\u0001\u0000\u0000\u0000QN\u0001\u0000\u0000\u0000QO\u0001"+
		"\u0000\u0000\u0000R\u0018\u0001\u0000\u0000\u0000ST\u0005a\u0000\u0000"+
		"TU\u0005n\u0000\u0000UY\u0005d\u0000\u0000VW\u0005o\u0000\u0000WY\u0005"+
		"r\u0000\u0000XS\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000Y\u001a"+
		"\u0001\u0000\u0000\u0000Z[\u0005n\u0000\u0000[\\\u0005o\u0000\u0000\\"+
		"]\u0005t\u0000\u0000]\u001c\u0001\u0000\u0000\u0000^_\u0005w\u0000\u0000"+
		"_`\u0005h\u0000\u0000`a\u0005i\u0000\u0000ab\u0005l\u0000\u0000bc\u0005"+
		"e\u0000\u0000c\u001e\u0001\u0000\u0000\u0000de\u0005f\u0000\u0000ef\u0005"+
		"o\u0000\u0000fg\u0005r\u0000\u0000g \u0001\u0000\u0000\u0000\u0004\u0000"+
		"*QX\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}