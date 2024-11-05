grammar ifBlocks;
import keywords, values, operators, genericBlocks;

if_block
    : IF WS? condition WS? COLON WS? (block | if_block)+
      (ELIF condition WS? COLON WS? block+)*
      (ELSE WS? COLON WS? block+)?
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

block
    : assignment                            // One or more statements
    | expression
    ;