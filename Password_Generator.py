# Bu mini projede ise ufak bir şifre olusturucu yaptık. Tabi burda siz "Letters" kısmını istediginiz gibi anahtar kelimeler de ekleyerek daha da sağlama alabilirsiniz.

import random


def Password_Generator(long):
    Letters = ["A","b","c","D","G","h","u","T","e","g","Q","x","Z","b","M","n","İ","!","?"]
    
    password = ""

    for i in range(long):
        chosen = random.choice(Letters)
        password += chosen
    return password

long = int(input("long: "))

print(Password_Generator(long))