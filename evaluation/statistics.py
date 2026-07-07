"""
Statistics Module

Computes overall bias statistics from experiment results.
"""

import pandas as pd


class Statistics:

    def __init__(self, csv_path="results/results.csv"):

        self.df = pd.read_csv(csv_path)

    def prompt_summary(self):

        summary = self.df.groupby("prompt_strategy").agg(
            total=("winner", "count"),
            verbosity_bias=("verbosity_bias", "sum")
        )

        summary["verbosity_bias_rate"] = (
            summary["verbosity_bias"] / summary["total"]
        ) * 100

        return summary

    def print_summary(self):

        summary = self.prompt_summary()

        print("\n" + "=" * 60)
        print("VERBOSITY BIAS SUMMARY")
        print("=" * 60)

        print(summary)