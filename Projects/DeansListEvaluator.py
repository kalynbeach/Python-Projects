# Dean's List Evaluator by Kalyn Beach

# Given a grade, calculate the student's GPA and determine if the student made
# the Dean's list:

def list():
    gradeA = input("Enter number of A's: ");
    gradeB = input("Enter number of B's: ");
    gradeC = input("Enter number of C's: ");
    gradeD = input("Enter number of D's: ");
    gradeF = input("Enter number of F's: ");

    gpaA = gradeA * 4.0;
    gpaB = gradeB * 3.0;
    gpaC = gradeC * 2.0;
    gpaD = gradeD * 1.0;
    gpaF = gradeF * 0.0;

    gpa = (gpaA + gpaB + gpaC + gpaD + gpaF) / (gradeA + gradeB + gradeC + gradeD + gradeF);

    if (gpa >= 3.5):
        evaluation = "You made it to the Dean's List!";
    else:
        evaluation = "You cannot make it to the Dean's List.";

    print "GPA is ", gpa;
    print evaluation;
    
