import random
from words import word_list

def get_words():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    tries = 6
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []  # fixed typo from guesses_word to guessed_words

    while not guessed and tries > 0:
        guess = input("Please complete the word: ").upper()
        
        # Case 1: Player guesses a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        # Case 2: Player guesses the whole word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the correct word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = guess

        # Invalid guess
        else:
            print("Not a valid guess.")

        # Display the hangman and current progress
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # End game messages
    if guessed:
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_words()
    play(word)
    while input("Want to play again (Y/N)? ").upper() == "Y":
        word = get_words()
        play(word)


if __name__ == "__main__":
    main()
t