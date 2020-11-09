import random
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
            dataExtracted = "" #Datos extraidos de la memoria principal
            for i in range(X, Y+1):
              dataExtracted += mainMemo.content[i]
            block.validation = "1"
            block.tag = address.tag
            block.data = dataExtracted
            self.cola.append([block.tag, address.index])
            break
      else:
        ## No hay espacio, entonces aplicamos la política de FIFO
        fifo = self.cola.popleft() ## Tomamos el primer elemento que se agregó
        tag, idx = fifo[0], fifo[1]
        pos = int(idx, 2)

        ## Posiciones en la memoria principal
        X = int( tag+idx+("0"*len(address.offset)), 2)
        Y = int( tag+idx+("1"*len(address.offset)), 2)
        dataExtracted = "" #Datos extraidos de la memoria principal
        for i in range(X, Y+1):
          dataExtracted += mainMemo.content[i]
        
        for block in self.content[pos]:
          if block.tag == tag and block.dirty == "0":
            ##Como son iguales y están en el mismo indice
            block.data = dataExtracted
            self.cola.append([block.tag, idx])
            break
          elif block.tag == tag and block.dirty == "1":
            ##Hay que actualizar main memory
            block.dirty = "0"
            mainMemo.updateRAM(X, Y, block.data)
            self.cola.append([block.tag, idx])
            break

  ## Metodo de escritura -> Escribir en la memoria caché con un address
  def write(self, stringAddress, mainMemo):
    ##Escribir

    ##Recibe un objeto de la clase address
    address = Address(stringAddress)
    pos = int(address.index, 2)

    randomData = random.randint(0, 18446744073709551615)
    data = "{0:064b}".format(randomData)

    flag = False
    isSpace = False

    for block in self.content[pos]:
      ## La bandera significa que encontramos la etiqueta en el conjunto, True si la encontramos, False en caso contrario
      if block.tag == address.tag:
        flag = True
        ## Modificamos en la memoria cache
        block.data = data
        block.dirty = "1"
      if block.validation == "0":
        isSpace = True
    
    if flag == False:
      if isSpace == True:
        ## Aun hay espacio y podemos agregar el bloque
        for block in self.content[pos]:
          if block.validation == "0":
            ##Agregar el bloque
            block.dirty = "1"
            block.validation = "1"
            block.tag = address.tag
            block.data = data
            self.cola.append([block.tag, address.index])
            break
      else:
        ## No hay espacio, entonces aplicamos la política de FIFO
        fifo = self.cola.popleft() ## Tomamos el primer elemento que se agregó
        tag, idx = fifo[0], fifo[1]
        pos = int(idx, 2)

        for block in self.content[pos]:
          if block.tag == tag:
            ##Como son iguales y están en el mismo indice
            block.data = data
            block.dirty = "1"
            self.cola.append([block.tag, idx])
            break