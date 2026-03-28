from manim import *
import numpy as np

DASHEDCOLOR = YELLOW_A
FCOLOR = BLUE_A
ACOLOR = RED_A
BCOLOR = GREEN_A

# write decimal separator with commas instead of dots
def comma(num):
    if num==0:
        return "0"
    if num == int(num):
        return str(int(num))
    return ("%.2f" % num).replace('.', ',')

def showparentheses(str_num):
    if str_num[0]=="-":
        return f"({str_num})"
    return str_num

def f(x, a, b):
    return a*x+b

class ProduitAffine(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        MathTex.set_default(font_size=72)
        myTemplate.add_to_preamble(r"\usepackage{libertinus,libertinust1math,calrsfs,icomma,amsmath, xcolor}")
        myTemplate.add_to_preamble(r"""\mathcode`\;="303B""")
        myTemplate.add_to_preamble(r"\definecolor{BLUE_A}{HTML}{C7E9F1}\definecolor{RED_A}{HTML}{F7A1A3}\definecolor{GREEN_A}{HTML}{C9E2AE}")
        Tex.set_default(font_size=72)
        # axes
        axes = NumberPlane(
                x_range=(-16.1, 16.1, 1),
                y_range=(-9.1,9.1,1),
                x_length=16,
                y_length=9,
                tips=True,
                background_line_style={
                    "stroke_width": 1,
                    "stroke_opacity": .4,
                },
                axis_config={
                    "stroke_width": 2,
                    "stroke_opacity":1,
                    "font_size":12,
                },
        )
        
        axes.add_coordinates()

        objects_in_frame = Group(axes)

        self.play(Create(axes), self.camera.auto_zoom(objects_in_frame))
        
        self.wait()
      
        # affine function f = a·x+b
        a = ValueTracker(1)
        b = ValueTracker(1)

        # graph of f
        WIDTH = 3
        f_graph = always_redraw(lambda: 
            axes.plot(
                lambda x: f(x, a.get_value(), b.get_value()),
                x_range=[-16,16,20],
                color=FCOLOR,
                stroke_width=WIDTH,
            )
        )

        Cf = always_redraw(lambda:
            Label(
                MathTex(
                    r"y = {\color{RED_A}"+comma(a.get_value())+
                    r"} \cdot x + {\color{GREEN_A}"+showparentheses(comma(b.get_value()))+
                    r"}",
                    tex_template=myTemplate,
                ).next_to(axes.c2p(1,10,0),RIGHT)
            )
        )

        objects_in_frame.add(Cf)

        # label containing a, b, y=ax+b
        parameters = always_redraw(lambda:
            Label(
                MathTex(
                r"{ \color{RED_A} a } &= { \color{RED_A}", comma(a.get_value()),
                r"} \\", r"{\color{GREEN_A} b } &= {\color{GREEN_A} ", comma(b.get_value()),
                r"}",
                tex_template=myTemplate,
                )
            ).next_to(axes.coords_to_point(-10,10,0), RIGHT)
        )
        
        objects_in_frame.add(parameters)

        self.play(self.camera.auto_zoom(objects_in_frame))
        self.play(Write(parameters))
        self.wait(2)
        self.play(Write(Cf))
        self.wait(2)
        self.play(Create(f_graph))
        self.wait(2)


        # ordonnée à l'origine B(0;b)
        B = always_redraw(lambda:
            Dot(axes.coords_to_point(0, b.get_value(), 0), color=GREEN_A)
        )
        Bcoords = always_redraw(lambda:
            MathTex(r"(0 ; {\color{GREEN_A}"+comma(b.get_value())+"})",
                tex_template=myTemplate,
            ).next_to(B, LEFT)
        )
        objects_in_frame.add(B, Bcoords)

        self.play(Write(B), Write(Bcoords))




        self.wait(2)


        self.play(
                b.animate.set_value(-5),
                run_time=3,
                )
        
        self.wait(2)

        self.play(
                b.animate.set_value(5),
                run_time=3,
                )
        
        self.wait(2)

        self.play(
                b.animate.set_value(-1),
                run_time=3,
                )
       
        self.wait(2)

        self.play(
                a.animate.set_value(-1),
                run_time=3,
                )

        self.wait(2)

        self.play(
                a.animate.set_value(0),
                run_time=3,
                )

        self.wait(2)

        self.play(
                a.animate.set_value(2),
                run_time=3,
                )

        self.wait(2)


        # right now a = 2, b = -1

        # dashed lines for  "when i move x by 1, i move y by a"
        # P on Cf at x = 3
        # Q on Cf at x = 4
        # R st PQR is rectangle in R and R below Cf
        x = 3
        P = Dot(axes.coords_to_point(x, f(x, a.get_value(), b.get_value()), 0), color=DASHEDCOLOR, radius=.04)

        x = 4
        Q = Dot(axes.coords_to_point(x, f(x, a.get_value(), b.get_value()), 0), color=DASHEDCOLOR, radius=.04)
        R = Dot(axes.coords_to_point(x, f(3, a.get_value(), b.get_value()), 0), color=DASHEDCOLOR, radius=.04)


        xline = DashedLine(P, R, color=DASHEDCOLOR, stroke_width=2)
        dx = MathTex("1", color=DASHEDCOLOR, font_size=20).next_to(xline,DOWN*.5)
        yline = DashedLine(R, Q, color=ACOLOR, stroke_width=2)
        dy = MathTex(comma(a.get_value()), color=ACOLOR, font_size=20).next_to(yline,RIGHT*.5)
        V = Arrow(axes.c2p(6,4,0), axes.c2p(7,6,0), buff=0, stroke_width=1, tip_length=.1)
        v = Tex(r"$\begin{pmatrix} 1 \\ {\color{RED_A} 2}\end{pmatrix}$", font_size=28, tex_template=myTemplate).next_to(V,RIGHT*.5)

        newframe = VGroup([P, Q, R, xline, yline, dx, dy, v,V])

        WIDTH = 1
        self.play(self.camera.auto_zoom(newframe).scale(2), f_graph.animate.set_stroke_width(1))
        self.wait()
        self.play(Create(P))
        self.wait(1)
        self.play(Create(Q))
        self.wait(1)
        self.play(Create(V))
        self.wait(2)
        self.play(Create(xline))
        self.play(Create(yline))
        self.wait(1)
        self.play(Write(dx))
        self.play(Write(dy))
        self.wait(1)
        self.play(Write(v))
        self.wait(2)
        
        self.play(self.camera.auto_zoom(objects_in_frame), f_graph.animate.set_stroke_width(3))
        WIDTH = 3

        self.wait(2)
        self.play(
                Uncreate(xline),
                Uncreate(yline),
                Unwrite(dx),
                Unwrite(dy),
                Uncreate(P),
                Uncreate(Q),
                Unwrite(v),
                Uncreate(V),
        )
    
        self.wait(2)

        self.play(
                a.animate.set_value(-3),
                b.animate.set_value(5),
                run_time=3,
                )

        self.wait()

        # right now a = -3, b = 5

        # dashed lines for  "when i move x by 1, i move y by a"
        # P on Cf at x = 2
        # Q on Cf at x = 3
        # R st PQR is rectangle in R and R above Cf
        # S on Cf at x=4
        # T st PST rectangle in T
        x = 2
        P = Dot(axes.coords_to_point(x, f(x, a.get_value(), b.get_value()), 0), color=DASHEDCOLOR, radius=.04)

        x = 3
        Q = Dot(axes.coords_to_point(x, f(x, a.get_value(), b.get_value()), 0), color=DASHEDCOLOR, radius=.04)
        R = Dot(axes.coords_to_point(x, f(2, a.get_value(), b.get_value()), 0), color=DASHEDCOLOR, radius=.04)
        x = 4
        S = Dot(axes.coords_to_point(x, f(x, a.get_value(), b.get_value()), 0), color=DASHEDCOLOR, radius=.04)
        T = Dot(axes.coords_to_point(x, f(2, a.get_value(), b.get_value()), 0), color=DASHEDCOLOR, radius=.04)


        xline = DashedLine(P, R, color=DASHEDCOLOR, stroke_width=2)
        dx = MathTex("1", color=DASHEDCOLOR, font_size=20).next_to(xline,UP*.5)
        yline = DashedLine(R, Q, color=ACOLOR, stroke_width=2)
        dy = MathTex(comma(a.get_value()), color=ACOLOR, font_size=20).next_to(yline,RIGHT*.5)
        V = Arrow(axes.c2p(5,-1,0), axes.c2p(6,-4,0), stroke_width=2, tip_length=.1, buff=0)
        v = Tex(r"$\begin{pmatrix} 1 \\ {\color{RED_A} -3}\end{pmatrix}$", font_size=28, tex_template=myTemplate).next_to(V,RIGHT*.5)
        
        xline2 = DashedLine(P, T, color=DASHEDCOLOR, stroke_width=2)
        dx2 = MathTex("2", color=DASHEDCOLOR, font_size=20).next_to(xline2,UP*.5)
        yline2 = DashedLine(T, S, color=ACOLOR, stroke_width=2)
        dy2 = MathTex(comma(2*a.get_value()), color=ACOLOR, font_size=20).next_to(yline2,RIGHT*.5)
        V2 = Arrow(axes.c2p(8,-1,0), axes.c2p(10,-7,0), stroke_width=2, tip_length=.1, buff=0)
        v2 = Tex(r"$\begin{pmatrix} 2 \\ -6\end{pmatrix} = 2 \begin{pmatrix} 1 \\ {\color{RED_A} -3}\end{pmatrix}$", font_size=28, tex_template=myTemplate).next_to(V2,RIGHT*.5)

        newframe = VGroup([P, Q, R, S, T, xline, yline, dx, dy, xline2, yline2, dx2, dy2, v, v2, V, V2])

        WIDTH = 2
        self.play(self.camera.auto_zoom(newframe).scale(1.1), f_graph.animate.set_stroke_width(2))
        self.wait()
        self.play(Create(P))
        self.wait(1)
        self.play(Create(Q))
        self.wait(1)
        self.play(Create(V))
        self.wait(2)
        self.play(Create(xline))
        self.play(Create(yline))
        self.wait(1)
        self.play(Write(dx))
        self.play(Write(dy))
        self.wait(1)
        self.play(Write(v))

        self.wait(2)
        
        self.play(
                Uncreate(xline),
                Uncreate(yline),
                Unwrite(dx),
                Unwrite(dy),
                Uncreate(Q),
                #Uncreate(V),
                #Unwrite(v),
        )

        self.wait(2)
        
        self.play(Create(S))
        self.wait(1)
        self.play(Create(V2))
        self.wait(2)
        self.play(Create(xline2))
        self.play(Create(yline2))
        self.wait(1)
        self.play(Write(dx2))
        self.play(Write(dy2))
        self.wait(1)
        self.play(Write(v2))
        self.wait(2)

        self.play(self.camera.auto_zoom(objects_in_frame), f_graph.animate.set_stroke_width(3))
        WIDTH = 3

        self.wait(2)
        self.play(
                Uncreate(xline2),
                Uncreate(yline2),
                Unwrite(dx2),
                Unwrite(dy2),
                Uncreate(P),
                Uncreate(S),
                Uncreate(V),
                Unwrite(v),
                Uncreate(V2),
                Unwrite(v2),
        )
    
        self.wait(2)


        self.play(
            FadeOut(B), 
            FadeOut(Bcoords),
            FadeOut(Cf),
            FadeOut(f_graph),
            FadeOut(parameters),
            FadeOut(axes),
        )

        self.wait()





