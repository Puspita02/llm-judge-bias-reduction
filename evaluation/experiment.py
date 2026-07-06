"""
Experiment Runner

Runs the same evaluation using different prompting strategies.
"""

from utils.parser import parse_judge_output
from prompts.prompt_builder import build_prompt

from prompts.baseline import BASELINE_PROMPT
from prompts.role_prompt import ROLE_PROMPT
from prompts.cot_prompt import COT_PROMPT
from prompts.rubric_prompt import RUBRIC_PROMPT
from prompts.position_neutral import POSITION_NEUTRAL_PROMPT
from prompts.self_check import SELF_CHECK_PROMPT


PROMPTS = {
    "baseline": BASELINE_PROMPT,
    "role": ROLE_PROMPT,
    "cot": COT_PROMPT,
    "rubric": RUBRIC_PROMPT,
    "position_neutral": POSITION_NEUTRAL_PROMPT,
    "self_check": SELF_CHECK_PROMPT,
}


class ExperimentRunner:

    def __init__(self, judge):
        self.judge = judge

    def run(self, question, answer_a, answer_b):

        results = {}

        for prompt_name, strategy in PROMPTS.items():

            print(f"\nRunning: {prompt_name}")

            # Build the complete prompt
            full_prompt = build_prompt(
                strategy,
                question,
                answer_a,
                answer_b
            )

            # Generate model response
            raw_output = self.judge.generate(full_prompt)

            # Parse the output
            parsed_output = parse_judge_output(raw_output)

            # Save result
            results[prompt_name] = parsed_output

        return results