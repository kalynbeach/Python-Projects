# Order Calculator by Kalyn Beach

# Given quantity, item price, and sales tax, calculate total order price:

def order():
    quantity     = input("Enter item quantity: ");
    itemPrice    = input("Enter item price: ");
    salesTax     = input("Enter sales tax rate: ");
    
    grossPrice   = quantity * itemPrice;
    taxDue       = grossPrice * (salesTax / 100.00);
    orderTotal   = grossPrice + taxDue;
    
    print "Total order price: ", orderTotal;
