class player :
    masukan = None
    def __init__ (self):
        self.level=None
        self.name =None
        self.mana = None
        self.health = None
    def setlevel(self):
        while True:
            print('masukan level :')
            masukan = input()
            if int(masukan) >0 and int(masukan) <101:
                self.level=masukan
                break
            else :
                print('input salah')
    def setname(self):
         while True:
            print('masukan nama :')
            masukan = input()
            if len(masukan) > 3 :
                self.name=masukan
                break
            else :
                print('input salah')
    def setmana (self):
        while True :
            print('masukan jumlah mana :')
            masukan= input()
            if int(masukan) >=0 and int(masukan) <101:
                self.mana=masukan
                break
            else :
                print('input salah')
    def sethealth(self):
        self.health = (int(self.level) * int(self.mana) + (int(self.level) + 100))

    def printinfo(self):
        print('nama :',self.name,'level :',self.level,'health',self.health,'mana :',self.mana)

a= player()
a.setlevel()
a.setname()
a.setmana()
a.sethealth()
a.printinfo()

b= player()
b.setlevel()
b.setname()
b.setmana()
b.sethealth()
b.printinfo()