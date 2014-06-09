# Tax Filer by Kalyn Beach

# Input Income records from a file and return a list of records:

def read(fileName):
    listOfWorkers = [];
    inFile = open(fileName, 'rU'); # read in "universal end-of-line" mode
    for line in inFile:
        # Strip unnecessary '\n' from right end:
        line = line.rstrip('\n');
        worker = line.split(',');
        # worker = ['last-name', 'first-name', 'score']
        listOfWorkers.append(worker);
    inFile.close();
    return listOfWorkers;

# Output a list of workers records into a file :

def write(listOfWorkers, fileName):
    outFile = open(fileName, 'w');
    for worker in listOfWorkers:
        string = ','.join(worker);
        print >> outFile, string;
    outFile.close();

# Input worker records, add tax, and output income:

def taxes():
    inFileName = raw_input('Enter name of file to read from: ');
    listOfWorkers = read(inFileName);
    listOfWorkers.sort();
    for worker in listOfWorkers:
        # worker = ['first-name', 'last-name', 'income']
        income = float(worker[2]); # Convert income string into float income
        worker.append(str(theTax(income)));
    outFileName = raw_input('Enter name of file to write into: ');
    write(listOfWorkers, outFileName);
    print 'Workers processed:', len(listOfWorkers);

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

# Input student records from a file; determine and output min, max, and average scores:

def summary():
    inFileName = raw_input('Enter name of file to read from: ');
    listOfWorkers = read(inFileName);
    counter = len(listOfWorkers);
    print 'Workers processed:', counter;
    if (counter > 0):
        total = 0;
        firstWorker = listOfWorkers[0];
        firstIncome = firstWorker[2];
        minIncome = float(firstIncome);
        maxIncome = float(firstIncome);
        for worker in listOfWorkers:
            income = float(worker[2]);
            total = total + income;
            if (income < minIncome): minIncome = income;
            if (maxIncome < income): maxIncome = income;
        print 'Average income:', round(total / float(counter));
        print 'Lowest income:', minIncome;
        print 'Highest income:', maxIncome;
