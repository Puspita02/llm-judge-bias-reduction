OUTPUT_FORMAT = """
Return ONLY a valid JSON object.

JSON schema:

{
    "winner": "<A or B>",
    "reason": "<your reason>"
}

Rules:
- winner must be either "A" or "B"
- reason must explain your decision in one sentence
- Do not include markdown
- Do not include any extra text
"""