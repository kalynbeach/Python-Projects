# Singer Advisor by Kalyn Beach

# Input singer name and output rating of given singer:

def singers():
    print "This program rates singers.";
    excellentList = ['Robert Plant', 'Justin Vernon', 'Alex Turner'];
    goodList = ['Thom Yorke', 'Ed Droste'];
    soSoList = ['Kanye West', 'Matt Bellamy'];
    poorList = ['Britney Spears', 'Chris Brown'];
    listOfAllSingers = excellentList + goodList + soSoList + poorList;
    print "List of all singers: ", listOfAllSingers;

    while(True):
        singer = raw_input("Enter singer name (unquoted): ");
        if (singer in excellentList): rating = "Excellent";
        elif (singer in goodList): rating = "Good";
        elif (singer in soSoList): rating = "So-so";
        elif (singer in poorList): rating = "Poor";
        print "Singer: ", singer;
        print "Rating: ", rating;
        ans = inputYesNo("Process more? [Yes/No]: ");
        if (ans == 'No' or 'no'): break;
    print "So long...";

# Input valid answer for Yes/No question:

def inputYesNo(prompt):
    response = raw_input(prompt);
    while (response != 'Yes' and response != 'No' and response != 'no'):
        print "Invalid response: ", response;
        response = raw_input(prompt);
    return response;
        

    
