grammar main;
import genericBlocks, ifBlocks;

// parser rules

stat
    : expr
    ;

expr
    : code* EOF
    ;

code
    : block                           // A block of code is a sequence of statements
    | if_block
    ;

WS_SKIPPED
    : [\t\r\n] -> skip
    ;