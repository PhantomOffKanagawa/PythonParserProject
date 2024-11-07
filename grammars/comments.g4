parser grammar comments;
/*
    Defines all possible types of python comments
 */

// Comments are mostly lexical
comment
    : SINGLE_LINE_COMMENT
    | MULTI_LINE_COMMENT
    ;