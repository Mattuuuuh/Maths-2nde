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
    return x**3/3 - 3*x+2 + np.exp(-x-2)

def g(x):
    return -np.arctan(x)+2

class InegaliteGraphique(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{libertinus,libertinust1math,calrsfs, icomma}")
        MathTex.set_default(font_size=72)
        Tex.set_default(font_size=72)
        # axes
        axes = NumberPlane(
                x_range=(-4.9, 3.9, 1),
                y_range=(-5.5,7.5,1),
                x_length=16,
                y_length=9,
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

        objects_in_frame = Group(axes)

        self.play(self.camera.auto_zoom(objects_in_frame))
        self.play(Create(axes))
        
        self.wait()
       
        # graphs of f and g
        f_graph = axes.plot(
                f,
                x_range=[-4.5,3.5,1],
                color=BLUE_E,
                stroke_width=4,
        )
        g_graph = axes.plot(
                g,
                x_range=[-4.5,3.5,1],
                color=RED_E,
                stroke_width=4,
        )
        Cf = MathTex(r"\mathcal{C}_f", color=BLUE_E, tex_template=myTemplate)
        Cg = MathTex(r"\mathcal{C}_g", color=RED_E, tex_template=myTemplate)
        Cf.move_to(axes.c2p(-1,4))
        Cg.move_to(axes.c2p(-.5, -1))

        self.play(Create(f_graph), run_time=2)
        self.play(Write(Cf))
        self.play(Create(g_graph), run_time=2)
        self.play(Write(Cg))

        # x through domain, from x=-4.5 to x=3.5 and back
        tick_length=.2
        x = ValueTracker(-4.5)

        xtick = always_redraw(lambda:
                Line(axes.c2p(x.get_value(), -tick_length), axes.c2p(x.get_value(), +tick_length), color=XCOLOR)
        )
        xlabel = always_redraw(lambda:
            MathTex("x", color=XCOLOR).next_to(xtick, DOWN)
        )
        self.play(Create(xtick), Create(xlabel))
        self.play(x.animate.set_value(3.5), run_time=2)
        self.play(x.animate.set_value(-4.5), run_time=2)

        # draw lines to f(x) and g(x)
        fline = always_redraw(lambda:
                axes.get_lines_to_point(axes.c2p(x.get_value(), f(x.get_value())), color=BLUE_E, stroke_width=2)
        )
        gline = always_redraw(lambda:
                axes.get_lines_to_point(axes.c2p(x.get_value(), g(x.get_value())), color=RED_E, stroke_width=2)
        )

        # write f(x) < g(x) and rezoom
        
        flabel = MathTex("f(x)", color=BLUE_E, tex_template=myTemplate)
        greater_symbol = MathTex(">", tex_template=myTemplate).next_to(flabel, RIGHT)
        smaller_symbol = MathTex("<", tex_template=myTemplate).next_to(flabel, RIGHT)
        equality_symbol = MathTex("=", tex_template=myTemplate).next_to(flabel, RIGHT)
        glabel = MathTex("g(x)", color=RED_E, tex_template=myTemplate).next_to(smaller_symbol,RIGHT)

        full_label = VGroup([flabel, smaller_symbol, greater_symbol, equality_symbol, glabel]).next_to(axes, 2*DOWN)
        objects_in_frame.add(full_label)

        self.play(self.camera.auto_zoom(objects_in_frame))

        self.play(Create(fline))
        self.play(Write(flabel))
        self.wait(2)
        self.play(Create(gline))
        self.play(Write(glabel))
        self.wait(2)
        self.play(Write(smaller_symbol))
        
        self.wait(2)
    
        # change fonts to show big/small
        self.play(
                flabel.animate.set_font_size(54),
                glabel.animate.set_font_size(90),
        )

        self.wait(2)

        # move to -3.371 and change to f(x) = g(x)
        self.play(x.animate.set_value(-3.371), run_time=5)
    
        self.play(
                Transform(smaller_symbol, equality_symbol), 
                flabel.animate.set_font_size(72), 
                glabel.animate.set_font_size(72),
        )

        # move to -3.3 and change to f(x) > g(x)
        self.play(x.animate.set_value(-3.3), run_time=2)
    
        self.play(
                # TODO bug in Transform here (overlap)
                Transform(equality_symbol, greater_symbol), 
                flabel.animate.set_font_size(90), 
                glabel.animate.set_font_size(54),
        )

        # move to .063 and change to f(x) = g(x)
        self.play(x.animate.set_value(.06), run_time=5)
    
        self.play(
                Transform(greater_symbol,equality_symbol), 
                flabel.animate.set_font_size(72), 
                glabel.animate.set_font_size(72),
        )

        # move to .1 and change to f(x) < g(x)
        self.play(x.animate.set_value(.1), run_time=2)
    
        self.play(
                Transform(equality_symbol, smaller_symbol), 
                flabel.animate.set_font_size(54), 
                glabel.animate.set_font_size(90),
        )

        # move to 2.768 and change to f(x) = g(x)
        self.play(x.animate.set_value(2.768), run_time=5)
    
        self.play(
                Transform(smaller_symbol, equality_symbol), 
                flabel.animate.set_font_size(72), 
                glabel.animate.set_font_size(72),
        )

        # move to 2.8 and change to f(x) > g(x)
        self.play(x.animate.set_value(2.8), run_time=2)
    
        self.play(
                Transform(equality_symbol, greater_symbol), 
                flabel.animate.set_font_size(90), 
                glabel.animate.set_font_size(54),
        )

        # move to 3.5 
        self.play(x.animate.set_value(3.5), run_time=5)

        self.wait(3)

##
