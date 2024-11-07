lexer grammar values;

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