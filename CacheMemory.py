from math import log2
import blockClass as block

class CacheMemory:
  def __init__(self, cntBlocks, blocksSize, cntVias):
    self.cntBlocks = cntBlocks
    self.blocksSize = blocksSize
    self.cntVias = cntVias
    self.cntSets = cntBlocks//cntVias

    ##Inicialización de la memoria caché con todos los espacios vacíos
    self.content = [ [ block("0", "0", "", "") for _ in range(cntVias) ] for _ in range(self.cntSets)  ]