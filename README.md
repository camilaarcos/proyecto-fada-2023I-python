# Proyecto final 2023-I FADA
## Codificación Huffmann

Existen muchos métodos para la compresión de datos, uno de estos es la codificación Huffman. Este método consiste en generar una tabla para codificar un determinado símbolo. Este método fue desarrollado por David A. Huffman mientras era estudiante y publicado en _A Method for the Construction of Minimum-Redundancy Codes_. El algoritmo de Huffman utiliza una distribución de probabilidad uniforme para codificar los símbolos.

En este proyecto usted deberá implementar el algoritmo para codificar archivos de texto que contienen los siguientes símbolos: 

No se diferencian mayúsculas de minúsculas. El algoritmo puede agrupar los símbolos para mejorar la compresión, sin embargo para efectos de este taller solo considere un símbolo a la vez.

### Codificación

Revisar esta animación [aquí](https://cmps-people.ok.ubc.ca/ylucet/DS/Huffman.html).

Asumamos que deseamos codificar el mensaje:


Inicialmente contamos la frecuencia de los datos:

| Carácter | Frecuencia |
|----------|------------|
| m        | 2          |
| i        | 2          |
| espacio  | 3          |
| p        | 2          |
| a        | 3          |
| s        | 2          |
| o        | 2          |
| n        | 1          |
| e        | 1          |
| r        | 2          |
| g        | 1          |

Esto nos genera este arbol de Huffman.

![alt text](https://github.com/cardel/proyecto-fada-2023I-python/blob/main/readme/huffman.png?raw=true)


Cada nodo interno contiene la suma de las frecuencias de los nodos hijos, y cada nodo hoja es un carácter del mensaje original. Desde este árbol, puedes generar la tabla de códigos Huffman siguiendo las ramas izquierda y derecha desde la raíz hasta cada hoja, asignando un **0** a cada borde izquierdo y un **1** a cada borde derecho.

A partir de este árbol podemos generar la codificación de los caracteres:

| Carácter | Código Huffman |
|----------|----------------|
| espacio  | 000            |
| r        | 001            |
| e        | 01000          |
| n        | 01001          |
| o        | 0101           |
| g        | 0110           |
| s        | 0111           |
| a        | 100            |
| p        | 101            |
| i        | 110            |
| m        | 111            |

Posteriormente codificamos nuestro string:

> 111110000101100011111001010100100001000011100010100101010110001100111100001

### Decodificación

Tomando el archivo binario, lo que nos permite obtener una decodificación, leemos el archivo binario y extraemos los bits.

Pasando a binario

| Código Binario | Carácter |
|----------------|----------|
| 111            | m        |
| 110            | i        |
| 000            | espacio  |
| 101            | p        |
| 100            | a        |
| 0111           | s        |
| 110            | i        |
| 0101           | o        |
| 01001          | n        |
| 000            | espacio  |
| 01000          | e        |
| 0111           | s        |
| 000            | espacio  |
| 101            | p        |
| 001            | r        |
| 0101           | o        |
| 0110           | g        |
| 001            | r        |
| 100            | a        |
| 111            | m        |
| 100            | a        |
| 001            | r        |


## Implementación

Este proyecto tiene las siguientes clases

1. La clase`HuffmanBinaryTree`implementa el árbol de Huffman. 
   - `getNumberKey()`: este método retorna la key. Si es numérica retorna el valor, en caso de no serlo retorna -1.
   - `getLeft()`: retorna el hijo izquierdo, en caso de no tenerlo retorna un puntero nulo (None o null).
   - `getRight()`: retorna el hijo derecho, en caso de no tenerlo retorna un puntero nulo (None o null).
2. La clase `HuffmanCoding`, se encarga de codificar un string a binario
   - `encode(cadena)`: este método recibe la cadena y genera el árbol correspondiente y retorna la cadena codificada en binario como String.
   - `getTree()`: este método retorna el árbol.
   - `getTable()`: este método retorna una HashMap (Java) o un diccionario (Python) conteniendo la tabla de la codificación.
   - `getSummary()`: este método retorna un HashMap (Java) o un diccionario (Python) con la siguiente información:
     - Porcentaje de compresión.
     - Número de nodos del árbol.
     - Profundidad del árbol.
3. La clase `HuffmanDecoding`, se encarga de transformar de binario a string.
   - `decode(cadena, arbol)`: `cadena` es una secuencia de 0 y 1 como String y `arbol` es un objeto de tipo HuffmanBinaryTree.

