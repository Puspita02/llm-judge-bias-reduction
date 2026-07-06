"""
Qwen Judge
"""

from judges.base_judge import BaseJudge


class QwenJudge(BaseJudge):

    def evaluate(self, question, answer_a, answer_b):

        return {
            "winner": "A",
            "reason": "Mock evaluation (API not connected yet)"
        }