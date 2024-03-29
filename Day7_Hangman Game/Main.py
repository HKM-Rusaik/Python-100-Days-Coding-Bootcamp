import random
from hangman_word import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

display = []
for letter in range(word_length):
    display += "_"



while not end_of_game:
    guess = input("Guess a letter : ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.!")
            print(chosen_word)
       
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    from hangman_art import stages
    print(stages[lives])