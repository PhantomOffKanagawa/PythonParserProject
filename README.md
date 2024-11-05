Available at: https://github.com/PhantomOffKanagawa/PythonParserProject
> This is a project designed to create a very basic parser for python in ANTLR ironically run in Python
> This was a solo project by me, that was developed on python 3.12.7 with the module `antlr4-python3-runtime==4.9.3`

### How to Run
- `conda create -n popl-parser python=3.12.7`
- `pip install antlr4-python3-runtime==4.9.3`
- `python main.py`
- Wait a second, cause its slow due to no tab scoping

To run python:
`python3 main.py`

To compile main antlr
`antlr4 -Dlanguage=Python3 ./grammars/main.g4 -o ./libraries`

TODO:
- [ ] Indentation