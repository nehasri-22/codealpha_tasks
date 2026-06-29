# codealpha_tasks
import random
# Predefined list of words
words = ["apple", "banana", "grapes", "orange", "mango"]
# Choose a random word
word = random.choice(words)
# To store guessed letters
guessed_letters = []
# Number of incorrect guesses allowed
max_attempts = 6
attempts_left = max_attempts
print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
# Game loop
while attempts_left > 0:
    display_word = ""
    # Show current progress
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())
    print("Attempts left:", attempts_left)
    print("Guessed letters:", guessed_letters)
    # Check if player has won
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word:", word)
        break
    # Take input
    guess = input("Enter a letter: ").lower()
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue
    # Add guess to list
    guessed_letters.append(guess)
    # Check correctness
    if guess in word:
        print("✅ Good guess!")
    else:
        print("❌ Wrong guess!")
        attempts_left -= 1
# If player loses
if attempts_left == 0:
    print("\n💀 Game Over! The word was:", word)
     neha
