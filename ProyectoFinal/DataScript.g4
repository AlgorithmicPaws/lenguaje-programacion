
grammar DataScript; // rename to distinguish from Expr.g4

prog:   stat+ ;

stat:   expr NEWLINE                  # expression
    |   assignment NEWLINE            # statement
    |   print NEWLINE                 # show
    |   structureControl NEWLINE      # control
    |   functionProc NEWLINE          # function
    |   fileOperation NEWLINE         # fileOp
    |   NEWLINE                       # blank
    ;
    
assignment: ID '=' (expr|reading)      # assign; 

functionProc : 'funcion' ID '(' parametros ')' '{' stat*  '}' # functionStatement;

parametros : 
           | ID (',' ID)* 
           ;
           
args  : 
      | expr (',' expr)* 
      ;

structureControl  : ifStatement      
                  | whileStatement   
                  | forStatement
                  ;

ifStatement: 'Si' '(' exprL ')' '{' stat* '}' # if
           | 'Si' '(' exprL ')' '{' stat* '}' NEWLINE 'Sino' '{' stat* '}' # ifElse 
           ;
           
whileStatement : 'Mientras' '(' exprL ')' '{' stat* '}' # while;

forStatement : 'Para' '(' assignment ';' exprL ';' assignment ')' '{' stat* '}' # for;

print : ID '=' 'leer(' TYPE  ')'                     # read
      | 'imprimir(' (|expr (',' expr)*) ')'          # printExpr
      | 'graficar' graphType '(' graphParams ')'     # graph
      ; 

graphType: 'barras'
         | 'lineas'
         | 'dispersion'
         | 'histograma'
         ;
         
graphParams:  ID (|','  ID) (|',' STR (|',' INT) );
      
fileOperation: 'abrir(' ID ',' STR ')'               # openFile
             | 'cerrar(' ID ')'                      # closeFile
             | 'escribir(' ID ',' STR ')'            # writeFile
             | 'borrar(' ID ')'                      # deleteFile
             | reading                               # readingFile
             ;
             
reading: 'leerLinea(' ID ',' (INT|exprA) ')'   # readLine
       | 'leerTodo(' ID ')'                    # readAll
       ;
      
expr: exprL                        # Logic
    | exprA                        # Aritmetic
    | 'Retornar' expr              # return
    ;

exprL: exprL op=('&' | '|') exprL       # andOr
     | '!' exprL                        # negation
     | exprA op=('<<' | '<=') exprA     # minor
     | exprA op=('>>' | '>=') exprA     # greater
     | exprA '==' exprA                 # equals
     | exprL '==' exprL                 # equalsL
     |   '(' exprL ')'                  # parensL
     | BOL                              # bool
     | ID                               # idL
     ;

exprA:  'Punto(' exprA ',' exprA ')'   # dot
    |   'Cruz(' exprA ',' exprA ')'    # cross
    |   'Inversa(' exprA ')'           # reverse
    |   'Transpuesta(' exprA ')'       # transpose
    |   '-' exprA                      # negative
    |   exprA '^' exprA                # power
    |   'Raiz(' exprA ',' INT ')'      # rooti
    |   'Raiz(' exprA')'               # root
    |   exprA op=('%'|'//') exprA      # modDivent
    |   exprA op=('*'|'/') exprA       # mulDiv
    |   exprA op=('+'|'-') exprA       # addSub
    |   trigFunc                       # trigFunction
    |   '|' exprA '|'		       # abs
    |   ID '(' args ')'                # functionCall
    |   INT                            # int
    |   'entero(' exprA ')'            # castInt
    |   FLO                            # float
    |   complex                        # comp
    |   ID                             # id
    |   HEX			       # hex
    |   STR                            # str
    |   exprA '.separar()'             # split
    |   dataFrame                      # dfAssign
    |   array                          # arrayAssign
    |   dict                           # dictAssign
    |   list                           # listAssign
    |   '(' exprA ')'                  # parens
    ;

list: '[' ( | expr (',' expr)* ) ']'     # lists
    | ID '.agregar(' expr ')'            # listAppend
    | ID ('[' exprA ']')+                # listElement
    | ID ('[' exprA ']')+ '=' expr       # listElementassign
    | ID '.indice(' expr ')'             # listIndex
    | ID '.tam()'                        # listLen
    | ID '.borrar(' expr ')'             # listRemove
    | ID '.eliminar()'                   # listClear
    | ID                  # listId
    ;

dict: '{' ( | dictItem (',' dictItem)* ) '}' # dicts
    | ID '[' expr ']'                        # dictElement
    | ID '[' expr ']' '=' expr               # dictElementassign
    | ID '.llaves()'                         # dictKeys
    | ID '.valores()'                        # dictValues
    | ID '.actualizar(' dict ')'             # dictUpdate
    ;

dictItem: expr ':' expr                  
    ;
    
array: 'arreglo(' exprA ')'                  # arrays
     | 'arr.' ID '[' INT (',' INT)* ']'      # arrayElement    
     ;
     
dataFrame: 'mc(' (list | dict | ID) ')'                    # createDataFrame
         | 'cargarCSV(' STR ')'                            # loadCSV
         | ID '.guardarCSV(' STR ')'                       # saveCSV
         | column                                          # columnDataFrame
         | ID '.fila(' INT ')'                             # selectRow
         | ID '.filtrar(' filter ')'                       # filterRows
         | ID '.agregarColumna(' STR ',' expr ')'          # addColumn
         | ID '.eliminarColumna(' STR ')'                  # dropColumn
         | ID '.descripcion()'                             # describeDataFrame
         | ID '.cabeza(' INT ')'                           # headDataFrame
         | ID '.unir(' ID ',' STR ')'                      # mergeDataFrames
         ;
      
column: ID '.columna(' (STR | ID) ')'                      # selectColumn;
         
filter: filter op=('&' | '|') filter       # andOrF
      | column op=('<<' | '<=') exprA     # minorF
      | column op=('>>' | '>=') exprA     # greaterF
      | column '==' exprA                 # equalsF
      |   '(' filter ')'                  # parensF
      ;

complex: INT op=('+'|'-') IMG        # complejo
       | IMG                         # img
       ;

trigFunc : 'cos(' exprA ')'              # CosFunc
         | 'sen(' exprA ')'              # SenFunc
         | 'tan(' exprA ')'              # TanFunc
         ;


TYPE:   'Entero'|'Decimal';
AND :   '&' ;
OR  :   '|' ;
NOT :   '!' ; 
BOL :   'Verdadero'|'Falso';
MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
MOD :   '%' ;
DIVE:   '//';
POW :   '^' ;
MIN :   '<<';
MINE:   '<=';
GRE :   '>>';
GREE:   '>=';
EQU :   '==';
TAN :   'tan' ;
ID  :   [a-zA-Z][a-zA-Z0-9]* ;      // match identifiers
INT :   [0-9]+ ;         // match integers
FLO :  [0-9]+'.'[0-9]+;
IMG: [0-9]+('j'|'i')
   | [0-9]+'.'[0-9]+('j'|'i');
HEX :   '0x' [a-fA-F0-9]+ ; //lo devuelve como num decimal
STR :   '"' (~["])* '"';
COMENTARIO: '/*'  ~[\n]* -> skip ;  // Comentarios de múltiples líneas
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ;       // toss out whitespace
