# Generated from LabeledExpr.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LabeledExprParser import LabeledExprParser
else:
    from LabeledExprParser import LabeledExprParser

# This class defines a complete listener for a parse tree produced by LabeledExprParser.
class LabeledExprListener(ParseTreeListener):

    # Enter a parse tree produced by LabeledExprParser#prog.
    def enterProg(self, ctx:LabeledExprParser.ProgContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#prog.
    def exitProg(self, ctx:LabeledExprParser.ProgContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#printExpr.
    def enterPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#printExpr.
    def exitPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#assign.
    def enterAssign(self, ctx:LabeledExprParser.AssignContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#assign.
    def exitAssign(self, ctx:LabeledExprParser.AssignContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#blank.
    def enterBlank(self, ctx:LabeledExprParser.BlankContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#blank.
    def exitBlank(self, ctx:LabeledExprParser.BlankContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#parens.
    def enterParens(self, ctx:LabeledExprParser.ParensContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#parens.
    def exitParens(self, ctx:LabeledExprParser.ParensContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#Abs.
    def enterAbs(self, ctx:LabeledExprParser.AbsContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#Abs.
    def exitAbs(self, ctx:LabeledExprParser.AbsContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#MulDiv.
    def enterMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#MulDiv.
    def exitMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#AddSub.
    def enterAddSub(self, ctx:LabeledExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#AddSub.
    def exitAddSub(self, ctx:LabeledExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#TrigFunction.
    def enterTrigFunction(self, ctx:LabeledExprParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#TrigFunction.
    def exitTrigFunction(self, ctx:LabeledExprParser.TrigFunctionContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#hex.
    def enterHex(self, ctx:LabeledExprParser.HexContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#hex.
    def exitHex(self, ctx:LabeledExprParser.HexContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#id.
    def enterId(self, ctx:LabeledExprParser.IdContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#id.
    def exitId(self, ctx:LabeledExprParser.IdContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#int.
    def enterInt(self, ctx:LabeledExprParser.IntContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#int.
    def exitInt(self, ctx:LabeledExprParser.IntContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#CosFunc.
    def enterCosFunc(self, ctx:LabeledExprParser.CosFuncContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#CosFunc.
    def exitCosFunc(self, ctx:LabeledExprParser.CosFuncContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#SenFunc.
    def enterSenFunc(self, ctx:LabeledExprParser.SenFuncContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#SenFunc.
    def exitSenFunc(self, ctx:LabeledExprParser.SenFuncContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#TanFunc.
    def enterTanFunc(self, ctx:LabeledExprParser.TanFuncContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#TanFunc.
    def exitTanFunc(self, ctx:LabeledExprParser.TanFuncContext):
        pass


