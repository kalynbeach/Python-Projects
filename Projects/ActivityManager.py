# Activity Manager by Kalyn Beach

# Determines activity based on inputted temperature:

def theActivity(temp):
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
    return activity;


# Find average temperature with a pretest loop:

def weatherPretest():
    total = 0; counter = 0; 
    currentTemp = input('Enter temperature (0..100), negative to quit: ');
    while (currentTemp >= 0):
        total = total + currentTemp;
        counter = counter + 1;
        print 'Activity: ', theActivity(temp = currentTemp);
        currentTemp = input('Enter temperature (0..100), negative to quit: ');
    print 'Temperatures processed:', counter;
    summarize(total, counter);
    
# Display average temperature:

def summarize(total, counter):
    if (counter > 0):
        average = float(total) / counter;
        print 'Average temperature:', average;

# Find average temperature with an interrupted loop:

def weatherInterrupted():
    total = 0; counter = 0;
    while (True):
        currentTemp = input('Enter score (0..100), negative to quit: ');
        if (currentTemp < 0):
            break;
        total = total + currentTemp;
        counter = counter + 1;
        print 'Activity:', theActivity(temp = currentTemp);
    print 'Temperatures processed:', counter;
    summarize(total, counter);



