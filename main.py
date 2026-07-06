from judges.qwen import QwenJudge
from evaluation.experiment import ExperimentRunner
from evaluation.position_bias import PositionBiasEvaluator

from prompts.baseline import BASELINE_PROMPT


def main():

    print("=" * 60)
    print("LLM JUDGE BIAS EVALUATION")
    print("=" * 60)

    # ---------------------------------------------------
    # Load Judge
    # ---------------------------------------------------

    judge = QwenJudge()
    judge.load_model()

    # ---------------------------------------------------
    # Example Data
    # ---------------------------------------------------

    question = "Explain what Artificial Intelligence is."

    answer_a = """
Artificial Intelligence (AI) is a branch of computer science that enables
machines to perform tasks that normally require human intelligence such as
reasoning, learning, perception, and decision-making.
"""

    answer_b = """
AI is when computers become smart.
"""

    # ---------------------------------------------------
    # Run Prompt Experiments
    # ---------------------------------------------------

    experiment = ExperimentRunner(judge)

    results = experiment.run(
        question,
        answer_a,
        answer_b
    )

    print("\n" + "=" * 60)
    print("PROMPT EXPERIMENT RESULTS")
    print("=" * 60)

    for prompt_name, result in results.items():

        print(f"\nPrompt : {prompt_name}")
        print(f"Winner : {result['winner']}")
        print(f"Reason : {result['reason']}")

    # ---------------------------------------------------
    # Position Bias Experiment
    # ---------------------------------------------------

    print("\n" + "=" * 60)
    print("POSITION BIAS TEST")
    print("=" * 60)

    bias_evaluator = PositionBiasEvaluator(judge)

    bias_result = bias_evaluator.evaluate(
        BASELINE_PROMPT,
        question,
        answer_a,
        answer_b
    )

    print("\nOriginal Order")
    print(bias_result["original"])

    print("\nSwapped Order")
    print(bias_result["swapped"])

    print("\nPosition Bias Detected:")
    print(bias_result["position_bias"])


if __name__ == "__main__":
    main()