import random

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Welcome to Hangman!")
    
    word = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6  # Adjust the number of attempts allowed
    
    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", max_attempts - incorrect_attempts)
        print("Guessed letters:", guessed_letters)
        
        guess = input("Guess a letter or the whole word: ").lower().strip()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Oops! That letter is not in the word.")
                incorrect_attempts += 1
        elif len(guess) > 1 and guess.isalpha():
            if guess == word:
                print("Congratulations! You guessed the word:", word)
            else:
                print("Sorry, that's not the word.")
                incorrect_attempts += 1
        else:
            print("Invalid input. Please enter a valid letter or word.")
            continue
        
        if incorrect_attempts >= max_attempts:
            print("\nSorry, you lost! The word was:", word)
            break
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
