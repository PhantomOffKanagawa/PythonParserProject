# test_indents.py
def debug_tokens(input_text):
    from antlr4 import InputStream, CommonTokenStream, Token
    from grammars.FullLexer import FullLexer
    
    # Create lexer
    input_stream = InputStream(input_text)
    lexer = FullLexer(input_stream)
    
    # Get all tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    # Print each token with type and position
    for token in token_stream.tokens:
        print(f"Token: {token.text!r:<20} "
              f"Type: {lexer.symbolicNames[token.type]:<10} "
              f"Line: {token.line} "
              f"Column: {token.column}")
        if (token.type == Token.EOF):
            print("EOF")

# Test with sample input
with open('./final_tests/project_deliverable_3.py', 'r') as file:
    test_input = file.read()

debug_tokens(test_input)