grammar blocks;
import operators, comments, ifBlocks, loopBlocks;
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