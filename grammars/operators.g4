grammar operators;
import keywords, values;

assignment
    : VARIABLE WS? assignment_operator WS? expression
    ;

expression
    : value WS? (operator WS? value WS?)*               // Expression with operators and values
    ;

array
    : LBRACKET (WS? value WS? (COMMA WS? value WS?)*)? WS? RBRACKET
    ;

count
    : NUMBER
    | VARIABLE
    ;

value
    : NUMBER                                // Number literals
    | VARIABLE
    | BOOLEAN                               // Boolean literals
    | STRING                                // String literals
    | LPAREN expression RPAREN              // Parenthesized expression
    | array
    ;

assignment_operator
    : ASSIGNMENT_OP                            // Assignment
    ;

operator
    : ARITHMETIC_OP                            // Arithmetic operators
    ;

condition
    : logical_condition
    ;

logical_condition
    : WS? comparison_condition (WS? (LOGICAL_OP | COMPARISON_OP) WS? comparison_condition)*
    ;

comparison_condition
    : NOT_OP WS? comparison_condition
    | LPAREN WS? logical_condition WS? RPAREN
    // | value WS? COMPARISON_OP WS? value
    | value
    ;