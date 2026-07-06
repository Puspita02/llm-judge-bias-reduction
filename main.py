from judges.hf_judge import HuggingFaceJudge


def main():

    judge = HuggingFaceJudge("qwen")

    print()

    print("Architecture works!")

    print()

    print(judge.model_name)


if __name__ == "__main__":
    main()