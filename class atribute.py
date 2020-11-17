class persons():
    def __init__ (self,nama,umur):
        self.nama = nama
        self.umur = umur
    
    def setname(self,namabaru) :
        self.nama=namabaru

    def getnama(self) :
        return self.nama      

orang1=persons('aki',17)
print(orang1.nama)
print(orang1.umur)
orang1.setname('sujo')
print(orang1.getnama())