grammar ifBlocks;
// import keywords, values, operators, genericBlocks;

if_block
    : IF WS? condition WS? COLON WS? NEWLINE block
      (ELIF condition WS? COLON WS? NEWLINE block)*
      (ELSE WS? COLON WS? NEWLINE block)?
    ;