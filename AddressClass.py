class Address:
  def __init__(self, string):
    self.tag = string[0:5]
    self.index = string[5:8]
    self.offset = string[8:11]