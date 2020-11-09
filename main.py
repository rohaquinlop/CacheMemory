from interface import interfaz as I
from CacheMemory import CacheMemory as cacheMem
from mainMemory import MainMemory

def main():
  """
  Tamaño del bloque = 8 bytes
  Bloques en Cache = 16
  Número de vías = 2
  """
  cache = cacheMem(16, 8, 2)
  mainMem = MainMemory()

  I(cache, mainMem)

  ##Guardar los datos en txt
  cacheFile = open("cacheOutput.txt", "w")

  for c in cache.content:
    line = "|{}|{}|\n".format(c[0].dirty+" "+c[0].tag + " "+ c[0].data, c[1].dirty+" "+c[1].tag + " " + c[1].data)
    cacheFile.write(line)
  
  totalRates = cache.cntHits+cache.cntMiss
  if totalRates > 0:
    line = "- - - - -\n"
    totalRates = cache.cntHits+cache.cntMiss
    hitsRate = (cache.cntHits*100)/totalRates
    line += "Hits rate: {:.2f}% | Miss rate: {:.2f}%\n".format( hitsRate, 100-hitsRate)
    line += "- - - - -\n"
    cacheFile.write(line)

  cacheFile.close()

  ##Guardar los datos en txt
  RAMoutput = open("RAMoutput.txt", "w")

  for c in mainMem.content:
    line = "{}\n".format(c)
    RAMoutput.write(line)

  RAMoutput.close()


main()