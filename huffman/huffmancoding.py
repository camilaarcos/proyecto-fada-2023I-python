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
            lo = heap.pop(0)
            hi = heap.pop(0)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
            heap.sort(key=lambda x: x[0])
        self.tree = heap[0]
        # Utiliza una estructura de datos llamada heap para construir
        # el arbol de manera eficiente
        # Paso 3: Generar la tabla de codificación
        self.table = {char: code for char, code in self.tree[1:]}

        # Paso 4: Codificar el texto
        encoded_text = ''.join(self.table[char] for char in text)

        return encoded_text


    def getTree(self):

        return self.tree

    def getTable(self):

        return self.table



    def getSummary(self):

        compression_percentage = self._calculate_compression_percentage()
        num_nodes = self._count_nodes(self.tree)
        depth = self._calculate_depth(self.tree)
        # Crea el resumen
        summary = {
            "Porcentaje de compresión": compression_percentage,
            "Número de nodos del árbol": num_nodes,
            "Profundidad del árbol": depth
        }

        return summary


    def _calculate_compression_percentage(self):
        if self.tree is None:
            return 0

        original_size = len(''.join(self.table.keys())) * 8
        encoded_size = len(''.join(self.table.values()))
        compression_percentage = (original_size - encoded_size) / original_size * 100
        return compression_percentage


    def _count_nodes(self, tree):
        if tree is None:
            return 0
        return 1 + self._count_nodes(tree.left) + self._count_nodes(tree.right)


    def _calculate_depth(self, tree):
        if tree is None:
            return 0
        return 1 + max(self._calculate_depth(tree.left), self._calculate_depth(tree.right))

