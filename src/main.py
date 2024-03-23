from manim import *


class WordEmbeddingsExample(Scene):
    def construct(self):
        # タイトル
        title = Text("Word Embeddings Example").to_edge(UP)
        self.play(Write(title))

        # 説明テキスト
        explanation_text = Text(
            "Word embeddings map words to vectors of real numbers.",
            font_size=24,
        ).next_to(
            title, DOWN, buff=0.5
        )  # タイトルとの間隔を設定
        self.play(Write(explanation_text))
        self.wait(1)

        # ベクトルの例
        vector1 = Arrow(start=[0, 0, 0], end=[2, -1, 0], buff=0, color=BLUE)
        vector1_label = Text("King", font_size=24).next_to(vector1, RIGHT)
        vector2 = Arrow(start=[0, 0, 0], end=[-1, -2, 0], buff=0, color=GREEN)
        vector2_label = Text("Man", font_size=24).next_to(vector2, LEFT)
        result_vector = Arrow(start=[0, 0, 0], end=[1, -3, 0], buff=0, color=RED)
        result_vector_label = Text("King - Man + Woman = Queen", font_size=24).next_to(
            result_vector, UP
        )

        self.play(GrowArrow(vector1), Write(vector1_label))
        self.play(GrowArrow(vector2), Write(vector2_label))
        self.wait(1)
        self.play(
            ReplacementTransform(vector1.copy(), result_vector),
            ReplacementTransform(vector2.copy(), result_vector),
        )
        self.play(Write(result_vector_label))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
