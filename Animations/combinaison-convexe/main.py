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
    if num == int(num):
        return str(int(num))
    return ("%.2f" % num).replace('.', ',')

class CombinaisonConvexe(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{libertinus,libertinust1math,calrsfs, icomma}\mathcode`\;="303B')
        self.tex_template=myTemplate
        MathTex.set_default(font_size=72)
        Tex.set_default(font_size=72)
       
        # axis
        xaxis = Arrow(6*LEFT, 6*RIGHT, max_tip_length_to_length_ratio=.01, stroke_width=3)
        self.play(Create(xaxis))
        
        # placing x=10
        ten_tick = Line(3*LEFT + tick_length*UP, 3*LEFT + tick_length*DOWN, color=XCOLOR)
        ten_label = MathTex("10", 
                tex_template=self.tex_template,
                color=XCOLOR,
                )
        ten_label.next_to(ten_tick, DOWN)
        
        self.play(Create(ten_tick))
        self.play(Write(ten_label))

        # placing x=17
        seventeen_tick = Line(3*RIGHT + tick_length*UP, 3*RIGHT + tick_length*DOWN, color=YCOLOR)
        seventeen_label = MathTex("17", 
                tex_template=self.tex_template,
                color=YCOLOR,
                )
        seventeen_label.next_to(seventeen_tick, DOWN)
        
        self.play(Create(seventeen_tick))
        self.play(Write(seventeen_label))

        # weight W for combination
        # lambda * 10 + (1-lambda)* 17 = 17 - lambda*7
        W = ValueTracker(.5)

        # writing convex combination
        combination_text = always_redraw(lambda:
            Label(MathTex(
            f"{comma(W.get_value())}\\times10 + {comma(1-W.get_value())}\\times17", 
            tex_template=self.tex_template,
            tex_to_color_map={"10":XCOLOR, "17":YCOLOR},
            )
            ).move_to([3,3,0])
        )

        self.play(Write(combination_text))
        
        # placing the middle
        middle_tick = Line(tick_length*UP, tick_length*DOWN, color=FCOLOR)
        middle_label = always_redraw(lambda:
            MathTex(comma(17-7*W.get_value()), 
            tex_template=self.tex_template,
            color=FCOLOR,
            ).next_to(middle_tick, UP)
        )
        self.play(Create(middle_tick))
        self.play(Write(middle_label))

        # writing the weight lambda
        weigth_text = always_redraw(lambda:
            MathTex(
            f"\\lambda = {comma(W.get_value())}", 
            tex_template=self.tex_template,
            ).move_to(2*DOWN)
        )
        
        self.play(Write(weigth_text))

        # moving stuff :)

        self.wait(2)

        self.play(
                W.animate.set_value(1),
                middle_tick.animate.move_to(3*LEFT),
                run_time=5,
                )

        self.wait(2)

        self.play(
                W.animate.set_value(0),
                middle_tick.animate.move_to(3*RIGHT),
                run_time=5,
                )
        
        self.wait(2)


