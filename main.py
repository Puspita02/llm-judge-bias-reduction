
from utils.loader import load_mtbench


def main():

    print("=" * 60)
    print("LLM Judge Bias Reduction")
    print("=" * 60)

    print("\nLoading MT-Bench...\n")

    dataset = load_mtbench()

    print("Dataset Loaded Successfully!")

    print(f"\nTotal Questions: {len(dataset)}")

    print("\nFirst Sample:\n")

    print(dataset[0])


if __name__ == "__main__":
    main()