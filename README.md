Available at: https://github.com/PhantomOffKanagawa/PythonParserProject
> This is a project designed to create a very basic parser for python in ANTLR ironically run in Python.\
> This was a solo project by me, that was developed on python 3.12.7 with the module `antlr4-python3-runtime==4.9.3`

### How to Run
- `conda create -n popl-parser python=3.12.7`
- `conda activate popl-parser`
- `pip install antlr4-python3-runtime==4.9.3`
- `pip install graphviz` and install [Graphviz](https://graphviz.org/download/) if going to generate images
- `python main.py --deliverable 3 --verbose`
- Voila, the text output is in the 

### To Compile
> Manual compilation of main w/ antlr4

`python ./scripts/combine_grammars.py`\
`antlr4 -Dlanguage=Python3 ./grammars/FullLexer.g4 ./grammars/FullParser.g4`

### Results
- [Deliverable 1 Results](./final_tests/project_deliverable_1_results.md)
  - [Image (svg)](./final_tests/deliverable_1.svg)
  - [Image (png)](./final_tests/project_deliverable_1_parse_tree.png)
- [Deliverable 2 Results](./final_tests/project_deliverable_2_results.md)
  - [Image (png)](./final_tests/project_deliverable_2_parse_tree.png)
- [Deliverable 3 Results](./final_tests/project_deliverable_3_results.md)
  - [Image (png)](./final_tests/project_deliverable_3_parse_tree.png)

### File Structure
> (#, #, #) Show what grammars are relevant to what deliverables \
> e.g. "`ifBlocks.g4` (2, 3): ..." shows that ifBlocks is relevant to deliverables #2 & #3, first introduced for deliverable #2 

- `main.py`: Main python file that tests the grammar against any of the 3 deliverables
- `final_tests`: Directory of all the test result views
  - `project_deliverable_1_results.md`: Markdown of results including parse tree as image and text
  - `project_deliverable_1.svg`: More viewable image of deliverable 1 due to no inline python code
  - `project_deliverable_1_parse_tree.png`: Image of parse tree for deliverable 1
  - `project_deliverable_2_results.md`: Markdown of results including parse tree as image and text
  - `project_deliverable_2_parse_tree.png`: Image of parse tree for deliverable 2
  - `project_deliverable_3_results.md`: Markdown of results including parse tree as image and text
  - `project_deliverable_3_parse_tree.png`: Image of parse tree for deliverable 3
- `grammar_archive`: Directory of old grammar attempts that failed
  - `AA_indents_action_file.g4`: Attempt at porting indents to js for VS Code extension visualizer
- `grammars`: Directory of all my individual grammar files
  - `AA_indents.g4` (2, 3): Define indent logic (AA to make sure it is added on top)
  - `blocks.g4` (2, 3): Define code blocks
  - `comments.g4` (3): Define single and multi line comments
  - `fullLexer.g4`: (Generated) One true lexer to rule them all cause everything hates multi file grammar
  - `fullParser.g4`: (Generated) One true lexer to rule them all
  - `ifBlocks.g4` (2, 3): Handle conditions and if statement blocks
  - `keywords.g4` (1, 2, 3): Define tokens for keywords/reserved words
  - `loopBlocks.g4` (3): Handle for & while loops and iterables
  - `main.g4` (1, 2, 3): Define how to enter the grammar
  - `operators.g4` (1, 2, 3): Define tokens for different operators
  - `values.g4` (1, 2, 3): Define variables, numbers, etc.
- `scripts`: Directory of helper scripts
  - `combine_grammars.py`: Combines all of the grammars in the grammar directory into one Parser and Lexer
  - `indentActions.js`: Another attempt at converting indentation to js
  - `test_indents.py`: Script to show token names more explicity used in testing indentation

### TODO:
- [X] Deliverable 1 Working with Separate *.g4 files
- [X] Indentation Working
- [X] Deliverable 2 Working with Full.g4
- [X] Deliverable 3 Working with Full.g4
- [X] Get parse tree outputs working
- [ ] Get parse trees working without inline code (or just prettier)