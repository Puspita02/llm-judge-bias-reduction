"""
MT-Bench Loader

Loads:
- Questions
- Two model answers
"""

import json
from pathlib import Path


def load_jsonl(file_path):

    data = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))

    return data


def load_mtbench(
    mtbench_path,
    model_a="gpt-4",
    model_b="vicuna-13b-v1.3"
):

    mtbench_path = Path(mtbench_path)

    questions = load_jsonl(
        mtbench_path / "question.jsonl"
    )

    answers_a = load_jsonl(
        mtbench_path /
        "model_answer" /
        f"{model_a}.jsonl"
    )

    answers_b = load_jsonl(
        mtbench_path /
        "model_answer" /
        f"{model_b}.jsonl"
    )

    map_a = {
        x["question_id"]: x
        for x in answers_a
    }

    map_b = {
        x["question_id"]: x
        for x in answers_b
    }

    dataset = []

    for q in questions:

        qid = q["question_id"]

        if qid not in map_a:
            continue

        if qid not in map_b:
            continue

        dataset.append({

            "id": qid,

            "category": q["category"],

            "question": q["turns"][0],

            "answer_a":
                map_a[qid]["choices"][0]["turns"][0],

            "answer_b":
                map_b[qid]["choices"][0]["turns"][0]

        })

    return dataset