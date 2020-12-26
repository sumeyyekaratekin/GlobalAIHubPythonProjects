# Global AI Hub Python Course Homework - 3
# Sümeyye Karatekin

import random

print("İsim Giriniz : ")
isim = str(input(""))
print("Merhaba, " + isim.capitalize() + ", Kelime Tahmin Oyununa Hoşgeldiniz..")
kelime_hayvan = ("kedi", "köpek", "tavşan", "ördek", "zürafa", "tavuk", "kaplumbağa", "leylek", "kelebek", "örümcek")
kelime_meyve = ("elma", "armut", "portakal", "şeftali", "avokado", "karpuz", "kayısı", "kiraz", "mandalina")
kelime_sebze = ("pırasa", "domates", "ıspanak", "kabak", "havuç", "patates", "patlıcan", "fasülye", "maydonoz", "brokoli")
kelime_cicek = ("menekşe", "papatya", "karanfil", "zambak", "sümbül", "leylak", "begonvil", "begonya", "orkide")

while True:
    print("Hangi kelimeyi tahmin etmek istiyorsunuz: Hayvan(1),Meyve(2), Sebze(3), Çiçek(4)")
    secim = input("Bir seçim giriniz (1 - 2 - 3 - 4 ):  ")
    if secim == "1":
        print("* * * Şimdi Hayvan tahmin et * * *")
        kelime = list(random.choice(kelime_hayvan))
    elif secim == "2":
        print("* * * Şimdi Meyve tahmin et * * *")
        kelime = list(random.choice(kelime_meyve))
    elif secim == "3":
        print("* * * Şimdi Sebze tahmin et * * *")
        kelime = list(random.choice(kelime_sebze))
    elif secim == "4":
        print("* * * Şimdi Çiçek tahmin et * * *")
        kelime = list(random.choice(kelime_cicek))
    else:
        print("\nHata!!! uygun seçim yapmadınız.")
        break
    hak = 5
    yeni_kelime = (list("_" * len(kelime)))
    harftahmin = []
    print("Toplam " + str(hak) + " hakkınız var")
    kac_harf = str(len(kelime))
    print("* * * Kelimemiz: " + kac_harf + " Karakter uzunluğundadır. * * *")
    print(yeni_kelime)

    while hak > 0 or yeni_kelime != kelime:
        tahmin = input("Lütfen bir karakter giriniz : ")
        if tahmin not in "abcçdefghıijklmnoöpqrsştuüvwxyz" or tahmin in harftahmin or len(tahmin) != 1:
            print("Geçersiz tahmin yaptınız. Lütfen tekrar deneyiniz... ")
        elif tahmin in kelime:
            for i, j in enumerate(kelime):  # enumerate()yöntem bir yinelenebilir sayacı ekler ve onu döndürür.
                # Döndürülen nesne bir numaralandırma nesnesidir.
                if tahmin == kelime[i]:
                    yeni_kelime[i] = tahmin
                    harftahmin.append(tahmin)
                    print(yeni_kelime)
        else:
            yeni_kelime = yeni_kelime
            harftahmin.append(tahmin)
            print(yeni_kelime)
            hak -= 1
        print(str(hak) + " hakkınız kaldı")
        if hak <= 0:
            print("Kaybetttiniz!!!!! Doğru Kelime : " + str(kelime))
            break
        elif yeni_kelime == kelime:
            print("Kazandınız!")
            break
    break
