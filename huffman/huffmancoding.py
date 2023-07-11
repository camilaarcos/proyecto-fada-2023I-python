from collections import defaultdict
from heapq import heappop, heappush

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Maria Camila Arcos
            Ricardo Arrubla
            Juan Camilo Molina>
    Version: <1>
    """
    def __init__(self):
        self.tree = None
        self.table = None
        self.summary = None

    def encode(self, text):
        """
        Codifica el texto.
        :param text: texto a codificar
        :return: texto codificado
        """
        if not text:
            return ""

        # Paso 1: Calcular la frecuencia de cada caracter en el texto
        frequencies = defaultdict(int)
        for char in text:
            frequencies[char] += 1

        # Paso 2: Construir el árbol de Huffman
        heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        self.tree = heap[0]
        #Utiliza una estructura de datos llamada heap para construir 
        #el arbol de manera eficiente
        # Paso 3: Generar la tabla de codificación
        self.table = {char: code for char, code in self.tree[1:]}

        # Paso 4: Codificar el texto
        encoded_text = ''.join(self.table[char] for char in text)

        return encoded_text


    def getTree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        return self.tree

    def getTable(self):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
        return self.table

    def getSummary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        if not self.tree:
            return ""
        
        # Calcula el porcentaje de compresión
        total_bits = sum(weight * len(code) for char, weight, code in self.tree[1:])
        compressed_bits = sum(len(code) for char, weight, code in self.tree[1:])
        compression_percentage = 100 - (compressed_bits / total_bits) * 100

        # Obtiene el número de nodos y la profundidad del árbol
        num_nodes = len(self.tree[1:])
        depth = max(len(code) for char, weight, code in self.tree[1:])

        # Crea el resumen
        summary = {
            "Porcentaje de compresión": compression_percentage,
            "Número de nodos del árbol": num_nodes,
            "Profundidad del árbol": depth
        }

        return summary