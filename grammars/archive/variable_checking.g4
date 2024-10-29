grammar variable_checking;

@parser::members {
# Symbol table to keep track of declared variables
declared_variables = set()
}

program
    : statement* EOF                        // A program is a sequence of statements
    ;

statement
    : assignment_define                     // Defining assignment statements
    | assignment                            // Assignment
    | expression                            // Expressions
    ;

assignment_define
    : VARIABLE ASSIGNMENT_DEFINE_OP expression
    ;

assignment
    : declared_variable ASSIGNMENT_OP expression {

    }
    ;

expression
    : value (operator value)*               // Expression with operators and values
    ;

declared_variable
    : VARIABLE {
# Check if the variable is in the symbol table
if $VARIABLE.text not in self.declared_variables:
    print(f"Error: Variable '{ $VARIABLE.text }' used before assignment.")
    }
    ;

value
    : NUMBER                                // Number literals
    | declared_variable {
    }
    ;

operator
    : ARITHMETIC_OP                         // Arithmetic operators
    // | COMPARISON_OP                         // Comparison operators
    // | LOGICAL_OP                            // Logical operators
    // | BITWISE_OP                            // Bitwise operators
    ;

// Lexer rules
NUMBER
    : [0-9]+ ('.' [0-9]+)?                  // Integer or floating-point numbers
    ;

VARIABLE
    : [a-zA-Z_][a-zA-Z_0-9]*                // Variable names (Python identifiers)
    ;

ASSIGNMENT_DEFINE_OP
    : '='                                   // Defining assignment operator
    ;

ASSIGNMENT_OP
    : '+=' | '-=' | '*=' | '/='             // Assignment operator
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

// BITWISE_OP
//     : '&' | '|' | '^' | '~' | '<<' | '>>'
//     ;

// Ignored tokens
WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;
