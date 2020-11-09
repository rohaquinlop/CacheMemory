class MainMemory:
  def __init__(self):
    ##Abrir el archivo
    self.file = open("RAMinput.txt", "r")
    self.lines = self.file.readlines()
    self.content = []

    for line in self.lines:
      self.content.append(line.strip())
  
  def updateRAM(self, X, Y, data):
    idx = 0
    for i in range(X, Y+1):
      self.content[i] = data[idx:idx+8]
      idx += 8