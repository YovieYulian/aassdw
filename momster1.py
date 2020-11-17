class momster :
    def __init__ (self,level):
        self.level=level
        self.health = self.setHealth() 
        self.attack = self.setatk()
        self.defend = self.setdefense()
        self.exp = self.setexp() 
    def setHealth(self):
        self.health = (10 + (2*(level/3)))
    def setatk (self):
        self.attack =( 2 + (1*(level+(level/3)))
    def setdefense(self):
        self.defend = ((level ** 3//4) + (level/2))