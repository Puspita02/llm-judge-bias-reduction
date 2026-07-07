"""
Verbosity Bias Evaluator

Checks whether the judge prefers longer answers.
"""


class VerbosityBiasEvaluator:

    def evaluate(self, answer_a, answer_b, winner):

        len_a = len(answer_a.split())
        len_b = len(answer_b.split())

        if len_a > len_b:
            longer = "A"
        elif len_b > len_a:
            longer = "B"
        else:
            longer = "Equal"

        if longer == "Equal":
            bias = False
        else:
            bias = (winner == longer)

        return {
            "length_a": len_a,
            "length_b": len_b,
            "longer_answer": longer,
            "winner": winner,
            "verbosity_bias": bias
        }