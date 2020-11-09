import random
from blockClass import Block
from AddressClass import Address

def interfaz(cache, mainMemo):
  Exit = False
  while not Exit:
    print("""
    - - - - - - - - - - - - -
    1) Leer de memoria cache.
    2) Escribir en memoria cache.
    3) Salir.
    """)
    opt = input("Digite su opción: ")

    for c in cache.content:
      print("|{}|{}|".format(c[0].dirty+" "+c[0].tag + " "+ c[0].data, c[1].dirty+" "+c[1].tag + " " + c[1].data))
    
    totalRates = cache.cntHits+cache.cntMiss
    if totalRates > 0:
      print("- - - - -")
      totalRates = cache.cntHits+cache.cntMiss
      hitsRate = (cache.cntHits*100)/totalRates
      print("Hits rate: {:.2f}% | Miss rate: {:.2f}%".format( hitsRate, 100-hitsRate))
      print("- - - - -")

    if opt in ["1", "2", "3"]:
      if opt == "3":
        Exit = True
      else:
        ##Leer en memoria o escribir en memoria
        ##Generar el número aleatorio

        addressRandom = random.randint(0, 2047)
        addressString = "{0:011b}".format(addressRandom)
        address = Address(addressString)

        print("Address: |{}|{}|{}|\n".format(address.tag, address.index, address.offset))
        print("- - - - -")

        if opt == "1":
          cache.read(addressString, mainMemo)
        else:
          cache.write(addressString, mainMemo)
    else:
      print("Opcion incorrecta")
    
    for c in cache.content:
      print("|{}|{}|".format(c[0].dirty+" "+c[0].tag + " "+ c[0].data, c[1].dirty+" "+c[1].tag + " " + c[1].data))
    
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

    for c in mainMemo.content:
      line = "{}\n".format(c)
      RAMoutput.write(line)

    RAMoutput.close()