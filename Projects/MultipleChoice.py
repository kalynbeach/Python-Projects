# Multiple Choice by Kalyn Beach

# Display quiz items:

def displayQuiz1():
    print 'Who was the first U.S. President?';
    print '(1) Abraham Lincoln';
    print '(2) George Washington';
    print '(3) John Lennon';
    print '(4) Franklin Roosevelt';

def displayQuiz2():
    print "In what year did man first land on the moon?";
    print "(1) 1963";
    print "(2) 1967";
    print "(3) 1969";
    print "(4) 1970";

def displayQuiz3():
    print 'The song "Stairway to Heaven" is by which of the following bands?';
    print "(1) The Beatles";
    print "(2) The Rolling Stones";
    print "(3) Black Sabbath";
    print "(4) Led Zeppelin";
    

# Display the quiz and evaluate user response:

def quiz():
    
    displayQuiz1();
    choice1 = input('Enter choice number: ');
    if (choice1 == 1 or choice1 == 4):
        print 'He was a president, but not the first one.';
    elif (choice1 == 2):
        print 'That is correct!';
    elif (choice1 == 3):
        print 'He was not a politician. He was a musician.';
    else:
        print "Sorry, that is not correct.";
        
    displayQuiz2();
    choice2 = input('Enter choice number: ');
    if (choice2 == 3):
        print "That is correct!";
    else:
        print "Sorry, that is not correct.";

    displayQuiz3();
    choice3 = input("Enter choice number: ");
    if (choice3 == 4):
        print "That is correct!"
    else:
        print "Sorry, that is not correct.";
    
