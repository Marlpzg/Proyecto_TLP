# Generalidades C#
C# fue creado por Microsoft para su plataforma .NET. 

Existen más lenguajes en donde es posible escribir .NET pero C# es el único que fue diseñado específicamente para ser utilizado en esta plataforma, es decir, C# es el lenguaje nativo de .NET

La sintaxis y estructuración de C# es muy similar a la C++. Sin embargo, su sencillez y alto nivel de productividad son equiparables a los de Visual Basic.

# Características
* __Sencillez:__ C# elimina muchos elementos que otros lenguajes incluyen y que son innecesarios en .NET. Por ejemplo:
	* El código es __autocontenido__, no necesita ficheros adicionales al propio fuente tales como ficheros de cabecera.
	* El tamaño de los tipos de datos básicos es fijo e independiente del compilador, sistema operativo o máquina para quienes se compile. 
* __Modernidad:__ Incorpora elementos muy útiles que en otros lenguajes como Java o C++ hay que simular, como un tipo básico decimal que permita realizar operaciones de alta precisión con reales de 128 bits, la inclusión de una instrucción __foreach__ que permita recorrecr colecciones con facilidad y es ampliable a tipos definidos por el usuario o la inclusión de un tipo básico __string__ para representar cadenas.
* __Orientación a objetos:__ Como todo lenguaje de programación de propósito general actual, C# es un lenguaje orientado a objetos. Este concepto es tan puro que no admite ni funciones ni variables globales sino que todo el código y datos han de definirse dentro de definiciones de tipos de datos.

