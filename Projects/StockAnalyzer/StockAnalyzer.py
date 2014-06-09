# Stock Analyzer by Kalyn Beach

import urllib;

# Stock checkup - Download and display a stock quote:

def checkup(symbol):
    keywords = ['Symbol', 'Price', 'Open', 'Date', 'Time', 'Volume'];
    stock = getStock(symbol, keywords);
    display(stock);

# Display stock quote from a dictionary:

def display(stock):
    string = str(stock); 
    # Strip single quotes from output:
    singleQuote = "'"; emptyString = '';
    text = string.replace(singleQuote, emptyString);
    print text;

# Evaluate investment - Download a quote and evaluate shares:

def evaluate(symbol, shares):
    keywords = ['Symbol', 'Price', 'Date', 'Time'];
    stock = getStock(symbol, keywords);
    price = float(stock['Price']);
    value = shares * price;
    investment = stock.copy();
    investment['Value'] = fpToString(value, 2);
    investment['Shares'] = str(shares);
    display(investment);

# Convert a floating point value to a string with specified decimal positions:

def fpToString(value, decimalPositions):
    string = str(round(value, decimalPositions));
    periodPosition = string.find('.');
    if (periodPosition >= 0):
        string = string[0: periodPosition + decimalPositions + 1];
    return string

# Analyze the information:

import time;
def analyze(symbol, seconds, checks):
    stock = getStock(symbol, 
                     keywords = ['Symbol', 'Price', 'Date', 'Time', 'Open']);
    display(stock);
    firstPrice = currentPrice = float(stock['Price']);
    minimum =  float(stock['Price']);
    maximum=  float(stock['Price']);
    total=  float(stock['Price']);
    for check in range(checks - 1):
        time.sleep(seconds);
        stock = getStock(symbol, keywords = ['Time', 'Price']);
        currentPrice = float(stock['Price']);
        change = currentPrice - firstPrice;
        stock['Change'] = fpToString(change, 2);
        display(stock);
        if currentPrice < minimum:
            minimum = currentPrice;
        if currentPrice > maximum:
            maximum = currentPrice;
        total = total + currentPrice;
    print 'First price:', firstPrice, 'Most recent price:', currentPrice;
    print 'Minumum:', minimum;
    print 'Maximum:', maximum;
    print 'Average:', (total /  checks); 
    
# Stock watch - Repeatedly download and display stock quotes:

import time;
def watch(symbol, seconds, checks):
    stock = getStock(symbol, 
                     keywords = ['Symbol', 'Price', 'Date', 'Time', 'Open']);
    display(stock);
    firstPrice = currentPrice = float(stock['Price']);
    for check in range(checks - 1):
        time.sleep(seconds);
        stock = getStock(symbol, keywords = ['Time', 'Price']);
        currentPrice = float(stock['Price']);
        change = currentPrice - firstPrice;
        stock['Change'] = fpToString(change, 2);
        display(stock);
    print 'First price:', firstPrice, 'Most recent price:', currentPrice;

# Download a stock quote as a dictionary:

def getStock(symbol, keywords):
    values = getList(symbol, keywords);
    dictionary = {};
    for keyword, value in zip(keywords, values):
        dictionary[keyword] = value;
    # You can also use: dictionary = dict(zip(keywords, list);
    return dictionary;

# Download a stock quote as a list:

def getList(symbol, keywords):
    text = getText(symbol, keywords);
    theList = text.split(',');
    return theList;
    # Example: ['YHOO','36.49','10/28/2004','2:28pm','35.83'];
    
# Download a stock quote as a string:

def getText(symbol, keywords):
    url = URL(symbol, keywords);
    webData = urllib.urlopen(url);
    text = webData.read();
    # Example: ''YHOO',36.47,'10/28/2004','2:26pm',35.83\r\n';
    webData.close();
    # Strip unnecessary characters:
    for char in ['\n', '\r', "'", '"']:
        text = text.replace(char, '');
    return text;
    # Example: 'YHOO,36.47,10/28/2004,2:26pm,35.83';

# Form a URL for financial data:

def URL(symbol, keywords):
    url  = location() + '?' + query(symbol, keywords);
    return url;
    # Example: 'http://finance.yahoo.com/d/quotes.csv?s=YHOO&f=sl1d1t1o&e=.csv';

# Return a yahoo location for financial data:

def location():
    return 'http://finance.yahoo.com/d/quotes.csv';
    # location = protocol + '://' + site + path;
    # protocol = 'http'; site = 'finance.yahoo.com'; path = '/d/quotes.csv';

# Form a query for specific data on a selected symbol:

def query(symbol, keywords): 
    return 's=' + symbol + '&' + format(keywords) + '&e=.csv';
    # Example: 's=YAHOO&f=sl1d1t1o&e=.csv';

# Format a list of keywords into an abbreviated query:

def format(keywords):
    abbreviation = {
        'Symbol' : 's', 'Price' : 'l1', 'Open' : 'o',
        'Date' : 'd1',  'Time' : 't1', 'Volume' : 'v'
    };
    format = 'f=';
    for keyword in keywords:
        format = format + abbreviation[keyword];    
    return format;
    # Example:
        # keywords = ['symbol', 'price', 'date', 'time', 'open'];
        # format(keywords) = 'f=sl1d1t1o&e=.csv';
