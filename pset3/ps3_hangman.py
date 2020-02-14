# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random,string

WORDLIST_FILENAME = "pset3\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    trueGuess = []
    for letter in lettersGuessed:
      if letter in secretWord:
        trueGuess.append(letter)

    trueGuess.sort()
    word = list(secretWord)
    word.sort()
    return trueGuess == word



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # Sorting lists to easily compare between them
    word = list(secretWord)
    # word.sort()
    lettersGuessed.sort()
    output = ""
    for char in secretWord:
      if char in lettersGuessed:
        output += char
      else:
        output += "_"

    return output


def getAvailableLetters(lettersGuessed):
    availableLetters = string.ascii_lowercase
    for char in lettersGuessed:
      availableLetters = availableLetters.translate({ord(char): None})

    return availableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    availableGuesses = 8
    gameStatues = ""
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")
    def ux():
      print("-------------")
      print(f"You have {availableGuesses} guesses left.")
      print(f"Available letters : {getAvailableLetters(lettersGuessed)}")
    ux()
    print("-------------")

    while availableGuesses!= 0:
      # Asking user for a guess 
      userGuess = (input("Please guess a letter: ")).lower()

      # check if the user guessed this letter before
      if userGuess not in lettersGuessed:
        # adding guess to guessed letters list
        lettersGuessed.append(userGuess)
        # Checking if user guessed is correct
        if userGuess in secretWord:
          print(f"Good Guess : {getGuessedWord(secretWord, lettersGuessed)}")
          ux()
        else:
            print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")
            availableGuesses -= 1
            ux()

      else:
        print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
        ux()

      if isWordGuessed(secretWord, lettersGuessed):
        print("-------------")
        print("Congratulations, you won!")
        gameStatues = "ok"
        break
    if gameStatues != "ok":

      print("-------------")
      print("	Sorry, you ran out of guesses. The word was else.")





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
