grammar main;
import blocks;

// parser rules

stat
    : expr | EOF
    ;

expr
    : block EOF
    ;

WS_SKIPPED
    : [\t] -> skip
    ;