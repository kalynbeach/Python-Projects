# Mixed-Up Words by Kalyn Beach

import random;

# Mix the words:

def mixWords(word):
    characterList = list(word);
    random.shuffle(characterList);
    shuffledWord = ''.join(characterList);
    return shuffledWord;

# Repeatedly play the game of mixed up words:

def play():
    maxAllowedAttempts = 4; 
    print rulesDisplay(maxAllowedAttempts);
    listOfWords = inputListOfWords('words.txt');
    while (True):
        playOneGame(maxAllowedAttempts, listOfWords);
        ans = inputYesNo('\nPlay more? [Yes/No]: ');
        if(ans.lower() == 'no'): break;
    print 'So long...';

# Return the rules for the mixed up words game:

def rulesDisplay(maxAllowedAttempts):
    return \
        'This program plays the game of mixed up words.\n' + \
        'You are to guess a secret word by typing one or more adjacent letters.\n' + \
        'You can make at most ' + str(maxAllowedAttempts) + ' attempts.\n';

# Input words from file and return a list of all words:

def inputListOfWords(fileName):
    inFile = open(fileName, 'rU'); # read in "universal end-of-line" mode
    listOfWords = [];
    for line in inFile:
        # Strip unnecessary '\n' from right end:
        line = line.rstrip('\n');
        if (len(line) > 0 and line.isalpha()): 
            listOfWords.append(line);
    inFile.close();
    return listOfWords;

# Input valid answer for a Yes/No question while ignoring case:

def inputYesNo(prompt):
    response = raw_input(prompt);
    while (response.lower() != 'yes' and response.lower() != 'no'):
        print 'Invalid response: ', response;
        response = raw_input(prompt);
    return response;    


# Play a single game of mixed up words:

def playOneGame(maxAllowedAttempts, listOfWords):
    secretWord = chooseSecretWord(listOfWords);
    attempt = 1;
    mixedUpWords = mixWords(secretWord)
    for attempt in range(1, maxAllowedAttempts + 1):
        display = gameDisplay(attempt, mixedUpWords);
        guess = inputGuess(display);
        if (guess == secretWord):
            print gameDisplay(attempt, mixedUpWords) + \
                  '\tYou won!';
            return;
    print gameDisplay(attempt,mixedUpWords) + \
          '\tYou lost. It is ' + secretWord + '.'; 

# Select a random word from a list of words: and return it in uppercase:

def chooseSecretWord(listOfWords):
    secretWord = random.choice(listOfWords);
    return secretWord.upper();

# Input player's guess and return it in uppercase:

def inputGuess(display):
    guess = raw_input(display + '\tYour guess: ');
    return guess.upper();

# Return, as a string, the current attempt number and letters guessed so far:

def gameDisplay(attempt, lettersGuessedSoFar):
    space = ' ';
    string = '('+str(attempt)+')' + \
          ':\t' + space.join(lettersGuessedSoFar);
    return string;

