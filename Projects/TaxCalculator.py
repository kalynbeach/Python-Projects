# Income Tax Calculator by Kalyn Beach.

# Given annual income, calculate income tax due:
def taxes():
    income = input("Enter annual income: ");
    if (income <= 7150):
        tax = 0.10 * income;
    elif (income <= 29050):
        tax = 0.15 * (income - 7150) + 715.00;
    elif (income <= 70350):
        tax = 0.25 * (income - 29050) + 4000.00;
    elif (income <= 146750):
        tax = 0.28 * (income - 70350) + 14325.00;
    elif (income <= 319100):
        tax = 0.33 * (income - 146750) + 35717.00;
    else: # income > 319100
        tax = 0.35 * (income - 319100) + 92562.50;
    print "Income tax due: ", tax;


    
        
