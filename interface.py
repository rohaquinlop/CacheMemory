import random
from blockClass import Block

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
      print("|{}|{}|".format(c[0].dirty+" "+c[0].tag, c[1].dirty+" "+c[1].tag))

    if opt in ["1", "2", "3"]:
      if opt == "3":
        Exit = True
      else:
        ##Leer en memoria o escribir en memoria
        ##Generar el número aleatorio

        addressRandom = random.randint(0, 2047)
        addressString = "{0:011b}".format(addressRandom)

        if opt == "1":
          cache.read(addressString, mainMemo)
        else:
          cache.write(addressString, mainMemo)
    else:
      print("Opcion incorrecta")