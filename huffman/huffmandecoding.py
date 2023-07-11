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
        pass

    def decode(self, text, tree):
        """
        Decodifica un texto en base a un árbol de Huffman.
        :param text: texto a decodificar
        :param tree: árbol de Huffman
        :return: texto decodificado
        """
        if not text or not tree:
            return ""


        decoded_text = ""
        node = tree

        for bit in text:
            if bit == "0":
                node = node.getLeft()
            else:
                node = node.getRight()

            if node.getNumberKey() != -1:
                decoded_text += str(node.getNumberKey())
                node = tree

        return decoded_text