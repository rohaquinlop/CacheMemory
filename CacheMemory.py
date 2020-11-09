from math import log2

class CacheMemory:
  def __init__(self, cntBlocks, blocksSize, cntVias):
    self.cntBlocks = cntBlocks
    self.blocksSize = blocksSize
    self.cntVias = cntVias
    self.cntSets = cntBlocks//cntVias
    self.cntIdex = log2(sets)