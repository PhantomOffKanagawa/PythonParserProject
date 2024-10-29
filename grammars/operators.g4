grammar operators;

assignment
    : VARIABLE ASSIGNMENT_OP expression
    ;

expression
    : value (operator value)*               // Expression with operators and values
    ;

value
    : NUMBER                                // Number literals
    | VARIABLE {
    }
    ;

operator
    : ARITHMETIC_OP                            // Arithmetic operators
    // | COMPARISON_OP                         // Comparison operators
    // | LOGICAL_OP                            // Logical operators
    // | BITWISE_OP                            // Bitwise operators
    ;

// Lexer rules
NUMBER
    : [0-9]+ ('.' [0-9]+)?                     // Integer or floating-point numbers
    ;

VARIABLE
    : [a-zA-Z_][a-zA-Z_0-9]*                   // Variable names (Python identifiers)
    ;

ASSIGNMENT_OP
    : '=' | '+=' | '-=' | '*=' | '/='          // Assignment operator
    ;

ARITHMETIC_OP
    : '+' | '-' | '*' | '/' | '%'
    ;

// COMPARISON_OP
//     : '==' | '!=' | '<' | '<=' | '>' | '>='
//     ;

// LOGICAL_OP
//     : 'and' | 'or' | 'not'
//     ;