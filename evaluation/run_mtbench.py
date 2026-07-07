"""
Run MT-Bench Evaluation
"""

from utils.mtbench_loader import load_mtbench
from evaluation.experiment import ExperimentRunner
from utils.logger import ResultLogger
from evaluation.verbosity_bias import VerbosityBiasEvaluator


class MTBenchRunner:

    def __init__(self, judge):

        self.judge = judge
        self.logger = ResultLogger()

    def run(self, limit=5):

        dataset = load_mtbench(
            "Datasets/FastChat/fastchat/llm_judge/data/mt_bench"
        )

        experiment = ExperimentRunner(self.judge)
        verbosity = VerbosityBiasEvaluator()

        all_results = []

        for sample in dataset[:limit]:

            print(f"\nEvaluating Question {sample['id']}")

            results = experiment.run(
                sample["question"],
                sample["answer_a"],
                sample["answer_b"]
            )

            # Evaluate each prompt strategy
            for prompt_name, result in results.items():

                vb = verbosity.evaluate(
                    sample["answer_a"],
                    sample["answer_b"],
                    result["winner"]
                )

                print(
                    f"{prompt_name} -> Verbosity Bias: {vb['verbosity_bias']}"
                )

                # Save results
                self.logger.log(
                    sample["id"],
                    sample["category"],
                    prompt_name,
                    result,
                    vb["verbosity_bias"]
                )

            all_results.append(results)

        return all_results