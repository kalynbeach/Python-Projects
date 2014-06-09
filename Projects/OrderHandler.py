# Order Handler by Kalyn Beach

# Calculate the total price, sales tax, and order total including shipping and
# handeling fees based on the order total:

def order():
    quantity   = input("Enter item quantity: ");
    itemPrice  = input("Enter item price: ");
    salesTax   = input("Enter sales tax rate (as a percent): ");

    totalPrice   = quantity * itemPrice;
    taxDue       = totalPrice * (salesTax / 100.00);
    orderTotal   = totalPrice + taxDue;

    if (orderTotal < 20):
        fee = 4.99;
    elif (orderTotal < 40):
        fee = 5.99;
    elif (orderTotal < 60):
        fee = 6.99;
    else: #orderTotal >= 60
        fee = 7.99;
        
    orderPrice   = orderTotal + fee;

    print "Total price (before tax and S&H fee): ", totalPrice;
    print "Sales tax on order: ", taxDue;
    print "Order total (before S&H fee): ", orderTotal;
    print "Shipping and handling fee: ", fee;
    print "Grand total of order (order price): ", orderPrice;
    
    
