import os

secenek = input("Hangi işlem?\n Toplama\n Çıkarma\n Bölme\n Çarpma\n:")

dosya = open("Metinler.txt","a")

if secenek == "Toplama" and "toplama":
    toplama_sayi = int(input("Sayı: "))
    toplama_sayi2 = int(input("Sayı: "))
    toplama_sonuc =  toplama_sayi+toplama_sayi2
    print("Sonuç: ",toplama_sonuc)
    dosya.write("\nSonuc (Toplama)\n")
    dosya.write(str(toplama_sonuc))
    dosya.close
elif secenek == "Çıkarma" and "çıkarma":
    cikarma_sayi = int(input("Sayı: "))
    cikarma_sayi2 = int(input("Sayı: "))
    cikarma_sonuc = cikarma_sayi-cikarma_sayi2
    print("Sonuç: ",cikarma_sonuc)
    dosya.write("\nSonuc (Cikarma)\n")
    dosya.write(str(cikarma_sonuc))
    dosya.close
elif secenek == "Bölme" and "bölme":
    bölme_sayi = int(input("Sayı: "))
    bölme_sayi2 = int(input("Sayı: "))
    bölme_sonuc = bölme_sayi/bölme_sayi2
    print("Sonuç: ",bölme_sonuc)
    dosya.write("\nSonuc (Bolme)\n")
    dosya.write(str(bölme_sonuc))
    dosya.close
elif secenek == "Çarpma" and "çarpma":
    carpma_sayi = int(input("Sayı: "))
    carpma_sayi2 = int(input("Sayı: "))
    carpma_sonuc = carpma_sayi*carpma_sayi2
    print("Sonuç: ",carpma_sonuc)
    dosya.write("\nSonuc (Carpma)\n")
    dosya.write(str(carpma_sonuc))
    dosya.close
else:
    print("Hata")
