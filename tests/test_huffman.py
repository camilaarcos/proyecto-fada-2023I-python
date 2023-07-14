import pytest
from huffman.huffmancoding import HuffmanCoding
from huffman.huffmandecoding import HuffmanDecoding



@staticmethod
def verify_tree(tree):
    """
    Verifica que el árbol de Huffman sea válido.
    :param tree: árbol de Huffman
    :return: True si el árbol es válido, False de lo contrario
    """
    key = tree.getNumberKey()
    if key != -1:
        left = tree.getLeft()
        right = tree.getRight()

        if left is not None and right is not None:
            condition = key >= left.getNumberKey() and key >= right.getNumberKey()
            return condition and verify_tree(left) and verify_tree(right)
        else:
            if left is None:
                condition = key >= right.getNumberKey()
                return condition and verify_tree(right)
            else:
                if right is None:
                    condition = key >= left.getNumberKey()
                    return condition and verify_tree(left)
                else:
                    return True
    else:
        return True

@pytest.mark.parametrize("filename", ["ejemplo1.in", "ejemplo2.in", "ejemplo3.in"])
def test_files(filename):
    with open(f'resources/{filename}', 'r') as file:
        text = file.read()

    coding = HuffmanCoding()
    encoded = coding.encode(text)
    tree = coding.getTree()

    decoding = HuffmanDecoding()
    decoded = decoding.decode(encoded, tree)

    assert verify_tree(tree)
    assert text == decoded
