from prompts.output_format import OUTPUT_FORMAT


def build_prompt(strategy, question, answer_a, answer_b):

    return f"""
{strategy}

Question:
{question}

Response A:
{answer_a}

Response B:
{answer_b}

Task

Compare Response A and Response B.

Select the better response.

{OUTPUT_FORMAT}
"""