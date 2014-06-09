# Seconds Calculations by Kalyn Beach

# Convert hours, minutes, and seconds to seconds using a pretest loop:

def secondsPretest():
    ans = raw_input('Ready to convert? [Yes/No]: ');
    while (ans == 'Yes' or ans == 'yes' or ans == 'Y' or ans == 'y'):
        while (True):
            hours   = input("Enter hours (non-nagetive): ");
            if (0 <= hours): break;
        while (True):
            minutes = input("Enter minutes (0..59): ");
            if (0 <= minutes < 60): break;
        while (True):
            seconds = input("Enter seconds (0..59): ");
            if (0 <= seconds < 60): break;
        secondsTotal = seconds + (60 * minutes) + (3600 * hours);
        print "The total time is ", secondsTotal, "seconds.";
        ans = raw_input('Convert more? [Yes/No]: ');
    print "So long...";

# Convert hours, minutes, and seconds to seconds using a interrupted loop:

def secondsInterrupted():
    while (True):
        while (True):
            hours   = input("Enter number of hours (non-negative): ");
            if (0 <= hours): break;
        while (True):
            minutes = input("Enter minutes (0..59): ");
            if (0 <= minutes < 60): break;
        while (True):
            seconds = input("Enter seconds (0..59): ");
            if (0 <= seconds < 60): break;
        secondsTotal = seconds + (60 * minutes) + (3600 * hours);
        print "The total time is ", secondsTotal, "seconds.";
        ans = raw_input('Convert more? [Yes/No]: ');
        if (ans == "No" or ans == "no"): break;
    print "So long...";
