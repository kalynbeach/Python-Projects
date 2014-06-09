# Order Calculator with GUI by Kalyn Beach.

from Tkinter import *;
from ScrolledText import *;

# Initialize program components:
def init():
    # Create and set up the main window:
    global window; 
    window = Tk();
    window.title('Order Calculator');
    createWidgets();
    positionWidgets();
    configureWidgets();
    # Display the window:
    window.mainloop();

# Create widget objects:
def createWidgets():
    global quantityLabel; quantityLabel = Label(window); 
    global quantityEntry; quantityEntry = Entry(window);
    global priceLabel; priceLabel = Label(window);
    global priceEntry; priceEntry = Entry(window);
    global rateLabel; rateLabel = Label(window);
    global rateEntry; rateEntry = Entry(window);
    global submitButton; submitButton = Button(window); 
    global clearButton; clearButton = Button(window); 
    global scrolledText; scrolledText = ScrolledText(window);

# Position the widgets in the window:
def positionWidgets():
    global quantityLabel;
    quantityLabel.grid(row = 0, column = 0, padx = 3, pady = 3);
    global quantityEntry;
    quantityEntry.grid(row = 0, column = 1, padx = 3, pady = 3);
    global priceLabel;
    priceLabel.grid(row = 1, column = 0, padx = 3, pady = 3);
    global priceEntry;
    priceEntry.grid(row = 1, column = 1, padx = 3, pady = 3);
    global rateLabel; 
    rateLabel.grid(row = 2, column = 0, padx = 3, pady = 3);
    global rateEntry; 
    rateEntry.grid(row = 2, column = 1, padx = 3, pady = 3);
    global submitButton;
    submitButton.grid(row = 3, column = 0, padx = 3);
    global clearButton;
    clearButton.grid(row = 3, column = 1, padx = 3);
    global scrolledText;
    scrolledText.grid(row = 4, column = 0, padx = 3, pady = 3,
                      columnspan = 2);

# Configure the widgets:
def configureWidgets():
    global quantityText, quantityLabel, quantityEntry; 
    quantityText = StringVar(); quantityText.set('0');
    quantityEntry.configure(
        textvariable = quantityText, width = 20);
    quantityLabel.configure(
        text = 'Quantity', width = 20,
        borderwidth = 2, relief = SUNKEN);
    global priceText, priceLabel, priceEntry;
    priceText = StringVar(); priceText.set('0');
    priceEntry.configure(
        textvariable = priceText, width = 20);
    priceLabel.configure(
        text = 'Item Price', width = 20,
        borderwidth = 2, relief = SUNKEN);
    global rateText, rateLabel, rateEntry; 
    rateText = StringVar(); rateText.set('0');
    rateEntry.configure(
        textvariable = rateText, width = 20);
    rateLabel.configure(
        text = 'Tax rate', width = 20,
        borderwidth = 2, relief = SUNKEN);
    global submitButton, clearButton;
    submitButton.configure(
        text = 'Submit', width = 20, command = submitAction);
    clearButton.configure(
        text = 'Clear', width = 20, command = clearAction);
    global scrolledText;
    scrolledText.configure(
        width = 40, borderwidth = 2, relief = SUNKEN); 

# Clear the scrolled text:
def clearAction():
    global quantityText, rateText, priceText, scrolledText;
    quantityText.set('0');
    rateText.set('0');
    priceText.set('0');
    scrolledText.delete('1.0', END);

# Calculate and display order total:
def submitAction():
    global quantityText, rateText, priceText;
    quantity = float(quantityText.get());
    taxRate = float(rateText.get());
    price = float(priceText.get());
    orderPrice = quantity * price;
    salesTax = orderPrice * (taxRate / 100.0);
    orderTotal = orderPrice + salesTax;
    outputString = '\n\tOrder Price:\t' + fpToString(orderPrice, 2) + \
             '\n\tSales Tax:\t$' + fpToString(salesTax, 2) + \
             '\n\tOrder Total:\t$' + fpToString(orderTotal, 2) + '\n';
    scrolledText.insert(END, outputString);

# Convert a floating point value to a string with specified decimal positions:
def fpToString(value, decimalPositions):
    string = str(round(value, decimalPositions));
    periodPosition = string.find('.');
    if (periodPosition >= 0):
        string = string[0: periodPosition + decimalPositions + 1];
    return string;
    # Example: fpToString(value = 3.14159, decimalPositions = 2) returns '3.14'.

# Create the GUI and show it:
init();
