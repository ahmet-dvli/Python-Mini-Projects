# Basit bir sekilde film veya kitap öneren bir program yazıcaz 


import random

recommendations = {

        " funny": ["The Mask","Superbad","Pineapple"],
        " thriller": ["Se7en","Gone Girl","Shutter Island"],
        " science fiction": ["Interstellar","Inception","Matrix"],
        " drama": ["The Pursuit of Happyness","Forrest Gump", "The Green Mile"]
}



def get_user_interest():
    interest = input("Enter your favorite genre (funny,thriller,science fiction,drama)").lower() 
    return interest



def recommend(interest):
    if interest in recommendations:
 
     print("My suggestion to you", random.choice(recommendations[interest]).lower())
        
    else:
        print("Unfortunately, I don't have any suggestions for this category.")

def main():
    print("Welcome to the book or movie recommendation site.")
    while True:
        user_interest = get_user_interest()
        recommend(user_interest)

        again = input("Would you like another suggestion ? (yes/no: ").lower()
        if again != "yes":
            print("See you later.")
            break

 
if __name__ == "__main__":
    main() 
  
# Evet bu kodda böyleydi. Bunu değiştirerek kitapda yapabilirsiniz.

 