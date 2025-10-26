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
                x_range=(-4.9, 4.1, 1),
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
                x_range=[-4.5,3.5,.1],
                color=BLUE_E,
                stroke_width=4,
        )
        g_graph = axes.plot(
                g,
                x_range=[-4.5,3.5,.1],
                color=RED_E,
                stroke_width=4,
        )
        Cf = MathTex(r"\mathcal{C}_f", color=BLUE_E, tex_template=myTemplate)
        Cg = MathTex(r"\mathcal{C}_g", color=RED_E, tex_template=myTemplate)
        Cf.move_to(axes.c2p(3.5,6.5))
        Cg.move_to(axes.c2p(3.75, .75))

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
                axes.get_lines_to_point(axes.c2p(x.get_value(), f(x.get_value())), color=BLUE_E, stroke_width=5)
        )
        gline = always_redraw(lambda:
                axes.get_lines_to_point(axes.c2p(x.get_value(), g(x.get_value())), color=RED_E, stroke_width=5)
        )
        

        # prewrite f(x) < g(x) 
        
        flabel = MathTex("f(x)", color=BLUE_E, tex_template=myTemplate)
        symbol = MathTex("<", tex_template=myTemplate).next_to(flabel,RIGHT)
        glabel = MathTex("g(x)", color=RED_E, tex_template=myTemplate).next_to(symbol,RIGHT)
        
        full_label = VGroup([flabel, symbol, glabel]).next_to(axes, 2*DOWN)
        objects_in_frame.add(full_label)
        
        greater_symbol = MathTex(">", tex_template=myTemplate).move_to(symbol)
        smaller_symbol = MathTex("<", tex_template=myTemplate).move_to(symbol)
        equality_symbol = MathTex("=", tex_template=myTemplate).move_to(symbol)

        # prewrite {x st. f(x) > g(x)}
        setlabel = MathTex(
                r"\Bigl\{ x \in [-3,5 ; 4,5] \text{ tq. } f(x) \leq g(x) \Bigr\} =",
                tex_template=myTemplate,
                tex_to_color_map={'f(x)':BLUE_E, 'g(x)':RED_E, ' x ':XCOLOR},
        )
        firstset = MathTex(r"[-4,5 ; -3,37]",
                tex_template=myTemplate,
                color=YELLOW,
        ).next_to(setlabel, RIGHT)
        cup = MathTex(r"\cup",
                tex_template=myTemplate,
        ).next_to(firstset,RIGHT)
        secondset = MathTex(r"[0,06 ; 2,77]",
                tex_template=myTemplate,
                color=GREEN,
        ).next_to(cup,RIGHT)

        intervals = VGroup([setlabel,firstset,cup,secondset])
        intervals.next_to(full_label, 2*DOWN)
    
        # dezoom

        objects_in_frame.add(intervals)
        self.play(self.camera.auto_zoom(objects_in_frame))
        
        ## write
        self.play(Write(setlabel))
    
        self.wait(2)

        self.play(Create(fline))
        self.play(Write(flabel))
        self.wait(2)
        self.play(Create(gline))
        self.play(Write(glabel))
        self.wait(2)
        # change fonts to show big/small
        self.play(
                Write(symbol),
                flabel.animate.set_font_size(54),
                glabel.animate.set_font_size(90),
        )

        self.wait(2)

        # move to -3.371 and change to f(x) = g(x)
        # hightlight -4.5 to -3.371
        x0 = -3.37120546
        highlight = Line(axes.c2p(-4.5,0), axes.c2p(x0,0), color=YELLOW, stroke_width=5)

        self.play(
                x.animate.set_value(x0),
                Create(highlight),
                run_time=5,
        )

        self.play(
                Transform(symbol, equality_symbol), 
                flabel.animate.set_font_size(72), 
                glabel.animate.set_font_size(72),
        )

        self.wait(2)

        # move to -3.3 and change to f(x) > g(x)
        # write first interval
        self.play(x.animate.set_value(-3.3), run_time=2)
    
        self.play(
                Transform(symbol, greater_symbol), 
                flabel.animate.set_font_size(90), 
                glabel.animate.set_font_size(54),
        )

        self.wait(2)

        self.play(Write(firstset))

        self.wait(2)

        # move to .063 and change to f(x) = g(x)
        x1 = .063504168
        self.play(x.animate.set_value(x1), run_time=5)
    
        self.play(
                Transform(symbol,equality_symbol), 
                flabel.animate.set_font_size(72), 
                glabel.animate.set_font_size(72),
        )

        self.wait(2)
        
        self.play(Write(cup))

        self.wait(2)

        # move to .15 and change to f(x) < g(x)
        # hightlight .063 to .15
        highlight = Line(axes.c2p(.15,0), axes.c2p(.1,0), color=GREEN, stroke_width=5)
        self.play(
                x.animate.set_value(.15), 
                Create(highlight),
                run_time=2,
        )
    
        self.play(
                Transform(symbol, smaller_symbol), 
                flabel.animate.set_font_size(54), 
                glabel.animate.set_font_size(90),
        )

        self.wait(2)

        # move to 2.768 and change to f(x) = g(x)
        # hightlight .15 to 2.768
        x3 = 2.768435594
        highlight = Line(axes.c2p(.15,0), axes.c2p(x3,0), color=GREEN, stroke_width=5)
        self.play(
                x.animate.set_value(x3), 
                Create(highlight),
                run_time=5,
        )

        self.play(
                Transform(symbol, equality_symbol), 
                flabel.animate.set_font_size(72), 
                glabel.animate.set_font_size(72),
        )

        self.wait(2)

        # move to 2.8 and change to f(x) > g(x)
        # show second interval
        self.play(x.animate.set_value(2.8), run_time=2)
    
        self.play(
                Transform(symbol, greater_symbol), 
                flabel.animate.set_font_size(90), 
                glabel.animate.set_font_size(54),
        )

        self.wait(2)

        self.play(Write(secondset))

        self.wait(2)

        # move to 3.5 
        self.play(x.animate.set_value(3.5), run_time=5)

        self.wait(2)

        # deconstruct everything
        self.play(
                Uncreate(fline),
                Uncreate(gline),
                Uncreate(xtick),
                Unwrite(xlabel),
        )
        self.play(
                Unwrite(full_label),
        )

        self.wait(2)

##
