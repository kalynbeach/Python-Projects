# Weather Advisor by Kalyn Beach

# Given the current temperature in Fahrenheit, determine the advisable activity
# for the given weather:

def weather():
    temperature = input("Enter the current temperature (in Fahrenheit, between 0 and 100): ");

    if (temperature < 0 or temperature > 100):
        print "Invalid temperature: ", temperature;
    else:
        if (temperature <= 40):
            activity = "Get some sleep at home.";
        elif (temperature <= 60):
            activity = "Browse the Internet.";
        elif (temperature <= 75):
            activity = "Take a walk in the park.";
        elif (temperature <= 90):
            activity = "Sunbathe on the lawn.";
        else:
            activity = "Go to the beach.";

    print activity;
