"""
Dataset Loader Module

Loads benchmark datasets used in the project.
"""

from datasets import load_dataset


def load_mtbench():
    """
    Load the MT-Bench benchmark dataset.

    Returns
    -------
    Dataset
        Hugging Face Dataset object.
    """

    dataset = load_dataset(
        "HuggingFaceH4/mt_bench_prompts",
        split="train"
    )

    return dataset