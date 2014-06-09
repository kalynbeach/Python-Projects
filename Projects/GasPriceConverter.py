# Gas Price Converter by Kalyn Beach

# Given the price of a gallon of gas and the exchange rate of the Euro to the US
# dollar, find the Euro price of a liter of gas:

def gasConverter():
    gallonPrice  = input("Enter the price per gallon in US dollars: ");
    exchangeRate = input("Enter the current value of 1 Euro compared to 1 US dollar: ");

    literPrice   = float(gallonPrice) / 0.264172;
    euroPrice    = float(literPrice) * 0.7954;

    print euroPrice;
    
        
    
