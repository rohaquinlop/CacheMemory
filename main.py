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


main()