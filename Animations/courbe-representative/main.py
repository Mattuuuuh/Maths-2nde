from manim import *
import numpy as np

XCOLOR = RED_A
YCOLOR = PURPLE_A
FCOLOR = GOLD_A
PCOLOR = GREEN

# write decimal separator with commas instead of dots
def comma(num):
    return f'{num}'.replace('.', ',')

class Courbe(MovingCameraScene):
    def f(self, x):
        return 6/(x**2+3)

    # maybe decimal points are more relevant actually
    def rational_pointf(self,x):
        denom = 1
        while denom*x != int(denom*x):
            denom+=1

        p = 6
        q = x**2+3
        p*= denom**2
        q*= denom**2
        p, q = int(p), int(q)
        d = np.gcd(p,q)
        p//=d
        q//=d
        return p,q

    # add points (x,y) to plane
    def add_pointsf(self, xsamples, animate=True):
        xtick=self.x[0]
        ytick=self.y[0]
        dots = VGroup()
        for xvalue in xsamples:
            # show xtick and label to correct position
            if animate:
                self.play(xtick.animate.move_to(self.axes.c2p(xvalue,0)))
            xlabel = MathTex(xvalue, color=XCOLOR)
            xlabel.next_to(xtick, direction=DOWN)
            if animate:
                self.play(Write(xlabel))

            # compute y
            yvalue = self.f(xvalue)
            p,q = self.rational_pointf(xvalue)
            if q==1:
                image_label = MathTex(f"f({comma(xvalue)}) = {p}")
            else:
                image_label = MathTex(f"f({comma(xvalue)}) = \dfrac{{{p}}}{{{q}}}")
            image_label.next_to(self.f_expr, direction=RIGHT*4)
            if animate:
                self.play(Create(image_label))

            # put point and lines, animate to (x,y)
            dot = Dot(self.axes.c2p(xvalue,0), color=PCOLOR, radius=.05)
            dots.add(dot)
            xline = self.axes.get_vertical_line(self.axes.c2p(xvalue,yvalue), color=PCOLOR)
            yline = self.axes.get_horizontal_line(self.axes.c2p(xvalue,0), color=PCOLOR)
            if animate:
                self.play(Create(dot),Create(yline))
                self.play(
                        dot.animate.shift(yvalue*UP),
                        yline.animate.shift(yvalue*UP),
                        Create(xline), 
                )
            else:
                dot.shift(yvalue*UP)
                self.play(Create(dot), run_time=.1)
            # cleanup
            if animate:
                self.play(
                        Uncreate(xline),
                        Uncreate(yline),
                        Uncreate(image_label),
                        Unwrite(xlabel),
                )
        return dots
    # interpolate from (x,y) points
    def affine_interpolationf(self, xsamples):
        points = [self.axes.c2p(x, self.f(x)) for x in xsamples]
        pointpairs = zip(points[:-1], points[1:])
        
        lines = VGroup()
        for pointpair in pointpairs:
            p1,p2 = pointpair
            interpol = Line(
                    start=p1,
                    end=p2,
                    color=PCOLOR,
            )
            #self.play(Create(interpol))
            lines.add(interpol)

        self.play(Create(lines))
        return lines

    def construct(self):
        # axes
        axes = NumberPlane(
                x_range=(-5.1, 5.1, 1),
                y_range=(-3.1,3.1,1),
                #x_length=8,
                #y_length=3,
                tips=True,
                background_line_style={
                    "stroke_width": 1,
                    "stroke_opacity": .4,
                },
                x_axis_config={
                    "color":XCOLOR,
                    "stroke_opacity":.8,
                },
                y_axis_config={
                    "color":YCOLOR,
                    "stroke_opacity":.8,
                },
        )
        self.play(Create(axes))
        
        self.wait()
        
        # x tick
        tick_length = .2
        xtick = Line(start=axes.c2p(-5, tick_length), end=axes.c2p(-5,-tick_length), color=XCOLOR)
        xlabel = (MathTex('x', color=XCOLOR).next_to(xtick, direction=DOWN))

        self.play(Create(xtick), Write(xlabel))
        
        x = VGroup(xtick, xlabel)

        self.play(x.animate.shift(10*RIGHT))
        self.play(x.animate.shift(-10*RIGHT))
        
        #self.play(FadeOut(xtick), Unwrite(xlabel))
        self.play(Unwrite(xlabel))
        
        # y tick
        tick_length = .2
        ytick = Line(start=axes.c2p(tick_length,3), end=axes.c2p(-tick_length,3), color=YCOLOR)
        ylabel = (MathTex('y', color=YCOLOR).next_to(ytick, direction=LEFT))

        self.play(Create(ytick), Create(ylabel))
        
        y = VGroup(ytick, ylabel)

        self.play(y.animate.shift(6*DOWN))
        self.play(y.animate.shift(-6*DOWN))

        self.play(FadeOut(ytick), Unwrite(ylabel))

        # function to graph
        f_expr = Label(MathTex("f(x) = \dfrac{6}{x^2 + 3}"), color=FCOLOR)
        f_expr.move_to(axes.c2p(-2,-2), RIGHT)

        self.play(Write(f_expr))
        self.wait()

        # bookkeeping
        self.axes=axes
        self.x=x
        self.y=y
        self.f_expr = f_expr

        # first run at graphing f
        xsamples = [-5, 0, 5]
        dots = self.add_pointsf(xsamples)
        lines = self.affine_interpolationf(xsamples)
        self.play(lines.animate.set_opacity(.3))
        self.wait()

        # second run
        xsamples = [-3, 3]
        dots = self.add_pointsf(xsamples)
        self.play(FadeOut(lines))
        lines = self.affine_interpolationf([-5,-3,0,3,5])
        self.play(lines.animate.set_opacity(.3))
        self.wait()

        # third run
        xsamples=np.arange(-5,5.1,.5)
        dots = self.add_pointsf(xsamples, animate=False)
        self.play(FadeOut(lines))
        lines = self.affine_interpolationf(np.arange(-5,5.1,.5))
        self.play(lines.animate.set_opacity(.3))
        
        self.play(FadeOut(lines),Uncreate(xtick))
        self.wait(2)
        
        f_graph = axes.plot(
                lambda x: self.f(x),
                x_range=[-5,5,1],
                color=GOLD,
                stroke_width=3,
        )

        self.play(Create(f_graph))

        self.wait(3)


