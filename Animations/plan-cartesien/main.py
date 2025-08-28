from manim import *
import numpy as np

XCOLOR = RED_A
YCOLOR = PURPLE_A
FCOLOR = GOLD_A
PCOLOR = GREEN
tick_length=.2
small_tick_length=.1

# write decimal separator with commas instead of dots
def comma(num):
    if num==0:
        return "0"
    return ("%.2f" % num).rstrip('.0') .replace('.', ',')

class PlanCartesien(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{libertinus,libertinust1math,calrsfs, icomma}\mathcode`\;="303B')
        self.tex_template=myTemplate
        MathTex.set_default(font_size=72)
        Tex.set_default(font_size=72)
        
        # axes
        xaxis = Line(6*LEFT, 6*RIGHT)
        xticks = VGroup([Line(UP,DOWN, stroke_width=1).scale(small_tick_length).shift(x*RIGHT) for x in np.arange(-6, 6.1,1)])
        x1 = MathTex("1", tex_template=self.tex_template, font_size=36)
        x1.next_to(RIGHT, DOWN/2)
        x0 = MathTex("0", tex_template=self.tex_template, font_size=36)
        x0.next_to([0,0,0], DOWN/2)

        yaxis = Line(4*DOWN, 4*UP)
        yticks = VGroup([Line(LEFT,RIGHT, stroke_width=1).scale(small_tick_length).shift(y*UP) for y in np.arange(-4, 4.1,1)])
        y1 = MathTex("1", tex_template=self.tex_template, font_size=36)
        y1.next_to(UP, LEFT/2)
        
        self.play(Create(xaxis))
        self.play(Create(xticks))
        self.play(Write(x0))
        self.play(Write(x1))
        self.camera.auto_zoom([xaxis, yaxis])

        self.wait()
        
        # xtick way and back
        xtick = Line(UP*tick_length, DOWN*tick_length, color=XCOLOR)
        xtick.move_to(4*LEFT)
        xlabel = MathTex("x", color=XCOLOR)
        xlabel.next_to(xtick, UP)
        self.play(Create(xtick), Write(xlabel))

        always_redraw(lambda: xlabel.next_to(xtick, UP))
        self.play(xtick.animate.shift(8*RIGHT), rate_func = there_and_back, run_time=2)
        
        self.play(Uncreate(xtick), Unwrite(xlabel))

        self.wait()
        
        # ytick way and back
        self.play(Uncreate(x0), Create(yaxis))
        self.play(Create(yticks))
        self.play(Write(y1))
        ytick = Line(LEFT*tick_length, RIGHT*tick_length, color=YCOLOR)
        ytick.move_to(3*UP)
        ylabel = MathTex("y", color=YCOLOR)
        ylabel.next_to(ytick, RIGHT)
        self.play(Create(ytick), Write(ylabel))

        always_redraw(lambda: ylabel.next_to(ytick, RIGHT))
        self.play(ytick.animate.shift(6*DOWN), rate_func=there_and_back, run_time=2)
        
        self.play(Uncreate(ytick), Unwrite(ylabel))

        self.wait()

        # drawing (1,2)
        p1 = self.draw_point(1,2, color=GREEN, point_name="P")
        self.wait()
        
        # drawing (3,-2)
        p2 = self.draw_point(3,-2, color=YELLOW, point_name="Q")
        self.wait()
        
        # drawing (-4,2)
        p3 = self.draw_point(-4,2, color=PINK, point_name="R")
        self.wait()
        
        self.play(
                Uncreate(p1),
                Uncreate(p2),
                Uncreate(p3),
                )

        self.wait(3)

    def draw_point(self, x,y, color=GREEN, point_name="P"):
        point_label = MathTex(point_name+f"({x} ; {y})", 
                tex_template=self.tex_template,
                tex_to_color_map={f"{x}":XCOLOR, f"{y}":YCOLOR, point_name:color},
                )
        point_label = Label(point_label)
        point_label.to_edge(UP+RIGHT)
        self.play(Write(point_label))

        xtracker = ValueTracker(0)
        ytracker = ValueTracker(0)

        xsign = int(np.sign(x))
        ysign = int(np.sign(y))
        
        # x tick moving into position
        xtick = Line(UP*tick_length, DOWN*tick_length, color=XCOLOR)
        xlabel = always_redraw(lambda: Text(comma(xtracker.get_value()), color=XCOLOR).next_to(xtick,ysign*DOWN))
        
        self.play(Create(xtick), Write(xlabel))

        self.play(
                xtick.animate.shift(RIGHT*x),
                xtracker.animate.set_value(x), 
                run_time=2,
                #rate_func=rate_functions.ease_out_back,
                )
        
        # y tick moving into position
        # with dashed lines
        ytick = Line(LEFT*tick_length, RIGHT*tick_length, color=YCOLOR)
        ylabel = always_redraw(lambda: Text(comma(ytracker.get_value()), color=YCOLOR).next_to(ytick,xsign*LEFT))

        self.play(Create(ytick), Write(ylabel))
        
        vline = always_redraw(lambda: DashedLine([x,0,0], [x,ytracker.get_value(),0], color=XCOLOR))
        hline = DashedLine([0,0,0],[x,0,0], color=YCOLOR)
        
        # dot P
        point = Dot(x*RIGHT, color=color, radius=.04)
        
        self.add(hline, point, vline)
        self.play(
                point.animate.shift(UP*y),
                ytick.animate.shift(UP*y),
                ytracker.animate.set_value(y),
                hline.animate.shift(UP*y),
                run_time=2,
                #rate_func=rate_functions.ease_out_back,
                )
        
        P = MathTex(point_name+f"({x} ; {y})", 
                tex_template=self.tex_template,
                tex_to_color_map={f"{x}":XCOLOR, f"{y}":YCOLOR, point_name:color},
                font_size=64,
                )
        P.next_to(point, ysign*UP+xsign*RIGHT)
        self.play(Write(P))
        
        # clean constructions
        self.play(
                FadeOut(vline),
                FadeOut(hline),
                Uncreate(xtick),
                Uncreate(ytick),
                Unwrite(xlabel),
                Unwrite(ylabel),
                Unwrite(point_label),
                )

        return VGroup([point, P])

##
