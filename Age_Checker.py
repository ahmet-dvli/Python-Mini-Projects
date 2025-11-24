# Yaş kontrolü ile ilgili mini bir proje yazalım.
from datetime import datetime


class AgeChecker():
    def __init__(self):
       print("Welcome to age checker.")

    def run(self):
      year_of_birth = int(input("Write your year of birth."))

      current_year = datetime.now().year

      Age = current_year - year_of_birth

      if Age >= 18:
        print(f"You are adult.")
      elif Age:
        print(f"You are not adult.")

if __name__ == "__main__":
    app = AgeChecker()
    app.run()
