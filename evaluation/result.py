"""
Evaluation Result
"""

from dataclasses import dataclass


@dataclass
class EvaluationResult:
    question_id: int
    model: str
    prompt_type: str
    winner: str
    reason: str