from evaluation.verbosity_bias import VerbosityBiasEvaluator


answer_a = """
Artificial Intelligence is a branch of computer science that enables
machines to perform tasks requiring human intelligence such as learning,
reasoning and decision making.
"""

answer_b = """
AI makes computers smart.
"""


winner = "A"


evaluator = VerbosityBiasEvaluator()


result = evaluator.evaluate(
    answer_a,
    answer_b,
    winner
)


print(result)