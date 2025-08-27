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
    return (x-4)/3

def g(x):
    return -(x-1)/2

def h(x):
    return f(x)*g(x)

class ProduitAffine(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{libertinus,libertinust1math,calrsfs}")
        MathTex.set_default(font_size=72)
        Tex.set_default(font_size=72)
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

        objects_in_frame = Group(axes)

        self.play(Create(axes), self.camera.auto_zoom(objects_in_frame))
        
        self.wait()
       
        # graphs of f and g
        f_graph = axes.plot(
                f,
                x_range=[-2,6,1],
                color=BLUE_E,
                stroke_width=4,
        )
        g_graph = axes.plot(
                g,
                x_range=[-2,6,1],
                color=RED_E,
                stroke_width=4,
        )
        h_graph = axes.plot(
                h,
                x_range=[-2,6,1],
                color=GOLD_E,
                stroke_width=4,
        )
        Cf = MathTex(r"\mathcal{C}_f", color=BLUE_E, tex_template=myTemplate)
        Cg = MathTex(r"\mathcal{C}_g", color=RED_E, tex_template=myTemplate)
        Cf.next_to(f_graph, UP+RIGHT).shift(LEFT*2)
        Cg.next_to(g_graph, DOWN+RIGHT).shift(LEFT*2)

        objects_in_frame.add(f_graph,g_graph, Cf, Cg)
        self.play(self.camera.auto_zoom(objects_in_frame))
        self.play(Create(f_graph), Write(Cf))
        self.play(Create(g_graph), Write(Cg))

        # x through domain
        domain = Label(MathTex(r"\mathcal{D} = [-2 ; 6]", color=XCOLOR, tex_template=myTemplate), color=XCOLOR)
        domain.next_to(axes, RIGHT).shift(UP*2)
        objects_in_frame.add(domain)
        self.play(self.camera.auto_zoom(objects_in_frame))
        self.play(Write(domain))
    
        tick_length=.2
        xtick = Line(axes.c2p(-2, -tick_length), axes.c2p(-2, +tick_length), color=XCOLOR)
        xlabel = MathTex("x", color=XCOLOR).next_to(xtick, UP)
        x = VGroup(xtick, xlabel)
        
        self.play(Create(x))
        self.play(x.animate.shift(8*RIGHT))
        self.play(x.animate.shift(8*LEFT))
        self.play(Unwrite(xlabel))

        # sign of f, g at x
        fline = DashedLine(axes.c2p(-2,0), axes.c2p(-2, f(-2)), color=BLUE_E)
        flabel = MathTex("f(-2) < 0", font_size=50, color=BLUE_E).next_to(fline, DOWN)
        gline = DashedLine(axes.c2p(-2,0), axes.c2p(-2, g(-2)), color=RED_E)
        glabel = MathTex("g(-2) > 0", font_size=50, color=RED_E).next_to(gline, UP)
        
        objects_in_frame.add(fline,flabel,gline,glabel)
        self.play(self.camera.auto_zoom(objects_in_frame))
        
        self.play(Create(fline))
        self.play(Write(flabel))
        self.play(Uncreate(fline), Unwrite(flabel))
        self.play(Create(gline))
        self.play(Write(glabel))
        self.play(Uncreate(gline), Unwrite(glabel))
        
        objects_in_frame.remove(fline,flabel,gline,glabel)
        self.play(self.camera.auto_zoom(objects_in_frame))
        self.play(Uncreate(xtick))

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

        # first interval
        interval1=Line(axes.c2p(-2,0), axes.c2p(1,0), color=GREEN, stroke_width=5)
        I1label = always_redraw(lambda: MathTex("[-2 ; "+comma(min(1,np.round(xtracker.get_value(),1)))+"]", color=GREEN).next_to(axes,RIGHT))
        objects_in_frame.add(I1label)

        self.play(FadeIn(hsync),Write(I1label), self.camera.auto_zoom(objects_in_frame))
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
       
        # second interval
        self.play(hsync.animate.set_color(YELLOW))
        
        interval2=Line(axes.c2p(1,0), axes.c2p(4,0), color=YELLOW, stroke_width=5)
        I2label = always_redraw(lambda: MathTex("[1 ; "+comma(min(4,np.round(xtracker.get_value(),1)))+"]", color=YELLOW).next_to(I1label,DOWN*3))
        objects_in_frame.add(I2label)
        self.play(Write(I2label), self.camera.auto_zoom(objects_in_frame))
        
        self.play(
                xtracker.animate.set_value(4), 
                hsync.animate.shift(RIGHT*3),
                Create(interval2),
                run_time=3,
                rate_func=linear,
                )

        self.play(hsync.animate.scale(1.1), run_time=.5)
        self.play(hsync.animate.scale(0.909), run_time=.5)
        
        # third interval
        self.play(hsync.animate.set_color(PINK))
        
        interval3=Line(axes.c2p(4,0), axes.c2p(6,0), color=PINK, stroke_width=5)
        I3label = always_redraw(lambda: MathTex("[4 ; "+comma(min(6,np.round(xtracker.get_value(),1)))+"]", color=PINK).next_to(I2label, DOWN*3))
        objects_in_frame.add(I3label)
        self.play(Write(I3label), self.camera.auto_zoom(objects_in_frame))
        
        self.play(
                xtracker.animate.set_value(6), 
                hsync.animate.shift(RIGHT*2),
                Create(interval3),
                run_time=3,
                rate_func=linear,
                )
        
        self.play(FadeOut(hsync))

        #self.wait(3)
        #self.play(Create(h_graph))
        
        self.wait(3)


##
