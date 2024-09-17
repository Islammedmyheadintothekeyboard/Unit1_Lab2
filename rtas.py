
class Rat:

  def __init__(self, gender, weight):
    self.gender = gender
    self.weight = int(weight)
    self.litter = 0

  def __str__(self):
    return str(self.weight)

  def __repr__(self):
    return str(self.weight)
  
  def getweight(self):
    return self.weight

  def getsex(self):
    return self.gender

  def canbreed(self):
    if self.litter >= 5:
      return False
    else:
      return True

  def mute(self, muteval):
    self.weight *= muteval
    self.weight = int(self.weight)


  def __lt__(self, othweight):
    return self.getweight() < othweight.getwight()

  def __gt__(self, othweight):
    return self.getweight() > othweight.getweight()
  
  def __le__(self, othweight):
    return self.getweight() <= othweight.getweight()

  def __ge__(self, othweight):
    return self.getweight() >= othweight.getweight()

  def __eq__(self, othweight):
    return self.getweight() == othweight.getweight()