# Fine Calculator by Kalyn Beach

#

def calc():
    
    speed    = input("Enter the driver's speed: ");

    if (speed < 45):
        print "There is no speed violation.";
    elif (speed >= 46):
        fine = 10 * (speed - 45);
    elif (speed >= 56):
        fine = (15 * (speed - 55)) + (10 * (speed - 45));
    elif (speed >= 66):
        fine = (20 * (speed - 65)) + (15 * (speed - 55)) + (10 * (speed - 45));

    print fine
