# Converters by Kalyn Beach

# Convert Centimeters to Inches:

def C2I():
    Centimeters = input("Enter length in centimeters:" );
    Inches      = Centimeters / 2.54;
    print Centimeters, "Centimeters =", Inches, "Inches";

# Convert Inches to Centimeters:

def I2C():
    Inches      = input("Enter length in inches:");
    Centimeters = Inches * 2.54;
    print Inches, "Inches =", Centimeters, "Centimeters";

    
# Convert Liters to Gallons:

def L2G():
    Liters  = input("Enter amount in liters:");
    Gallons = Liters * 0.264172;
    print Liters, "Liters =", Gallons, "Gallons";

# Convert Gallons to Liters:

def G2L():
    Gallons = input("Enter amount in gallons:");
    Liters  = Gallons / 0.264172;
    print Gallons, "Gallons =", Liters, "Liters";
    
    
# Convert Meters to Yards:

def M2Y():
    Meters = input("Enter distance in meters:");
    Yards  = Meters * 1.09361;
    print Meters, "Meters =", Yards, "Yards";

# Convert Yards to Meters:

def Y2M():
    Yards  = input("Enter distance in yards:");
    Meters = Yards / 1.09361;
    print Yards, "Yards =", Meters, "Meters";
    

# Convert Kilograms to Pounds

def K2P():
    Kilograms = input("Enter weight in kilograms:");
    Pounds    = Kilograms * 2.20462;
    print Kilograms, "Kilograms =", Pounds, "Pounds";

# Convert Pounds to Kilometers

def P2K():
    Pounds    = input("Enter weight in pounds:");
    Kilograms = Pounds / 2.20462;
    print Pounds, "Pounds =", Kilograms, "Kilograms";
    
