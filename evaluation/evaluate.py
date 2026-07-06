"""
Evaluation Pipeline
"""

from evaluation.result import EvaluationResult


class Evaluator:

    def __init__(self, judge, prompt_name):
        self.judge = judge
        self.prompt_name = prompt_name

    def evaluate(
        self,
        sample,
        answer_a,
        answer_b
    ):

        result = self.judge.evaluate(
            sample["question"],
            answer_a,
            answer_b
        )

        return EvaluationResult(
            question_id=sample["id"],
            model="qwen",
            prompt_type=self.prompt_name,
            winner=result["winner"],
            reason=result["reason"]
        )