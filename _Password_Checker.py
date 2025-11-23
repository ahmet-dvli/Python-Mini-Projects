 # python_password_checker.py
# (SIMPLE)



class PasswordChecker:
    def __init__(self,password):
        self.password = password

    def check_length(self):
        return len(self.password) >= 8
    
    def has_upper(self):
        return any(c.isupper() for c in self.password)
    
    def has_lower(self):
        return any(c.islower() for c in self.password)
    
    def has_digit(self):
        return any(c.isdigit() for c in self.password)
    
    def has_special(self):
        special_chars = "!?*@%+^"
        return any(c in special_chars for c in self.password)
    
    def is_strong(self):
        return all([
            self.check_length(),
            self.has_upper(),
            self.has_lower(),
            self.has_digit(),
            self.has_special()
        ])
if __name__ == "__main__":
    password = input("Şifre girin: ")
    checker = PasswordChecker(password)

    if checker.is_strong():
        print("Şifre güçlü!")
    else:
        eksik = []
        if not checker.check_length():
            eksik.append("en az 8 karakter")
        if not checker.has_upper():
            eksik.append("büyük harf")
        if not checker.has_lower():
            eksik.append("küçük harf")
        if not checker.has_digit():
            eksik.append("rakam")
        if not checker.has_special():
            eksik.append("özel karakter (!@#$%^&*)")

        print("Şifre zayıf! Eksik kriterler:", ", ".join(eksik))