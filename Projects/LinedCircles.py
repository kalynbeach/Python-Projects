# Lined Circles by Kalyn Beach.

import random;
# A blueprint for individual circle objects:
class Circle:
    # Initialize variables of a Circle object:
    def __init__(self, x, y, r):  # (x, y) is center, r is radius;
        self.x = x; self. y = y;
        self.r = r; 
        self.color = (0, 0, 0);
    # Use the pen to draw the circle object:
    def draw(self, pen):
        pen.color(self.color);
        pen.fill(True);
        # Move the pen to the center of the circle:
        pen.up(); pen.goto(self.x, self.y - self.r); pen.down();
        pen.circle(self.r); 
        pen.fill(False);
    # Update the color variable of the circle object:
    def setColor(self, red, green, blue):
        self.color = (red, green, blue);
    # Randomly update the color of the circle object:
    def randomColor(self):
        red = random.randint(0, 1); green = random.randint(0, 1); blue = random.randint(0, 1);
        self.color = (red, green, blue);

# A blueprint for sets of lined circles: 
class LinedCircles:
    # Initialize variables of a LinedCircles object:
    def __init__(self, x, y, radius, distance, number):
        self.list = [];
        for c in range(number):
            circle = Circle(x, y, radius);
            self.list.append(circle);
            x = x + distance; # replaces radius = radius - distance;
        self.randomColors();
    # Use the pen to draw the lined circles object:
    def draw(self, pen):
        for circle in self.list:
            circle.draw(pen);
    # Randomly update the colors of all lined circles:
    def randomColors(self):
        for circle in self.list:
            circle.randomColor();
    # Play a circle show:
    def show(self, pen, seconds, sets):
        import time;
        for set in range (sets):
            pen.reset(); # pen.clear();
            self.draw(pen);
            pen.up(); pen.goto(0, 0);
            self.randomColors();
            time.sleep(seconds);
            
import turtle;

# A setup for sample program executions: 
class Demo:
    # Initialze variables of a Demo object:
    def __init__(self):
        self.pen = turtle.Pen(); 
        self.width = self.pen.window_width();
        self.height = self.pen.window_height();
        self.span = min(self.width, self.height);
    # Draw a single circle:
    def circle(self):
        self.pen.reset();
        radius = self.span / 2 - 20;
        circle = Circle(x=0, y=0, r=radius);
        circle.setColor(red=1, green=0, blue=0);
        circle.draw(self.pen);
    # Draw a set of lined circles:
    def circleDrawing(self):
        self.pen.reset();
        radius = 10;
        distance = self.span / 2 - 20; 
        circles = LinedCircles(
            0, 0, radius, distance, number=6);
        circles.draw(self.pen);
    # Play a show of randomly colored lined circles:
    def circleShow(self):
        self.pen.reset();
        radius = 10;
        distance = self.span / 2 - 20; 
        circles = LinedCircles(
            0, 0, radius, distance, number=6);
        circles.show(self.pen, seconds=3, sets=100);
    def linedCircleShow(self):
        radius = self.span / 3;
        x0 = - radius + 10
        y0 = 0
        number = 18
        distance = 2*radius / number
        circles = LinedCircles(x0, y0, radius, distance, number);
        circles.show(self.pen, seconds=3, sets=10);

# These statements can launch a circle show:
demo = Demo();
demo.linedCircleShow();
# demo.circleShow();
