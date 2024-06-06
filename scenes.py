from manim import *
from manim_slides.slide import Slide

class Top(Slide):
    def construct(self):
        self.the_basic_setup()
        self.why_not_integers()
        self.prime_fields()
        self.hierarchy()
        self.extension_fields()

    def the_basic_setup(self):
        ### The stuff we want to encrypt, usually called the "plaintext",
        ### and can represent almost anything,
        pt_txt = Tex(r"\texttt{ATTACK AT DAWN}", font_size= 80)
        self.play(Write(pt_txt))
        self.next_slide()
        ### but we generally represent it just as ones and zeroes.
        pt_bin = Tex(r"\texttt{10101100111101}", font_size= 80)
        self.play(Transform(pt_txt, pt_bin))
        self.next_slide()
        ### We can then encrypt it
        encrypt_arrow = Arrow(start= UP * 2, end= DOWN * 2, buff= MED_LARGE_BUFF)
        ct_bin = Tex(r"\texttt{01010011000010}", font_size= 80).shift(DOWN * 2)
        self.play(pt_txt.animate.shift(UP * 2))
        self.play(
            Write(encrypt_arrow),
            Write(ct_bin),
        )
        self.next_slide()
        ### by doing a bunch of math,
        mafs = MathTex(r'''\begin{matrix}
            + & - \\
            \times & \div
        \end{matrix}''', font_size= 80)
        self.play(Write(mafs))
        self.next_slide()
        ### But we can't do normal binary math
        weird = Tex(r"$\leftarrow$ Weird", font_size= 70, color= "yellow").shift(RIGHT * 3)
        self.play(Write(weird))
        self.next_slide()
        ### because binary numbers aren't finite
        finite = Tex(r"Must be \emph{finite}", font_size= 70, color= "yellow").shift(RIGHT * 4)
        self.play(Transform(weird, finite))
        self.next_slide()
        self.play(
            Unwrite(encrypt_arrow),
            Unwrite(ct_bin),
            Unwrite(pt_txt),
            Unwrite(mafs),
            Unwrite(weird),
        )

    def why_not_integers(self):
        ### If we add two 3-digit binary numbers
        addition = MathTex(r"111 + 111", font_size= 80)
        self.play(Write(addition))
        self.next_slide()
        ### we get a 4-digit number.
        addition_full = MathTex(r"111 + 111 = 1110", font_size= 80)
        self.play(Transform(addition, addition_full))
        self.next_slide()
        ### If we multiply them, we get a 6-digit number.
        mult = MathTex(r"111 \times 111 = 110001", font_size= 80).shift(DOWN)
        self.play(
            addition.animate.shift(UP),
            Write(mult),
        )
        self.next_slide()
        ### This occurs because what we actually have
        self.play(
            Unwrite(addition),
            Unwrite(mult),
        )
        self.next_slide()
        ### are operations
        mafs = MathTex(r'''\begin{matrix}
            + & - \\
            \times & \div
        \end{matrix}''', font_size= 50).shift(2 * DOWN)
        self.play(Write(mafs))
        self.next_slide()
        ### which act on binary numbers
        binary = MathTex(r"\{0, 1, 10, 11, \cdots\}", font_size=80)
        self.play(Write(binary))
        self.next_slide()
        ### and the set of binary numbers
        self.play(mafs.animate.set_color('grey'))
        ### is infinite.
        infinite = MathTex(r"\infty", font_size=70, color= "yellow").shift(2 * UP)
        arrow = Arrow(start= infinite.get_bottom(), end= binary.get_top(), color="yellow")
        self.play(
            Write(infinite),
            Write(arrow),
        )
        self.next_slide()
        self.play(
            Unwrite(infinite),
            Unwrite(arrow),
            Unwrite(binary),
            Unwrite(mafs),
        )
        self.next_slide()
        ### You might think that this isn't a problem since
        table = Table([[
            "42", "1", "44.1",
        ], [
            "69,000,000", "4", "80.6",
        ]], col_labels= [
            Tex(""), mem_a := Tex("Min. size (Bytes)"), time_a := Tex(r"Time* of $n \times n$ (ns)"),
        ])
        for col in table.get_columns():
            for grp in col:
                for obj in grp:
                    obj.set_opacity(0)
        self.play(Write(table))
        self.next_slide()
        ### computers handle arbitrary-size numbers all the time.
        self.play(*(
            obj.animate.set_opacity(1) for grp in table.get_columns()[0] for obj in grp
        ))
        self.next_slide()
        ### We can't use them for encryption though, since their implementations leak how
        ### how big they are.
        disclaimer = Tex(
            "*according to sketchy Python I spent 30 seconds on",
            font_size=20,
        ).shift((3 * DOWN) + (3 * RIGHT))
        self.play(
            *(
                obj.animate.set_opacity(1) \
                    for col in table.get_columns()[1:] \
                        for grp in col \
                            for obj in grp
            ),
            Write(disclaimer),
        )
        self.next_slide()
        ### They would also be super slow,
        ### and proving they're secure would be much more difficult.
        self.play(
            Unwrite(table),
            Unwrite(disclaimer),
        )

    def prime_fields(self):
        ### The first trick we need is modulo arithmetic,
        ma = MathTex(r"3 + 3 = 6", font_size= 80)
        self.play(Write(ma))
        ### where numbers simply wrap around.
        ma_actual = MathTex(r"3 + 3 = 0\quad(\operatorname{mod} 6)", font_size= 80)
        self.play(Transform(ma, ma_actual))
        self.next_slide()
        ### You can pick a different "modulo" at which you jump
        ### back to zero.
        ma_alt = MathTex(r"3 + 3 = 2\quad(\operatorname{mod} 4)", font_size= 80)
        self.play(Transform(ma, ma_alt))
        self.next_slide()
        ### However, it turns out that in order to have division,
        division = MathTex(r"\div", font_size= 100, color= "red").shift(2 * DOWN)
        self.play(
            Write(division),
            Transform(ma, ma_alt.shift(UP)),
        )
        self.next_slide()
        ### the modulo must be prime.
        ma_prime = MathTex(r"3 + 3 = 1\quad(\operatorname{mod} 5)", font_size= 80).shift(UP)
        self.play(
            Transform(ma, ma_prime),
            division.animate.set_color("green"),
        )
        self.next_slide()
        ### But we now have definitions for the four basic operations,
        mafs = MathTex(r'''\begin{matrix}
            + & - \\
            \times & \div
        \end{matrix}''', font_size= 80).shift(2 * DOWN)
        self.play(Transform(division, mafs))
        self.next_slide()
        #### (which is just "do them modulo p")
        pf_mafs = MathTex(r'''\begin{matrix}
            + & - \\
            \times & \div
        \end{matrix}\quad(\operatorname{mod} p)''', font_size= 80).shift(2 * DOWN)
        self.play(Transform(division, pf_mafs))
        self.next_slide()
        ### for a finite set.
        pf_set = MathTex(r"\{0, 1, 2, \cdots, p - 1\}", font_size= 80).shift(UP)
        self.play(Transform(ma, pf_set))
        self.next_slide()
        ### Any set of mathematical objects
        fb = SurroundingRectangle(ma, buff= 0.1)
        self.play(Create(fb))
        self.next_slide()
        ### which we can add, subtract, multiply, and divide,
        fb_ops = SurroundingRectangle(division, buff= 0.1)
        self.play(Transform(fb, fb_ops))
        self.next_slide()
        ### is called a field.
        field_text = Tex(r"A \emph{Field}", font_size= 80).to_corner(UR)
        fb_field = SurroundingRectangle(VGroup(ma, division), buff= 0.1)
        self.play(
            Write(field_text),
            Transform(fb, fb_field),
        )
        ### This type of field is known as a prime field.
        self.next_slide()
        prime_field_text = Tex(r"A \emph{Prime Field}", font_size= 80).to_corner(UR)
        self.play(Transform(field_text, prime_field_text))
        ### Prime fields are one type of Galois field-
        self.next_slide()
        gf_text_text = Tex(r"A \emph{Galois Field}", font_size= 80).to_corner(UR)
        self.play(Transform(field_text, gf_text_text))
        ### the type with a prime number of elements.
        self.next_slide()
        gf_text = MathTex(r"\operatorname{GF}(p)", font_size= 80).to_corner(UR)
        self.play(Transform(field_text, gf_text))
        ### This isn't what we need to represent a sequence of bits, but it does
        ### let us represent just one.
        self.next_slide()
        gf2_text = MathTex(r"\operatorname{GF}(2)", font_size= 80).to_corner(UR)
        gf2_set = MathTex(r"\{0, 1\}", font_size= 80).shift(UP)
        gf2_mafs = MathTex(r'''\begin{matrix}
            + & - \\
            \times & \div
        \end{matrix}\quad(\operatorname{mod} 2)''', font_size= 80).shift(2 * DOWN)
        self.play(
            Transform(field_text, gf2_text),
            Transform(ma, gf2_set),
            Transform(division, gf2_mafs),
        )
        self.next_slide()
        self.play(
            Unwrite(field_text),
            Uncreate(fb),
            Unwrite(ma),
            Unwrite(division),
        )

    def hierarchy(self):
        fields = Tex(r"Fields", font_size= 80).shift(UP)
        self.play(Write(fields))
        self.next_slide()

    def extension_fields(self):
        pass # TODO