# Sintaxis
El preprocesador no interpreta de ninguna manera el código fuente del fichero sino que solo interpreta de dicho fichero lo que se denominan **directivas de preprocesado**. Estas directivas son línas de texto del fichero fuente que se caracterizan porque en ellas el primer carácter no blanco que aparece es una almohadilla (#).

La principal utilidad del preprocesador en C# es la de permitir determinar cuáles regiones de código de un fichero fuente se han de compilar.
 
Algunos componentes más usados en el preprocesador son: **identificadores**, **cadenas**, **eliminación de identificadores**, **compilación condicional**, **generación de avisos y errores** entre otros.

# Comentarios
En C# existen dos tipos de comentarios, los de una sola línea que empiezan con dos barras ( // ) y los multilínea que empiezan con barra y asterisco ( /* ) y cierran con asterisco barra ( */ ). El presente tokenizador inicia eliminando todos los comentarios del código, para ello hace uso de las siguientes expresiones regulares:
* **Comentario de línea**: `\/\/[\s\S]*?\n`
* **Comentario multi-línea**: `\/\*[\s\S]*?\*\/`

# Identificadores
Un identificador será una secuencia de cualquier número de
caracteres alfanuméricos –incluidas vocales acentuadas y eñes- tales que el primero de ellos no sea un número. Entre los identificadores usados en el código c# de los ejemplos se encuentran: 
* **System**: Indica que las funciones que estamos usando pertenecen a la estructura básica de C# y de la plataforma .Net.
* **Bubblesort**: La clasificación de burbuja es un algoritmo de clasificación simple. Este algoritmo de clasificación es un algoritmo basado en comparación en el que se compara cada par de elementos adyacentes y los elementos se intercambian si no están en orden.
* **MySort**: Método de clasificación personalizado.
* **Main**: Es el punto de entrada del programa, donde se inicia y finaliza el control.
* **args**: El parámetro args almacena todos los argumentos de la línea de comandos que proporciona el usuario cuando ejecuta el programa.
* **j**: Variable usada en las instrucciones condicionales como contador.
* **i**: Variable usada em las instrucciones condicionales como contador.
* **Length**: Cuenta el número de caracteres de una cadena, incluidos todos los espacios y devuelve el número.
* **Console**: Representa los flujos estándar de entrada, salida y error para aplicaciones de consola. Esta clase no puede heredarse.
* **WriteLine**: Este método es el que se usa para mostrar texto en la consola, el método escribe en la pantalla el valor que le pasemos como parámetro
* **Write**: Escribe la representación de texto del valor o valores especificados en el flujo de salida estándar.
* **Read**: Lee el siguiente carácter del flujo de entrada estándar.
* **Funciona**: Comprueba el funcionamiento del Step 1.
Los indicadores son tokenizados utilizando la siguiente expresión regular: `^([a-zA-Z_][a-zA-Z\\d_$]*)$`

# Palabras reservadas
Los siguientes nombres no son válidos como identificadores ya que tienen un significado especial en el lenguaje: 

**abstract, as, base, bool, break, byte, case, catch, char, checked, class, const,
 continue, decimal, default, delegate, do, double, else, enum, event, explicit, extern,
 false, finally, fixed, float, for, foreach, goto, if, implicit, in, int, interface, internal, lock,
 is, long, namespace, new, null, object, operator, out, override, params, private,
 protected, public, readonly, ref, return, sbyte, sealed, short, sizeof, stackalloc, static,
 string, struct, switch, this, throw, true, try, typeof, uint, ulong, unchecked, unsafe, ushort,
 using, virtual, void, while**.
 
 Las palabras usadas en este código son:
|  Original |  En lexer |
|---|---|
| using  | 'USAR'  |
|  namespace |  'ESPACIO_NOMBRES' |
|  class | 'CLASE'  |
|  static | 'ESTATICO'  |
|new   |  'NUEVO' |
| if  |    'CONDICIONAL'|
|  for  |'BUCLE_PARA'|
|  foreach |  'BUCLE_RECORRIDO' |
|  while |  'BUCLE_MIENTRAS' |
|  private |   'ACCESO_PRIVADO'|
| public  | 'ACCESO_PUBLICO'  |
| in  |   'DENTRO_DE'|
| true |  'VERDADERO' |
| false | 'FALSO'  |
| return | 'RETORNAR'  |

# Operadores y operadores compuestos
Un operador en C# es un símbolo formado por uno o más caracteres que permite
realizar una determinada operación entre uno o más datos y produce un resultado.Hay que tener en cuenta que C# permite la redefinición del significado de la mayoría de los operadores según el tipo de dato sobre el que se apliquen. En este código se usaron de 4 tipos: **Aritméticos, relacionales, de asignación y lógicos.**


#### Tabla de operadores

|  Original |  En lexer |
|---|---|
| = | 'ASIGNAR' |
|  + |  'SUMAR'|
|  - | 'RESTAR'  |
|  / | 'DIVIDIR'  |
|*   |  'MULTIPLICAR' |
| %  |  'MODULO' |
| >  |    'MENOR_QUE'|
|  <  |'NEGACION'|
|  ! |  'BUCLE_RECORRIDO' |
|  & |   'AND_LOGICO'|
| \|  | 'OR_LOGICO'  |

#### Tabla de operadores compuestos

|  Original |  En lexer |
|---|---|
| >= |  'MAYOR_IGUAL'|
|  <= | 'MENOR_IGUAL' |
|  ++ |  'INCREMENTO'|
|  -- | 'DECREMENTO'|
|==   | 'COMPARAR_IGUAL' |
| ===  | 'COMPARAR_IGUAL_TIPADO' |
|  != |'COMPARAR_DIF'|
|  && | 'AND_LOGICO_CONDICIONAL'  |
|  \|\|  |  'OR_LOGICO_CONDICIONAL' |



# Tipos de datos
Los tipos de datos básicos son ciertos tipos de datos tan comúnmente utilizados en la
escritura de aplicaciones que en C# se ha incluido una sintaxis especial para tratarlos. Por ejemplo, para representar números enteros de 32 bits con signo se utiliza el tipo de
dato System.Int32 definido en la BCL, aunque a la hora de crear un objeto a de este tipo
que represente el valor 2 se usa la siguiente sintaxis:
 
 `System.Int32 a = 2;`
 
Dado lo frecuente que es el uso de este tipo también se ha predefinido en C# el alias int para el mismo, por lo que la definición de variable anterior queda así de compacta:

`int a = 2; ` 

#### Tabla de tipo de datos
|  Original |  En lexer |
|---|---|
| int |'TIPO_ENTERO' |
|  string | 'TIPO_CADENA'|
|  void | 'TIPO_VACIO' |
|  bool | 'TIPO_BOOLEANO'  |
|char |  'TIPO_CARACTER'|
| float  |    'TIPO_FLOTANTE'|
|  double |'TIPO_DOUBLE'|


# Caracteres especiales
Son los caracteres usados para poder construir las instrucciones programáticas en C# entre ellos se encuentran:

#### Tabla de puntuacion


|  Original |  En lexer |
|---|---|
| . |'PUNTO' |
|  ; | 'PUNTO_COMA'|
|  \' | 'COMILLA_SIMPLE' |
|  , | 'COMA' |
|( | 'PAREN_IZQ' |
| )  |   'PARENT_DER' |
|  [ |'CORCHETE_IZQ'|
|  ] |  'CORCHETE_DER'|
|" | 'COMILLA_DOBLE' |
| {  |  'LLAVE_IZQ'  |
|  } |'LLAVE_DER'|



