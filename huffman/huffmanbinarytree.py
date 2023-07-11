

class HuffmanBinaryTree:
  """
  Clase que implementa un árbol binario de Huffman
  Autor:<Maria Camila Arcos
           Ricardo Arrubla
          Juan Camilo  Molina>
  """ 
  def __init__(self):
    """
    Constructor de la clase
    """
    self.key = None
    self.left = None
    self.right = None


  def getNumberKey(self):
    """
    Retorna el valor de la llave, 
    si es un string retorna -1, si es un 
    numero retorna el numero.
    """
    if isinstance(self.key, int) or isinstance(self.key, float):
            return self.key
    return -1

  def getLeft(self):
    """
    Retorna el hijo izquierdo del arbol.
    """
    return self.left
  

  def getRight(self):
    """
    Retorna el hijo derecho del arbol.
    """
    return self.right
