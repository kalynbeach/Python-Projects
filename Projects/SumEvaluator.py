# Sum Evaluator by Kalyn Beach

def sumTotal(a, b):
    theSum = 0;
    while (a <= b):
        theSum = theSum + a;
        a = a + 1;
    return theSum;

def repeat():
    print "This program sums up sequences of numbers."
    while (True):
        bottom = input("Enter sequence bottom: ");
        top = input("Enter sequence top: ");
        theSum = sumTotal(a = bottom, b = top);
        print "Bottom:", bottom, "Top:", top;
        print "Sum: ", theSum;
        ans = raw_input("Sum up more? [Yes/No]: ");
        if(ans == "No" or ans == "no"): break;
    print "Bye.";
