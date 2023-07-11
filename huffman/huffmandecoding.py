from .huffmanbinarytree import HuffmanBinaryTree
class HuffmanDecoding:
    """
    Clase HuffmanDecoding
    Esta clase se encarga de decodificar un texto en base a un árbol de Huffman
    Autor: <Maria Camila Arcos
            Ricardo Arrubla
            Juan Camilo Molina>
    Version: <1>
    """
    def __init__(self):
        self.table = None

    def decode(self, text, tree):
        """
        Decodifica un texto en base a un árbol de Huffman.
        :param text: texto a decodificar
        :param tree: árbol de Huffman
        :return: texto decodificado
        """
        if not text or not tree:
            return ""
        self.table = self._build_table(tree)
        decoded_text = ""
        current_code = ""

        for bit in text:
            current_code += bit
            if current_code in self.table:
                decoded_text += self.table[current_code]
                current_code = ''

        return decoded_text

    def _build_table(self, tree, code='', table=None):
        if table is None:
            table = {}
        if isinstance(tree, HuffmanBinaryTree):
            if tree.getNumberKey() != -1:
                table[code] = tree.value
            else:
                self._build_table(tree.left, code + '0', table)
                self._build_table(tree.right, code + '1', table)
        return table