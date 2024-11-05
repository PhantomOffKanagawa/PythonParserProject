lexer grammar keywords;

// Deliverable 1 Keywords

ASSIGNMENT_OP
    : '=' | '+=' | '-=' | '*=' | '/='          // Assignment operator
    ;

ARITHMETIC_OP
    : '+' | '-' | '*' | '/' | '%'
    ;

LBRACKET: '[';
RBRACKET: ']';
COMMA   : ',';

// Deliverable 2 Keywords
IF      : 'if';
ELIF    : 'elif';
ELSE    : 'else';
COLON   : ':';
LPAREN  : '(';
RPAREN  : ')';

COMPARISON_OP
    : '==' | '!=' | '<' | '<=' | '>' | '>='
    ;

LOGICAL_OP
    : 'and' | 'or'
    ;

NOT_OP
    : 'not'
    ;

// Deliverable 3 Keywords
WHILE   : 'while';
FOR     : 'for';