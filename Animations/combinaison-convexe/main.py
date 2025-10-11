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
       
        # xaxis (-6, -3, 0) --> (6,-3,0) with padding left/right
        xaxis = Arrow([-6,-3,0]+LEFT,[6,-3,0]+RIGHT, max_tip_length_to_length_ratio=.01, stroke_width=3)
        self.play(Create(xaxis))
        
        # placing x=10
        ten_tick = Line([-6,-3,0] + tick_length*UP, [-6,-3,0] + tick_length*DOWN, color=XCOLOR)
        ten_label = MathTex("10", 
                tex_template=self.tex_template,
                color=XCOLOR,
                )
        ten_label.next_to(ten_tick, DOWN)
        
        self.play(Create(ten_tick))
        self.play(Write(ten_label))

        # placing x=17
        seventeen_tick = Line([6,-3,0] + tick_length*UP, [6,-3,0] + tick_length*DOWN, color=YCOLOR)
        seventeen_label = MathTex("17", 
                tex_template=self.tex_template,
                color=YCOLOR,
                )
        seventeen_label.next_to(seventeen_tick, DOWN)
        
        self.play(Create(seventeen_tick))
        self.play(Write(seventeen_label))

        # weight Wx for x combination
        # lambda * 10 + (1-lambda)* 17 = 17 - lambda*7
        # W(-6) + (1-W)(6) = 6 - 12W
        Wx = ValueTracker(.5)
        
        # writing convex combination
        combination_text = always_redraw(lambda:
            Label(MathTex(
            f"{comma(Wx.get_value())}\\times10 + {comma(1-Wx.get_value())}\\times17", 
            tex_template=self.tex_template,
            tex_to_color_map={"10":XCOLOR, "17":YCOLOR},
            )
            ).move_to([3,3,0])
        )

        self.play(Write(combination_text))
        
        # placing the middle
        middle_tick = always_redraw(lambda:
                Line(tick_length*UP, tick_length*DOWN, color=FCOLOR)
                .move_to([6-12*Wx.get_value(),-3,0])
        )
        middle_label = always_redraw(lambda:
            MathTex(comma(17-7*Wx.get_value()), 
            tex_template=self.tex_template,
            color=FCOLOR,
            ).next_to(middle_tick, UP)
        )
        self.play(Create(middle_tick))
        self.play(Write(middle_label))

        # writing the weight lambda
        weigth_text = always_redraw(lambda:
            MathTex(
            f"\\lambda = {comma(Wx.get_value())}", 
            tex_template=self.tex_template,
            ).next_to(xaxis,DOWN)
        )
        
        self.play(Write(weigth_text))

        # moving stuff :)

        self.wait(2)

        self.play(
                Wx.animate.set_value(0),
                run_time=5,
                )

        self.wait(2)

        self.play(
                Wx.animate.set_value(1),
                run_time=5,
                )
        
        self.wait(2)

        # yaxis [-7, -2, 0] --> [-7,2,0] with up/down padding
        yaxis = Arrow([-7,-2,0]+DOWN,[-7,2,0]+UP, max_tip_length_to_length_ratio=.01, stroke_width=3)
        self.play(Create(yaxis))

        # dezoom a bit and move left
        self.play(self.camera.frame.animate.scale(1.2).move_to([-1,0,0]))

        # placing x=10
        ten_tickY = Line([-7,-2,0]+tick_length*LEFT,  [-7,-2,0]+tick_length*RIGHT, color=XCOLOR)
        ten_labelY = MathTex("10", 
                tex_template=self.tex_template,
                color=XCOLOR,
                )
        ten_labelY.next_to(ten_tickY, LEFT)
        
        self.play(Create(ten_tickY))
        self.play(Write(ten_labelY))

        # placing x=17
        seventeen_tickY = Line([-7,2,0]+tick_length*LEFT, [-7,2,0]+tick_length*RIGHT, color=YCOLOR)
        seventeen_labelY = MathTex("17", 
                tex_template=self.tex_template,
                color=YCOLOR,
                )
        seventeen_labelY.next_to(seventeen_tickY, LEFT)
        
        self.play(Create(seventeen_tickY))
        self.play(Write(seventeen_labelY))

        # weight W for combination
        # lambda * 10 + (1-lambda)* 17 = 17 - lambda*7
        Wy = ValueTracker(Wx.get_value())

        # placing the middle
        middle_tickY = always_redraw(lambda:
                Line(tick_length*LEFT, tick_length*RIGHT, color=FCOLOR)
                .move_to([-7, 2-4*Wy.get_value(),0])
        )
        middle_labelY = always_redraw(lambda:
            MathTex(comma(17-7*Wy.get_value()), 
            tex_template=self.tex_template,
            color=FCOLOR,
            font_size=36,
            ).next_to(middle_tickY, RIGHT)
        )
        self.play(Create(middle_tickY))

        # don't show, too cluttered
        #self.play(Write(middle_labelY))
        self.play(Unwrite(middle_label))

        # writing the weight lambda
        weigth_textY = always_redraw(lambda:
            MathTex(
            f"\\lambda = {comma(Wy.get_value())}", 
            tex_template=self.tex_template,
            ).next_to(yaxis,LEFT).rotate(PI/2)
        )
    
        self.play(Write(weigth_textY))

        # moving stuff :)
    
        """
        self.play(
                Wy.animate.set_value(0),
                Wx.animate.set_value(0),
                run_time=5,
                )

        self.wait(2)
        """
        # create A 
        A = Dot([-6,-2,0])
        Alabel = MathTex("A", tex_template=self.tex_template, font_size=48).next_to(A,LEFT+DOWN, .1)
        self.play(
                Create(A),
                Write(Alabel),
        )


        # placing M( 6-12*Wx, 2 - 4*Wy ), at (0,0) when Wx=Wy=.5 (middle point)
        # with dotted lines to M
        M = always_redraw(lambda:
                Dot([6 - 12*Wx.get_value(), 2-4*Wy.get_value(),0],
                color=GOLD_E,),
        )
        
        dottedX = always_redraw(lambda:
                DashedLine([6 - 12*Wx.get_value(), 2-4*Wy.get_value(),0],
                    [6 - 12*Wx.get_value(), -3, 0],
                    color=GOLD_E,
                )
        )
        
        dottedY = always_redraw(lambda:
                DashedLine([6 - 12*Wx.get_value(), 2-4*Wy.get_value(),0],
                    [-7, 2-4*Wy.get_value(), 0],
                    color=GOLD_E,
                )
        )

        self.play(Create(dottedX), Create(dottedY), Create(M))
       
        # move to middle
        self.play(
                Wy.animate.set_value(0.5),
                Wx.animate.set_value(0.5),
                run_time=5,
                )
        self.wait(1)
        
        # create M midpoint
        Mid = Dot([0,0,0])
        Midlabel = MathTex("M", tex_template=self.tex_template, font_size=48).next_to(Mid,UP, .1)
        self.play(
                Create(Mid),
                Write(Midlabel),
        )

        self.wait(1)

        # move to B
        self.play(
                Wy.animate.set_value(0),
                Wx.animate.set_value(0),
                run_time=5,
                )
        self.wait(1)

        # create B
        B = Dot([6,2,0])
        Blabel = MathTex("B", tex_template=self.tex_template, font_size=48).next_to(B,RIGHT+UP, .1)
        self.play(
                Create(B),
                Write(Blabel),
        )

        self.wait(2)

        # sliding and creating the segment [AB]
        ABsegment = Line([6,2,0], [-6,-2,0])

        self.play(
                Wy.animate.set_value(1),
                Wx.animate.set_value(1),
                Create(ABsegment),
                run_time=5,
                )
        
        self.wait(2)

        # showing that when Wx = 1/3 and Wy = 1/2 (different weights), the point is NOT on the segment
        self.play(Uncreate(combination_text))
        
        # zoom a bit and move left
        self.play(self.camera.frame.animate.scale(.95))

        self.play(
                Wx.animate.set_value(.33),
                Wy.animate.set_value(.5),
                run_time=5,
        )
        
        self.wait(2)
        
        # show P not on [AB]
        Plabel = MathTex("P \\not\\in [AB]", tex_template=self.tex_template, color=GOLD_E).next_to(M,RIGHT)
        self.play(Write(Plabel))

        self.wait(2)

        self.play(Uncreate(dottedX), 
                Uncreate(dottedY),
                Uncreate(middle_tick),
                Uncreate(middle_tickY),
        )

        self.wait(2)



##
