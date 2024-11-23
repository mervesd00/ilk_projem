a=int(input("boyunuzu giriniz:"))
b=int(input("kilonuzu giriniz:"))
index=a/(b*b)
print("boy kilo indexsiniz:{}".format(index))

yol=int(input("arac kac km yol gitmistir:"))
lpg=int(input("arac km basina kac lt benzin harciyor:"))
lt=45
mark=yol*lpg*45
print("surucunun odemesi gereken tutar={}".format(mark))

age=int(input("please enter your age:"))
if age < 18:
    print("you cant enter this place!!")
else: 
    print("have a nice day")    


print( """******************** 
islemler:
1.toplama
2.cikarma
3.carpma
4.bolme

********************""")
op=int(input("yapmak istediginiz islemin numarsini girin:"))
x1=int(input("birinci sayiyi girin:"))
x2=int(input("ikinci sayiyi girin:"))
if op==1:
    print("sonuc:{}".format(x1+x2))
elif op==2:
    print("sonuc:",x1-x2)
elif op==3:
    print("sonuc:",x1*x2)
elif op==4:
    print("sonuc:",x1/x2)  
else:
    print("hatali islem sectiniz")


    


