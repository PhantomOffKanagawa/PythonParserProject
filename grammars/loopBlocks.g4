grammar loopBlocks;
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