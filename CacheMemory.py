from math import log2
from collections import deque
from blockClass import Block
from AddressClass import Address

class CacheMemory:
  def __init__(self, cntBlocks, blocksSize, cntVias):
    self.cntBlocks = cntBlocks
    self.blocksSize = blocksSize
    self.cntVias = cntVias
    self.cntSets = cntBlocks//cntVias
    self.cntHits = 0
    self.cntMiss = 0
    self.cola = deque() #Unicamente la etiqueta y el indice -> [tag, idx]

    ##Inicialización de la memoria caché con todos los espacios vacíos
    self.content = [ [ Block("0", "0", "", "") for _ in range(cntVias) ] for _ in range(self.cntSets)  ]
  
  ## Metodo de escritura -> Leer de la memoria caché con un address
  def read(self, stringAddress):
    ##Recibe un objeto de la clase address
    address = Address(stringAddress)

  ## Metodo de lectura -> Escribir en la memoria caché con un address
  def write(self, stringAddress):
    ##Recibe un objeto de la clase address
    address = Address(stringAddress)