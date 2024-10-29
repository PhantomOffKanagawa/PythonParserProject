grammar main;
import operators;

// parser rules

stat
    : expr
    ;

expr
    : statement* EOF                        // A program is a sequence of statements
    ;

statement
    : assignment                            // Assignment
    | expression                            // Expressions
    ;

// Ignored tokens
WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;
