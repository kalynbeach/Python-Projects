# Commission Calculator by Kalyn Beach

# Calculate the commission earned given the salesperson's monthly sales total: 

def com():
    
    salesTotal     = input("Enter the salesperson's monthly sales total: ");
    excess         = (salesTotal - 1000.0);

    if (salesTotal <= 1000):
        commission = (salesTotal * 0.05);
    else:
        commission = (excess * 0.10) + 50; # 50 being the $50 from the 5% commission of the first $1000 in sales

    print "The salesperson's commission is: ", commission;
