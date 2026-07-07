"""
Result Logger
"""

import csv
from pathlib import Path


class ResultLogger:

    def __init__(self, file_path="results/results.csv"):

        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():

            with open(self.file_path, "w", newline="", encoding="utf-8") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "question_id",
                    "category",
                    "prompt_strategy",
                    "winner",
                    "reason",
                    "verbosity_bias"
                ])

    def log(
        self,
        question_id,
        category,
        prompt_name,
        result,
        verbosity_bias
    ):

        with open(self.file_path, "a", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                question_id,
                category,
                prompt_name,
                result["winner"],
                result["reason"],
                verbosity_bias
            ])