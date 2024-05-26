import random
words =['python','java','kotlin','javascript','ruby','swift']

# Randomly choose a word from the letter
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8 # number of allowed attepmts

print("Welcome to Hangman!")

while attempts > 0  and '_' in word_display:
    print("\n"+' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess #reveal letter
    else:
        print("The letter doesnt appear in the word, Sorry!")
        attempts -= 1 # reducing the attempts


# Game conclusion

if '_' not in word_display:
     print("You guessed the word!")
     print(' '.join(word_display))
     print("You Survived!")
else:
    print("Your ran out of attepmts. The word was"+ chosen_word)
    print('You lost!')