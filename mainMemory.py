class MainMemory:
  def __init__(self):
    ##Abrir el archivo
    self.file = open("RAMinput.txt", "r")
    self.lines = self.file.readlines()
    self.content = []

    for line in self.lines:
      self.content.append(line.strip())