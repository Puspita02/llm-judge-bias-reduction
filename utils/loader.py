"""
Dataset Loader Module
---------------------

Loads benchmark datasets and converts them into
a unified format for evaluation.
"""

from datasets import load_dataset


def load_mtbench():
    """
    Load MT-Bench and convert it to a standard format.

    Returns
    -------
    list[dict]
    """

    dataset = load_dataset(
        "HuggingFaceH4/mt_bench_prompts",
        split="train"
    )

    samples = []

    for item in dataset:
        question = item["prompt"][0] if isinstance(item["prompt"], list) else item["prompt"]

        samples.append({
            "id": item["prompt_id"],
            "category": item["category"],
            "question": question,
            "reference": item["reference"]
        })

    return samples