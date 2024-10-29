# Python tester built on top of: https://github.com/AkiraHakuta/antlr4_Python3_examples

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from libraries.grammars.mainLexer import mainLexer
from libraries.grammars.mainParser import mainParser

def beautify_lisp_string(in_string):
    indent_size = 3
    add_indent = ' ' * indent_size
    out_string = in_string[0]  # no indent for 1st (
    indent = ''
    for i in range(1, len(in_string)):
        if in_string[i] == '(' and in_string[i + 1] != ' ':
            indent += add_indent
            out_string += "\n" + indent + '('
        elif in_string[i] == ')':
            out_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            out_string += in_string[i]
    return out_string

def parse_file(file_name):
    input_stream = FileStream(file_name)
    lexer = mainLexer(input_stream)

    # Adding custom error listener for the lexer
    lexer_error_listener = CustomErrorListener()
    lexer.removeErrorListeners()  # Remove default error listeners
    lexer.addErrorListener(lexer_error_listener)  # Add custom error listener

    token_stream = CommonTokenStream(lexer)

    # Tokenizing and listing any lexer errors
    print(f"Tokenizing {file_name}:")
    token_stream.fill()
    tokens = token_stream.tokens
    for tk in tokens:
        print(tk)

    # Parsing and listing any parser errors
    parser = mainParser(token_stream)
    parser.removeErrorListeners()  # Remove default console error listeners
    parser_error_listener = CustomErrorListener()
    parser.addErrorListener(parser_error_listener)  # Custom error listener

    tree = parser.stat()

    # Print the parse tree
    print("Parse tree:")
    lisp_tree_str = tree.toStringTree(recog=parser)
    print(beautify_lisp_string(lisp_tree_str))
    print()

    if lexer_error_listener.errors:
        print("Lexer Errors:")
        for error in lexer_error_listener.errors:
            print(error)
        print()

    if parser_error_listener.errors:
        print("Parser Errors:")
        for error in parser_error_listener.errors:
            print(error)

    # parser_errors = parser.getNumberOfSyntaxErrors()
    # if parser_errors > 0:
    #     print(f"\nParser Errors: {parser_errors}\n")

    print()

# Custom error listener to capture errors
class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)
        print(error_message)

# Test on a sample file
parse_file('deliverable1-test1.expr')
