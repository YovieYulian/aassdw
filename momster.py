class momster :
    def __init__ (self,level) :
        self.level= level
        self.health = None
        self.attack =  None
        self.defend = None
        self.exp = None
    def setHealth (self):
        self.health = 10 + (2*(int(self.level)/3))
    def setatk (self):
        self.attack = (2 + (1*(int(self.level)+(int(self.level)/3))
    def setdefense(self):
        self.defend =((self.level ** 3//4) + (int(self.level)/2))
    def setexp(self):
        self.exp = (25*(int(self.level)+(int(self.health)/5)))
    def printinfo(self):
        print('health',self.health,'atk',self.attack,'defense',self.defend,'exp drop',self.exp)

a = momster(5)
a.setHealth()
a.setatk()
a.setdefense()
a.setexp()
a.printinfo()