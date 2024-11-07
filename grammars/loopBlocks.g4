parser grammar loopBlocks;
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