#Global AI Hub Python Course Homework - 2
#Sümeyye Karatekin
name=str(input("Please enter your name: ")).capitalize()
surname=str(input("Please enter your surname: ")).capitalize()
age=int(input("Please enter your age: "))
birthdate=int(input("Please enter your date of birth: "))

print("\n * * * User Information * * * ")
list=[name,surname,age,birthdate]

for i in list:
    print(i)
if(2020 - list[3] == list[2]):      #Doğum tarihi ile yaş bilgisinin doğru olması durumda çalışan kısım
    # yanlış ise else bloğu çalışacak
    if (list[2] <= 18):     #Yaşın 18 e küçük eşit olması durumunda çalışacak kısım
        print("You can't go out because it's to dangerous. #stayhome ")
    elif (list[2] > 18):    #Yaşın 18 e küçük eşit olması durumunda çalışacak kısım
        print("You can go out to the street.")
else:
    print(list)
    print("You entered incorrectly.")
