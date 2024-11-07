grammar AA_indents_action_file;

tokens { INDENT, DEDENT }

// @lexer::header {
// // Empty header as functionality is moved to actions file
// }

// @lexer::members {
// // Core functionality moved to actions file
// }

NEWLINE
    : ( {this.atStartOfInput()}? SPACES
    | ( '\r'? '\n' | '\r' ) SPACES? )
    {
let newLine = this.text.replace(/[^\r\n]+/g, "");
let spaces = this.text.replace(/[\r\n]+/g, "");
let next = this._input.LA(1);

if (next === '\r' || next === '\n' || next === '\f' || next === '#') {
    this.skip();
} else {
    this.emit(this.commonToken(this.NEWLINE, ""));
    let indent = this.getIndentationCount(spaces);
    
    if (this.mIndent === -1) {
        this.mIndent = indent;
        this.indents.push(indent);
    }
    
    let previous = this.indents.length === 0 ? 0 : this.indents[this.indents.length - 1];
    
    if (indent === previous) {
        this.skip();
    } else if (indent > previous) {
        this.indents.push(indent);
        this.emit(this.createIndent());
    } else {
        while (this.indents.length > 0 && this.indents[this.indents.length - 1] > indent) {
            this.emit(this.createDedent());
            this.indents.pop();
        }
    }
}
    }
    ;

SPACES
    : [ \t]+ -> skip
    ;

program: statement+ EOF;

statement
    : assignment NEWLINE
    | NEWLINE
    ;

assignment
    : VARIABLE SPACES? ASSIGNMENT_OP SPACES? expression
    ;

expression
    : literal                                      # literalExpr
    | VARIABLE                                     # variableExpr  
    | expression ARITHMETIC_OP expression          # arithmeticExpr
    | '[' (expression (',' SPACES? expression)*)? ']' # arrayExpr
    ;

literal
    : NUMBER
    | STRING 
    | BOOLEAN
    ;

VARIABLE: [a-zA-Z][a-zA-Z0-9_]*;
ASSIGNMENT_OP: '=' | '+=' | '-=' | '*=' | '/=';
ARITHMETIC_OP: '+' | '-' | '*' | '/' | '%';
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' ~["\r\n]* '"' | '\'' ~['\r\n]* '\'';
BOOLEAN: 'True' | 'False';

WS: [ \t]+ -> skip;