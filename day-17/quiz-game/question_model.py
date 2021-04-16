from typing import Text


class Question:

    def __init__(self, q_text, answer):
        self.q_text = q_text
        self.answer = answer

new_q = Question("2+2", "4")