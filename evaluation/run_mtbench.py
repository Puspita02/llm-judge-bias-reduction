"""
Run experiments on MT-Bench.
"""

from utils.loader import load_mtbench
from evaluation.experiment import ExperimentRunner


class MTBenchRunner:

    def __init__(self, judge):
        self.judge = judge

    def run(self, limit=5):

        dataset = load_mtbench()

        experiment = ExperimentRunner(self.judge)

        all_results = []

        for sample in dataset[:limit]:

            print(f"\nEvaluating Question {sample['id']}")

            # Temporary answers for testing
            answer_a = "This is a detailed answer."

            answer_b = "This is a short answer."

            result = experiment.run(
                sample["question"],
                answer_a,
                answer_b
            )

            all_results.append({
                "id": sample["id"],
                "category": sample["category"],
                "results": result
            })

        return all_results