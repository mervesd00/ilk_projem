# print("""********************
#       sisteme hosgeldiniz!
      
# ********************
# """)
# sys_kullaniciadi="mdilayy"
# sys_pasword="12345"
# counter=3
# while True:
#     kullaniciadi= input("kullanici adinizi girin:")
#     pasword=input("pasword giriniz:")
 
#     if (sys_kullaniciadi!=kullaniciadi and sys_pasword!=pasword):
#         print("kullanici adi ve pasword hatali!")
#         counter-=1
#     elif(sys_kullaniciadi==kullaniciadi and sys_pasword!=pasword):
#         print("pasword hatali!")
#         counter-=1
#     elif(sys_kullaniciadi!=kullaniciadi and sys_pasword==pasword):
#         print("kullanici adi hatali!")
#         counter-=1
#     elif(sys_kullaniciadi==kullaniciadi and sys_pasword==pasword):
#         print("hesabininza giris yapiliyor...")
#         break
#     if counter==0 :
#         print("cok fazla hatali giris sistemden cikiliyor..")
#         break

# print("""
#       *********************
#       ATM islemler:
#       1.islem=bakiye sorgulama
#       2.islem=para yatirma
#       3.islem=para cekme
#       !sistemden cikmak icin "q" tusuna basin!
#       **********************""")
# bakiye=1000
# while True:
#     islem=input("yapmak istediginiz islemi secin:")
#     if islem=="q":
#         print("cikis yapiliyor...")
#         break
#     elif islem=="1":
#         print("bakiyeniz={}".format(bakiye))
#     elif islem=="2":
#         miktar=int(input("yatirmak isytediginiz miktari girn:"))
#         bakiye+=miktar
#     elif islem=="3":
#         miktar=int(input("cekmek isytediginiz miktari girn:"))
#         if bakiye-miktar<0:
#             print("yetersiz bakiye...")
#             continue
#         bakiye-=miktar


# while True:
#     sayi=input("bir sayi giriniz:")
#     if sayi=="q":
#         print("programdan cikiliyor...")
#         break
#     else:
#         sayi=int(sayi)
#         faktoriyel=1
#         for x in range(2,sayi+1):
#             faktoriyel*=x
#         print(" {}!={}".format(sayi,faktoriyel))

# a=1
# b=1
# fibonaci=[a,b]
# for i in range(20):
#     a,b=b,a+b     #aynı anda atama yapman gerkliyse iki atmanın arasınına = koy
#     fibonaci.append(b)
# print(fibonaci)







