Available at: https://github.com/PhantomOffKanagawa/PythonParserProject
> This is a project designed to create a very basic parser for python in ANTLR ironically run in Python.\
> This was a solo project by me, that was developed on python 3.12.7 with the module `antlr4-python3-runtime==4.9.3`

### How to Run
- `conda create -n popl-parser python=3.12.7`
- `conda activate popl-parser`
- `pip install antlr4-python3-runtime==4.9.3`
- `python main.py`
- Voila

### To Compile
> Manual compilation of main w/ antlr4

`python ./scripts/combine_grammars.py`\
`antlr4 -Dlanguage=Python3 ./grammars/full.g4 -o ./libraries`

### Results
- [Deliverable 1 Results](./final_tests/project_deliverable_1_results.txt)
- [Deliverable 2 Results](./final_tests/project_deliverable_2_results.txt)
- [Deliverable 3 Results](./final_tests/project_deliverable_3_results.txt)

### File Structure
- `AA_indents.g4`: Define indent logic
- `blocks.g4`: Define code blocks
- `comments.g4`: Define single and multi line comments
- `full.g4`: One true grammar to rule them all cause everything hates multi file grammar
- `ifBlocks.g4`: Handle conditions and if statement blocks
- `keywords.g4`: Define tokens for keywords/reserved words
- `loopBlocks.g4`: Handle for & while loops and iterables
- `main.g4`: Define how to enter the grammar
- `operators.g4`: Define tokens for different operators
- `values.g4`: Define variables, numbers, etc.

### TODO:
- [X] Deliverable 1 Working with Separate *.g4 files
- [X] Indentation Working
- [X] Deliverable 2 Working with Full.g4
- [X] Deliverable 3 Working with Full.g4
- [ ] Get parse tree outputs working