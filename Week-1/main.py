baslik="Taşıt Kredisi"
print(baslik)
baslik="Hemen SATIN AL"
print(baslik)
 
vade = 36
ekVade = 6
 
#float,decimal,double
aylikOdeme= 200.50
 
#-------------------
 
#bool, boolean, => True or False
yukselisteMi = False
 
#-------------------
 
#matematiksel operatörler
#toplama
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
 
#çıkartma
print(5 -5)
print(vade - ekVade)
 
#çarpma
print(5*5)
print(vade*2)
print(vade * ekVade)
 
#bölme
print(5/5)
print(vade/2)
print(vade/ekVade)
 
yeniVade = vade/2
fiyat = 100
indirimliFiyat = fiyat - 20
 
print(yeniVade)
print(indirimliFiyat)
 
#mod operatoru = bir sayının bir sayıya bölümünden kalan değeri hesaplama
print(10%2)
print(vade%ekVade)
 
 
#mantıksal operatorler
print(1==1) # 2 eşittir operatörü "eşit mi?"" anlamındadır ve eşit ise True döner Değilse False
print(1==2)
 
print(1 > 2) # büyüktür operatörü. büyük ise true değilse false
print(3 > 1)
 
print(1 != 1) #Eşit Değildir ifadesi. Burada false dönecek çünkü eşit
print(1 != 2) #Eşit Değildir ifadesi. Burada true dönecek çünkü eşit değil
 
#or / and keywords
# or birden fazla operatör kullanılacağı zaman kullanılır. 
# Bağlanan 2 operatörden birinin doğru olması durumunda TRUE döner
 
# and her ikisi doğru olmalı. İlk olarak çalıştırılır karışık kullanımlarda
 
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2) 
 
 
#karar yapıları ( if else  / else if)
sayi1 = 15
sayi2 = 15
# sayi1 > sayi2 ise ekrana "sayi1 daha büyük yazdır"
#if else yapısında bir karar true ise diğer kararlara uğramaz ve true olanı yazdırır direkt
#condition = şart geliyor aşağıda
if sayi1 < sayi2:
    print("sayi1 daha küçüktür")
    print("Hala if bloğu içindeyim")
 
elif sayi1 == sayi2:
    print("İki sayı eşittir")
else:
    print("Sayi1 sayi2'den büyüktür")
 
#indent önemli. mesela yukarıda ilk ifden sonra tab boşluğuyla printler yazılı ancak aşağıdaki print bunların hizasında değil.
#bu şekilde olduğunda bu print if'e bağlı değildir.
print("Burası If bloğunun disindadır")
 
 