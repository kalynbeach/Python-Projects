# Class-based Mandelbrot Patterns by Kalyn Beach.

import turtle;
import colorsys;


class MandelbrotPatterns:
    # Initialize the pen, and determine the window width and height:
    def __init__(self):
        self.pen = turtle.Pen(); 
        self.width = self.pen.window_width();
        self.height = self.pen.window_height(); 

    # Given numbers u0, v0, and side, design a pattern:
    def mandelbrot(self, u0, v0, side):
        #self.pen, self.width, self.height = init();
        self.pen.tracer(False);   
        for x in range(-self.width/2, +self.width/2):
            for y in range (-self.height/2, +self.height/2):
                self.draw(side, u0, v0, x, y);
            if (x % 20 == 0):
                self.pen.tracer(True); self.pen.tracer(False);
        self.pen.tracer(True);

    # Draw in color a pattern element at point (x, y):
    def draw(self, side, u0, v0, x, y):
        maxCount = 25;
        u = u0 + x * (side / 100.0);
        v = v0 - y * (side / 100.0);
        a = 0 ; b = 0; count = 0; 
        while (count < maxCount and a * a + b * b <= 4):
            count = count + 1;
            a1 = a * a - b * b + u;
            b1 = 2 * a * b + v;
            a = a1; b = b1;
        ez = float(count) / maxCount;
        color = colorsys.hsv_to_rgb(ez, ez, ez);
        self.pen.color(color);
        self.pen.up(); self.pen.goto(x, y); self.pen.down();
        self.pen.forward(1);
