Available at: https://github.com/PhantomOffKanagawa/PythonParserProject
> This is a project designed to create a very basic parser for python in ANTLR ironically run in Python.\
> This was a solo project by me, that was developed on python 3.12.7 with the module `antlr4-python3-runtime==4.9.3`

### How to Run
- `conda create -n popl-parser python=3.12.7`
- `pip install antlr4-python3-runtime==4.9.3`
- `python main.py`
- Wait a ~~second~~ minute, cause its slow

### To Compile
> Manual compilation of main w/ antlr4

`python combine_grammars.py`\
`antlr4 -Dlanguage=Python3 ./grammars/full.g4 -o ./libraries`

### Results
- [Deliverable 1 Results](./final_tests/project_deliverable_1_results.txt)

### File Structure
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
- [ ] Indentation
- [ ] Deliverable 2 Working with Full.g4
- [ ] Deliverable 3 Working with Full.g4