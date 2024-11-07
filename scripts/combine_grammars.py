#combine_grammars.py
import os
import re

def detect_grammar_type(content):
    first_line = content.split('\n')[0].strip()
    if 'lexer grammar' in first_line:
        return 'lexer'
    elif 'parser grammar' in first_line:
        return 'parser'
    elif 'grammar' in first_line:
        return 'combined'
    return None

def extract_grammar_name(content):
    first_line = content.split('\n')[0].strip()
    match = re.search(r'(?:lexer |parser )?grammar\s+(\w+);', first_line)
    return match.group(1) if match else None

def clean_grammar_content(content):
    # Split into lines and filter
    lines = content.split('\n')
    
    # Remove grammar declaration line
    if lines and any(x in lines[0].lower() for x in ['grammar', 'lexer', 'parser']):
        lines = lines[1:]
        
    # Remove import statements
    lines = [line for line in lines if not line.strip().startswith('import')]
    
    # Remove empty lines from start
    while lines and not lines[0].strip():
        lines.pop(0)
        
    return '\n'.join(lines)

def combine_grammars():
    grammar_files = [f for f in os.listdir('grammars') if f.endswith('.g4')]
    grammar_files.sort()

    lexer_rules = []
    parser_rules = []
    lexer_names = []
    parser_names = []

    # First pass - categorize and collect rules
    for filename in grammar_files:
        if filename.startswith('Full'):
            continue

        with open(os.path.join('grammars', filename), 'r') as f:
            content = f.read()
            grammar_type = detect_grammar_type(content)
            name = extract_grammar_name(content)
            
            # Clean content before adding
            cleaned_content = clean_grammar_content(content)

            if grammar_type == 'lexer':
                lexer_rules.append(cleaned_content)
                lexer_names.append(name)
            elif grammar_type == 'parser':
                parser_rules.append(cleaned_content)
                parser_names.append(name)
            elif grammar_type == 'combined':
                # Split combined grammar into lexer and parser parts
                lexer_part = re.findall(r'[A-Z][A-Z_]*\s*:', content)
                parser_part = re.findall(r'[a-z][a-z_]*\s*:', content)
                lexer_rules.extend(lexer_part)
                parser_rules.extend(parser_part)

    # Generate lexer grammar
    lexer_content = f"lexer grammar FullLexer;\n\n"
    lexer_content += "\n\n".join(lexer_rules)
    
    # Generate parser grammar
    parser_content = f"parser grammar FullParser;\n\n"
    parser_content += f"options {{ tokenVocab=FullLexer; }}\n\n"
    parser_content += "\n\n".join(parser_rules)

    # Write output files
    with open(os.path.join('grammars', 'FullLexer.g4'), 'w') as f:
        f.write(lexer_content)
    
    with open(os.path.join('grammars', 'FullParser.g4'), 'w') as f:
        f.write(parser_content)

    # Return ANTLR compilation command
    return "antlr4 -Dlanguage=Python3 ./grammars/FullLexer.g4 ./grammars/FullParser.g4"

if __name__ == "__main__":
    command = combine_grammars()
    print(f"Generated grammar files. Compile with:\n{command}")