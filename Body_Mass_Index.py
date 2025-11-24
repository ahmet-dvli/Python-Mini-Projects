# Bu mini projede ise vücüt kitle endeksimizin kontrolunu yapıcaz.
from datetime import datetime
def main():
    print("Welcome to Body mass index calculator.")

    height = float(input("Write your height.")) # UNUTMA int = tam sayı , float = kesirli sayı.
    weight = float(input("Write your weight."))

    height = height / 100
    BMI = weight / (height ** 2)

    if BMI >= 30:
     print(f"obese.")
    elif BMI >= 18.5 and BMI <25:
     print(f"Normal.")
    elif BMI >= 25 and BMI < 29.9:
     print(f"Overweight.")
    else:
      print(f"Underweight.")

if __name__ == "__main__":
    main()

