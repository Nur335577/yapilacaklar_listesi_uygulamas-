def menu():
    print("Yapılacaklar Listesine Hoş Geldiniz!")
    print("1 - listeye ekleme yap")
    print("2 - listeden silme yap")
    print("3 - çıkış yap ")
    print("4 - yapılacaklar listesini görüntüle")

menu()
my_list = []

def tekrar():
    print("5 - Menüyü dön...")

while True :
    tekrar()
    sec = input("Gerçekleştirmek istediğiniz işlemi seçiniz :")

    if (sec == "1"):
        ekle = input("Listeye ekleme yap :")
        my_list.append(ekle)
    elif (sec == "5"):
        menu()
    if (sec =="2") :
        sil = input("listeden silmek istediğiniz şeyi seçin :")
        try:
          my_list.remove(sil)
        except:
            print(f"{sil} listede tanımlı değildir...")
    elif (sec == "5"):
        menu()
    if (sec == "3"):
        print("çıkış yapılıyor...")
        break
    if (sec == "4"):
      print(my_list)
    elif (sec == "5"):
        menu()






