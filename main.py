from judges.qwen import QwenJudge
from evaluation.run_mtbench import MTBenchRunner


def main():

    print("=" * 60)
    print("LLM JUDGE BIAS EVALUATION")
    print("=" * 60)

    # Load Judge
    judge = QwenJudge()
    judge.load_model()

    # Run MT-Bench experiments
    runner = MTBenchRunner(judge)

    results = runner.run(limit=3)

    print("\n" + "=" * 60)
    print("EXPERIMENT FINISHED")
    print("=" * 60)
    print(f"Processed {len(results)} MT-Bench questions.")


if __name__ == "__main__":
    main()