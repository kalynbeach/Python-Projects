# Tax Manager by Kalyn Beach

# Takes the inputted income, determines the tax bracket, and returns the tax due:

def theTax(income):
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
    return tax;
        

# Calculate income tax due given an income with a pretest loop:

def taxesPretest():
    
    counter = 0; totalIncome = 0; totalTax = 0;
    income = input("Enter annual income, negative to quit: ");
    
    while (income >= 0):
        totalIncome = totalIncome + income;
        totalTax = totalTax + theTax(income);
        counter = counter + 1;
        print "Income tax due: ", theTax(income = income);
        income = input("Enter annual income, negative to quit: ");
        
    print "Incomes processed: ", counter;
    summarize(totalIncome, totalTax, counter);

# Display average income and tax:

def summarize(totalIncome, totalTax, counter):
    if (counter > 0):
        averageIncome = float(totalIncome) / counter;
        averageTax = float(totalTax) / counter;
        print "Average income: ", averageIncome;
        print "Average income tax: ", averageTax;

# Calculate income tax due given an income with an interrupted loop:

def taxesInterrupted():

    counter = 0; totalIncome = 0; totalTax = 0;
    income = input("Enter annual income, negative to quit: ");
    
    while (True):
        totalIncome = totalIncome + income;
        totalTax = totalTax + theTax(income = income);
        counter = counter + 1;
        print "Income tax due: ", theTax(income = income);
        income = input("Enter annual income, negative to quit: ");

        if (income < 0):
            break;

    print "Incomes processed: ", counter;
    summarize(totalIncome, totalTax, counter);
