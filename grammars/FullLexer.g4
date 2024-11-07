lexer grammar FullLexer;

/*
    Lexer rules for indentation scoping
 */

// Define INDENT and DEDENT tokens to be used later
tokens { INDENT, DEDENT }

// Define Header
@lexer::header {
from antlr4 import *
from antlr4.Token import CommonToken
from collections import deque
}

// This ANTLR lexer grammar handles indentation-based syntax similar to Python.
// It defines custom behavior for handling indents and dedents, which are crucial
// for parsing languages where indentation signifies block structure.

// Members section for the lexer
@lexer::members {
# Deques to manage tokens and indentation levels
tokens = deque()
indents = deque()
mIndent = -1
lastToken = None

# Emit a token and add it to the token queue
def emit(self, token=None):
    if token is None:
        token = self._factory.create(self._tokenFactorySourcePair, 
                                    self._type, 
                                    self._text, 
                                    self._channel, 
                                    self._tokenStartCharIndex, 
                                    self.getCharIndex()-1,
                                    self._tokenStartLine, 
                                    self._tokenStartColumn)

    self._token = token
    self.tokens.append(token)  # Add token to the queue
    return token

# Override nextToken to handle EOF and manage indentation tokens
def nextToken(self):
    if (self._input.LA(1) == Token.EOF and len(self.indents) > 0):
        for i in range(len(self.tokens) - 1, -1, -1):
            if self.tokens[i].type == Token.EOF:
                self.tokens.pop()

        self.emit(self.commonToken(self.NEWLINE, ""))

        while (len(self.indents) > 0):
            self.emit(self.createDedent())
            self.indents.pop()

        self.emit(self.commonToken(Token.EOF, "<EOF>"))

    next_token = super().nextToken()

    if next_token.channel == Token.DEFAULT_CHANNEL:
        self.lastToken = next_token

    return next_token if len(self.tokens) == 0 else self.tokens.popleft()

# Create a DEDENT token
def createDedent(self):
    dedent = CommonToken(
        self._tokenFactorySourcePair,
        self.DEDENT,
        self.DEFAULT_TOKEN_CHANNEL,
        self.getCharIndex()-1,
        self.getCharIndex()-1
    )
    dedent.line = self.lastToken.line
    dedent.text = "<DEDENT>"  # Custom text representation
    return dedent

# Create an INDENT token
def createIndent(self):
    indent = CommonToken(
        self._tokenFactorySourcePair,
        self.INDENT,
        self.DEFAULT_TOKEN_CHANNEL,
        self.getCharIndex()-1,
        self.getCharIndex()-1
    )
    indent.line = self.lastToken.line
    indent.text = "<INDENT>"  # Custom text representation
    return indent

# Create a common token with specified type and text
def commonToken(self, type, text):
    stop = self.getCharIndex() - 1
    start = stop if len(text) == 0 else stop - len(text) + 1

    return CommonToken(self._tokenFactorySourcePair, type, self.DEFAULT_TOKEN_CHANNEL, start, stop)

# Static method to count indentation levels
@staticmethod
def getIndentationCount(spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count += 4 - count % 4
        else:
            count += 1

    return count

# Check if at the start of input
def atStartOfInput(self):
    return self.column == 0 and super().line == 1
}

// Rule to handle newlines and indentation
NEWLINE
    : ( {self.atStartOfInput()}? SPACES
    | ( '\r'? '\n' | '\r' ) SPACES? )
   {
newLine = self.text.replace("[^\r\n]+", "")
spaces = self.text.replace("[\r\n]+", "")
if next == '\r' or next == '\n' or next == '\f' or next == '#':
    self.skip()
else:
    self.emit(self.commonToken(self.NEWLINE, ""))
    indent = self.getIndentationCount(spaces)
    if self.mIndent == -1:
        self.mIndent = indent
        self.indents.append(indent)
    previous = 0 if len(self.indents) == 0 else self.indents[-1]
    if (indent == previous):
        self.skip()
    elif (indent > previous):
        self.indents.append(indent)
        self.emit(self.createIndent())
    else:
        while (len(self.indents) > 0 and self.indents[-1] > indent):
            self.emit(self.createDedent())
            self.indents.pop()
    }
    ;

// Rule to handle spaces (tabs) and skip them
SPACES
    : [\t]+ -> skip
    ;

/*
  Lexer definitions for all keywords
 */

// Deliverable 1 Keywords
// Assignment Operators
ASSIGNMENT_OP
    : '=' | '+=' | '-=' | '*=' | '/='
    ;

// Arithmetic Operators
ARITHMETIC_OP
    : '+' | '-' | '*' | '/' | '%'
    ;

// Brackets and Comma for Array
LBRACKET: '[';
RBRACKET: ']';
COMMA   : ',';

// Deliverable 2 Keywords
// If Else Keywords
IF      : 'if';
ELIF    : 'elif';
ELSE    : 'else';
COLON   : ':';
LPAREN  : '(';
RPAREN  : ')';

// Comparison Operators
COMPARISON_OP
    : '==' | '!=' | '<' | '<=' | '>' | '>='
    ;

// Logical Operators
LOGICAL_OP
    : 'and' | 'or'
    ;

// Not Operator
NOT_OP
    : 'not'
    ;

// Deliverable 3 Keywords
// Loop Keywords
WHILE   : 'while';
FOR     : 'for';
RANGE   : 'range';
IN      : 'in';

// Single Line Comment
SINGLE_LINE_COMMENT
    : '#' ~[\r\n]*
    ;

// Multi Line Comment
MULTI_LINE_COMMENT
    : '"""' .*? '"""'
    | '\'\'\'' .*? '\'\'\''
    | '```' .*? '```'
    ;

/*
  Lexer definitions for values
 */


// Number
NUMBER
    : '-'? [0-9]+ ('.' [0-9]+)?                     // Integer or floating-point numbers
    ;

// Boolean
BOOLEAN
    : 'True' | 'False'                         // Boolean literals
    ;

// String
STRING
    : '"' (ESC | ~["\\])* '"'                   // Double quoted string
    | '\'' (ESC | ~['\\])* '\''                  // Single quoted string
    ;

// Escape Sequences for Strings
ESC
    : '\\' [btnfr"'\\]                          // Escape sequences
    ;

// Variable
VARIABLE
    : [a-zA-Z_][a-zA-Z_0-9]*                   // Variable names (Python identifiers)
    ;

// Required Whitespace
WS
    : [ ]+
    ;

// Skipped Whitespace
WS_SKIPPED
    : [ \t] -> skip
    ;