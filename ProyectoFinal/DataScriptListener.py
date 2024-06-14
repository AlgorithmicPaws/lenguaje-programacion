# Generated from DataScript.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DataScriptParser import DataScriptParser
else:
    from DataScriptParser import DataScriptParser

# This class defines a complete listener for a parse tree produced by DataScriptParser.
class DataScriptListener(ParseTreeListener):

    # Enter a parse tree produced by DataScriptParser#prog.
    def enterProg(self, ctx:DataScriptParser.ProgContext):
        pass

    # Exit a parse tree produced by DataScriptParser#prog.
    def exitProg(self, ctx:DataScriptParser.ProgContext):
        pass


    # Enter a parse tree produced by DataScriptParser#expression.
    def enterExpression(self, ctx:DataScriptParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DataScriptParser#expression.
    def exitExpression(self, ctx:DataScriptParser.ExpressionContext):
        pass


    # Enter a parse tree produced by DataScriptParser#statement.
    def enterStatement(self, ctx:DataScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#statement.
    def exitStatement(self, ctx:DataScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#show.
    def enterShow(self, ctx:DataScriptParser.ShowContext):
        pass

    # Exit a parse tree produced by DataScriptParser#show.
    def exitShow(self, ctx:DataScriptParser.ShowContext):
        pass


    # Enter a parse tree produced by DataScriptParser#control.
    def enterControl(self, ctx:DataScriptParser.ControlContext):
        pass

    # Exit a parse tree produced by DataScriptParser#control.
    def exitControl(self, ctx:DataScriptParser.ControlContext):
        pass


    # Enter a parse tree produced by DataScriptParser#function.
    def enterFunction(self, ctx:DataScriptParser.FunctionContext):
        pass

    # Exit a parse tree produced by DataScriptParser#function.
    def exitFunction(self, ctx:DataScriptParser.FunctionContext):
        pass


    # Enter a parse tree produced by DataScriptParser#fileOp.
    def enterFileOp(self, ctx:DataScriptParser.FileOpContext):
        pass

    # Exit a parse tree produced by DataScriptParser#fileOp.
    def exitFileOp(self, ctx:DataScriptParser.FileOpContext):
        pass


    # Enter a parse tree produced by DataScriptParser#blank.
    def enterBlank(self, ctx:DataScriptParser.BlankContext):
        pass

    # Exit a parse tree produced by DataScriptParser#blank.
    def exitBlank(self, ctx:DataScriptParser.BlankContext):
        pass


    # Enter a parse tree produced by DataScriptParser#assign.
    def enterAssign(self, ctx:DataScriptParser.AssignContext):
        pass

    # Exit a parse tree produced by DataScriptParser#assign.
    def exitAssign(self, ctx:DataScriptParser.AssignContext):
        pass


    # Enter a parse tree produced by DataScriptParser#functionStatement.
    def enterFunctionStatement(self, ctx:DataScriptParser.FunctionStatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#functionStatement.
    def exitFunctionStatement(self, ctx:DataScriptParser.FunctionStatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#parametros.
    def enterParametros(self, ctx:DataScriptParser.ParametrosContext):
        pass

    # Exit a parse tree produced by DataScriptParser#parametros.
    def exitParametros(self, ctx:DataScriptParser.ParametrosContext):
        pass


    # Enter a parse tree produced by DataScriptParser#args.
    def enterArgs(self, ctx:DataScriptParser.ArgsContext):
        pass

    # Exit a parse tree produced by DataScriptParser#args.
    def exitArgs(self, ctx:DataScriptParser.ArgsContext):
        pass


    # Enter a parse tree produced by DataScriptParser#structureControl.
    def enterStructureControl(self, ctx:DataScriptParser.StructureControlContext):
        pass

    # Exit a parse tree produced by DataScriptParser#structureControl.
    def exitStructureControl(self, ctx:DataScriptParser.StructureControlContext):
        pass


    # Enter a parse tree produced by DataScriptParser#if.
    def enterIf(self, ctx:DataScriptParser.IfContext):
        pass

    # Exit a parse tree produced by DataScriptParser#if.
    def exitIf(self, ctx:DataScriptParser.IfContext):
        pass


    # Enter a parse tree produced by DataScriptParser#ifElse.
    def enterIfElse(self, ctx:DataScriptParser.IfElseContext):
        pass

    # Exit a parse tree produced by DataScriptParser#ifElse.
    def exitIfElse(self, ctx:DataScriptParser.IfElseContext):
        pass


    # Enter a parse tree produced by DataScriptParser#while.
    def enterWhile(self, ctx:DataScriptParser.WhileContext):
        pass

    # Exit a parse tree produced by DataScriptParser#while.
    def exitWhile(self, ctx:DataScriptParser.WhileContext):
        pass


    # Enter a parse tree produced by DataScriptParser#for.
    def enterFor(self, ctx:DataScriptParser.ForContext):
        pass

    # Exit a parse tree produced by DataScriptParser#for.
    def exitFor(self, ctx:DataScriptParser.ForContext):
        pass


    # Enter a parse tree produced by DataScriptParser#read.
    def enterRead(self, ctx:DataScriptParser.ReadContext):
        pass

    # Exit a parse tree produced by DataScriptParser#read.
    def exitRead(self, ctx:DataScriptParser.ReadContext):
        pass


    # Enter a parse tree produced by DataScriptParser#printExpr.
    def enterPrintExpr(self, ctx:DataScriptParser.PrintExprContext):
        pass

    # Exit a parse tree produced by DataScriptParser#printExpr.
    def exitPrintExpr(self, ctx:DataScriptParser.PrintExprContext):
        pass


    # Enter a parse tree produced by DataScriptParser#graph.
    def enterGraph(self, ctx:DataScriptParser.GraphContext):
        pass

    # Exit a parse tree produced by DataScriptParser#graph.
    def exitGraph(self, ctx:DataScriptParser.GraphContext):
        pass


    # Enter a parse tree produced by DataScriptParser#graphType.
    def enterGraphType(self, ctx:DataScriptParser.GraphTypeContext):
        pass

    # Exit a parse tree produced by DataScriptParser#graphType.
    def exitGraphType(self, ctx:DataScriptParser.GraphTypeContext):
        pass


    # Enter a parse tree produced by DataScriptParser#graphParams.
    def enterGraphParams(self, ctx:DataScriptParser.GraphParamsContext):
        pass

    # Exit a parse tree produced by DataScriptParser#graphParams.
    def exitGraphParams(self, ctx:DataScriptParser.GraphParamsContext):
        pass


    # Enter a parse tree produced by DataScriptParser#openFile.
    def enterOpenFile(self, ctx:DataScriptParser.OpenFileContext):
        pass

    # Exit a parse tree produced by DataScriptParser#openFile.
    def exitOpenFile(self, ctx:DataScriptParser.OpenFileContext):
        pass


    # Enter a parse tree produced by DataScriptParser#closeFile.
    def enterCloseFile(self, ctx:DataScriptParser.CloseFileContext):
        pass

    # Exit a parse tree produced by DataScriptParser#closeFile.
    def exitCloseFile(self, ctx:DataScriptParser.CloseFileContext):
        pass


    # Enter a parse tree produced by DataScriptParser#writeFile.
    def enterWriteFile(self, ctx:DataScriptParser.WriteFileContext):
        pass

    # Exit a parse tree produced by DataScriptParser#writeFile.
    def exitWriteFile(self, ctx:DataScriptParser.WriteFileContext):
        pass


    # Enter a parse tree produced by DataScriptParser#deleteFile.
    def enterDeleteFile(self, ctx:DataScriptParser.DeleteFileContext):
        pass

    # Exit a parse tree produced by DataScriptParser#deleteFile.
    def exitDeleteFile(self, ctx:DataScriptParser.DeleteFileContext):
        pass


    # Enter a parse tree produced by DataScriptParser#readingFile.
    def enterReadingFile(self, ctx:DataScriptParser.ReadingFileContext):
        pass

    # Exit a parse tree produced by DataScriptParser#readingFile.
    def exitReadingFile(self, ctx:DataScriptParser.ReadingFileContext):
        pass


    # Enter a parse tree produced by DataScriptParser#readLine.
    def enterReadLine(self, ctx:DataScriptParser.ReadLineContext):
        pass

    # Exit a parse tree produced by DataScriptParser#readLine.
    def exitReadLine(self, ctx:DataScriptParser.ReadLineContext):
        pass


    # Enter a parse tree produced by DataScriptParser#readAll.
    def enterReadAll(self, ctx:DataScriptParser.ReadAllContext):
        pass

    # Exit a parse tree produced by DataScriptParser#readAll.
    def exitReadAll(self, ctx:DataScriptParser.ReadAllContext):
        pass


    # Enter a parse tree produced by DataScriptParser#Logic.
    def enterLogic(self, ctx:DataScriptParser.LogicContext):
        pass

    # Exit a parse tree produced by DataScriptParser#Logic.
    def exitLogic(self, ctx:DataScriptParser.LogicContext):
        pass


    # Enter a parse tree produced by DataScriptParser#Aritmetic.
    def enterAritmetic(self, ctx:DataScriptParser.AritmeticContext):
        pass

    # Exit a parse tree produced by DataScriptParser#Aritmetic.
    def exitAritmetic(self, ctx:DataScriptParser.AritmeticContext):
        pass


    # Enter a parse tree produced by DataScriptParser#return.
    def enterReturn(self, ctx:DataScriptParser.ReturnContext):
        pass

    # Exit a parse tree produced by DataScriptParser#return.
    def exitReturn(self, ctx:DataScriptParser.ReturnContext):
        pass


    # Enter a parse tree produced by DataScriptParser#idL.
    def enterIdL(self, ctx:DataScriptParser.IdLContext):
        pass

    # Exit a parse tree produced by DataScriptParser#idL.
    def exitIdL(self, ctx:DataScriptParser.IdLContext):
        pass


    # Enter a parse tree produced by DataScriptParser#andOr.
    def enterAndOr(self, ctx:DataScriptParser.AndOrContext):
        pass

    # Exit a parse tree produced by DataScriptParser#andOr.
    def exitAndOr(self, ctx:DataScriptParser.AndOrContext):
        pass


    # Enter a parse tree produced by DataScriptParser#negation.
    def enterNegation(self, ctx:DataScriptParser.NegationContext):
        pass

    # Exit a parse tree produced by DataScriptParser#negation.
    def exitNegation(self, ctx:DataScriptParser.NegationContext):
        pass


    # Enter a parse tree produced by DataScriptParser#minor.
    def enterMinor(self, ctx:DataScriptParser.MinorContext):
        pass

    # Exit a parse tree produced by DataScriptParser#minor.
    def exitMinor(self, ctx:DataScriptParser.MinorContext):
        pass


    # Enter a parse tree produced by DataScriptParser#bool.
    def enterBool(self, ctx:DataScriptParser.BoolContext):
        pass

    # Exit a parse tree produced by DataScriptParser#bool.
    def exitBool(self, ctx:DataScriptParser.BoolContext):
        pass


    # Enter a parse tree produced by DataScriptParser#parensL.
    def enterParensL(self, ctx:DataScriptParser.ParensLContext):
        pass

    # Exit a parse tree produced by DataScriptParser#parensL.
    def exitParensL(self, ctx:DataScriptParser.ParensLContext):
        pass


    # Enter a parse tree produced by DataScriptParser#equals.
    def enterEquals(self, ctx:DataScriptParser.EqualsContext):
        pass

    # Exit a parse tree produced by DataScriptParser#equals.
    def exitEquals(self, ctx:DataScriptParser.EqualsContext):
        pass


    # Enter a parse tree produced by DataScriptParser#equalsL.
    def enterEqualsL(self, ctx:DataScriptParser.EqualsLContext):
        pass

    # Exit a parse tree produced by DataScriptParser#equalsL.
    def exitEqualsL(self, ctx:DataScriptParser.EqualsLContext):
        pass


    # Enter a parse tree produced by DataScriptParser#greater.
    def enterGreater(self, ctx:DataScriptParser.GreaterContext):
        pass

    # Exit a parse tree produced by DataScriptParser#greater.
    def exitGreater(self, ctx:DataScriptParser.GreaterContext):
        pass


    # Enter a parse tree produced by DataScriptParser#parens.
    def enterParens(self, ctx:DataScriptParser.ParensContext):
        pass

    # Exit a parse tree produced by DataScriptParser#parens.
    def exitParens(self, ctx:DataScriptParser.ParensContext):
        pass


    # Enter a parse tree produced by DataScriptParser#arrayAssign.
    def enterArrayAssign(self, ctx:DataScriptParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by DataScriptParser#arrayAssign.
    def exitArrayAssign(self, ctx:DataScriptParser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dot.
    def enterDot(self, ctx:DataScriptParser.DotContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dot.
    def exitDot(self, ctx:DataScriptParser.DotContext):
        pass


    # Enter a parse tree produced by DataScriptParser#float.
    def enterFloat(self, ctx:DataScriptParser.FloatContext):
        pass

    # Exit a parse tree produced by DataScriptParser#float.
    def exitFloat(self, ctx:DataScriptParser.FloatContext):
        pass


    # Enter a parse tree produced by DataScriptParser#mulDiv.
    def enterMulDiv(self, ctx:DataScriptParser.MulDivContext):
        pass

    # Exit a parse tree produced by DataScriptParser#mulDiv.
    def exitMulDiv(self, ctx:DataScriptParser.MulDivContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listAssign.
    def enterListAssign(self, ctx:DataScriptParser.ListAssignContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listAssign.
    def exitListAssign(self, ctx:DataScriptParser.ListAssignContext):
        pass


    # Enter a parse tree produced by DataScriptParser#negative.
    def enterNegative(self, ctx:DataScriptParser.NegativeContext):
        pass

    # Exit a parse tree produced by DataScriptParser#negative.
    def exitNegative(self, ctx:DataScriptParser.NegativeContext):
        pass


    # Enter a parse tree produced by DataScriptParser#split.
    def enterSplit(self, ctx:DataScriptParser.SplitContext):
        pass

    # Exit a parse tree produced by DataScriptParser#split.
    def exitSplit(self, ctx:DataScriptParser.SplitContext):
        pass


    # Enter a parse tree produced by DataScriptParser#root.
    def enterRoot(self, ctx:DataScriptParser.RootContext):
        pass

    # Exit a parse tree produced by DataScriptParser#root.
    def exitRoot(self, ctx:DataScriptParser.RootContext):
        pass


    # Enter a parse tree produced by DataScriptParser#hex.
    def enterHex(self, ctx:DataScriptParser.HexContext):
        pass

    # Exit a parse tree produced by DataScriptParser#hex.
    def exitHex(self, ctx:DataScriptParser.HexContext):
        pass


    # Enter a parse tree produced by DataScriptParser#id.
    def enterId(self, ctx:DataScriptParser.IdContext):
        pass

    # Exit a parse tree produced by DataScriptParser#id.
    def exitId(self, ctx:DataScriptParser.IdContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dictAssign.
    def enterDictAssign(self, ctx:DataScriptParser.DictAssignContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dictAssign.
    def exitDictAssign(self, ctx:DataScriptParser.DictAssignContext):
        pass


    # Enter a parse tree produced by DataScriptParser#power.
    def enterPower(self, ctx:DataScriptParser.PowerContext):
        pass

    # Exit a parse tree produced by DataScriptParser#power.
    def exitPower(self, ctx:DataScriptParser.PowerContext):
        pass


    # Enter a parse tree produced by DataScriptParser#comp.
    def enterComp(self, ctx:DataScriptParser.CompContext):
        pass

    # Exit a parse tree produced by DataScriptParser#comp.
    def exitComp(self, ctx:DataScriptParser.CompContext):
        pass


    # Enter a parse tree produced by DataScriptParser#modDivent.
    def enterModDivent(self, ctx:DataScriptParser.ModDiventContext):
        pass

    # Exit a parse tree produced by DataScriptParser#modDivent.
    def exitModDivent(self, ctx:DataScriptParser.ModDiventContext):
        pass


    # Enter a parse tree produced by DataScriptParser#cross.
    def enterCross(self, ctx:DataScriptParser.CrossContext):
        pass

    # Exit a parse tree produced by DataScriptParser#cross.
    def exitCross(self, ctx:DataScriptParser.CrossContext):
        pass


    # Enter a parse tree produced by DataScriptParser#castInt.
    def enterCastInt(self, ctx:DataScriptParser.CastIntContext):
        pass

    # Exit a parse tree produced by DataScriptParser#castInt.
    def exitCastInt(self, ctx:DataScriptParser.CastIntContext):
        pass


    # Enter a parse tree produced by DataScriptParser#addSub.
    def enterAddSub(self, ctx:DataScriptParser.AddSubContext):
        pass

    # Exit a parse tree produced by DataScriptParser#addSub.
    def exitAddSub(self, ctx:DataScriptParser.AddSubContext):
        pass


    # Enter a parse tree produced by DataScriptParser#reverse.
    def enterReverse(self, ctx:DataScriptParser.ReverseContext):
        pass

    # Exit a parse tree produced by DataScriptParser#reverse.
    def exitReverse(self, ctx:DataScriptParser.ReverseContext):
        pass


    # Enter a parse tree produced by DataScriptParser#int.
    def enterInt(self, ctx:DataScriptParser.IntContext):
        pass

    # Exit a parse tree produced by DataScriptParser#int.
    def exitInt(self, ctx:DataScriptParser.IntContext):
        pass


    # Enter a parse tree produced by DataScriptParser#str.
    def enterStr(self, ctx:DataScriptParser.StrContext):
        pass

    # Exit a parse tree produced by DataScriptParser#str.
    def exitStr(self, ctx:DataScriptParser.StrContext):
        pass


    # Enter a parse tree produced by DataScriptParser#abs.
    def enterAbs(self, ctx:DataScriptParser.AbsContext):
        pass

    # Exit a parse tree produced by DataScriptParser#abs.
    def exitAbs(self, ctx:DataScriptParser.AbsContext):
        pass


    # Enter a parse tree produced by DataScriptParser#functionCall.
    def enterFunctionCall(self, ctx:DataScriptParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by DataScriptParser#functionCall.
    def exitFunctionCall(self, ctx:DataScriptParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dfAssign.
    def enterDfAssign(self, ctx:DataScriptParser.DfAssignContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dfAssign.
    def exitDfAssign(self, ctx:DataScriptParser.DfAssignContext):
        pass


    # Enter a parse tree produced by DataScriptParser#transpose.
    def enterTranspose(self, ctx:DataScriptParser.TransposeContext):
        pass

    # Exit a parse tree produced by DataScriptParser#transpose.
    def exitTranspose(self, ctx:DataScriptParser.TransposeContext):
        pass


    # Enter a parse tree produced by DataScriptParser#trigFunction.
    def enterTrigFunction(self, ctx:DataScriptParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by DataScriptParser#trigFunction.
    def exitTrigFunction(self, ctx:DataScriptParser.TrigFunctionContext):
        pass


    # Enter a parse tree produced by DataScriptParser#rooti.
    def enterRooti(self, ctx:DataScriptParser.RootiContext):
        pass

    # Exit a parse tree produced by DataScriptParser#rooti.
    def exitRooti(self, ctx:DataScriptParser.RootiContext):
        pass


    # Enter a parse tree produced by DataScriptParser#lists.
    def enterLists(self, ctx:DataScriptParser.ListsContext):
        pass

    # Exit a parse tree produced by DataScriptParser#lists.
    def exitLists(self, ctx:DataScriptParser.ListsContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listAppend.
    def enterListAppend(self, ctx:DataScriptParser.ListAppendContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listAppend.
    def exitListAppend(self, ctx:DataScriptParser.ListAppendContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listElement.
    def enterListElement(self, ctx:DataScriptParser.ListElementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listElement.
    def exitListElement(self, ctx:DataScriptParser.ListElementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listElementassign.
    def enterListElementassign(self, ctx:DataScriptParser.ListElementassignContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listElementassign.
    def exitListElementassign(self, ctx:DataScriptParser.ListElementassignContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listIndex.
    def enterListIndex(self, ctx:DataScriptParser.ListIndexContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listIndex.
    def exitListIndex(self, ctx:DataScriptParser.ListIndexContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listLen.
    def enterListLen(self, ctx:DataScriptParser.ListLenContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listLen.
    def exitListLen(self, ctx:DataScriptParser.ListLenContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listRemove.
    def enterListRemove(self, ctx:DataScriptParser.ListRemoveContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listRemove.
    def exitListRemove(self, ctx:DataScriptParser.ListRemoveContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listClear.
    def enterListClear(self, ctx:DataScriptParser.ListClearContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listClear.
    def exitListClear(self, ctx:DataScriptParser.ListClearContext):
        pass


    # Enter a parse tree produced by DataScriptParser#listId.
    def enterListId(self, ctx:DataScriptParser.ListIdContext):
        pass

    # Exit a parse tree produced by DataScriptParser#listId.
    def exitListId(self, ctx:DataScriptParser.ListIdContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dicts.
    def enterDicts(self, ctx:DataScriptParser.DictsContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dicts.
    def exitDicts(self, ctx:DataScriptParser.DictsContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dictElement.
    def enterDictElement(self, ctx:DataScriptParser.DictElementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dictElement.
    def exitDictElement(self, ctx:DataScriptParser.DictElementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dictElementassign.
    def enterDictElementassign(self, ctx:DataScriptParser.DictElementassignContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dictElementassign.
    def exitDictElementassign(self, ctx:DataScriptParser.DictElementassignContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dictKeys.
    def enterDictKeys(self, ctx:DataScriptParser.DictKeysContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dictKeys.
    def exitDictKeys(self, ctx:DataScriptParser.DictKeysContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dictValues.
    def enterDictValues(self, ctx:DataScriptParser.DictValuesContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dictValues.
    def exitDictValues(self, ctx:DataScriptParser.DictValuesContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dictUpdate.
    def enterDictUpdate(self, ctx:DataScriptParser.DictUpdateContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dictUpdate.
    def exitDictUpdate(self, ctx:DataScriptParser.DictUpdateContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dictItem.
    def enterDictItem(self, ctx:DataScriptParser.DictItemContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dictItem.
    def exitDictItem(self, ctx:DataScriptParser.DictItemContext):
        pass


    # Enter a parse tree produced by DataScriptParser#arrays.
    def enterArrays(self, ctx:DataScriptParser.ArraysContext):
        pass

    # Exit a parse tree produced by DataScriptParser#arrays.
    def exitArrays(self, ctx:DataScriptParser.ArraysContext):
        pass


    # Enter a parse tree produced by DataScriptParser#arrayElement.
    def enterArrayElement(self, ctx:DataScriptParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#arrayElement.
    def exitArrayElement(self, ctx:DataScriptParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#createDataFrame.
    def enterCreateDataFrame(self, ctx:DataScriptParser.CreateDataFrameContext):
        pass

    # Exit a parse tree produced by DataScriptParser#createDataFrame.
    def exitCreateDataFrame(self, ctx:DataScriptParser.CreateDataFrameContext):
        pass


    # Enter a parse tree produced by DataScriptParser#loadCSV.
    def enterLoadCSV(self, ctx:DataScriptParser.LoadCSVContext):
        pass

    # Exit a parse tree produced by DataScriptParser#loadCSV.
    def exitLoadCSV(self, ctx:DataScriptParser.LoadCSVContext):
        pass


    # Enter a parse tree produced by DataScriptParser#saveCSV.
    def enterSaveCSV(self, ctx:DataScriptParser.SaveCSVContext):
        pass

    # Exit a parse tree produced by DataScriptParser#saveCSV.
    def exitSaveCSV(self, ctx:DataScriptParser.SaveCSVContext):
        pass


    # Enter a parse tree produced by DataScriptParser#columnDataFrame.
    def enterColumnDataFrame(self, ctx:DataScriptParser.ColumnDataFrameContext):
        pass

    # Exit a parse tree produced by DataScriptParser#columnDataFrame.
    def exitColumnDataFrame(self, ctx:DataScriptParser.ColumnDataFrameContext):
        pass


    # Enter a parse tree produced by DataScriptParser#selectRow.
    def enterSelectRow(self, ctx:DataScriptParser.SelectRowContext):
        pass

    # Exit a parse tree produced by DataScriptParser#selectRow.
    def exitSelectRow(self, ctx:DataScriptParser.SelectRowContext):
        pass


    # Enter a parse tree produced by DataScriptParser#filterRows.
    def enterFilterRows(self, ctx:DataScriptParser.FilterRowsContext):
        pass

    # Exit a parse tree produced by DataScriptParser#filterRows.
    def exitFilterRows(self, ctx:DataScriptParser.FilterRowsContext):
        pass


    # Enter a parse tree produced by DataScriptParser#addColumn.
    def enterAddColumn(self, ctx:DataScriptParser.AddColumnContext):
        pass

    # Exit a parse tree produced by DataScriptParser#addColumn.
    def exitAddColumn(self, ctx:DataScriptParser.AddColumnContext):
        pass


    # Enter a parse tree produced by DataScriptParser#dropColumn.
    def enterDropColumn(self, ctx:DataScriptParser.DropColumnContext):
        pass

    # Exit a parse tree produced by DataScriptParser#dropColumn.
    def exitDropColumn(self, ctx:DataScriptParser.DropColumnContext):
        pass


    # Enter a parse tree produced by DataScriptParser#describeDataFrame.
    def enterDescribeDataFrame(self, ctx:DataScriptParser.DescribeDataFrameContext):
        pass

    # Exit a parse tree produced by DataScriptParser#describeDataFrame.
    def exitDescribeDataFrame(self, ctx:DataScriptParser.DescribeDataFrameContext):
        pass


    # Enter a parse tree produced by DataScriptParser#headDataFrame.
    def enterHeadDataFrame(self, ctx:DataScriptParser.HeadDataFrameContext):
        pass

    # Exit a parse tree produced by DataScriptParser#headDataFrame.
    def exitHeadDataFrame(self, ctx:DataScriptParser.HeadDataFrameContext):
        pass


    # Enter a parse tree produced by DataScriptParser#mergeDataFrames.
    def enterMergeDataFrames(self, ctx:DataScriptParser.MergeDataFramesContext):
        pass

    # Exit a parse tree produced by DataScriptParser#mergeDataFrames.
    def exitMergeDataFrames(self, ctx:DataScriptParser.MergeDataFramesContext):
        pass


    # Enter a parse tree produced by DataScriptParser#selectColumn.
    def enterSelectColumn(self, ctx:DataScriptParser.SelectColumnContext):
        pass

    # Exit a parse tree produced by DataScriptParser#selectColumn.
    def exitSelectColumn(self, ctx:DataScriptParser.SelectColumnContext):
        pass


    # Enter a parse tree produced by DataScriptParser#equalsF.
    def enterEqualsF(self, ctx:DataScriptParser.EqualsFContext):
        pass

    # Exit a parse tree produced by DataScriptParser#equalsF.
    def exitEqualsF(self, ctx:DataScriptParser.EqualsFContext):
        pass


    # Enter a parse tree produced by DataScriptParser#minorF.
    def enterMinorF(self, ctx:DataScriptParser.MinorFContext):
        pass

    # Exit a parse tree produced by DataScriptParser#minorF.
    def exitMinorF(self, ctx:DataScriptParser.MinorFContext):
        pass


    # Enter a parse tree produced by DataScriptParser#greaterF.
    def enterGreaterF(self, ctx:DataScriptParser.GreaterFContext):
        pass

    # Exit a parse tree produced by DataScriptParser#greaterF.
    def exitGreaterF(self, ctx:DataScriptParser.GreaterFContext):
        pass


    # Enter a parse tree produced by DataScriptParser#parensF.
    def enterParensF(self, ctx:DataScriptParser.ParensFContext):
        pass

    # Exit a parse tree produced by DataScriptParser#parensF.
    def exitParensF(self, ctx:DataScriptParser.ParensFContext):
        pass


    # Enter a parse tree produced by DataScriptParser#andOrF.
    def enterAndOrF(self, ctx:DataScriptParser.AndOrFContext):
        pass

    # Exit a parse tree produced by DataScriptParser#andOrF.
    def exitAndOrF(self, ctx:DataScriptParser.AndOrFContext):
        pass


    # Enter a parse tree produced by DataScriptParser#complejo.
    def enterComplejo(self, ctx:DataScriptParser.ComplejoContext):
        pass

    # Exit a parse tree produced by DataScriptParser#complejo.
    def exitComplejo(self, ctx:DataScriptParser.ComplejoContext):
        pass


    # Enter a parse tree produced by DataScriptParser#img.
    def enterImg(self, ctx:DataScriptParser.ImgContext):
        pass

    # Exit a parse tree produced by DataScriptParser#img.
    def exitImg(self, ctx:DataScriptParser.ImgContext):
        pass


    # Enter a parse tree produced by DataScriptParser#CosFunc.
    def enterCosFunc(self, ctx:DataScriptParser.CosFuncContext):
        pass

    # Exit a parse tree produced by DataScriptParser#CosFunc.
    def exitCosFunc(self, ctx:DataScriptParser.CosFuncContext):
        pass


    # Enter a parse tree produced by DataScriptParser#SenFunc.
    def enterSenFunc(self, ctx:DataScriptParser.SenFuncContext):
        pass

    # Exit a parse tree produced by DataScriptParser#SenFunc.
    def exitSenFunc(self, ctx:DataScriptParser.SenFuncContext):
        pass


    # Enter a parse tree produced by DataScriptParser#TanFunc.
    def enterTanFunc(self, ctx:DataScriptParser.TanFuncContext):
        pass

    # Exit a parse tree produced by DataScriptParser#TanFunc.
    def exitTanFunc(self, ctx:DataScriptParser.TanFuncContext):
        pass



del DataScriptParser