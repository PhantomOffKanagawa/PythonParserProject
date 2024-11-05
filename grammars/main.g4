grammar main;
import blocks;

// parser rules

stat
    : expr
    ;

expr
    : block? EOF
    ;

WS_SKIPPED
    : [\t] -> skip
    ;