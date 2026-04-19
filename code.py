# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)

# -----------------------------------

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_ "
    return result


def get_available_letters(letters_guessed):
    result = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            result += letter
    return result


def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    guesses = 6
    warnings = 3
    letters_guessed = []

    while guesses > 0:
        print("\nYou have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        # invalid input
        if not guess.isalpha() or len(guess) != 1:
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left.")
            else:
                guesses -= 1
                print("Oops! That is not a valid letter. You lost one guess.")
            continue

        # already guessed
        if guess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left.")
            else:
                guesses -= 1
                print("Oops! You've already guessed that letter. You lost one guess.")
            continue

        letters_guessed.append(guess)

        # correct guess
        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            if guess in "aeiou":
                guesses -= 2
            else:
                guesses -= 1

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            score = guesses * len(set(secret_word))
            print("Your total score is:", score)
            return

    print("Sorry, you ran out of guesses. The word was:", secret_word)


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")

    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if my_word[i] == "_":
            if other_word[i] in my_word:
                return False
        elif my_word[i] != other_word[i]:
            return False

    return True


def show_possible_matches(my_word):
    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)

    if len(matches) == 0:
        print("No matches found")
    else:
        print(" ".join(matches))


def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    guesses = 6
    warnings = 3
    letters_guessed = []

    while guesses > 0:
        print("\nYou have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        # hint feature
        if guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue

        if not guess.isalpha() or len(guess) != 1:
            if warnings > 0:
                warnings -= 1
                print("Invalid input. Warnings left:", warnings)
            else:
                guesses -= 1
                print("Invalid input. Lost one guess.")
            continue

        if guess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Already guessed. Warnings left:", warnings)
            else:
                guesses -= 1
                print("Already guessed. Lost one guess.")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Wrong guess:", get_guessed_word(secret_word, letters_guessed))
            if guess in "aeiou":
                guesses -= 2
            else:
                guesses -= 1

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            score = guesses * len(set(secret_word))
            print("Your total score is:", score)
            return

    print("Sorry, you lost. The word was:", secret_word)


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)

    # For hints version, comment above and use below:
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)