"""
Position Bias Evaluation

Measures whether the judge changes its decision
when the order of responses is swapped.
"""

from prompts.prompt_builder import build_prompt
from utils.parser import parse_judge_output


class PositionBiasEvaluator:

    def __init__(self, judge):
        self.judge = judge

    def evaluate(self, strategy, question, answer_a, answer_b):

        # ---------- Original Order ----------
        prompt_original = build_prompt(
            strategy,
            question,
            answer_a,
            answer_b
        )

        original = parse_judge_output(
            self.judge.generate(prompt_original)
        )

        # ---------- Swapped Order ----------
        prompt_swapped = build_prompt(
            strategy,
            question,
            answer_b,
            answer_a
        )

        swapped = parse_judge_output(
            self.judge.generate(prompt_swapped)
        )

        # Convert swapped winner back to original labels
        if swapped["winner"] == "A":
            swapped_original = "B"
        elif swapped["winner"] == "B":
            swapped_original = "A"
        else:
            swapped_original = "Unknown"

        biased = original["winner"] != swapped_original

        return {
            "original": original,
            "swapped": swapped,
            "position_bias": biased
        }