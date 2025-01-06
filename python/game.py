import random

# List of words to guess from
words = ["ghost", "modi", "supercomputer"]
word = random.choice(words)

# Initialize game variables
total_chances = 10
guessed_word = "-" * len(word)
guessed_letters = []

print("Welcome to the game of guessing the word!")
print("You have 10 chances to guess the word.")
print(f"The word has {len(word)} letters.")
print("The word is", guessed_word)

# Game loop
while total_chances > 0 and guessed_word != word:
    print(f"\nYou have {total_chances} chances left.")
    letter = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if letter in guessed_letters:
        print("You already guessed that letter. Try a different one.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(letter)

    # Check if the guessed letter is in the word
    if letter in word:
        print(f"Good guess! The letter {letter} is in the word.")
        # Update guessed_word with the correct letter
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
    else:
        total_chances -= 1
        print(f"Wrong guess! The letter {letter} is not in the word.")
    
    # Display the current guessed word
    print("The word is", guessed_word)

    # Check if the player has guessed the word correctly
    if guessed_word == word:
        print(f"Congratulations! You've guessed the word {word} correctly!")
        break

if guessed_word != word:
    print(f"Sorry, you've run out of chances. The word was {word}.")
