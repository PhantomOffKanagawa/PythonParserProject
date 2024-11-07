parser grammar main;
import blocks;
/*
  Start of parser grammar
 */

// Entry point
stat
    : expr
    ;

// Grammar for file
// Block of code followed by any ending dedents and then end of file
expr
    : first_block (DEDENT* EOF)
    ;
