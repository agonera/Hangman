from random import choice
import sys


def get_word_list(path):
    word_list = []
    try:
        with open(path) as f:
            for line in f:
                for word in line.split():
                    if '_' in word:
                        print(f"Invalid input data: the word contains '_': {word}")
                        continue
                    word = word.upper()
                    word_list.append(word)
            return word_list
    except IOError:
        print("Invalid file path.")
        exit(1)


def get_random_word(list_of_words):
    if not list_of_words:
        print("Error: empty list of words.")
        exit(1)
    random_word = choice(list_of_words)
    charlist = list(random_word)
    return charlist


def display(charlist):
    formatted = ' '.join(charlist)
    print(formatted)


def update_original(index, charlist):
    charlist[index] = "_"
    return charlist


def update_to_guess(index, letter, charlist):
    charlist[index] = letter
    return charlist


def main():
    if len(sys.argv) < 2:
        print("No file given.")
        exit(1)
    path = sys.argv[1]
    word_list = get_word_list(path)
    original = get_random_word(word_list)
    to_guess = "_" * len(original)
    to_guess = list(to_guess)

    attempts_left = 3
    while attempts_left > 0 and '_' in to_guess:
        display(to_guess)
        letter = input("Enter a letter: ").upper()
        if letter == '_':
            continue
        if letter not in original:
            attempts_left = attempts_left - 1
            print(f"Miss! Attempts left: {attempts_left}")
        else:
            index = original.index(letter)
            original = update_original(index, original)
            to_guess = update_to_guess(index, letter, to_guess)

    if attempts_left > 0:
        display(to_guess)
        print("Congrats! You've won.")
    else:
        print("GAME OVER: 0 attempts left.")


if __name__ == '__main__':
    main()
