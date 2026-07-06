from judges.qwen import QwenJudge


def main():

    judge = QwenJudge()

    print("Judge object created successfully!")

    print(judge.model_name)


if __name__ == "__main__":
    main()