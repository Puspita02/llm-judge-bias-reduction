from utils.loader import load_mtbench
from judges.qwen import QwenJudge


def main():

    dataset = load_mtbench()

    sample = dataset[0]

    judge = QwenJudge()

    result = judge.evaluate(
        question=sample["question"],
        answer_a="This is answer A.",
        answer_b="This is answer B."
    )

    print("=" * 60)
    print("Sample Evaluation")
    print("=" * 60)

    print("\nQuestion:")
    print(sample["question"])

    print("\nWinner:")
    print(result["winner"])

    print("\nReason:")
    print(result["reason"])


if __name__ == "__main__":
    main()