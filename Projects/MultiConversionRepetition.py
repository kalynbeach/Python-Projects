# Multi-Conversion Repetition by Kalyn Beach

# Display menu items:

def displayMenu():
    print "-- Conversions Menu --  ";
    print "(0) Exit the menu";
    print "(1) Convert Fahrenheit to Celcius";
    print "(2) Convert Celsius to Fahrenheit";
    print "(3) Convert Inches to Centimeters";
    print "(4) Convert Centimeters to Inches";
    print "(5) Convert Gallons to Liters";
    print "(6) Convert Liters to Gallons";
    print "(7) Convert Yards to Meters";
    print "(8) Convert Meters to Yards";
    print "(9) Convert Pounds to Kilograms";
    print "(10) Convert Kilograms to Pounds";

# Display menu and execute user choice repeatedly:

def repeat():
    while (True):
        displayMenu();
        choice = input("Enter choice number: ");
        if (choice == 0):
            break;
        elif (choice == 1):
            F2C();
        elif (choice == 2):
            C2F();
        elif (choice == 3):
            I2C();
        elif (choice == 4):
            C2I();
        elif (choice == 5):
            G2L();
        elif (choice == 6):
            L2G();
        elif (choice == 7):
            Y2M();
        elif (choice == 8):
            M2Y();
        elif (choice == 9):
            P2K();
        elif (choice == 10):
            K2P();
        else:
            print "Invalid choice: ", choice;
    print "Bye.";

# Convert Fahrenheit to Celsius:

def F2C():
    Fahrenheit = input("Enter degrees in Fahrenheit: ");
    Celsius    = (5.0 / 9.0) * (Fahrenheit - 32);
    print Fahrenheit, "Fahrenheit =", Celsius, "Celsius";

# Convert Celsius to Fahrenheit:

def C2F():
    Celsius    = input("Enter degrees in Celsius: ");
    Fahrenheit = (9.0 / 5.0) * Celsius + 32;
    print Celsius, "Celsius =", Fahrenheit, "Fahrenheit";

# Convert Centimeters to Inches:

def C2I():
    Centimeters = input("Enter length in centimeters: " );
    Inches      = Centimeters / 2.54;
    print Centimeters, "Centimeters =", Inches, "Inches";

# Convert Inches to Centimeters:

def I2C():
    Inches      = input("Enter length in inches: ");
    Centimeters = Inches * 2.54;
    print Inches, "Inches =", Centimeters, "Centimeters";
  
# Convert Liters to Gallons:

def L2G():
    Liters  = input("Enter amount in liters: ");
    Gallons = Liters * 0.264172;
    print Liters, "Liters =", Gallons, "Gallons";

# Convert Gallons to Liters:

def G2L():
    Gallons = input("Enter amount in gallons: ");
    Liters  = Gallons / 0.264172;
    print Gallons, "Gallons =", Liters, "Liters";
        
# Convert Meters to Yards:

def M2Y():
    Meters = input("Enter distance in meters: ");
    Yards  = Meters * 1.09361;
    print Meters, "Meters =", Yards, "Yards";

# Convert Yards to Meters:

def Y2M():
    Yards  = input("Enter distance in yards: ");
    Meters = Yards / 1.09361;
    print Yards, "Yards =", Meters, "Meters";
    
# Convert Kilograms to Pounds

def K2P():
    Kilograms = input("Enter weight in kilograms: ");
    Pounds    = Kilograms * 2.20462;
    print Kilograms, "Kilograms =", Pounds, "Pounds";

# Convert Pounds to Kilometers

def P2K():
    Pounds    = input("Enter weight in pounds: ");
    Kilograms = Pounds / 2.20462;
    print Pounds, "Pounds =", Kilograms, "Kilograms";
