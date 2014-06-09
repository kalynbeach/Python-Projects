# Number Guesser by Kalyn Beach

# Find the user's secret number:

def guess():
    print("Think of a secret number.");
    print("Multiply it by 5.");
    print("Add 6 to the result.");
    print("Multiply the previous result by 4.");
    print("Add 9.");
    print("Again, multiply by 5.");

    result = input("Enter the result of the above operations: ");
    secret = (result - 165) / 100;

    print("Your secret number is "), secret;
