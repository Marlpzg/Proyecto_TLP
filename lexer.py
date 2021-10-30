#----------------------------------
#   Lexer C#
#----------------------------------
import re
print("Este lexer puede acceder a los archivos fuente dentro de la carpeta source.")
archivo = input("Introduzca el nombre del archivo a tokenizar (Sin extension): ")
f = open('./source/'+archivo+'.cs', 'r')
#Vaciar archivos
log = open('./source/'+archivo+' - Step 1.txt', 'w')
print ("Codigo separado por lineas:\n", file=log)
log.close()

result = open('./source/'+archivo+' - Step 2.txt', 'w')
print ("Tokenizacion inicial:\n", file=result)
result.close()

final = open('./source/'+archivo+' - Step 3.txt', 'w')
print ("Hash Table de la tokenizacion:\n", file=final)
final.close()

finalRes = open('./source/'+archivo+' - Hash Table.txt', 'w')
print ("Hash Table de la tokenizacion:\n", file=finalRes)
finalRes.close()

#Preparar archivos
log = open('./source/'+archivo+' - Step 1.txt', 'a')
result = open('./source/'+archivo+' - Step 2.txt', 'a')
final = open('./source/'+archivo+' - Step 3.txt', 'a')
finalRes = open('./source/'+archivo+' - Hash Table.txt', 'a')

#Expresiones regulares
identificadores = {
    'IDENTIFICADOR': r'^([a-zA-Z_][a-zA-Z\\d_$]*)$'
}
claves_identificador = identificadores.keys()

cadenas = {
    'CADENA': r'"(.*?)"'
}

commentarios = {
    'COMENTARIO_LINEA': r'\/\/[\s\S]*?\n',
    'COMENTARIO_MULTILINEA': r'\/\*[\s\S]*?\*\/'
}

operadores = {
    '=': 'ASIGNAR',
    '+': 'SUMAR',
    '-': 'RESTAR',  
    '/': 'DIVIDIR',
    '*': 'MULTIPLICAR',
    '%': 'MODULO',
    '>': 'MAYOR_QUE', 
    '<': 'MENOR_QUE',
    '!': 'NEGACION',
    '&': 'AND_LOGICO',
    '|': 'OR_LOGICO'
}
claves_operadores = operadores.keys()

operadores_comp = {
    '>=': 'MAYOR_IGUAL', 
    '<=': 'MENOR_IGUAL ',
    '++': 'INCREMENTO',
    '--': 'DECREMENTO',
    '==': 'COMPARAR_IGUAL',
    '===': 'COMPARAR_IGUAL_TIPADO',
    '!=': 'COMPARAR_DIF',
    '&&': 'AND_LOGICO_CONDICIONAL',
    '||': 'OR_LOGICO_CONDICIONAL'
}
claves_operadores_comp = operadores_comp.keys()

palabras_reservadas = {
    'using': 'USAR',
    'namespace': 'ESPACIO_NOMBRES',
    'class': 'CLASE',
    'static': 'ESTATICO',
    'new': 'NUEVO',
    'if': 'CONDICIONAL',
    'for': 'BUCLE_PARA',
    'foreach': 'BUCLE_RECORRIDO', 
    'while': 'BUCLE_MIENTRAS',
    'private': 'ACCESO_PRIVADO',
    'public': 'ACCESO_PUBLICO',
    'in': 'DENTRO_DE',
    'true': 'VERDADERO',
    'false': 'FALSO',
    'return': 'RETORNAR'
}
claves_palabras_res = palabras_reservadas.keys()

tipos_de_datos = {
    'int': 'TIPO_ENTERO',
    'string': 'TIPO_CADENA',
    'void': 'TIPO_VACIO',
    'bool': 'TIPO_BOOLEANO',
    'char': 'TIPO_CARACTER',
    'float': 'TIPO_FLOTANTE',
    'double': 'TIPO_DOUBLE'
}
claves_tipos_de_datos = tipos_de_datos.keys()

puntuacion = {
    '.': 'PUNTO',
    ';': 'PUNTO_COMA',
    '\'': 'COMILLA_SIMPLE',
    ',': 'COMA',
    '(': 'PAREN_IZQ',
    ')': 'PARENT_DER',
    '[': 'CORCHETE_IZQ',
    ']': 'CORCHETE_DER',
    '"': 'COMILLA_DOBLE',
    '{': 'LLAVE_IZQ',
    '}': 'LLAVE_DER'
}
claves_puntuacion = puntuacion.keys()
claves = list(claves_operadores)+list(claves_operadores_comp)+list(claves_palabras_res)+list(claves_puntuacion)+list(claves_tipos_de_datos)

