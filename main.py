from random import randint


def get_word_list(path):
    wordlist = []
    with open(path) as f:
        for line in f:
            for word in line.split():
                word.upper()
                wordlist.append(word)
        return wordlist


def get_random_word(word_list=[]):
    word = list(word_list[randint(0, len(word_list))])
    return word


def display(word):
    for letter in word:
        print(letter, end=" ")
    print()


def update_original(index, word=[]):
    word[index] = "_"
    return word


def update_to_guess(index, letter, word=[]):
    word[index] = letter
    return word


path = input("Enter file path: ")
word_list = get_word_list(path)
original = get_random_word(word_list)
to_guess = ""
for i in range(len(original)):
    to_guess = to_guess + "_"
to_guess = list(to_guess)

attempts = 3
while attempts > 0 and '_' in to_guess:
    display(to_guess)
    letter = input("Enter a letter: ").upper()
    if letter not in original:
        attempts = attempts - 1
        print("Miss! Attempts left:", attempts)
        continue
    else:
        index = original.index(letter)
        original = update_original(index, original)
        to_guess = update_to_guess(index, letter, to_guess)

if attempts > 0:
    display(to_guess)
    print("Congrats! You've won.")
else:
    print("GAME OVER: 0 attempts left.")
exit(0)
