list_metotları = []
for metot in dir(list):
    if metot.startswith("__"):
        continue
    list_metotları.append(metot)

set_metotları = []
for metot in dir(set):
    if metot.startswith("__"):
        continue
    set_metotları.append(metot)

string_metotları = []
for metot in dir(str):
    if metot.startswith("__"):
        continue
    string_metotları.append(metot)

tuple_metotları = []
for metot in dir(tuple):
    if metot.startswith("__"):
        continue
    tuple_metotları.append(metot)

dict_metotları = []
for metot in dir(dict):
    if metot.startswith("__"):
        continue
    dict_metotları.append(metot)
# Bunu böyle yaparak aslında bu metotların hepsi bir listede tutulmuş oluyor.
Baslıklar = ["List Metotları","Set Metotları","String Metotları","Tuple Metotları","Dict Metotları"]
Sınıflar = [list_metotları, set_metotları, string_metotları, tuple_metotları, dict_metotları]

# Aslında listeleme islemimiz burda bitti sayılır.Ama eğer bunu calıstırırsak en uzun kelimeye sahip olana göre listeleyeceği icin önceki "metotların" kelimesi bitince kalan yerlerede "--" isareti gelicek bunu önlemek için ise önce en fazla kelimeye sahip olan "metotdu" buluyoruz.
max_len = 0
for sınıf in Sınıflar:
    if len(sınıf) > max_len:
        max_len = len(sınıf)

with open("Metotlar.txt", "w") as f:
# Bu yukarıda yazdığımız aslında bize en uzun listeyi bulmamızı sağlayacaktır.
    for baslık in Baslıklar:
        print(baslık,end="")
        print(" "* (30 - len(baslık)),end="")
        f.write(baslık)
        f.write(" " * (30 - len(baslık)))
    for i in range(max_len):
        print()
        f.write("\n")
        for sınıf in Sınıflar:
            if i >= len(sınıf):
                print("-------" , end="")
                print(" " * 23,end="")
                f.write("-------")
                f.write(" " * 23)
            else:
                print(sınıf[i],end="")
                print(" " * (30 - len(sınıf[i])),end="")
                f.write(sınıf[i])
                f.write(" " * (30 - len(sınıf[i])))
# Evet aslında tamamen böyleydi bu minik proje burda ufak bir yardım aldığım bir youtube kanalı olan "Pythonà Giriş" adlı kanala çok teşekkkür ederim.
