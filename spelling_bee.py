# spelling_bee.py
# Generate potential solutions to the New York Times Spelling Bee game.

import math
import sys


def get_input():
    """Get the Spelling Bee letters from the user, or return an error message if input is invalid.

    :return: A list of seven letters.
    """
    while True:
        try:
            user_input = input(
                "Enter 7 letters, with the hex's center letter first: ")
            if user_input == "q":
                sys.exit()
            elif len(user_input) != 7:
                raise ValueError("Input not seven characters.")
            elif user_input.isalpha() == False:
                raise ValueError("Invalid characters in input.")
            else:
                letters = [l.lower() for l in user_input]
                return letters
        except Exception as e:
            print(f"{e}")
            print("Input must be seven letters only (no spaces, no punctuation).\n")


def get_solutions(dictionary_file: str, puzzle_letters: list):
    """Filter the given dictionary file for possible solutions to the Spelling Bee's letters.

    :param dictionary_file: The dictionary to search for viable words.
    :param puzzle_letters: A list of the Spelling Bee puzzle's letters, with the required (i.e., center) letter first in the list.
    :return: A list of solutions to the puzzle.
    """
    with open(dictionary_file, 'r') as in_file:
        solutions = in_file.read().split("\n")

    # filter dictionary for viable words; words must be 4 letters long and not contain punctuation
    solutions = [word for word in solutions if len(word) >= 4]
    solutions = [word for word in solutions if word.isalpha()]

    # keep only words that have the required puzzle letter
    solutions = [word for word in solutions if puzzle_letters[0] in word]

    # remove words that have letters other than the puzzle letters
    # find other letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    invalid_letters = [c for c in alphabet if c not in puzzle_letters]

    remaining_words = solutions[:]
    for word in remaining_words:
        for letter in invalid_letters:
            if letter in word:
                solutions.remove(word)
                break

    return solutions


def output_grid(solutions: list, puzzle_letters: list):
    """Print a grid showing the first letter of each solution and how many letters long each solution is.

    :param solutions: The list of possible solutions.
    :param puzzle_letters: The letters of the Spelling Bee puzzle.
    """

    # make a copy of the puzzle_letters list so we don't mess it up
    puzzle_letters = puzzle_letters[:]
    # make a dictionary to contain number of solutions per letter
    words_per_letter = {letter: {} for letter in puzzle_letters}

    # for each solution, add 1 to the solutions_per_letter[letter][length] where letter is the first letter of the solution and length is len(solution)
    lengths = {}
    for word in solutions:
        first_letter = word[0]
        word_length = len(word)

        i = words_per_letter[first_letter].setdefault(word_length, 0)
        i += 1
        words_per_letter[first_letter][word_length] = i

        total_words_of_length = lengths.setdefault(word_length, 0)
        total_words_of_length += 1
        lengths[word_length] = total_words_of_length

    # sort the lengths from smallest to biggest
    lengths = dict(sorted(lengths.items()))

    # Print X axis label (top)
    print("   ", end="")
    for length in lengths:
        print(f"{length:<3}", end="")
    print("Σ")

    # for each letter, print that letter, then a space, then the value of each dict in it
    puzzle_letters.sort()
    for letter in puzzle_letters:
        print(f"{letter:<3}", end="")
        for length in lengths:
            number_of_words = words_per_letter[letter].setdefault(length, 0)
            if number_of_words == 0:
                x = "-"
                print(f"{x:<3}", end="")
            else:
                print(f"{number_of_words:<3}", end="")
        sum_of_letter = sum(words_per_letter[letter].values())
        if sum_of_letter == 0:
            sum_of_letter = "-"
        print(sum_of_letter)

    # print the final, sum row
    print("Σ", end="  ")
    for length in lengths.values():
        print(f"{length:<3}", end="")
    # print total number of solutions
    print(len(solutions))
    print()


def two_letter_lists(solutions: list, puzzle_letters: list):
    """Show a list of the first two letters of each word, with the number of occurrences of those two letters at the start of each word.

    :param solutions: _description_
    :param puzzle_letters: _description_
    """
    bigrams = {}
    for word in solutions:
        bigram = word[0:2]
        bigram_solutions = bigrams.setdefault(bigram, 0)
        bigram_solutions += 1
        bigrams[bigram] = bigram_solutions
    bigrams = dict(sorted(bigrams.items()))

    # print a line break between bigrams that start with different letters.
    prev_letter = None
    current_line = []
    for k, v in bigrams.items():
        current_letter = k[0]
        if prev_letter is not None and current_letter != prev_letter:
            print(", ".join(current_line))
            current_line = []
        current_line.append(f"{k.upper()}-{v}")
        prev_letter = current_letter
    print(", ".join(current_line))


def show_solutions(solutions: list):
    """Print a three-column list of the Spelling Bee words.

    :param solutions: The puzzle's list of words.
    """
    solutions.sort()
    # get the length of the list, divide by desired columns
    list_size = len(solutions)
    # print word n, then the word in position n + (list_size / 3)
    for n in range(math.floor(len(solutions) / 2)):
        print(f"{solutions[n]:<12}", end="")
        try:
            right_col_word = solutions[n + int(len(solutions) / 2)]
            print(f"{right_col_word}")
        except:
            print()


# Define constants and variables
DICTIONARY_FILE = "dictionary.txt"

MENU = """
1) Show hint grid
2) Show two-letter list
3) Show solutions
4) Enter new letters
"""

# main loop
while True:
    print("===Spelling Bee Solver===")
    print("(enter q to quit)\n")
    letters = get_input()
    solutions = get_solutions(DICTIONARY_FILE, letters)

    while True:
        for letter in letters:
            print(letter, end=" ")
        print()
        print(MENU)
        menu_choice = input("Pick a menu option: ")
        print()
        if menu_choice == "1":
            print("\nHints")
            output_grid(solutions, letters)
            print()
        elif menu_choice == "2":
            two_letter_lists(solutions, letters)
            print()
        elif menu_choice == "3":
            print(f"{len(solutions)} possible solutions: ")
            show_solutions(solutions)
            print()
        elif menu_choice == "4":
            break
