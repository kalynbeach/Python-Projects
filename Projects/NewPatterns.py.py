# New Patterns by Kalyn Beach

import turtle;

# Create a blue pen and determine the window's width and height:def init():
def init():
    pen = turtle.Pen();
    pen.color(0, 0, 1); # blue
    width = pen.window_width();
    height = pen.window_height();
    return pen, width, height;
    
# Given a number, design a pattern:
def pattern(number): # Example: pattern(5);
    pen, w, h = init();
    # Switch off tracing for higher speed:
    pen.tracer(False);   
    for x in range(-w/2, +w/2):
        for y in range (-h/2, +h/2):
            draw(pen, number, x, y);
        # Temporarily switch on tracing to observe drawing:
        if (x % 100 == 0):
            pen.tracer(True); pen.tracer(False);
    pen.tracer(True);
    # If this program freezes on a Mac, add the following line:
    #turtle._root.mainloop();

# Draw a pattern element at point (x, y):
def draw(pen, number, x, y):
    a = y * (number / 100.0);
    b = x * (number / 100.0);
    ez = int(a*a+(b*a) + b*b+(a*b)); 
    # Try ez = int(a*a + b*b) and other expressions.
    if (ez % 2 == 0):
        pen.up(); pen.goto(x, y); pen.down();
        pen.circle(1);

#pattern(5);
