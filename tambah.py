class tambah :
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
     
    def tambah(self):
       hasil = self.a + self.b
       print(hasil)
a = tambah(1,1)
a.tambah()