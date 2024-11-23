# Python tester built on top of: https://github.com/AkiraHakuta/antlr4_Python3_examples

import argparse

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from grammars.FullLexer import FullLexer
from grammars.FullParser import FullParser

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

def visualize_parse_tree(tree, output_file="parse_tree"):
    """Create a visual representation of the parse tree"""

    # For graph visualization
    # Avoiding import errors when not needed
    from graphviz import Digraph
    from antlr4.tree.Tree import ParseTree
    import uuid

    dot = Digraph(comment='Parse Tree')
    dot.attr(rankdir='TB')
    
    # Track nodes and edges
    nodes = {}
    
    def add_node(tree_node):
        # Generate unique ID
        node_id = str(uuid.uuid4())
        
        # Get node text
        if hasattr(tree_node, 'symbol'):
            node_text = f"{tree_node.symbol.text}\n{type(tree_node).__name__}"
        else:
            node_text = type(tree_node).__name__
        
        # Add node to graph
        dot.node(node_id, node_text)
        nodes[tree_node] = node_id
        
        # Process children
        for i in range(tree_node.getChildCount()):
            child = tree_node.getChild(i)
            child_id = add_node(child)
            dot.edge(node_id, child_id)
            
        return node_id
    
    # Build the graph
    add_node(tree)
    
    # Save the visualization
    dot.render(output_file, view=True, format='png')
    
    return output_file + '.png'

def parse_file(file_name, verbose=True, image=False):
    input_stream = FileStream(file_name)
    lexer = FullLexer(input_stream)

    # Adding custom error listener for the lexer
    lexer_error_listener = CustomErrorListener()
    lexer.removeErrorListeners()  # Remove default error listeners
    lexer.addErrorListener(lexer_error_listener)  # Add custom error listener

    token_stream = CommonTokenStream(lexer)

    # Tokenizing and listing any lexer errors
    if verbose:
        print(f"Tokenizing {file_name}:")
    token_stream.fill()
    tokens = token_stream.tokens
    if verbose:
        for tk in tokens:
            print(f'{tk} {lexer.symbolicNames[tk.type]}')

    # Parsing and listing any parser errors
    parser = FullParser(token_stream)
    parser.removeErrorListeners()  # Remove default console error listeners
    parser_error_listener = CustomErrorListener()
    parser.addErrorListener(parser_error_listener)  # Custom error listener

    tree = parser.stat()

    # Visualize the parse tree
    if image:
        output_file = visualize_parse_tree(tree, output_file=file_name.replace('.py', '_parse_tree'))
        print(f"Parse tree visualization saved to {output_file}")

    # Print the parse tree
    if verbose:
        print("Parse tree:")
        lisp_tree_str = tree.toStringTree(recog=parser)
        print(beautify_lisp_string(lisp_tree_str))
        print()

    # Print any lexer errors
    if lexer_error_listener.errors and verbose:
        print("Lexer Errors:")
        for error in lexer_error_listener.errors:
            print(error)
        print()

    # Print any parser errors
    if parser_error_listener.errors and verbose:
        print("Parser Errors:")
        for error in parser_error_listener.errors:
            print(error)
            print()

    # parser_errors = parser.getNumberOfSyntaxErrors()
    # if parser_errors > 0:
    #     print(f"\nParser Errors: {parser_errors}\n")

    return (len(lexer_error_listener.errors) == 0 and len(parser_error_listener.errors) == 0)

# Custom error listener to capture errors
class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)
        print(error_message)

# Test on class requirements

parser = argparse.ArgumentParser(description='Python Parser')
parser.add_argument('--verbose', action=argparse.BooleanOptionalAction, help='Print verbose output')
parser.add_argument('--file', type=str, default="", help='Python file to parse')
parser.add_argument('--deliv', type=int, default=-1, help='Deliverable to check against (1 - 3)')
parser.add_argument('--image', action='store_true', help='Generate image of parse tree')
args = parser.parse_args()

match args.deliv:
    case 1:
        deliverable = parse_file('./final_tests/project_deliverable_1.py', verbose=args.verbose, image=args.image)
    case 2:
        deliverable = parse_file('./final_tests/project_deliverable_2.py', verbose=args.verbose, image=args.image)
    case 3:
        deliverable = parse_file('./final_tests/project_deliverable_3.py', verbose=args.verbose, image=args.image)
    case -1:
        pass
    case _:
        print("Invalid deliverable")

if (args.deliv > 0 and args.deliv < 4):
    print(f"Project Deliverable {args.deliv}: {'Passed' if deliverable else 'Failed'}")

# Untested
if args.file != "":
    parse_file(args.file, verbose=args.verbose, image=args.image)

if args.deliv == -1 and args.file == "":
    print("No file or deliverable specified")
    print("python main.py --file? <file_name> --deliv? <1-3> --verbose? --image?")