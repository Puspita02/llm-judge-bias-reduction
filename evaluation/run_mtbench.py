"""
Run experiments on MT-Bench
"""

from utils.loader import load_mtbench
from evaluation.experiment import ExperimentRunner
from utils.logger import ResultLogger


class MTBenchRunner:

    def __init__(self, judge):

        self.judge = judge

        self.logger = ResultLogger()

    def run(self, limit=5):

        dataset = load_mtbench()

        experiment = ExperimentRunner(self.judge)

        all_results = []

        for sample in dataset[:limit]:

            print(f"\nEvaluating Question {sample['id']}")

            # Temporary answers
            answer_a = "This is a detailed answer."

            answer_b = "This is a short answer."

            results = experiment.run(
                sample["question"],
                answer_a,
                answer_b
            )

            # Save every prompt result
            for prompt_name, result in results.items():

                self.logger.log(
                    sample["id"],
                    sample["category"],
                    prompt_name,
                    result
                )

            all_results.append(results)

        return all_results