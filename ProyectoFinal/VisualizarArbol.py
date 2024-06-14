from antlr4 import *
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from antlr4.tree.Trees import Trees

def main():
    input_stream = FileStream('ejemplo.txt')
    lexer = LabeledExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = LabeledExprParser(tokens)
    tree = parser.prog()  # parse

    # Mostrar el árbol de análisis
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main()

