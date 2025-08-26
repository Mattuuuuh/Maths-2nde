from manim import *
import numpy as np

XCOLOR = RED_A
YCOLOR = PURPLE_A
FCOLOR = GOLD_A
PCOLOR = GREEN

# write decimal separator with commas instead of dots
def comma(num):
    return f'{num}'.replace('.', ',')

def f(x):
    return x-4

def g(x):
    return -(x-1)/2

def h(x):
    return f(x)*g(x)

class ProduitAffine(MovingCameraScene):
    def construct(self):
        # axes
        axes = NumberPlane(
                x_range=(-2.1, 6.1, 1),
                y_range=(-4.1,3.1,1),
                #x_length=8,
                #y_length=4,
                tips=True,
                background_line_style={
                    "stroke_width": 1,
                    "stroke_opacity": .4,
                },
                x_axis_config={
                    #"color":XCOLOR,
                    "stroke_width": 2,
                    "stroke_opacity":1,
                },
                y_axis_config={
                    #"color":YCOLOR,
                    "stroke_width": 2,
                    "stroke_opacity":1,
                },
        )
        
        axes.add_coordinates()

        self.play(Create(axes))
        
        self.wait()
       
        # graphs of f and g
        f_graph = axes.plot(
                f,
                x_range=[-2,6,1],
                color=BLUE_E,
                stroke_width=3,
        )
        g_graph = axes.plot(
                g,
                x_range=[-2,6,1],
                color=RED_E,
                stroke_width=3,
        )
        h_graph = axes.plot(
                h,
                x_range=[-2,6,1],
                color=PURPLE_E,
                stroke_width=3,
        )

        self.play(Create(f_graph),Create(g_graph))

        # hsync line passing through
        # while f and g don't change sign
        hsync = DashedLine(
                axes.c2p(-2,-7), 
                axes.c2p(-2,7),
                color=GREEN,
                dashed_ratio=.5,
                dash_length=.1,
                )
        
        xtracker = ValueTracker(-2)

        interval1=Line(axes.c2p(-2,0), axes.c2p(1,0), color=GREEN, stroke_width=5)
        I1label = always_redraw(lambda: Text("[-2 ; "+comma(min(1,np.round(xtracker.get_value(),1)))+"]", color=GREEN).move_to(axes.c2p(7,2)))

        self.play(Create(hsync),Write(I1label))
        self.wait()
        self.play(
                xtracker.animate.set_value(1), 
                hsync.animate.shift(RIGHT*3),
                Create(interval1),
                run_time=3,
                rate_func=linear,
                )

        self.play(hsync.animate.scale(1.1), run_time=.5)
        self.play(hsync.animate.scale(0.909), run_time=.5)
        
        self.play(hsync.animate.set_color(YELLOW))
        
        interval2=Line(axes.c2p(1,0), axes.c2p(4,0), color=YELLOW, stroke_width=5)
        I2label = always_redraw(lambda: Text("[1 ; "+comma(min(4,np.round(xtracker.get_value(),1)))+"]", color=YELLOW).move_to(axes.c2p(7,1)))
        self.play(Write(I2label))
        
        self.play(
                xtracker.animate.set_value(4), 
                hsync.animate.shift(RIGHT*3),
                Create(interval2),
                run_time=3,
                rate_func=linear,
                )

        self.play(hsync.animate.scale(1.1), run_time=.5)
        self.play(hsync.animate.scale(0.909), run_time=.5)
        
        
        #self.play(Create(h_graph))

        self.wait(3)

##
