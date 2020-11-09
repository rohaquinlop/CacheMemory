from math import log2
from collections import deque
from blockClass import Block
from AddressClass import Address
from mainMemory import MainMemory

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
  def read(self, stringAddress, mainMemo):
    ##Recibe un objeto de la clase address
    address = Address(stringAddress)
    pos = int(address.index, 2)

    flag = False
    isSpace = False

    for block in self.content[pos]:
      ## La bandera significa que encontramos la etiqueta en el conjunto, True si la encontramos, False en caso contrario
      if block.tag == address.tag:
        flag = True
      if block.validation == "0":
        isSpace = True
    
    if flag == True:
      self.cntHits += 1
    else:
      ##Ocurre un miss
      self.cntMiss += 1
      if isSpace == True:
        ## Aun hay espacio y podemos agregar el bloque
        for block in self.content[pos]:
          if block.validation == "0":
            ##Agregar el bloque
            X = int(address.tag+address.index+("0"*len(address.offset)), 2) ##Posiciones del arreglo | Inicio
            Y = int(address.tag+address.index+("1"*len(address.offset)), 2) ##Posiciones del arreglo | Fin
            dataExtracted = ""
            for i in range(X, Y+1):
              dataExtracted += mainMemo.content[i]
            block.validation = "1"
            block.tag = address.tag
            block.data = dataExtracted
            self.cola.append([block.tag, pos])
            break

  ## Metodo de lectura -> Escribir en la memoria caché con un address
  def write(self, stringAddress, mainMemo):
    ##Recibe un objeto de la clase address
    address = Address(stringAddress)