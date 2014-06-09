# Weather Advices by Kalyn Beach

# Advice which activity should be done given a temperature, then count
# and average out all given temperatures with a pretest loop:

def weatherPretest():
    total = 0; counter = 0;
    temp  = input("Enter temperature in Fahrenheit, -9999 to quit: ");
    while (temp != -9999):
        if (temp < 40):
            activity = "Get some sleep at home.";
        elif (temp < 60):
            activity = "Browse the Internet.";
        elif (temp < 75):
            activity = "Take a walk in the park.";
        elif (temp < 90):
            activity = "Sunbathe on the lawn.";
        else:
            activity = "Go to the beach.";
        print activity;
        
        total   = total + temp;
        counter = counter + 1;
        temp = input("Enter temperature in Fahrenheit, -9999 to quit: ");
        
    print 'Temperatures processed:', counter;
    average = float(total) / counter;
    print 'Average Temperature:', average;

# Advice which activity should be done given a temperature, then count
# and average out all given temperatures with a interrupted loop:

def weatherInterrupted():
    total = 0; counter = 0;
    while(True):
        temp = input("Enter temperature in Fahrenheit, -9999 to quit: ");
        if (temp < 40):
            activity = "Get some sleep at home.";
        elif (temp < 60):
            activity = "Browse the Internet.";
        elif (temp < 75):
            activity = "Take a walk in the park.";
        elif (temp < 90):
            activity = "Sunbathe on the lawn.";
        else:
            activity = "Go to the beach.";
        print activity;
        
        if (temp == -9999):
                break;
            
        total   = total + temp;
        counter = counter + 1;
        
    print 'Temperatures processed:', counter;
    average = float(total) / counter;
    print 'Average Temperature:', average;


        

        
