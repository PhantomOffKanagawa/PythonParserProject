lexer grammar values;

// Lexer rules
NUMBER
    : '-'? [0-9]+ ('.' [0-9]+)?                     // Integer or floating-point numbers
    ;

BOOLEAN
    : 'True' | 'False'                         // Boolean literals
    ;

STRING
    : '"' (ESC | ~["\\])* '"'                   // Double quoted string
    | '\'' (ESC | ~['\\])* '\''                  // Single quoted string
    ;

ESC
    : '\\' [btnfr"'\\]                          // Escape sequences
    ;

VARIABLE
    : [a-zA-Z_][a-zA-Z_0-9]*                   // Variable names (Python identifiers)
    ;

WS // Required Whitespace
    : [ ]+
    ;

NEWLINE
    : '\r'? [ ]* '\n' | '\r'                         // Newline
    ;