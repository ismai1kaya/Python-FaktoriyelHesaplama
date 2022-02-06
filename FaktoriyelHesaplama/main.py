print("**************\nFAKTÖRİYEL HESAPLAMA\n\n"
      "Çıkış yapmak için q'ya basınız\n**************")

while True:

    sayi = input("Hesaplamak istediğiniz sayıyı giriniz:")

    if(sayi == "q"):
        print("Programdan Çıkılıyor...")
        break
    sayi = int(sayi)
    faktoriyel =1

    for i in range(1,sayi+1):
        faktoriyel *=i

    print("{} sayısının faktöriyeli {}'dır".format(sayi, faktoriyel))

