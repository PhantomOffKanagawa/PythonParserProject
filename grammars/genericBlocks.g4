grammar genericBlocks;
import operators, comments;

block
    : line+
    ;

line
    : assignment
    | comment
    ;