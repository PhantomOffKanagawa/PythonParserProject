lexer grammar keywords;
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