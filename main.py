from utils.loader import load_mtbench
from judges.qwen import QwenJudge
from evaluation.evaluate import Evaluator


def main():

    dataset = load_mtbench()

    sample = dataset[0]

    answer_a = """
    Hawaii has beautiful beaches, volcanoes,
    local culture and many tourist attractions.
    """

    answer_b = """
    Hawaii has beaches.
    """

    judge = QwenJudge()

    evaluator = Evaluator(
        judge,
        "baseline"
    )

    result = evaluator.evaluate(
        sample,
        answer_a,
        answer_b
    )

    print(result)


if __name__ == "__main__":
    main()