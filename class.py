class yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgileri_goster(self):
        print("""
        yazilimci objesinin ozelliklerini
        isim: {} 
        soyisim: {}
        numara:{}
        maas:{}
        diller:{}
                                           
              
    """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller)) 

    def zam_yap(self,zam_miktari):
        print("zam yapiliyor...")

        self.maas +=zam_miktari
    def dil_ekle(self,yeni_dil): 
        print(" dil ekleniyor...")
        self.diller.append(yeni_dil)
yazilimci1=yazilimci("merve","sevtekin",5560,100,["python","c"]) 
yazilimci1.zam_yap(100)
yazilimci1.dil_ekle("c++")
yazilimci1.bilgileri_goster()
