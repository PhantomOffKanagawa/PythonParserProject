parser grammar ifBlocks;
// import keywords, values, operators, genericBlocks;
/*
  Defines if statements
 */

// If statement, can be followed by n elif statements and an optional else statement
if_block
    : IF WS? condition WS? COLON WS? NEWLINE block
      (elif_block)*
      (else_block)?
    ;

elif_block
    : ELIF condition WS? COLON WS? NEWLINE block
    ;

else_block
    : ELSE COLON WS? NEWLINE block
    ;