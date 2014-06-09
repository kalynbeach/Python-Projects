# Seconds Counter by Kalyn Beach

# Given hours, minutes, and seconds, count the total number of seconds:

def countSeconds():
    hours        = input("Enter number of hours: ");
    minutes      = input("Enter number of minutes: ");
    seconds      = input("Enter number of seconds: ");
    secondsTotal = seconds + (60 * minutes) + (3600 * hours);
    
    print "Total number of seconds: ", secondsTotal;
    
