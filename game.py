import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("========================================")
    print("   WELCOME TO THE NUMBER GUESSING GAME  ")
    print("========================================")
    print("I have selected a number between 1 and 100. Can you guess it?\n")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please keep your guess between 1 and 100.")
                continue
                
            if guess < secret_number:
                print("📉 Too low! Try again.\n")
            elif guess > secret_number:
                print("📈 Too high! Try again.\n")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    play_game()
