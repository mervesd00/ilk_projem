class calisan():
    def __init__(self,isim,maas,departman):
        print("calisan sinifinin init fonk.. ")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgileri_goster(self):
        print("calisan ozellikleri")
        print("isim={}\nmaas={}\ndepartman={}".format(self.isim,self.maas,self.departman)) 
    def departman_degis(self,yeni_departman):
        self.departman= yeni_departman
calisan1=calisan("merve",1000000,"siber")
calisan1.departman_degis("yapay zeka")
calisan1.bilgileri_goster()

class yonetici(calisan):
    pass
    def zam_yap(self,miktar):
        self.maas+=miktar

yonetici1=yonetici("dilay",100000,"robotik")
yonetici1.zam_yap(5000)
yonetici1.bilgileri_goster()





        