OgrenciAd = "SÜMEYYE"
OgrenciSoyad = "KARATEKİN"
sayac = 1
while sayac < 4:
    ogrenci_ad= input("Lütfen Adınızı Giriniz : ")
    ogrenci_soyad = input("Lütfen Soyadınızı Giriniz: ")
    if (ogrenci_ad!= OgrenciAd and ogrenci_soyad != OgrenciSoyad):
        print("\nAdınız ve Soyadınız Hatalı Lütfen tekrar deneyiniz..")
        sayac += 1
    elif (ogrenci_ad== OgrenciAd and ogrenci_soyad != OgrenciSoyad):
        print("\nSoyadınız Hatalı!!!, Lütfen tekrar deneyiniz..")
        sayac += 1
    elif (ogrenci_ad!= OgrenciAd and ogrenci_soyad == OgrenciSoyad):
        print("\nAdınız Hatalı!!!, Lütfen tekrar deneyiniz..")
        sayac += 1
    else:
        print("Hoşgeldin... ", OgrenciAd.capitalize())
        sayac = 5
        z = 1
    if sayac == 4:
        print("Lütfen Tekrar Deneyiniz..")
        z = 0

if z == 1:
    print(" Şimdi ders seçimi yapabilirsiniz..")

    def return_failed():
        return " Sınıfta Kaldınız.."

    dersler = ["JAVA", "PYTHON", "MATH", "OOP", "STAT","ML"]
    secilen_ders = []

    print(dersler)
    x = 1
    y = 0
    while (x < 4) and (y < 4):

        ogrenci_ders = input("Lütfen derslerinizi tek tek, minimum 3 ve maksimum 5 olarak seçiniz. ")
        if ogrenci_ders in dersler:
            secilen_ders.append(ogrenci_ders)
            print(secilen_ders)
            print(len(secilen_ders), " tane ders seçildi..")
            x += 1
        else:
            print(" Lütfen mevcut kurslardan bir kurs girin, yalnızca 4 hata hakkınız var. ")
            y += 1
        if y == 4:
            print(return_failed())

    while (3 < x <= 5):

        print(" 3 ile 5 kurs arasında seçim yapma hakkına sahipsiniz, lütfen kalan kursların adlarını doğru yazınız. ")
        devam = input(" Daha fazla ders eklemek ister misiniz; evet ise EVET, yoksa HAYIR yazınız : ")

        if devam == "EVET":
            ogrenci_ders = input("Lütfen ders seçiniz : ")
            if ogrenci_ders in dersler:
                secilen_ders.append(ogrenci_ders)
                print(secilen_ders)
                print(len(secilen_ders), " tane ders seçildi..")
                x += 1
        else:
            x += 2
            print("Sınavlarınız")
            break
    if y != 4:
        print("Seçtiğiniz dersler: ", secilen_ders, " ")

        ders_exam = input("Sınavlar için kurslardan birini seçiniz : ")
        print("Dersinizin sınavlarına girdiniz.. :", ders_exam, "dersi için")

        a = int(input("Arasınav notu giriniz:  "))
        f = int(input("Final notu giriniz:  "))
        p = int(input("Proje ödevi notu giriniz:  "))

        ortalama = (a * 30 + f * 50 + p * 20) / 100

        print("Sınavların ağırlıkları sırasıyla ; ara sınavın% 30'u, finalin% 50'si ve projenin % 20'si ")

        print(OgrenciAd.capitalize(), "bu hesaplamadan sonraki dönem ortalamanız : ", ortalama)
        if (ortalama) > 90:
            print("AA ile geçtiniz..")
        elif 70 < (ortalama) <= 90:
            print("BB ile geçtiniz..")
        elif 50 < (ortalama) <= 70:
            print("CC ile geçtiniz..")
        elif 30 < (ortalama) <= 50:
            print("DD ile geçtiniz..")
        else:
            print(" FF ile kaldınız..")