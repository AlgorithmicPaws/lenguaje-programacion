from DataScriptVisitor import DataScriptVisitor
from DataScriptParser import DataScriptParser
import math
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class EvalVisitor(DataScriptVisitor):
    memory = {}
    funciones = {}
    files = {}

    def visitAssign(self, ctx: DataScriptParser.AssignContext):
        id_ = ctx.ID().getText()
        if ctx.expr():
            value = self.visit(ctx.expr())
            self.memory[id_] = value
        else:
            value = self.visit(ctx.reading())
            self.memory[id_] = value
        return value

#TIPOS DE DATOS
      
    def visitBool(self, ctx: DataScriptParser.BoolContext):
        return ctx.BOL().getText()
  
    def visitInt(self, ctx: DataScriptParser.IntContext):
        return int(ctx.INT().getText())
        
    def visitCastInt(self, ctx: DataScriptParser.CastIntContext):
        return int(self.visit(ctx.exprA()))
        
    def visitFloat(self, ctx: DataScriptParser.FloatContext):
        return float(ctx.FLO().getText())
        
    def visitImg(self, ctx: DataScriptParser.ImgContext):
        texto = ctx.getText()
        numero_complejo = str(texto).replace('i', 'j')
        # Convertir el texto a un número complejo
        numero_complejo = complex(numero_complejo)
        return numero_complejo
        
    def visitComplejo(self, ctx: DataScriptParser.ComplejoContext):
        left = self.visit(ctx.complex(0))
        right = self.visit(ctx.complex(1))
        if ctx.op.type == ComplexLanguageParser.ADD:
            texto = str(left + '+' + right)
        else: texto = str(left + '-' + right)
        numero_complejo = str(texto).replace('i', 'j')
        numero_complejo = complex(texto)
        return numero_complejo
        
    def visitStr(self, ctx: DataScriptParser.StrContext):
        return str(ctx.STR().getText())[1:-1]
        
    def visitSplit(self, ctx: DataScriptParser.SplitContext):
        return self.visit(ctx.exprA()).split()

    def visitId(self, ctx: DataScriptParser.IdContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return self.memory[id_]
        return 0

    def visitHex(self, ctx: DataScriptParser.HexContext):
        hex_value = ctx.getText()
        decimal_value = int(hex_value[2:], 16)
        return decimal_value
        
        
#ESTRUCTURAS DE DATOS

    # DATAFRAMES
    
    def visitCreateDataFrame(self, ctx: DataScriptParser.CreateDataFrameContext):
        if ctx.list_():
            data = self.visit(ctx.list_())
            df = pd.DataFrame(data)
        elif ctx.dict_():
            data = self.visit(ctx.dict_())
            df = pd.DataFrame(data)
        elif ctx.ID():
            id_ = ctx.ID().getText()
            if id_ in self.memory:
                df = pd.DataFrame(self.memory[id_])
            else:
                print(f"Error: el DataFrame '{id_}' no está definido.")
                return None
        else:
            print(f"Error: entrada no válida para crear un DataFrame.")
            return None
        
        id_ = ctx.ID().getText()
        self.memory[id_] = df
        return df

    # Función para cargar un DataFrame desde un archivo CSV
    def visitLoadCSV(self, ctx: DataScriptParser.LoadCSVContext):
        file_name = ctx.STR().getText()[1:-1]
        return pd.read_csv(file_name)

    # Función para guardar un DataFrame a un archivo CSV
    def visitSaveCSV(self, ctx: DataScriptParser.SaveCSVContext):
        id_ = ctx.ID().getText()
        file_name = ctx.STR().getText()[1:-1]
        if id_ in self.memory and isinstance(self.memory[id_], pd.DataFrame):
            self.memory[id_].to_csv(file_name, index=False)
            return 'Verdadero'
        else:
            print(f"Error: el DataFrame '{id_}' no está definido.")
            return 'Falso'

    # Función para seleccionar una columna de un DataFrame
    def visitSelectColumn(self, ctx: DataScriptParser.SelectColumnContext):
        if ctx.ID() == 1:
            id_ = ctx.ID().getText()
        else:
            id_ = ctx.ID(0).getText()
        if ctx.ID(1):
            column_name = self.visit(ctx.ID(1))
        else:
            column_name = ctx.STR().getText()[1:-1]
        if isinstance(column_name, str):
            if id_ in self.memory and isinstance(self.memory[id_], pd.DataFrame):
                return self.memory[id_][column_name]
            else:
                print(f"Error: el DataFrame '{id_}' no está definido.")
                return None
        else:
            print(f"Error: el nombre de la columna debe ser una cadena.")
            return None

    # Función para seleccionar una fila de un DataFrame
    def visitSelectRow(self, ctx: DataScriptParser.SelectRowContext):
        id_ = ctx.ID().getText()
        row_index = int(ctx.INT().getText())
        if id_ in self.memory and isinstance(self.memory[id_], pd.DataFrame):
            return self.memory[id_].iloc[row_index]
        else:
            print(f"Error: el DataFrame '{id_}' no está definido.")
            return None

    # Función para filtrar filas de un DataFrame
    def visitFilterRows(self, ctx: DataScriptParser.FilterRowsContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory and isinstance(self.memory[id_], pd.DataFrame):
            filtro = self.visit(ctx.filter_())
            return self.memory[id_].loc[filtro]
        else:
            print(f"Error: el DataFrame '{id_}' no está definido.")
            return None
            
    def visitAndOrF(self, ctx: DataScriptParser.AndOrFContext):
        left = self.visit(ctx.filter())
        right = self.visit(ctx.filter())

        if ctx.op.type == DataScriptParser.AND:
            return left and right
        else:
            return left or right
    
    def visitMinorF(self, ctx: DataScriptParser.MinorFContext):
        left = self.visit(ctx.column())
        right = self.visit(ctx.exprA())
        if ctx.op.type == DataScriptParser.MIN:
            return left < right
        else:
            return left <= right
                
    def visitGreaterF(self, ctx: DataScriptParser.GreaterFContext):
        left = self.visit(ctx.column())
        right = self.visit(ctx.exprA())
        if ctx.op.type == DataScriptParser.GRE:
            return left > right
        else:
            return left >= right
        
    def visitEqualsF(self, ctx: DataScriptParser.EqualsFContext):
        left = self.visit(ctx.column())
        right = self.visit(ctx.exprA())
        return left == right
        
    def visitParensF(self, ctx: DataScriptParser.ParensFContext):
        return self.visit(ctx.filter())
            
    # Función para agregar una columna a un DataFrame
    def visitAddColumn(self, ctx: DataScriptParser.AddColumnContext):
        id_ = ctx.ID().getText()
        column_name = ctx.STR().getText()[1:-1]
        column_value = self.visit(ctx.expr())
        if id_ in self.memory and isinstance(self.memory[id_], pd.DataFrame):
            self.memory[id_][column_name] = column_value
            return self.memory[id_]
        else:
            print(f"Error: el DataFrame '{id_}' no está definido.")
            return None

    # Función para eliminar una columna de un DataFrame
    def visitDropColumn(self, ctx: DataScriptParser.DropColumnContext):
        id_ = ctx.ID().getText()
        column_name = ctx.STR().getText()[1:-1]
        if id_ in self.memory and isinstance(self.memory[id_], pd.DataFrame):
            self.memory[id_].drop(columns=[column_name], inplace=True)
            return self.memory[id_]
        else:
            print(f"Error: el DataFrame '{id_}' no está definido.")
            return None

    # Función para describir un DataFrame
    def visitDescribeDataFrame(self, ctx: DataScriptParser.DescribeDataFrameContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory and isinstance(self.memory[id_], pd.DataFrame):
            return self.memory[id_].describe()
        else:
            print(f"Error: el DataFrame '{id_}' no está definido.")
            return None

    # Función para obtener las primeras N filas de un DataFrame
    def visitHeadDataFrame(self, ctx: DataScriptParser.HeadDataFrameContext):
        id_ = ctx.ID().getText()
        n = int(ctx.INT().getText())
        if id_ in self.memory and isinstance(self.memory[id_], pd.DataFrame):
            return self.memory[id_].head(n)
        else:
            print(f"Error: el DataFrame '{id_}' no está definido.")
            return None

    # Función para unir dos DataFrames
    def visitMergeDataFrames(self, ctx: DataScriptParser.MergeDataFramesContext):
        id_1 = ctx.ID(0).getText()
        id_2 = ctx.ID(1).getText()
        on_column = ctx.STR().getText()[1:-1]
        if id_1 in self.memory and id_2 in self.memory:
            if isinstance(self.memory[id_1], pd.DataFrame) and isinstance(self.memory[id_2], pd.DataFrame):
                return pd.merge(self.memory[id_1], self.memory[id_2], on=on_column)
            else:
                print(f"Error: Uno o ambos de los DataFrames '{id_1}' y '{id_2}' no están definidos.")
                return None
        else:
            print(f"Error: Uno o ambos de los DataFrames '{id_1}' y '{id_2}' no están definidos.")
            return None

    # ARREGLOS
    
    def visitArrays(self, ctx: DataScriptParser.ArraysContext):
        array = np.array(self.visit(ctx.exprA()))
        return array
        
    def visitArrayElement(self, ctx: DataScriptParser.ArrayElementContext):
        if ctx.ID().getText() in self.memory:
            array = self.memory[ctx.ID().getText()]
            indices = tuple(int(idx.getText()) for idx in ctx.INT())
            valor = array[indices]
            return valor
        else:
            print("Error: el arreglo '{ctx.ID().getText()}' no está definida.")
            return None

    # DICCIONARIOS
    
    def visitDicts(self, ctx: DataScriptParser.DictsContext):
        dict_items = {}
        for item in ctx.dictItem():
            key = self.visit(item.expr(0))
            value = self.visit(item.expr(1))
            dict_items[key] = value
        return dict_items
        
    def visitDictKeys(self, ctx:DataScriptParser.DictKeysContext):
        if ctx.ID().getText() in self.memory:
            return list(self.memory[ctx.ID().getText()].keys())
        else:
            print("Error: el diccionario '{ctx.ID().getText()}' no está definida.")
            return None
            
    def visitDictValues(self, ctx:DataScriptParser.DictValuesContext):
        if ctx.ID().getText() in self.memory:
            return self.memory[ctx.ID().getText()].values()
        else:
            print("Error: el diccionario '{ctx.ID().getText()}' no está definida.")
            return None
            
    def visitDictUpdate(self, ctx:DataScriptParser.DictUpdateContext):
        if ctx.ID().getText() in self.memory:
            return self.memory[ctx.ID().getText()].update(ctx.dict())
        else:
            print("Error: el diccionario '{ctx.ID().getText()}' no está definida.")
            return None
            
    def visitDictElement(self, ctx:DataScriptParser.DictElementContext):
        if ctx.ID().getText() in self.memory:
            return self.memory[ctx.ID().getText()][self.visit(ctx.expr())]
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
            
    def visitDictElementassign(self, ctx:DataScriptParser.DictElementassignContext):
        if ctx.ID().getText() in self.memory:
            self.memory[ctx.ID().getText()][self.visit(ctx.expr(0))] = self.visit(ctx.expr(1))
            result = self.memory[ctx.ID().getText()][self.visit(ctx.expr(0))] 
            return result
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
       
    #LISTAS
    

    def visitLists(self, ctx:DataScriptParser.ListsContext):
        elementos = []
        for exp in ctx.expr():
            elementos.append(self.visit(exp))
        return elementos
       
    def visitListAppend(self, ctx:DataScriptParser.ListAppendContext):
        if ctx.ID().getText() in self.memory:
            self.memory[ctx.ID().getText()].append(self.visit(ctx.expr()))
            return self.memory[ctx.ID().getText()]
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
        
    def visitListElement(self, ctx:DataScriptParser.ListElementContext):
        if ctx.ID().getText() in self.memory:
            lista = self.memory[ctx.ID().getText()]
            indices = [int(idx.getText()) for idx in self.visit(ctx.exprA())]
            valor = lista
            for idx in indices:
                valor = valor[idx]
            return valor
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
            
    def visitListElementassign(self, ctx:DataScriptParser.ListElementassignContext):
        if ctx.ID().getText() in self.memory:
            lista = self.memory[ctx.ID().getText()]
            indices = [int(idx.getText()) for idx in self.visit(ctx.exprA())[:-1]]
            valor_final = int(ctx.INT()[-1].getText())
            asignar_valor = self.visit(ctx.expr())

            sublista = lista
            for idx in indices:
                sublista = sublista[idx]
            sublista[valor_final] = asignar_valor

            return lista
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
     
    def visitListIndex(self, ctx:DataScriptParser.ListIndexContext):
        if ctx.ID().getText() in self.memory:
            return self.memory[ctx.ID().getText()].index(self.visit(ctx.expr()))
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
        
    def visitListLen(self, ctx:DataScriptParser.ListLenContext):
        if ctx.ID().getText() in self.memory:
            return len(self.memory[ctx.ID().getText()])
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
            
    def visitListRemove(self, ctx:DataScriptParser.ListRemoveContext):
        if ctx.ID().getText() in self.memory:
            self.memory[ctx.ID().getText()].remove(self.visit(ctx.expr()))
            return 'Verdadero'
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
            
    def visitListClear(self, ctx:DataScriptParser.ListClearContext):
        if ctx.ID().getText() in self.memory:
            return self.memory[ctx.ID().getText()].clear()
        else:
            print("Error: la lista '{ctx.ID().getText()}' no está definida.")
            return None
       
#DECLARACION DE FUNCIONES
    
    def visitFunctionStatement(self, ctx:DataScriptParser.FunctionStatementContext):
        nombre_funcion = ctx.ID().getText()
        lista_parametros = ctx.parametros().ID()
        lista_statements = []
        for i in range(2, ctx.getChildCount()-1):
            if ctx.getChild(i).getText() == '{':
                for j in range(i+1, ctx.getChildCount()-1):

                    lista_statements.append(ctx.getChild(j))
        self.funciones[nombre_funcion] = (lista_parametros, lista_statements)
        return None

    def visitFunctionCall(self, ctx:DataScriptParser.FunctionCallContext):
        nombre_funcion = ctx.ID().getText()
        if nombre_funcion in self.funciones:
            parametros_definidos, funcion_definida = self.funciones[nombre_funcion]
            argumentos = [self.visit(param) for param in ctx.args().expr()]
            
            if len(argumentos) != len(parametros_definidos):
                print(f"Error: el número de argumentos proporcionados para '{nombre_funcion}' no coincide con la definición.")
                return None

            # Asignar los argumentos a los parámetros en el contexto de la función
            for parametro, argumento in zip(parametros_definidos, argumentos):
                self.memory[parametro.getText()] = argumento

            for i in range(len(funcion_definida)):
                if 'Retornar' in funcion_definida[i].getChild(0).getText():
                    result = self.visit(funcion_definida[i].getChild(0))
                    if result != None:
                         return result
                else:
                    self.visit(funcion_definida[i])
                
            # Visitar el nuevo contexto
            return 'Verdadero'
        else:
            print(f"Error: la función '{nombre_funcion}' no está definida.")
        return 'Falso'
        
#SENTENCIAS IF, IFELSE, WHILE, FOR
        
    def visitIf(self, ctx:DataScriptParser.IfContext):
        condicion = self.visit(ctx.exprL())
        if condicion == 'Verdadero':
            for i in range(5, ctx.getChildCount()-1):
                if 'Retornar' in ctx.getChild(i).getText():
                    return self.visit(ctx.getChild(i).expr())
                self.visit(ctx.getChild(i))  # Visitar el bloque de sentencias del if
        return None
        
    def visitIfElse(self, ctx:DataScriptParser.IfElseContext):
        condicion = self.visit(ctx.exprL())
        if condicion == 'Verdadero':
            for i in range(5, ctx.getChildCount()-1):
                if 'Retornar' in ctx.getChild(i).getText():
                    return self.visit(ctx.getChild(i).expr())
                self.visit(ctx.getChild(i))  # Visitar el bloque de sentencias del if
        else:
            for i in range(5, ctx.getChildCount()):
                if ctx.getChild(i).getText() == '{':
                    for j in range(i+1, ctx.getChildCount()-1):
                        if 'Retornar' in ctx.getChild(j).getText():
                            return self.visit(ctx.getChild(j).expr())
                        self.visit(ctx.getChild(j))  # Visitar el bloque de sentencias del if
        return None
        
        
    def visitWhile(self, ctx:DataScriptParser.WhileContext):
        while self.visit(ctx.exprL()) == 'Verdadero':
            for i in range(5, ctx.getChildCount()-1):
                if 'Retornar' in ctx.getChild(i).getText():
                    return self.visit(ctx.getChild(i).expr())
                self.visit(ctx.getChild(i))  # Visitar el bloque de sentencias del if
        return None
        
    def visitFor(self, ctx:DataScriptParser.ForContext):
        self.visit(ctx.assignment(0))
        while self.visit(ctx.exprL()) == 'Verdadero':
            for i in range(8, ctx.getChildCount()-1):

                self.visit(ctx.getChild(i))  # Visitar el bloque de sentencias del if
            self.visit(ctx.assignment(1))
        return None
        
#LEER, IMPRIMIR, GRAFICAR
        
    def visitRead(self, ctx: DataScriptParser.ReadContext):
        if ctx.TYPE().getText() == 'Entero':
            value = int(input())
        elif ctx.TYPE().getText() == 'Arreglo':
            value = input()
        else:
            value = float(input())
        id_ = ctx.ID().getText()
        self.memory[id_] = value
        return value
        
    def visitPrintExpr(self, ctx: DataScriptParser.PrintExprContext):
        text = ""
        for exp in ctx.expr():
            value = self.visit(exp)
            text += str(value)
        print(text)
        return 0
        
    def visitGraph(self, ctx: DataScriptParser.GraphContext):
            graph_type = ctx.graphType().getText()
            if ctx.graphParams().ID() == 1:
                data_id = ctx.graphParams().ID().getText()
            else:
                data_id = ctx.graphParams().ID(0).getText()
                y_id = ctx.graphParams().ID(1).getText() if graph_type != 'histograma' else None
            title = ctx.graphParams().STR().getText()[1:-1] if ctx.graphParams().STR() else None
            limit = int(ctx.graphParams().INT().getText()) if ctx.graphParams().INT() else None

            if data_id not in self.memory or (y_id and y_id not in self.memory):
                print(f"Error: Una de las variables '{data_id}' o '{y_id}' no está definida.")
                return None

            data = self.memory[data_id]
            y_data = self.memory[y_id] if y_id else None

            if limit:
                data = data[:limit]
                if y_data:
                    y_data = y_data[:limit]

            plt.figure()
            if graph_type == 'barras':
                plt.bar(data, y_data)
            elif graph_type == 'lineas':
                plt.plot(data, y_data)
            elif graph_type == 'dispersion':
                plt.scatter(data, y_data)
            elif graph_type == 'histograma':
                plt.hist(data, bins=limit if limit else 10)

            if title:
                plt.title(title)

            plt.show()
            return 'Verdadero'
        
# OPERACIONES DE ARCHIVOS

    def visitOpenFile(self, ctx: DataScriptParser.OpenFileContext):
        file_id = ctx.ID().getText()
        file_name = ctx.STR().getText()[1:-1]
        self.files[file_id] = open(file_name, 'a+')
        return 'Verdadero'

    def visitCloseFile(self, ctx: DataScriptParser.CloseFileContext):
        file_id = ctx.ID().getText()
        if file_id in self.files:
            self.files[file_id].close()
            del self.files[file_id]
        return 'Verdadero'

    def visitReadLine(self, ctx: DataScriptParser.ReadLineContext):
        file_id = ctx.ID().getText()
        numero_linea = 0
        if file_id in self.files:
            self.files[file_id].seek(0)
            for contenido_linea in self.files[file_id].readlines():
                if ctx.INT():
                    if numero_linea == int(ctx.INT().getText()):
                        return contenido_linea
                    numero_linea += 1
                else:
                    iterator = self.visit(ctx.exprA())
                    if numero_linea == iterator:
                        return contenido_linea
                    numero_linea += 1
        return 'Falso'

    def visitWriteFile(self, ctx: DataScriptParser.WriteFileContext):
        file_id = ctx.ID().getText()
        content = ctx.STR().getText()[1:-1]
        if file_id in self.files:
            self.files[file_id].write(str(content) + '\n')
        return 'Verdadero'

    def visitReadAll(self, ctx: DataScriptParser.ReadAllContext):
        file_id = ctx.ID().getText()
        if file_id in self.files:
            self.files[file_id].seek(0)
            return self.files[file_id].read()
        return 'Falso'
        
    def visitDeleteFile(self, ctx: DataScriptParser.DeleteFileContext):
        file_id = ctx.ID().getText()
        if file_id in self.files:
            os.remove(self.files[file_id].name)
            del self.files[file_id]
            return 'verdadero'
        return 'Falso'
        
#EXPRESIONES
        
    def visitLogic(self, ctx: DataScriptParser.LogicContext):
        return self.visit(ctx.exprL())
        
    def visitAritmetic(self, ctx: DataScriptParser.AritmeticContext):
        return self.visit(ctx.exprA())
        
    def visitReturn(self, ctx: DataScriptParser.ReturnContext):
        return self.visit(ctx.expr())
        
    #EXPRESIONES LOGICAS
        
    def visitAndOr(self, ctx: DataScriptParser.AndOrContext):
        left = True if self.visit(ctx.exprL(0)) == 'Verdadero' else False
        right = True if self.visit(ctx.exprL(1)) == 'Verdadero' else False

        if ctx.op.type == DataScriptParser.AND:
            if left and right:
                return 'Verdadero'
            else:
                return 'Falso'
        else:
            if left or right:
                return 'Verdadero'
            else:
                return 'Falso'
            
    def visitNegation(self, ctx: DataScriptParser.NegationContext):
        left = self.visit(ctx.exprL())
        if left == 'Falso':
            return 'Verdadero'
        else: 
            return 'Falso' 
    
    def visitMinor(self, ctx: DataScriptParser.MinorContext):
        left = self.visit(ctx.exprA(0))
        right = self.visit(ctx.exprA(1))
        if ctx.op.type == DataScriptParser.MIN:
            if left < right:
                return 'Verdadero'
            else: 
                return 'Falso'
        else:
            if left <= right:
                return 'Verdadero'
            else: 
                return 'Falso'
                
    def visitGreater(self, ctx: DataScriptParser.GreaterContext):
        left = self.visit(ctx.exprA(0))
        right = self.visit(ctx.exprA(1))
        if ctx.op.type == DataScriptParser.GRE:
            if left > right:
                return 'Verdadero'
            else: 
                return 'Falso'
        else:
            if left >= right:
                return 'Verdadero'
            else: 
                return 'Falso'
        
    def visitEquals(self, ctx: DataScriptParser.EqualsContext):
        left = self.visit(ctx.exprA(0))
        right = self.visit(ctx.exprA(1))
        if left == right:
            return 'Verdadero'
        else: 
            return 'Falso'
            
    def visitEqualsL(self, ctx: DataScriptParser.EqualsLContext):
        left = self.visit(ctx.exprL(0))
        right = self.visit(ctx.exprL(1))
        if left == right:
            return 'Verdadero'
        else: 
            return 'Falso'
            
    def visitIdL(self, ctx: DataScriptParser.IdLContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return self.memory[id_]
        return 0
            
    #EXPRESIONES ARITMETICAS
    
    def visitDot(self, ctx: DataScriptParser.DotContext):
        id_1 = ctx.exprA(0).getText() if ctx.exprA(0).ID() else self.visit(ctx.exprA(0))
        id_2 = ctx.exprA(1).getText() if ctx.exprA(0).ID() else self.visit(ctx.exprA(1))
        if id_1 in self.memory and id_2 in self.memory:
            matriz_1 = self.memory[id_1]
            matriz_2 = self.memory[id_2]
        else:
            matriz_1 = id_1
            matriz_2 = id_2
        if isinstance(matriz_1, np.ndarray) and isinstance(matriz_2, np.ndarray):
            if matriz_1.shape != matriz_2.shape:
                print(f"Error: Las matrices deben tener la misma longitud")
                return None
            producto_punto_numpy = np.dot(matriz_1, matriz_2)
            return producto_punto_numpy 
        else:
            if isinstance(matriz_1, list) and isinstance(matriz_2, list):
                if len(matriz_1) != len(matriz_2):
                    print(f"Error: Las matrices deben tener la misma longitud")
                    return None
                producto = 0
                for i in range(len(matriz_1)):
                    producto += matriz_1[i] * matriz_2[i]
                return producto
            else:  
                print(f"Error: Una o ambas de las matrices '{matriz_1}' y '{matriz_2}' no son una lista, un arreglo o no están definidas.")
                return None
                
    def visitCross(self, ctx: DataScriptParser.CrossContext):
        id_1 = ctx.exprA(0).getText() if ctx.exprA(0).ID() else self.visit(ctx.exprA(0))
        id_2 = ctx.exprA(1).getText() if ctx.exprA(0).ID() else self.visit(ctx.exprA(1))
        if id_1 in self.memory and id_2 in self.memory:
            matriz_1 = self.memory[id_1]
            matriz_2 = self.memory[id_2]
        else:
            matriz_1 = id_1
            matriz_2 = id_2
        if isinstance(matriz_1, np.ndarray) and isinstance(matriz_2, np.ndarray):
            if matriz_1.shape != matriz_2.shape:
                print(f"Error: Las matrices deben tener la misma longitud")
                return None
            producto_cruz_numpy = np.cross(matriz_1, matriz_2)
            return producto_cruz_numpy 
        else:
            if isinstance(matriz_1, list) and isinstance(matriz_2, list):
                vec1 = np.array(matriz_1)
                vec2 = np.array(matriz_2)
                if vec1.shape != vec2.shape:
                    print(f"Error: Las matrices deben tener la misma longitud")
                    return None
                resultado = np.cross(vec1, vec2)
                return resultado.tolist()
            else:  
                print(f"Error: Una o ambas de las matrices '{matriz_1}' y '{matriz_2}' no son una lista, un arreglo o no están definidas.")
                return None
                
    def visitReverse(self, ctx: DataScriptParser.ReverseContext):
        id_ = ctx.exprA().getText() if ctx.exprA().ID() else self.visit(ctx.exprA())
        if id_ in self.memory:
            matriz_1 = self.memory[id_] 
        else:
            matriz_1 = id_
        if isinstance(matriz_1, np.ndarray):
            try:
                matriz_inversa = np.linalg.inv(matriz_1)
            except np.linalg.LinAlgError:
                print("La matriz no es invertible (es una matriz singular)")
                return None
        else:
            if isinstance(matriz_1, list):
                if len(matriz_1) != len(matriz_1[0]):
                    print(f"Error: La matriz no es cuadrada")
                    return None
                vec1 = np.array(matriz_1)
                try:
                    matriz_inversa = np.linalg.inv(vec1)
                except np.linalg.LinAlgError:
                    print("La matriz no es invertible (es una matriz singular)")
                    return None
            else:  
                print(f"Error: La matriz '{matriz_1}' no es una lista, un arreglo o no está definida.")
                return None
                
    def visitTranspose(self, ctx: DataScriptParser.TransposeContext):
        id_ = ctx.exprA().getText() if ctx.exprA().ID() else self.visit(ctx.exprA())
        if id_ in self.memory:
            matriz_1 = self.memory[id_] 
        else:
            matriz_1 = id_
        if isinstance(matriz_1, np.ndarray):
            Transpose_numpy = np.transpose(matriz_1)
            return Transpose_numpy 
        else:
            if isinstance(matriz_1, list):
                if len(matriz_1) != len(matriz_1[0]):
                    print(f"Error: La matriz no es cuadrada")
                    return None
                transpuesta = [[] for _ in range(len(matriz_1[0]))]
                for i in range(len(matriz_1)):
                    for j in range(len(matriz_1[0])):
                        transpuesta[j].append(matriz_1[i][j])
                return transpuesta
            else:  
                print(f"Error: La matriz '{matriz_1}' no es una lista, un arreglo o no está definida.")
                return None
                
    def visitNegative(self, ctx: DataScriptParser.NegativeContext):
        left = self.visit(ctx.exprA())

        return - left
        
    def visitRooti(self, ctx: DataScriptParser.RootiContext):
        left = self.visit(ctx.exprA())
        right = int(ctx.INT().getText())

        return left ** (1/right)
        
    def visitRoot(self, ctx: DataScriptParser.RootContext):
        left = self.visit(ctx.exprA())

        return left ** (1/2)    
    
    def visitPower(self, ctx: DataScriptParser.PowerContext):
        left = self.visit(ctx.exprA(0))
        right = self.visit(ctx.exprA(1))

        return left ** right
        
    def visitModDivent(self, ctx: DataScriptParser.ModDiventContext):
        left = self.visit(ctx.exprA(0))
        right = self.visit(ctx.exprA(1))

        if ctx.op.type == DataScriptParser.MOD:
            return left % right
        else:
            if right != 0:
                return left // right
            else:
                return "Error: División por cero"
                

    def visitMulDiv(self, ctx: DataScriptParser.MulDivContext):
        left = self.visit(ctx.exprA(0))
        right = self.visit(ctx.exprA(1))

        if ctx.op.type == DataScriptParser.MUL:
            return left * right
        else:
            if right != 0:
                return left / right
            else:
                return "Error: División por cero"
                

    def visitAddSub(self, ctx: DataScriptParser.AddSubContext):
        left = self.visit(ctx.exprA(0))
        right = self.visit(ctx.exprA(1))

        return left + right if ctx.op.type == DataScriptParser.ADD else left - right

    def visitParens(self, ctx: DataScriptParser.ParensContext):
        return self.visit(ctx.exprA())
        
    def visitParensL(self, ctx: DataScriptParser.ParensLContext):
        return self.visit(ctx.exprL())

    def visitSenFunc(self, ctx: DataScriptParser.SenFuncContext):
        arg = math.radians(self.visit(ctx.exprA()))
        return round(float(math.sin(arg)), 3)

    def visitCosFunc(self, ctx: DataScriptParser.CosFuncContext):
        arg = math.radians(self.visit(ctx.exprA()))
        return round(float(math.cos(arg)), 3)

    def visitTanFunc(self, ctx: DataScriptParser.TanFuncContext):
        arg = math.radians(self.visit(ctx.exprA()))
        return round(float(math.tan(arg)), 3)

    def visitAbs(self, ctx: DataScriptParser.AbsContext):
        value = self.visit(ctx.exprA())
        return abs(value)