def getTokens(linea):
    #Primer filtro: Separar por espacios
    tokens = linea.split()
    #Segundo filtro: Encontrar tokens sin espacios
    i = 0
    stop = len(tokens)
    while i < stop:
        token = tokens[i]
        if not(token in claves):
            tokenBuffer = ""
            for j in range(0,len(token)):
                char = token[j]
                if char in claves:
                    extra = 0
                    if j < len(token)-1:
                        if token[j+1] == '+' or token[j+1] == '-' or token[j+1] == '=' or token[j+1] == '|' or token[j+1] == '&':
                            extra = 1
                    if(len(tokenBuffer)>0):
                        tokensMiddle = [tokenBuffer, token[j:]]
                    else:
                        tokensMiddle = [token[0:j+1+extra], token[j+1+extra:]]
                    tokensPrev = tokens[0:i]
                    tokensPost = tokens[i+1:]
                    tokens = tokensPrev+tokensMiddle+tokensPost
                    break
                else:
                    tokenBuffer += char
                    if tokenBuffer in claves :
                        if not(tokenBuffer+token[j+1] in claves) and token[j+1]==' ':
                            limit = j
                            if token[j+1] == '+' or token[j+1] == '-' or token[j+1] == '=' or token[j+1] == '|' or token[j+1] == '&':
                                limit = j+1
                            tokensMiddle = [token[0:limit+1], token[limit+1:]]
                            tokensPrev = tokens[0:i]
                            tokensPost = tokens[i+1:]
                            tokens = tokensPrev+tokensMiddle+tokensPost
                            break
        i+=1
        stop = len(tokens)

    for i,t in enumerate(tokens):
        if t == '==' and tokens[i+1] == '=':
            tokens[i] = '==='
            del tokens[i+1]

    print(tokens, file=result)
    return tokens

#--------------------------- MAIN --------------------------

lectura = f.read()
#Se eliminan los comentarios
lectura = re.sub(commentarios['COMENTARIO_MULTILINEA'], '', lectura)
lectura = re.sub(commentarios['COMENTARIO_LINEA'], '\n', lectura)

#Se separa el codigo en lineas
codigo =  lectura.split('\n')
lineaIndex = 1

hashTable = []
hashTableText = []

for linea in codigo:
    print ("Linea #",lineaIndex,"\n",linea, file=log)
    preTokens = getTokens(linea)

    #Deteccion de cadenas
    stringToken = ""
    stringFlag = False
    tokens = []

    for t in preTokens:
        if t=='"' and not(stringFlag):
            stringFlag = True
            stringToken += "\""
            continue

        if t=='"' and stringFlag:
            stringFlag = False
            stringToken = stringToken[:-1]
            stringToken += "\""
            tokens.append(stringToken)
            stringToken = ""
            continue

        if stringFlag:
            stringToken += t+" "

        if not(stringFlag):
            tokens.append(t)

    tokensText = tokens.copy()

    #Si la linea tiene contenido se utiliza
    if len(tokens) > 0:
        for idx, token in enumerate(tokens):
            flag = False

            if re.match(identificadores['IDENTIFICADOR'], token):
                tokens[idx] = {'IDENTIFICADOR': token}
                tokensText[idx] = tokens[idx]
                flag = True
            
            if token in claves_operadores:
                tokens[idx] = {"OPERADOR": token}
                tokensText[idx] = {"OPERADOR": operadores[token]}
                flag = True

            if token in claves_operadores_comp:
                tokens[idx] = {"OPERADOR": token}
                tokensText[idx] = {"OPERADOR": operadores_comp[token]}
                flag = True

            if token in claves_palabras_res:
                tokens[idx] = {"PALABRA_RESERVADA": token}
                tokensText[idx] = {"PALABRA_RESERVADA": palabras_reservadas[token]}
                flag = True

            if token in claves_puntuacion:
                tokens[idx] = {"PUNTUACION": token}
                tokensText[idx] = {"PUNTUACION": puntuacion[token]}
                flag = True

            if token in claves_tipos_de_datos:
                tokens[idx] = {"TIPO_DE_DATO": token}
                tokensText[idx] = {"TIPO_DE_DATO": tipos_de_datos[token]}
                flag = True
            
            if re.match(cadenas['CADENA'], token):
                tokens[idx] = {"CADENA": token.replace("\"", "")}
                tokensText[idx] ={"CADENA": token.replace("\"", "")}
                flag = True
            
            if token.isnumeric():
                tokens[idx] = {"NUMERO": token}
                tokensText[idx] = {"NUMERO": token}
                flag = True

            if not(flag):
                tokens[idx] = {"ERROR": token}
                tokensText[idx] = {"ERROR": token}
            
        lineaIndex += 1
        hashTable.append(tokens)
        hashTableText.append(tokensText)

print("[", file=final)
print("[", file=finalRes)
for i,row in enumerate(hashTable):
    end = ""
    if i < len(hashTable)-1:
        end = ","
    print("\t"+str(row)+end, file=final)
    print("\t"+str(hashTableText[i])+end, file=finalRes)
print("]", file=final)
print("]", file=finalRes)

log.close()
result.close()
final.close()
finalRes.close()