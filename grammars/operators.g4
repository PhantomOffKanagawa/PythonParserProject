parser grammar operators;
import keywords, values;
/*
  Lexer definitions for operators
 */

// Variable Assignment
assignment
    : VARIABLE WS? assignment_operator WS? expression
    ;

// Expressions
expression
    : value WS? (operator WS? value WS?)*               // Expression with operators and values
    ;

// Array
array
    : LBRACKET (WS? value WS? (COMMA WS? value WS?)*)? WS? RBRACKET
    ;

// Count for for loops
count
    : NUMBER
    | VARIABLE
    ;

// Possible values
value
    : NUMBER                                // Number literals
    | VARIABLE
    | BOOLEAN                               // Boolean literals
    | STRING                                // String literals
    | LPAREN expression RPAREN              // Parenthesized expression
    | array
    ;

// Wrapper for Assignment Operators
assignment_operator
    : ASSIGNMENT_OP                            // Assignment
    ;

// Wrapper for Arithmetic Operators
operator
    : ARITHMETIC_OP                            // Arithmetic operators
    ;

// All conditions
condition
    : WS? comparison_condition (WS? (LOGICAL_OP | COMPARISON_OP) WS? comparison_condition)*
    ;

// Comparison Conditions
comparison_condition
    : NOT_OP WS? comparison_condition
    | LPAREN WS? condition WS? RPAREN
    // | value WS? COMPARISON_OP WS? value
    | value
    ;