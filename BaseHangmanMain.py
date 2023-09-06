import random
import ColorCode
from Words import WordsList
from Body import Hangman
from time import sleep 

def StartupGame():
    # Display Starup Interface
    Title = "H-A-N-G-M-A-N"
    Author = "by nthndkid"
    Category = "Technology"
    print("\n" + ColorCode.Bold + ColorCode.LightRed + Title.center(61) + ColorCode.Reset)
    print((ColorCode.Underlined + Author + ColorCode.Reset).center(70))
    print(("Category: " + ColorCode.Green + Category + ColorCode.Reset).center(70))

def GameWord():
    # Randomize Word
    Word = random.choice(WordsList)
    return Word.upper()

def PlayGame(Word):
    # Intialization of Variables
    HiddenWord = "_" * len(Word)
    Attempt = 7
    Guessed = False
    GuessLetters = []
    GuessWords = []

    # Display Hangman
    sleep(1)
    print(ColorCode.Bold + ColorCode.LightGray + Hangman(Attempt).center(60) + ColorCode.Reset)
    print((ColorCode.Bold + HiddenWord + "" + ColorCode.Reset + "\n").center(60))

    # Loop until Guessed = True and Attempt is Greater than 8
    while not Guessed and Attempt > 0:
        UserGuess = input("\t\t   Enter Letter or Word: ").upper()
        # Check if User guess is a alphabetical and consist of only 1 letter
        if len(UserGuess) == 1 and UserGuess.isalpha():
            # Check if the User entered letter is already guessed
            if UserGuess in GuessLetters: 
                print((ColorCode.Underlined + ColorCode.Green + "The letter is already guessed!" + ColorCode.Reset).center(62))
            # If not guessed
            elif UserGuess not in Word:
                print((ColorCode.Yellow + UserGuess + " is not in the word." + ColorCode.Yellow).center(62))
                Attempt -= 1
                GuessLetters.append(UserGuess)
            # If guessed
            else:
                Exist = " is in the word"
                print((ColorCode.Green + UserGuess + Exist + ColorCode.Reset).center(62))
                GuessLetters.append(UserGuess)
                ListOfWord = list(HiddenWord) # Organize hidden word's letter in a list
                # Indicate the index and the letter inside the index, if the letter is same as the guess of the user
                Indicator = [i for i, letter in enumerate(Word) if letter == UserGuess]
                for index in Indicator:
                    ListOfWord[index] = UserGuess
                HiddenWord = "".join(ListOfWord) # Combine the letter of the hidden word in a list
                # Check if a underscore exist inside the hidden word
                if '_' not in HiddenWord:
                    Guessed = True
                    break
        # Check if the length of the user word is equal to the length of the word
        elif len(UserGuess) == len(Word) and UserGuess.isalpha():
            # If the Guess of the user is in the GuessWords
            if UserGuess in GuessWords:
                print((ColorCode.Bold + ColorCode.Green + "You guess the word, " + UserGuess + ColorCode.Reset).center(58))
            # if the Guess of the user is not in the Word
            elif UserGuess != Word:
                print((UserGuess + " is not the word.").center(58))
                Attempt -= 1
                GuessWords.append(UserGuess)
            else:
                Guessed = True
                HiddenWord = Word
                break
        elif UserGuess == Word:
            Guessed = True
            HiddenWord = Word
            break
        else:
            print((ColorCode.Bold + ColorCode.Yellow + "Not a valid guess!" + ColorCode.Reset).center(58))
        
        sleep(1)
        print(ColorCode.Bold + ColorCode.LightGray + Hangman(Attempt).center(60) + ColorCode.Reset)
        print(ColorCode.Bold + HiddenWord.center(60) + ColorCode.Reset, "\n")
    
    return Guessed

def GameResult(Guessed, Word):
    sleep(1)

    if Guessed:
        Message = (ColorCode.Bold +"Congrats, you guessed the word! " + ColorCode.Green + "You Win!" + ColorCode.Reset)
        print(Message.center(100))
    else:
        Message = (ColorCode.Bold + "Roger has been beheaded! The word was " + ColorCode.Yellow + Word + ColorCode.Reset +". Try again!")
        print(Message.center(100))


def HangmanMain():
    StartupGame()
    Word = GameWord()
    Guessed = PlayGame(Word)
    GameResult(Guessed, Word)

    sleep(1)
    TryAgain = input("\n\t\tDo you want to play again? (yes/no): ")
    while TryAgain.lower() ==  "yes":
        HangmanMain()

if __name__ == "__main__":
    HangmanMain()