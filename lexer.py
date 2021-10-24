#----------------------------------
#   Lexer C#
#----------------------------------

import re

f = open('test.cs', 'r')
#Vaciar archivos
log = open('log.txt', 'w')
print ("Resultados:\n", file=log)
log.close()

result = open('result.txt', 'w')
print ("Resultados:\n", file=result)
result.close()

#Preparar archivos
log = open('log.txt', 'a')
result = open('result.txt', 'a')

#Tokenizar:
#uso de identificadores
#palabras reservadas
#operadores
#caracteres
#palabras de inicio y fin de bloque
#constantes
#cadenas de caracteres
#entre otros

#Expresiones regulares
identificadores = {
    'IDENTIFICADOR': r'^([a-zA-Z_][a-zA-Z\\d_$]*)$'
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
    '>': 'MAYOR_QUE', 
    '<': 'MENOR_QUE',
    '!': 'NEGACION'
}
claves_operadores = operadores.keys()

operadores_comp = {
    '>=': 'MAYOR_IGUAL', 
    '<=': 'MENOR_IGUAL ',
    '++': 'INCREMENTO',
    '--': 'DECREMENTO',
    '==': 'COMPARAR_IGUAL',
    '!=': 'COMPARAR_DIF',
    '&&': 'AND',
    '||': 'OR'
}
claves_operadores_comp = operadores_comp.keys()

palabras_reservadas = {
    'using': 'USAR',
    'namespace': 'NOMBRE_ESPACIO',
    'class': 'CLASE',
    'static': 'ESTATICO',
    'new': 'NUEVO',
    'if': 'CONDICIONAL',
    'for': 'BUCLE_PARA',
    'foreach': 'BUCLE_RECORRIDO', 
    'private': 'ACCESO_PRIVADO',
    'public': 'ACCESO_PUBLICO',
    'in': 'DENTRO_DE'
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
                        if token[j+1] == '+' or token[j+1] == '-' or token[j+1] == '=':
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
                            if token[j+1] == '+' or token[j+1] == '-' or token[j+1] == '=':
                                limit = j+1
                            tokensMiddle = [token[0:limit+1], token[limit+1:]]
                            tokensPrev = tokens[0:i]
                            tokensPost = tokens[i+1:]
                            tokens = tokensPrev+tokensMiddle+tokensPost
                            break
        i+=1
        stop = len(tokens)

    s = "" 
    for t in tokens:
        s += t+" "

    print(tokens, file=result)
    return tokens

#--------------------------- MAIN --------------------------
#dataFlag = False

lectura = f.read()
#Se eliminan los comentarios
lectura = re.sub(commentarios['COMENTARIO_MULTILINEA'], '', lectura)
lectura = re.sub(commentarios['COMENTARIO_LINEA'], '\n', lectura)

#Se separa el codigo en lineas
codigo =  lectura.split('\n')
lineaIndex = 1

for linea in codigo:
    print ("Linea #",lineaIndex,"\n",linea, file=log)

    tokens = getTokens(linea)

    for token in tokens:
        if token in claves_operadores:
            token = 1
        #Reemplazar por valores de diccionarios
        #Identificar strings y numeros
        #PALABRA_RESERVADA('using') IDENTIFICADOR('System') PUNTUACION(PUNTO_COMA) <- Posible forma
        #['using', 'System', ';']
            
    lineaIndex += 1

log.close()
