grammar comments;
/*
    A file to define all possible types of python comments
 */

comment
    : SINGLE_LINE_COMMENT
    | MULTI_LINE_COMMENT
    ;

// Single Line Comment
SINGLE_LINE_COMMENT
    : '#' ~[\r\n]*
    ;

// Multi Line Comment
MULTI_LINE_COMMENT
    : '"""' .*? '"""'
    | '\'\'\'' .*? '\'\'\''
    | '```' .*? '```'
    ;