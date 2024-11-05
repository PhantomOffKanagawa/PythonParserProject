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
    // | COMPARISON_OP                         // Comparison operators
    // | LOGICAL_OP                            // Logical operators
    // | BITWISE_OP                            // Bitwise operators
    ;