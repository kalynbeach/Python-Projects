# Wage and Tax Calculations by Kalyn Beach

# Calculate gross wages, taxes due, and net wages given employee numer, hours
# worked, pay rate, and tax rate using an interrupted loop:

def taxesAndWages():
    
    counter = 0;
    totalNetWages = 0;
    totalTaxesDue = 0;
    
    while (True):
        print('...');
        while (True):
            empNum  = input('Enter employee number (1000..9999), 0 to quit: ');
            if (1000 <= empNum <= 9999 or empNum == 0):
                break;  # break out of the inner loop
        if (empNum == 0):
            break;  # break out of the outer loop
        while (True):
            hours   = input('Enter hours worked (0..168): ');
            if (0 <= hours <= 168): break;
        while (True):
            payRate = input('Enter pay rate (10..80): ');
            if (10 <= payRate <= 80): break;
        while(True):
            taxRate = input("Enter tax rate (0..50 percent): ");
            if (10 <= taxRate <= 50): break;
        grossWages = hours * payRate;
        if (hours > 40):
            extraPay = 0.20 * payRate * (hours - 40);
            grossWages = grossWages + extraPay;
        taxesDue = (grossWages * taxRate) / 100.0;
        netWages = grossWages - taxesDue;
        counter = counter + 1;
        totalNetWages = totalNetWages + netWages;
        totalTaxesDue = totalTaxesDue + taxesDue;
        print 'Employee number: ', empNum;
        print 'Gross wages: ', grossWages;
        print "Taxes due: ", taxesDue;
        print "Net Wages: ", netWages;

    if (counter > 0):
        averageNetWages = totalNetWages / counter;
        averageTaxesDue = totalTaxesDue / counter;
        print "Average net wages: ", averageNetWages;
        print "Average taxes due: ", averageTaxesDue;
        
                                        
