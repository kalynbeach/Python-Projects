# Leap Year Evaluator by Kalyn Beach

# Given a year on the Gregorian Calendar, evaluate if it is a leap year:

def leap():
    
    year         = input("Enter the year you want evaluated: "); 
    
    remainder4   = (year % 4);
    remainder100 = (year % 100);
    remainder400 = (year % 400);

    if (year < 1582):
        print "The Gregorian Calendar was introduced in 1582. Year must be after 1582.";
    elif (remainder4 == 0 and remainder100 == 0 and remainder400 != 0):
        print year, "is not a leap year.";
    elif (remainder4 != 0):
        print year, "is not a leap year.";   
    else:
        print year, "is a leap year.";

    

