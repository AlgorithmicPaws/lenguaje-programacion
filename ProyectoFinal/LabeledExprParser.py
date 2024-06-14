# Generated from LabeledExpr.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("(\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4\63\13")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5;\n\5\3\5\2\3\6\6\2\4\6")
        buf.write("\b\2\4\3\2\t\n\3\2\13\f\2D\2\13\3\2\2\2\4\30\3\2\2\2\6")
        buf.write("\'\3\2\2\2\b:\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2")
        buf.write("\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\20\5\6")
        buf.write("\4\2\20\21\7\21\2\2\21\31\3\2\2\2\22\23\7\16\2\2\23\24")
        buf.write("\7\3\2\2\24\25\5\6\4\2\25\26\7\21\2\2\26\31\3\2\2\2\27")
        buf.write("\31\7\21\2\2\30\17\3\2\2\2\30\22\3\2\2\2\30\27\3\2\2\2")
        buf.write("\31\5\3\2\2\2\32\33\b\4\1\2\33(\5\b\5\2\34\35\7\4\2\2")
        buf.write("\35\36\5\6\4\2\36\37\7\4\2\2\37(\3\2\2\2 (\7\17\2\2!(")
        buf.write("\7\16\2\2\"(\7\20\2\2#$\7\5\2\2$%\5\6\4\2%&\7\6\2\2&(")
        buf.write("\3\2\2\2\'\32\3\2\2\2\'\34\3\2\2\2\' \3\2\2\2\'!\3\2\2")
        buf.write("\2\'\"\3\2\2\2\'#\3\2\2\2(\61\3\2\2\2)*\f\n\2\2*+\t\2")
        buf.write("\2\2+\60\5\6\4\13,-\f\t\2\2-.\t\3\2\2.\60\5\6\4\n/)\3")
        buf.write("\2\2\2/,\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2")
        buf.write("\2\62\7\3\2\2\2\63\61\3\2\2\2\64\65\7\7\2\2\65;\5\6\4")
        buf.write("\2\66\67\7\b\2\2\67;\5\6\4\289\7\r\2\29;\5\6\4\2:\64\3")
        buf.write("\2\2\2:\66\3\2\2\2:8\3\2\2\2;\t\3\2\2\2\b\r\30\'/\61:")
        return buf.getvalue()


class LabeledExprParser ( Parser ):

    grammarFileName = "LabeledExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'|'", "'('", "')'", "'cos'", "'sen'", 
                     "'*'", "'/'", "'+'", "'-'", "'tan'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "TAN", "ID", "INT", "HEX", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_trigFunc = 3

    ruleNames =  [ "prog", "stat", "expr", "trigFunc" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    MUL=7
    DIV=8
    ADD=9
    SUB=10
    TAN=11
    ID=12
    INT=13
    HEX=14
    NEWLINE=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.StatContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.StatContext,i)


        def getRuleIndex(self):
            return LabeledExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = LabeledExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LabeledExprParser.T__1) | (1 << LabeledExprParser.T__2) | (1 << LabeledExprParser.T__4) | (1 << LabeledExprParser.T__5) | (1 << LabeledExprParser.TAN) | (1 << LabeledExprParser.ID) | (1 << LabeledExprParser.INT) | (1 << LabeledExprParser.HEX) | (1 << LabeledExprParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(LabeledExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(LabeledExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(LabeledExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = LabeledExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = LabeledExprParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(LabeledExprParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = LabeledExprParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(LabeledExprParser.ID)
                self.state = 17
                self.match(LabeledExprParser.T__0)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(LabeledExprParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = LabeledExprParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(LabeledExprParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class AbsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs" ):
                listener.enterAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs" ):
                listener.exitAbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs" ):
                return visitor.visitAbs(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class TrigFunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def trigFunc(self):
            return self.getTypedRuleContext(LabeledExprParser.TrigFuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigFunction" ):
                listener.enterTrigFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigFunction" ):
                listener.exitTrigFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigFunction" ):
                return visitor.visitTrigFunction(self)
            else:
                return visitor.visitChildren(self)


    class HexContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEX(self):
            return self.getToken(LabeledExprParser.HEX, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHex" ):
                listener.enterHex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHex" ):
                listener.exitHex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHex" ):
                return visitor.visitHex(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LabeledExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LabeledExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LabeledExprParser.T__4, LabeledExprParser.T__5, LabeledExprParser.TAN]:
                localctx = LabeledExprParser.TrigFunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.trigFunc()
                pass
            elif token in [LabeledExprParser.T__1]:
                localctx = LabeledExprParser.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(LabeledExprParser.T__1)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(LabeledExprParser.T__1)
                pass
            elif token in [LabeledExprParser.INT]:
                localctx = LabeledExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(LabeledExprParser.INT)
                pass
            elif token in [LabeledExprParser.ID]:
                localctx = LabeledExprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(LabeledExprParser.ID)
                pass
            elif token in [LabeledExprParser.HEX]:
                localctx = LabeledExprParser.HexContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(LabeledExprParser.HEX)
                pass
            elif token in [LabeledExprParser.T__2]:
                localctx = LabeledExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(LabeledExprParser.T__2)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(LabeledExprParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LabeledExprParser.MulDivContext(self, LabeledExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 40
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExprParser.MUL or _la==LabeledExprParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 41
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LabeledExprParser.AddSubContext(self, LabeledExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 43
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExprParser.ADD or _la==LabeledExprParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        self.expr(8)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TrigFuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_trigFunc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TanFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanFunc" ):
                listener.enterTanFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanFunc" ):
                listener.exitTanFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanFunc" ):
                return visitor.visitTanFunc(self)
            else:
                return visitor.visitChildren(self)


    class CosFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosFunc" ):
                listener.enterCosFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosFunc" ):
                listener.exitCosFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosFunc" ):
                return visitor.visitCosFunc(self)
            else:
                return visitor.visitChildren(self)


    class SenFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSenFunc" ):
                listener.enterSenFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSenFunc" ):
                listener.exitSenFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSenFunc" ):
                return visitor.visitSenFunc(self)
            else:
                return visitor.visitChildren(self)



    def trigFunc(self):

        localctx = LabeledExprParser.TrigFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_trigFunc)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LabeledExprParser.T__4]:
                localctx = LabeledExprParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(LabeledExprParser.T__4)
                self.state = 51
                self.expr(0)
                pass
            elif token in [LabeledExprParser.T__5]:
                localctx = LabeledExprParser.SenFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(LabeledExprParser.T__5)
                self.state = 53
                self.expr(0)
                pass
            elif token in [LabeledExprParser.TAN]:
                localctx = LabeledExprParser.TanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(LabeledExprParser.TAN)
                self.state = 55
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




