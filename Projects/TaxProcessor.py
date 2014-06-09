# Tax Processor by Kalyn Beach

# Input incomes and return them all as a list:

def inputListOfIncomes():
    listOfIncomes = [];
    currentIncome = input("Enter annual income, negative to quit: ");
    while (currentIncome >= 0):
        listOfIncomes.append(currentIncome);
        currentIncome = input("Enter annual income, negative to quit: ");
    return listOfIncomes;
        

# Calculates the tax given an inputted income:

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

# Display scores and corresponding letter grades:

def display(listOfIncomes, listOfTaxes):
    numberOfIncomes = len(listOfIncomes);
    if (numberOfIncomes > 0):
        print "-----------------";
        print 'Income Taxes';
        for index in range(numberOfIncomes):
            print listOfIncomes[index], '\t', listOfTaxes[index];

# Find the average of a numeric list:

def listAverage(numericList):
    total = 0;
    for number in numericList:
        total = total + number;
    return  float(total) / len(numericList);

# Display average income and tax:

def summarize(listOfIncomes, listOfTaxes):
    print "-----------------";
    print "Incomes processed: ", len(listOfIncomes);
    if (len(listOfIncomes) > 0):
        #averageIncome = float(listOfIncomes) / counter;
        #averageTax = float(totalTax) / counter;
        print "Average income: ", round(listAverage(listOfIncomes));
        print "Average income tax: ", round(listAverage(listOfTaxes));
        print "-----------------";
        
# Input incomes, sort them, and output taxes:

def incomes():
    listOfIncomes = inputListOfIncomes();
    listOfIncomes.sort();
    listOfTaxes = map(theTax, listOfIncomes);
    display(listOfIncomes, listOfTaxes);
    summarize(listOfIncomes, listOfTaxes);
    
