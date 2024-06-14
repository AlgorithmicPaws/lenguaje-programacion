
from antlr4 import *
from DataScriptLexer import DataScriptLexer
from DataScriptParser import DataScriptParser
from EvalVisitor import EvalVisitor
import sys

def main():
    input_file = None
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if not input_file.endswith('.ds'):
            print("Error: el archivo debe tener la extensión .ds")
            return

    if input_file:
        input_stream = FileStream(input_file)
    else:
        input_stream = InputStream(input())

    lexer = DataScriptLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = DataScriptParser(tokens)
    tree = parser.prog()  # parse

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()

