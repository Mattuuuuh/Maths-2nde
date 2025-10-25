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
    return x**3/3 - 2*x+3

def g(x):
    return -4*x**2 + 7

class InegaliteGraphique(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{libertinus,libertinust1math,calrsfs, icomma}")
        MathTex.set_default(font_size=72)
        Tex.set_default(font_size=72)
        # axes
        axes = NumberPlane(
                x_range=(-3.4, 2.1, 1),
                y_range=(-2.1,7.1,2),
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

        objects_in_frame = Group(axes)

        self.play(Create(axes), self.camera.auto_zoom(objects_in_frame))
        
        self.wait()
       
        # graphs of f and g
        f_graph = axes.plot(
                f,
                x_range=[-4,8,1],
                color=BLUE_E,
                stroke_width=4,
        )
        g_graph = axes.plot(
                g,
                x_range=[-4,8,1],
                color=RED_E,
                stroke_width=4,
        )
        Cf = MathTex(r"\mathcal{C}_f", color=BLUE_E, tex_template=myTemplate)
        Cg = MathTex(r"\mathcal{C}_g", color=RED_E, tex_template=myTemplate)
        Cf.next_to(f_graph, UP+RIGHT).shift(LEFT*2)
        Cg.next_to(g_graph, DOWN+RIGHT).shift(LEFT*2)

        objects_in_frame.add(f_graph,g_graph, Cf, Cg)
        #self.play(self.camera.auto_zoom(objects_in_frame))
        self.play(Create(f_graph), Write(Cf))
        self.play(Create(g_graph), Write(Cg))

        # x through domain
        domain = Label(MathTex(r"\mathcal{D} = [-2 ; 6]", color=XCOLOR, tex_template=myTemplate), color=XCOLOR)
        domain.next_to(axes, RIGHT).shift(UP*2)
        objects_in_frame.add(domain)
        #self.play(self.camera.auto_zoom(objects_in_frame))
        self.play(Write(domain))
    
        tick_length=.2
        xtick = Line(axes.c2p(-2, -tick_length), axes.c2p(-2, +tick_length), color=XCOLOR)
        xlabel = MathTex("x", color=XCOLOR).next_to(xtick, UP)
        x = VGroup(xtick, xlabel)
        
        self.play(Create(x))
        self.play(x.animate.shift(8*RIGHT))
        self.play(x.animate.shift(8*LEFT))
        self.play(Unwrite(xlabel))

