"""
MT-Bench Loader

Loads:
- Questions
- GPT-4 Answers
- Another Model's Answers

Returns a unified dataset.
"""

import json
from pathlib import Path


def load_jsonl(file_path):
    """Load a JSONL file."""

    data = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))

    return data


def load_mtbench(mtbench_path, model_a="gpt-4", model_b="vicuna-13b-v1.5"):

    mtbench_path = Path(mtbench_path)

    questions = load_jsonl(
        mtbench_path / "question.jsonl"
    )

    answers_a = load_jsonl(
        mtbench_path / "model_answer" / f"{model_a}.jsonl"
    )

    answers_b = load_jsonl(
        mtbench_path / "model_answer" / f"{model_b}.jsonl"
    )

    answer_map_a = {
        item["question_id"]: item
        for item in answers_a
    }

    answer_map_b = {
        item["question_id"]: item
        for item in answers_b
    }

    dataset = []

    for question in questions:

        qid = question["question_id"]

        if qid not in answer_map_a:
            continue

        if qid not in answer_map_b:
            continue

        dataset.append({

            "id": qid,

            "category": question.get(
                "category",
                "unknown"
            ),

            "question": question["turns"][0],

            "answer_a":
                answer_map_a[qid]["choices"][0]["turns"][0],

            "answer_b":
                answer_map_b[qid]["choices"][0]["turns"][0]

        })

    return dataset