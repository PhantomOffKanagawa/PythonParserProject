parser grammar blocks;
import operators, comments, ifBlocks, loopBlocks;
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