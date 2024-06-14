# Generated from LabeledExpr.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\r\6\rA\n")
        buf.write("\r\r\r\16\rB\3\16\6\16F\n\16\r\16\16\16G\3\17\3\17\3\17")
        buf.write("\3\17\6\17N\n\17\r\17\16\17O\3\20\5\20S\n\20\3\20\3\20")
        buf.write("\3\21\6\21X\n\21\r\21\16\21Y\3\21\3\21\2\2\22\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22\3\2\6\4\2C\\c|\3\2\62;\5\2\62;CHch\4")
        buf.write("\2\13\13\"\"\2a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3")
        buf.write("\2\2\2\r/\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2\23\67\3")
        buf.write("\2\2\2\259\3\2\2\2\27;\3\2\2\2\31@\3\2\2\2\33E\3\2\2\2")
        buf.write("\35I\3\2\2\2\37R\3\2\2\2!W\3\2\2\2#$\7?\2\2$\4\3\2\2\2")
        buf.write("%&\7~\2\2&\6\3\2\2\2\'(\7*\2\2(\b\3\2\2\2)*\7+\2\2*\n")
        buf.write("\3\2\2\2+,\7e\2\2,-\7q\2\2-.\7u\2\2.\f\3\2\2\2/\60\7u")
        buf.write("\2\2\60\61\7g\2\2\61\62\7p\2\2\62\16\3\2\2\2\63\64\7,")
        buf.write("\2\2\64\20\3\2\2\2\65\66\7\61\2\2\66\22\3\2\2\2\678\7")
        buf.write("-\2\28\24\3\2\2\29:\7/\2\2:\26\3\2\2\2;<\7v\2\2<=\7c\2")
        buf.write("\2=>\7p\2\2>\30\3\2\2\2?A\t\2\2\2@?\3\2\2\2AB\3\2\2\2")
        buf.write("B@\3\2\2\2BC\3\2\2\2C\32\3\2\2\2DF\t\3\2\2ED\3\2\2\2F")
        buf.write("G\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\34\3\2\2\2IJ\7\62\2\2J")
        buf.write("K\7z\2\2KM\3\2\2\2LN\t\4\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2")
        buf.write("\2\2OP\3\2\2\2P\36\3\2\2\2QS\7\17\2\2RQ\3\2\2\2RS\3\2")
        buf.write("\2\2ST\3\2\2\2TU\7\f\2\2U \3\2\2\2VX\t\5\2\2WV\3\2\2\2")
        buf.write("XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\b\21\2\2\\")
        buf.write("\"\3\2\2\2\b\2BGORY\3\b\2\2")
        return buf.getvalue()


class LabeledExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    MUL = 7
    DIV = 8
    ADD = 9
    SUB = 10
    TAN = 11
    ID = 12
    INT = 13
    HEX = 14
    NEWLINE = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'|'", "'('", "')'", "'cos'", "'sen'", "'*'", "'/'", 
            "'+'", "'-'", "'tan'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "TAN", "ID", "INT", "HEX", "NEWLINE", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "MUL", 
                  "DIV", "ADD", "SUB", "TAN", "ID", "INT", "HEX", "NEWLINE", 
                  "WS" ]

    grammarFileName = "LabeledExpr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


