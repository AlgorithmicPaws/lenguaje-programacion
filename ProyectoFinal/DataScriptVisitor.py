# Generated from DataScript.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DataScriptParser import DataScriptParser
else:
    from DataScriptParser import DataScriptParser

# This class defines a complete generic visitor for a parse tree produced by DataScriptParser.

class DataScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DataScriptParser#prog.
    def visitProg(self, ctx:DataScriptParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#expression.
    def visitExpression(self, ctx:DataScriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#statement.
    def visitStatement(self, ctx:DataScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#show.
    def visitShow(self, ctx:DataScriptParser.ShowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#control.
    def visitControl(self, ctx:DataScriptParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#function.
    def visitFunction(self, ctx:DataScriptParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#fileOp.
    def visitFileOp(self, ctx:DataScriptParser.FileOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#blank.
    def visitBlank(self, ctx:DataScriptParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#assign.
    def visitAssign(self, ctx:DataScriptParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#functionStatement.
    def visitFunctionStatement(self, ctx:DataScriptParser.FunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#parametros.
    def visitParametros(self, ctx:DataScriptParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#args.
    def visitArgs(self, ctx:DataScriptParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#structureControl.
    def visitStructureControl(self, ctx:DataScriptParser.StructureControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#if.
    def visitIf(self, ctx:DataScriptParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#ifElse.
    def visitIfElse(self, ctx:DataScriptParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#while.
    def visitWhile(self, ctx:DataScriptParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#for.
    def visitFor(self, ctx:DataScriptParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#read.
    def visitRead(self, ctx:DataScriptParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#printExpr.
    def visitPrintExpr(self, ctx:DataScriptParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#graph.
    def visitGraph(self, ctx:DataScriptParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#graphType.
    def visitGraphType(self, ctx:DataScriptParser.GraphTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#graphParams.
    def visitGraphParams(self, ctx:DataScriptParser.GraphParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#openFile.
    def visitOpenFile(self, ctx:DataScriptParser.OpenFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#closeFile.
    def visitCloseFile(self, ctx:DataScriptParser.CloseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#writeFile.
    def visitWriteFile(self, ctx:DataScriptParser.WriteFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#deleteFile.
    def visitDeleteFile(self, ctx:DataScriptParser.DeleteFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#readingFile.
    def visitReadingFile(self, ctx:DataScriptParser.ReadingFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#readLine.
    def visitReadLine(self, ctx:DataScriptParser.ReadLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#readAll.
    def visitReadAll(self, ctx:DataScriptParser.ReadAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#Logic.
    def visitLogic(self, ctx:DataScriptParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#Aritmetic.
    def visitAritmetic(self, ctx:DataScriptParser.AritmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#return.
    def visitReturn(self, ctx:DataScriptParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#idL.
    def visitIdL(self, ctx:DataScriptParser.IdLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#andOr.
    def visitAndOr(self, ctx:DataScriptParser.AndOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#negation.
    def visitNegation(self, ctx:DataScriptParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#minor.
    def visitMinor(self, ctx:DataScriptParser.MinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#bool.
    def visitBool(self, ctx:DataScriptParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#parensL.
    def visitParensL(self, ctx:DataScriptParser.ParensLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#equals.
    def visitEquals(self, ctx:DataScriptParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#equalsL.
    def visitEqualsL(self, ctx:DataScriptParser.EqualsLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#greater.
    def visitGreater(self, ctx:DataScriptParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#parens.
    def visitParens(self, ctx:DataScriptParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#arrayAssign.
    def visitArrayAssign(self, ctx:DataScriptParser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dot.
    def visitDot(self, ctx:DataScriptParser.DotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#float.
    def visitFloat(self, ctx:DataScriptParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#mulDiv.
    def visitMulDiv(self, ctx:DataScriptParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listAssign.
    def visitListAssign(self, ctx:DataScriptParser.ListAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#negative.
    def visitNegative(self, ctx:DataScriptParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#split.
    def visitSplit(self, ctx:DataScriptParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#root.
    def visitRoot(self, ctx:DataScriptParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#hex.
    def visitHex(self, ctx:DataScriptParser.HexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#id.
    def visitId(self, ctx:DataScriptParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dictAssign.
    def visitDictAssign(self, ctx:DataScriptParser.DictAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#power.
    def visitPower(self, ctx:DataScriptParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#comp.
    def visitComp(self, ctx:DataScriptParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#modDivent.
    def visitModDivent(self, ctx:DataScriptParser.ModDiventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#cross.
    def visitCross(self, ctx:DataScriptParser.CrossContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#castInt.
    def visitCastInt(self, ctx:DataScriptParser.CastIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#addSub.
    def visitAddSub(self, ctx:DataScriptParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#reverse.
    def visitReverse(self, ctx:DataScriptParser.ReverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#int.
    def visitInt(self, ctx:DataScriptParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#str.
    def visitStr(self, ctx:DataScriptParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#abs.
    def visitAbs(self, ctx:DataScriptParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#functionCall.
    def visitFunctionCall(self, ctx:DataScriptParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dfAssign.
    def visitDfAssign(self, ctx:DataScriptParser.DfAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#transpose.
    def visitTranspose(self, ctx:DataScriptParser.TransposeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#trigFunction.
    def visitTrigFunction(self, ctx:DataScriptParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#rooti.
    def visitRooti(self, ctx:DataScriptParser.RootiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#lists.
    def visitLists(self, ctx:DataScriptParser.ListsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listAppend.
    def visitListAppend(self, ctx:DataScriptParser.ListAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listElement.
    def visitListElement(self, ctx:DataScriptParser.ListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listElementassign.
    def visitListElementassign(self, ctx:DataScriptParser.ListElementassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listIndex.
    def visitListIndex(self, ctx:DataScriptParser.ListIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listLen.
    def visitListLen(self, ctx:DataScriptParser.ListLenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listRemove.
    def visitListRemove(self, ctx:DataScriptParser.ListRemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listClear.
    def visitListClear(self, ctx:DataScriptParser.ListClearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#listId.
    def visitListId(self, ctx:DataScriptParser.ListIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dicts.
    def visitDicts(self, ctx:DataScriptParser.DictsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dictElement.
    def visitDictElement(self, ctx:DataScriptParser.DictElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dictElementassign.
    def visitDictElementassign(self, ctx:DataScriptParser.DictElementassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dictKeys.
    def visitDictKeys(self, ctx:DataScriptParser.DictKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dictValues.
    def visitDictValues(self, ctx:DataScriptParser.DictValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dictUpdate.
    def visitDictUpdate(self, ctx:DataScriptParser.DictUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dictItem.
    def visitDictItem(self, ctx:DataScriptParser.DictItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#arrays.
    def visitArrays(self, ctx:DataScriptParser.ArraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#arrayElement.
    def visitArrayElement(self, ctx:DataScriptParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#createDataFrame.
    def visitCreateDataFrame(self, ctx:DataScriptParser.CreateDataFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#loadCSV.
    def visitLoadCSV(self, ctx:DataScriptParser.LoadCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#saveCSV.
    def visitSaveCSV(self, ctx:DataScriptParser.SaveCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#columnDataFrame.
    def visitColumnDataFrame(self, ctx:DataScriptParser.ColumnDataFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#selectRow.
    def visitSelectRow(self, ctx:DataScriptParser.SelectRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#filterRows.
    def visitFilterRows(self, ctx:DataScriptParser.FilterRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#addColumn.
    def visitAddColumn(self, ctx:DataScriptParser.AddColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#dropColumn.
    def visitDropColumn(self, ctx:DataScriptParser.DropColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#describeDataFrame.
    def visitDescribeDataFrame(self, ctx:DataScriptParser.DescribeDataFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#headDataFrame.
    def visitHeadDataFrame(self, ctx:DataScriptParser.HeadDataFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#mergeDataFrames.
    def visitMergeDataFrames(self, ctx:DataScriptParser.MergeDataFramesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#selectColumn.
    def visitSelectColumn(self, ctx:DataScriptParser.SelectColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#equalsF.
    def visitEqualsF(self, ctx:DataScriptParser.EqualsFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#minorF.
    def visitMinorF(self, ctx:DataScriptParser.MinorFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#greaterF.
    def visitGreaterF(self, ctx:DataScriptParser.GreaterFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#parensF.
    def visitParensF(self, ctx:DataScriptParser.ParensFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#andOrF.
    def visitAndOrF(self, ctx:DataScriptParser.AndOrFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#complejo.
    def visitComplejo(self, ctx:DataScriptParser.ComplejoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#img.
    def visitImg(self, ctx:DataScriptParser.ImgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#CosFunc.
    def visitCosFunc(self, ctx:DataScriptParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#SenFunc.
    def visitSenFunc(self, ctx:DataScriptParser.SenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataScriptParser#TanFunc.
    def visitTanFunc(self, ctx:DataScriptParser.TanFuncContext):
        return self.visitChildren(ctx)



del DataScriptParser