class KDA :
    rank = None
    def __init__ (self,kill,dead,asist):
        self.kill = kill
        self.dead = dead 
        self.asist = asist
    
    def getname(self):
        return self

    def kalkulasi(self):
        jumlah = self.kill +(self.asist * 0.75)-(self.dead * 0.5)
        print('KDA player adalah', jumlah)
        if(jumlah > 10):
            rank = ('GOLD')
        elif(jumlah <=10 and jumlah >=6):
            rank = ('SILVER')
        else:
            rank = ('BRONZE')
        print('rank player',rank)

pertama = KDA(2,10,1)
pertama.kalkulasi()