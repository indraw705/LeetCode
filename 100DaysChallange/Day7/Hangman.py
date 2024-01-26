import random
import hangman_words

print(hangman_words.logo)

chosen_word = (random.choice(hangman_words.names)).lower()

display = []
word_length = len(chosen_word)
for i in chosen_word:
    display += "_"
print(display)
attempt = 6
while attempt:
    guess = (input("please guess the word in name\n\t")).lower()
    for _ in range(word_length):
        if guess == chosen_word[_]:
            display[_] = guess
        if "_" not in display:
            break
    if guess not in chosen_word:
        print("Chosen word is not in the word. you loose your 1 life")
        attempt -= 1
        print(f"Attempts left : {attempt}")

    print(hangman_words.hangman_pics[6 - attempt])
    if attempt == 0 or "_" not in display:
        break
    print(display)

if "_" in display:
    print("You Lost")
    print(f"name was {chosen_word}")
else:
    print(hangman_words.winner)
