# Generated from LabeledExpr.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LabeledExprParser import LabeledExprParser
else:
    from LabeledExprParser import LabeledExprParser

# This class defines a complete generic visitor for a parse tree produced by LabeledExprParser.

class LabeledExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LabeledExprParser#prog.
    def visitProg(self, ctx:LabeledExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#printExpr.
    def visitPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#assign.
    def visitAssign(self, ctx:LabeledExprParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#blank.
    def visitBlank(self, ctx:LabeledExprParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#parens.
    def visitParens(self, ctx:LabeledExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#Abs.
    def visitAbs(self, ctx:LabeledExprParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#MulDiv.
    def visitMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#AddSub.
    def visitAddSub(self, ctx:LabeledExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#TrigFunction.
    def visitTrigFunction(self, ctx:LabeledExprParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#hex.
    def visitHex(self, ctx:LabeledExprParser.HexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#id.
    def visitId(self, ctx:LabeledExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#int.
    def visitInt(self, ctx:LabeledExprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#CosFunc.
    def visitCosFunc(self, ctx:LabeledExprParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#SenFunc.
    def visitSenFunc(self, ctx:LabeledExprParser.SenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#TanFunc.
    def visitTanFunc(self, ctx:LabeledExprParser.TanFuncContext):
        return self.visitChildren(ctx)



del LabeledExprParser