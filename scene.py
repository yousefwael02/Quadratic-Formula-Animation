from manim import *

class QuadraticFormula(Scene):
    def construct(self):
        
        # Initial formula
        equation = MathTex(r"ax^2 + bx + c = 0")
        self.play(Write(equation))
        self.wait(2)

        # Step 1: Divide by a
        title1 = Text("Divide by a")
        title1.to_edge(UP)
        self.play(Write(title1))

        step1 = MathTex(r"x^2 + \frac{b}{a}x + \frac{c}{a} = 0")
        self.play(Transform(equation, step1))
        self.wait(2)

        # Step 2: Complete the sqaure
        title2 = Text("Complete the square")
        title2.to_edge(UP)
        self.play(Unwrite(title1))
        self.play(Write(title2))

        step2 = MathTex(r"(x + \frac{b}{2a})^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0")
        self.play(Transform(equation, step2))
        self.wait(2)
