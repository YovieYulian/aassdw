class animal :
    color='ireng'
    def __init__ (self,name):
        self.name= name
    def eat(self,food):
        print(self.name,'memakan',food)
class dog(animal):
    color='puteh'
    def kejar(self,thing):
        print(self.name,'mengejar',thing)
    def cekwarna(self,color):
        print('teko animal',super().color)
        print('teko dog',dog.color)
        print('teko def dewe',color)      
class cat(animal):
    def gorogoro(self):
        print(self.name,'sedang goro goro')
class bird(animal):
    def __init__(self,name,iscanflay):
        super().__init__(name)
        self.iscanflay=iscanflay
    def terbang (self):
        print(self.name,self.iscanflay)
a = dog('asu')
a.eat('besi')
a.kejar('susu')
b = cat('koceng')
b.eat('ikan asin')
b.gorogoro()
c= bird('manuk','iso miber cok')
c.terbang()
a.cekwarna('abang')
        
