// Generated from /home/phantom/OneDrive_personal/Documents/School/PoPL/Project/grammars/ifBlocks.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class if_blocksLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, IF=2, ELIF=3, ELSE=4, COLON=5, AND=6, OR=7, NOT=8, LPAREN=9, RPAREN=10, 
		COMPARISON_OP=11, NUMBER=12, VARIABLE=13, ASSIGNMENT_OP=14, ARITHMETIC_OP=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "IF", "ELIF", "ELSE", "COLON", "AND", "OR", "NOT", "LPAREN", 
			"RPAREN", "COMPARISON_OP", "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'statement'", "'if'", "'elif'", "'else'", "':'", "'and'", "'or'", 
			"'not'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "IF", "ELIF", "ELSE", "COLON", "AND", "OR", "NOT", "LPAREN", 
			"RPAREN", "COMPARISON_OP", "NUMBER", "VARIABLE", "ASSIGNMENT_OP", "ARITHMETIC_OP"
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


	public if_blocksLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ifBlocks.g4"; }

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
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\nR\b\n\u0001\u000b\u0004\u000b"+
		"U\b\u000b\u000b\u000b\f\u000bV\u0001\u000b\u0001\u000b\u0004\u000b[\b"+
		"\u000b\u000b\u000b\f\u000b\\\u0003\u000b_\b\u000b\u0001\f\u0001\f\u0005"+
		"\fc\b\f\n\f\f\ff\t\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0003\rq\b\r\u0001\u000e\u0001\u000e\u0000\u0000\u000f"+
		"\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r"+
		"\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u0001\u0000\u0004\u0001\u000009\u0003\u0000AZ__az\u0004\u0000"+
		"09AZ__az\u0004\u0000%%*+--//\u0080\u0000\u0001\u0001\u0000\u0000\u0000"+
		"\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000"+
		"\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f"+
		"\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013"+
		"\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017"+
		"\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b"+
		"\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0001\u001f"+
		"\u0001\u0000\u0000\u0000\u0003)\u0001\u0000\u0000\u0000\u0005,\u0001\u0000"+
		"\u0000\u0000\u00071\u0001\u0000\u0000\u0000\t6\u0001\u0000\u0000\u0000"+
		"\u000b8\u0001\u0000\u0000\u0000\r<\u0001\u0000\u0000\u0000\u000f?\u0001"+
		"\u0000\u0000\u0000\u0011C\u0001\u0000\u0000\u0000\u0013E\u0001\u0000\u0000"+
		"\u0000\u0015Q\u0001\u0000\u0000\u0000\u0017T\u0001\u0000\u0000\u0000\u0019"+
		"`\u0001\u0000\u0000\u0000\u001bp\u0001\u0000\u0000\u0000\u001dr\u0001"+
		"\u0000\u0000\u0000\u001f \u0005s\u0000\u0000 !\u0005t\u0000\u0000!\"\u0005"+
		"a\u0000\u0000\"#\u0005t\u0000\u0000#$\u0005e\u0000\u0000$%\u0005m\u0000"+
		"\u0000%&\u0005e\u0000\u0000&\'\u0005n\u0000\u0000\'(\u0005t\u0000\u0000"+
		"(\u0002\u0001\u0000\u0000\u0000)*\u0005i\u0000\u0000*+\u0005f\u0000\u0000"+
		"+\u0004\u0001\u0000\u0000\u0000,-\u0005e\u0000\u0000-.\u0005l\u0000\u0000"+
		"./\u0005i\u0000\u0000/0\u0005f\u0000\u00000\u0006\u0001\u0000\u0000\u0000"+
		"12\u0005e\u0000\u000023\u0005l\u0000\u000034\u0005s\u0000\u000045\u0005"+
		"e\u0000\u00005\b\u0001\u0000\u0000\u000067\u0005:\u0000\u00007\n\u0001"+
		"\u0000\u0000\u000089\u0005a\u0000\u00009:\u0005n\u0000\u0000:;\u0005d"+
		"\u0000\u0000;\f\u0001\u0000\u0000\u0000<=\u0005o\u0000\u0000=>\u0005r"+
		"\u0000\u0000>\u000e\u0001\u0000\u0000\u0000?@\u0005n\u0000\u0000@A\u0005"+
		"o\u0000\u0000AB\u0005t\u0000\u0000B\u0010\u0001\u0000\u0000\u0000CD\u0005"+
		"(\u0000\u0000D\u0012\u0001\u0000\u0000\u0000EF\u0005)\u0000\u0000F\u0014"+
		"\u0001\u0000\u0000\u0000GH\u0005=\u0000\u0000HR\u0005=\u0000\u0000IJ\u0005"+
		"!\u0000\u0000JR\u0005=\u0000\u0000KR\u0005<\u0000\u0000LM\u0005<\u0000"+
		"\u0000MR\u0005=\u0000\u0000NR\u0005>\u0000\u0000OP\u0005>\u0000\u0000"+
		"PR\u0005=\u0000\u0000QG\u0001\u0000\u0000\u0000QI\u0001\u0000\u0000\u0000"+
		"QK\u0001\u0000\u0000\u0000QL\u0001\u0000\u0000\u0000QN\u0001\u0000\u0000"+
		"\u0000QO\u0001\u0000\u0000\u0000R\u0016\u0001\u0000\u0000\u0000SU\u0007"+
		"\u0000\u0000\u0000TS\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000"+
		"VT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000W^\u0001\u0000\u0000"+
		"\u0000XZ\u0005.\u0000\u0000Y[\u0007\u0000\u0000\u0000ZY\u0001\u0000\u0000"+
		"\u0000[\\\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001"+
		"\u0000\u0000\u0000]_\u0001\u0000\u0000\u0000^X\u0001\u0000\u0000\u0000"+
		"^_\u0001\u0000\u0000\u0000_\u0018\u0001\u0000\u0000\u0000`d\u0007\u0001"+
		"\u0000\u0000ac\u0007\u0002\u0000\u0000ba\u0001\u0000\u0000\u0000cf\u0001"+
		"\u0000\u0000\u0000db\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000"+
		"e\u001a\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000gq\u0005=\u0000"+
		"\u0000hi\u0005+\u0000\u0000iq\u0005=\u0000\u0000jk\u0005-\u0000\u0000"+
		"kq\u0005=\u0000\u0000lm\u0005*\u0000\u0000mq\u0005=\u0000\u0000no\u0005"+
		"/\u0000\u0000oq\u0005=\u0000\u0000pg\u0001\u0000\u0000\u0000ph\u0001\u0000"+
		"\u0000\u0000pj\u0001\u0000\u0000\u0000pl\u0001\u0000\u0000\u0000pn\u0001"+
		"\u0000\u0000\u0000q\u001c\u0001\u0000\u0000\u0000rs\u0007\u0003\u0000"+
		"\u0000s\u001e\u0001\u0000\u0000\u0000\u0007\u0000QV\\^dp\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}