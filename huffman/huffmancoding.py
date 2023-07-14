from collections import defaultdict
from heapq import heappop, heappush
from huffman.huffmanbinarytree import HuffmanBinaryTree

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
        self.tree = self.heapToTree(heap)
        while len(heap) > 1:
            lo = heap.pop(0)
            hi = heap.pop(0)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
            heap.sort(key=lambda x: x[0])

        # Utiliza una estructura de datos llamada heap para construir
        # el arbol de manera eficiente
        # Paso 3: Generar la tabla de codificación
        self.table = {char: code for char, code in heap[0][1:]}

        # Paso 4: Codificar el texto
        encoded_text = ''.join(self.table[char] for char in text)

        return encoded_text
    
    def heapToTree(self,heap:list):
        lista = heap.copy()

        arbol = type(HuffmanBinaryTree())

        while len(lista) > 1:
            lo = lista.pop(0)
            hi = lista.pop(0)
            tree = HuffmanBinaryTree()

            if(type(lo) == arbol and type(hi) == arbol):
                if(lo.getNumberKey() <= hi.getNumberKey()):
                    tree.setKey(lo.getNumberKey() + hi.getNumberKey())
                    tree.setLeft(lo)
                    tree.setRight(hi)
                else:
                    tree.setKey(lo.getNumberKey() + hi.getNumberKey())
                    tree.setLeft(hi)
                    tree.setRight(lo)
                lista.append(tree)
            
            elif(type(lo) == arbol and type(hi) != arbol):
                if(lo.getNumberKey() <= hi[0]):
                    tree.setKey(lo.getNumberKey() + hi[0])
                    tree.setLeft(lo)

                    treeDer = HuffmanBinaryTree()
                    treeDer.setKey(hi[0])
                    treeDer.setValue(hi[1][0])
                    
                    tree.setRight(treeDer)
                else:
                    tree.setKey(lo.getNumberKey() + hi[0])

                    treeIzq = HuffmanBinaryTree()
                    treeIzq.setKey(hi[0])
                    treeIzq.setValue(hi[1][0])
                    
                    tree.setLeft(treeIzq)
                    tree.setRight(lo)
                lista.append(tree)

            elif(type(lo) != arbol and type(hi) == arbol):
                if(lo[0] <= hi.getNumberKey()):
                    tree.setKey(lo[0] + hi.getNumberKey())
                    
                    treeIzq = HuffmanBinaryTree()
                    treeIzq.setKey(lo[0])
                    treeIzq.setValue(lo[1][0])

                    tree.setLeft(treeIzq)
                    tree.setRight(hi)
                else:
                    tree.setKey(lo[0] + hi.getNumberKey())

                    treeDer = HuffmanBinaryTree()
                    treeDer.setKey(lo[0])
                    treeDer.setValue(lo[1][0])

                    tree.setLeft(hi)
                    tree.setRight(treeDer)
                lista.append(tree)
            
            elif(type(lo) != arbol and type(hi) != arbol):
                key = lo[0] + hi[0]
                tree.setKey(key)
                if(lo[0] <= hi[0]):

                    treeIzq = HuffmanBinaryTree()
                    treeIzq.setKey(lo[0])
                    treeIzq.setValue(lo[1][0])

                    treeDer = HuffmanBinaryTree()
                    treeDer.setKey(hi[0])
                    treeDer.setValue(hi[1][0])

                    tree.setLeft(treeIzq)
                    tree.setRight(treeDer)
                else:
                    treeIzq = HuffmanBinaryTree()
                    treeIzq.setKey(hi[0])
                    treeIzq.setValue(hi[1][0])

                    treeDer = HuffmanBinaryTree()
                    treeDer.setKey(lo[0])
                    treeDer.setValue(lo[1][0])

                    tree.setLeft(treeIzq)
                    tree.setRight(treeDer)
                lista.append(tree)

        return lista[0]


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

