parser grammar FullParser;

options { tokenVocab=FullLexer; }

/*
  Defines code blocks
 */

// First block isn't indented
first_block
    :  (WS? line WS? NEWLINE*)* (WS? line WS?) NEWLINE*
    ;

// Nested blocks are indented
block
    : INDENT first_block DEDENT
    ;

// A line can be any of the following
line
    : assignment
    | comment
    | if_block
    | while_block
    | for_block
    ;

/*
    Defines all possible types of python comments
 */

// Comments are mostly lexical
comment
    : SINGLE_LINE_COMMENT
    | MULTI_LINE_COMMENT
    ;

// import keywords, values, operators, genericBlocks;
/*
  Defines if statements
 */

// If statement, can be followed by n elif statements and an optional else statement
if_block
    : IF WS? condition WS? COLON WS? NEWLINE block
      (elif_block)*
      (else_block)?
    ;

elif_block
    : ELIF condition WS? COLON WS? NEWLINE block
    ;

else_block
    : ELSE COLON WS? NEWLINE block
    ;

/*
   Defines all while or for block elements
 */

// While loop
while_block
    : WHILE WS? condition WS? COLON WS? NEWLINE block
    ;

// For loop
for_block
    : FOR WS? for_condition WS? COLON WS? NEWLINE block
    ;

// Conditions for for loops
for_condition
    : VARIABLE WS 'in' WS iterable
    ;

// Iterables for for loops
iterable
    : VARIABLE
    | array
    | RANGE LPAREN WS? count WS? (',' WS? count WS?){0,2} RPAREN
    ;

/*
  Start of parser grammar
 */

// Entry point
stat
    : expr
    ;

// Grammar for file
// Block of code followed by any ending dedents and then end of file
expr
    : first_block (DEDENT* EOF)
    ;


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