# Gas Cost Calculator by Kalyn Beach

# Given total distance, gas mileage, and gas price, calculate total cost of gas
# for the trip:

def gasCost():
    totalDistance = input("Enter the total distance (in miles): ");
    gasMileage    = input("Enter the gas mileage (in miles per gallon): ");
    gasPrice      = input("Enter the price of gas (in US dollars per gallon): ");

    cost = (float(totalDistance) / float(gasMileage)) * float(gasPrice);

    print("Here is the cost of gas for your trip: "), cost;
