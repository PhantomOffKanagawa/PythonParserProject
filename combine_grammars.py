import os

def combine_grammars():
    # Define the order of files to process
    grammar_files = [
        'values.g4',
        'operators.g4',
        'main.g4',
        'blocks.g4',
        'comments.g4',
        'ifBlocks.g4',
        # 'indentScoping.g4',
        'keywords.g4',
        'loopBlocks.g4',
    ]
    
    combined_content = []
    grammar_name = "grammar full;"
    rules = []
    
    # Process each grammar file
    for file_name in grammar_files:
        file_path = os.path.join('grammars', file_name)
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found")
            continue
            
        with open(file_path, 'r') as f:
            content = f.read()
            
            # Get the grammar name from main.g4
            # if file_name == 'main.g4':
            #     for line in content.split('\n'):
            #         if 'grammar' in line:
            #             grammar_name = line
            #             break
            
            # Extract rules (skip imports, grammar declaration, etc)
            lines = content.split('\n')
            for line in lines:
                if line.strip().startswith('import'):
                    continue
                if line.strip().startswith('grammar'):
                    continue
                if line.strip().startswith('lexer grammar'):
                    continue
                if line.strip():
                    rules.append(line)
    
    # Combine everything
    if grammar_name:
        combined_content.append(grammar_name)
    else:
        combined_content.append('grammar full;')
    
    combined_content.extend(rules)
    
    # Write the combined grammar
    output_path = os.path.join('grammars', 'full.g4')
    with open(output_path, 'w') as f:
        f.write('\n'.join(combined_content))
    
    print(f"Combined grammar written to {output_path}")

if __name__ == '__main__':
    combine_grammars()