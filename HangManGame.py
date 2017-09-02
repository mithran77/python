WORD_LIST  = ['god', 'puppy', 'cats', 'django']

class HangManGame:

    def __init__(self):
        self.word = WORD_LIST[random(0, 10)]
        self.wrongGuesses = 0
        self.wordGuessed = false
        self.guessedLetters = set()

    def getInput(self):
        guess = raw_input("Enter your guess : ")
        guessedLetters.add(guess)
        if guess not in self.word:
            self.wrongGuesses ++

    def displayUI(self):

        while (self.wrongGuesses < len(self.word) or not self.wordGuessed):
            self.displayHangMan()
            if self.wrongGuesses == len(self.word):
                break
            self.displayWord()
            getInput()

        else:
            print("Hahaha you have failed!!")

        if self.wordGuessed:
            print("Congrats you guessed right!!")


    def displayWord(self):
        result = '_'*len(self.word)
        
        for index, letter in enumerate(self.word):
            if letter in self.guessedLetters:
                if index == 0:
                    letter = letter.capitalize
                result[index] = letter

        if ('_' not in result):
            self.wordGuessed = true

        result = ' '.join(result)
        print("Word : " + result)

    def displayHangMan(self):
        guesses = self.wrongGuesses
        print('     -----')
        print('       \'')

        if guesses == 0:
            return true

        print('       O')
        guesses--

        if guesses == 0:
            return true

        resultList = ['       |', '      \\|', '      \\|/']
        counter = 0
        while (guesses > 0):
            result = resultList[counter]
            guesses--
            counter++

        print(result)

        if guesses == 0:
            return true

        print('       |')
        guesses--

        if guesses == 0:
            return true

        resultList = ["       '", "      /\'", "      /'\\"]
        counter = 0
        while (guesses > 0):
            result = resultList[counter]
            guesses--
            counter++

        print(result)

        if guesses == 0:
            return true




game = new HangManGame()
game.displayUI()
