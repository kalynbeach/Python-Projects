# Trip Advisor by Kalyn Beach

# Input travel destination and output advice:

def travel():
    print "This program gives advice on a number of travel destinations."
    dictionaryOfAllDestinations = \
        {'Seattle' : 'Amazing coffee and a really good place to live.',
         'San Francisco' : 'Great city with a great vibe.',
         'Los Angeles' : 'Cool things to see and good food, but the traffic is horrid.',
         'Washington D.C.' : 'Very interesting sights - check out the museums.'};
    listOfAllDestinations = dictionaryOfAllDestinations.keys();
    print "List of all destinations: ", listOfAllDestinations;

    while (True):
        destination = raw_input("Enter destination name (unquoted): ");
        if (destination in listOfAllDestinations):
            advice = dictionaryOfAllDestinations[destination];
        else: print "No advice for given destination.";
        print '---------------';
        print 'Destination: ', destination;
        print 'Advice: ', advice;
        print '---------------';
        ans = inputYesNo("Process more? [Yes/No]: ");
        if (ans == "No" or ans == "no"): break;
    print "So long...";

# Input valid answer for a Yes/No question:

def inputYesNo(prompt):
    response = raw_input(prompt);
    while (response != 'Yes' and response != 'No' and response != 'no'):
        print 'Invalid response: ', response;
        response = raw_input(prompt);
    return response;
