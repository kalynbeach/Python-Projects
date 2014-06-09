# Seconds Producer by Kalyn Beach

# Input value, low <= value:

def inputLo(prompt, low):
    while (True):
        value  = input(prompt);
        if (low <= value):
            return value;
        print 'Invalid input:', value;

# Input value, low <= value <= high:

def inputLoHi(prompt, low, high):
    while (True):
        value  = input(prompt);
        if (low <= value <= high):
            return value;
        print 'Invalid input:', value;

# Convert hours, minutes, and seconds to seconds using a pretest loop:

def secondsPretest():
    ans = raw_input('Ready to convert? [Yes/No]: ');
    while (ans == 'Yes' or ans == 'yes' or ans == 'Y' or ans == 'y'):
        while (True):
            hours   = inputLo(prompt = "Enter hours (non-negative): ",
                              low = 0);
            if (0 <= hours): break;
        while (True):
            minutes = inputLoHi(prompt = "Enter minutes (0..59): ",
                                low = 0, high = 59);
            if (0 <= minutes < 60): break;
        while (True):
            seconds = inputLoHi(prompt = "Enter seconds (0..59): ",
                                low = 0, high = 59);
            if (0 <= seconds < 60): break;
        secondsTotal = seconds + (60 * minutes) + (3600 * hours);
        print "The total time is ", secondsTotal, "seconds.";
        ans = raw_input('Convert more? [Yes/No]: ');
    print "So long...";

# Convert hours, minutes, and seconds to seconds using a interrupted loop:

def secondsInterrupted():
    while (True):
        while (True):
            hours   = inputLo(prompt = "Enter hours (non-negative): ",
                              low = 0);
            if (0 <= hours): break;
        while (True):
            minutes = inputLoHi(prompt = "Enter minutes (0..59): ",
                                low = 0, high = 59);
            if (0 <= minutes < 60): break;
        while (True):
            seconds = inputLoHi(prompt = "Enter seconds (0..59): ",
                                low = 0, high = 59);
            if (0 <= seconds < 60): break;
        secondsTotal = seconds + (60 * minutes) + (3600 * hours);
        print "The total time is ", secondsTotal, "seconds.";
        ans = raw_input('Convert more? [Yes/No]: ');
        if (ans == "No" or ans == "no"): break;
    print "So long...";










