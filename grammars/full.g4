grammar full;
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
// parser rules
stat
    : expr | EOF
    ;
expr
    : block EOF // Most accurate
    ;
WS_SKIPPED
    : [\t] -> skip
    ;
/*
  A file that tracks code blocks
 */
block
    : (WS? line WS? NEWLINE)* (WS? line WS?)
    ;
line
    : assignment
    | comment
    | if_block
    | while_block
    | for_block
    |
    ;
/*
    A file to define all possible types of python comments
 */
comment
    : SINGLE_LINE_COMMENT
    | MULTI_LINE_COMMENT
    ;
// Single Line Comment
SINGLE_LINE_COMMENT
    : '#' ~[\r\n]*
    ;
// Multi Line Comment
MULTI_LINE_COMMENT
    : '"""' .*? '"""'
    | '\'\'\'' .*? '\'\'\''
    | '```' .*? '```'
    ;
// import keywords, values, operators, genericBlocks;
if_block
    : IF WS? condition WS? COLON WS? NEWLINE block
      (ELIF condition WS? COLON WS? NEWLINE block)*
      (ELSE WS? COLON WS? NEWLINE block)?
    ;
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
/*
   Handles all while or for block elements
 */
while_block
    : 'while' WS? condition WS? COLON WS? block
    ;
for_block
    : 'for' WS? for_condition WS? COLON WS? block
    ;
for_condition
    : VARIABLE WS 'in' WS iterable
    ;
iterable
    : VARIABLE
    | array
    | 'range(' WS? count WS? (',' WS? count WS?){0,2} ')'
    ;