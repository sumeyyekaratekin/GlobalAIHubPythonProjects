#Global AI Hub Python Course Homework - 3
#Sümeyye Karatekin

import random
print("İsim Giriniz : ")
isim = str(input(""))
print("Merhaba, " + isim.capitalize() + ", Kelime Tahmin Oyununa Hoşgeldiniz..")
kelime_hayvan = ("Kedi", "köpek")
kelime_meyve = ("elma","armut","portakal","seftali","avokado","karpuz","kayisi","kiraz","mandalina")
kelime_sebze = ("pirasa","domates","ispanak","kabak","havuc","patates","patlican","fasulye","maydonoz","brokoli")
kelime_cicek = ("menekse","papatya","karanfil","zambak","sumbul","leylak","begonvil","begonya","orkide")

print("Hangi kelimeyi tahmin etmek istiyorsunuz: Hayvan(1),Meyve2), Sebze(3), Çiçek(4)")
secim = int(input("Bir deger giriniz : "))

while True:
    if secim <= 4 and secim >= 0 :
        if secim == 1:
            print("Şimdi Hayvan tahmin et")
            kelime = list(random.choice(kelime_hayvan))
        elif secim == 2:
            print("Şimdi Meyve tahmin et")
            kelime = list(random.choice(kelime_meyve))
        elif secim == 3:
            print("Şimdi Sebze tahmin et")
            kelime = list(random.choice(kelime_sebze))
        elif secim == 4:
            print("Şimdi Çiçek tahmin et")
            kelime = list(random.choice(kelime_cicek))
    else:
        print("\nHata!!! uygun seçim yapmadınız.")
        break


    hak = 5
    yeni_kelime = (list("_" * len(kelime)))
    harftahmin = []
    print("Toplam " + str(hak) + " hakkınız var")

    while hak > 0 or yeni_kelime != kelime:
        tahmin = input("Lütfen bir karakter giriniz : ")
        if tahmin not in "abcçdefgğhıijklmnoöpqrsştuüvwxyz" or tahmin in harftahmin or len(tahmin) != 1:
            print("Geçersiz tahmin yaptınız. Lütfen tekrar deneyiniz... ")
        elif tahmin in kelime:
            for i, j in enumerate(kelime):  #enumerate()yöntem bir yinelenebilir sayacı ekler ve onu döndürür.
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

