

class HuffmanBinaryTree:
  """
  Clase que implementa un árbol binario de Huffman
  Autor:<Maria Camila Arcos
           Ricardo Arrubla
          Juan Camilo  Molina>
  """ 
  def __init__(self):

    self.key = None
    self.left = None
    self.right = None


  def getNumberKey(self):
    if isinstance(self.key, int) or isinstance(self.key, float):
      return self.key
    return -1

  def getLeft(self):
    return self.left
  

  def getRight(self):
    return self.right
