# Spelling Bee Helper
Python script that helps you solve the [New York Times Spelling Bee puzzle](https://www.nytimes.com/puzzles/spelling-bee).

# Features
- Solve any spelling bee puzzle simply by entering the puzzle's letters.
- Choose between three levels of hints:
    1. **First Letter Grid:** A grid showing how many solutions start with each letter, sorted by length of solution.
    2. **Two Letter Lists:** Lists of two-letter combinations, showing how many words start with each pair of letters.
    3. **Solutions:** A list of possible words from the chosen dictionary file.

- Customize your experience by loading in a different dictionary as a text file.
    - Default dictionary comes from here: https://inventwithpython.com/dictionary.txt 
    - Alternate dictionary included from http://wordlist.aspell.net/12dicts-readme/

## Planned Features:
- Load different dictionaries from within the program itself (rather than having to modify the code).
- List solutions' common bigrams and trigrams (not just starting letters).