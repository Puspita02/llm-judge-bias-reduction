"""
Parser for LLM Judge Output
"""

import json
import re


def parse_judge_output(output: str):
    """
    Parse the LLM output into a structured dictionary.

    Returns:
        {
            "winner": "A" or "B",
            "reason": "..."
        }
    """

    # Try JSON parsing first
    try:
        start = output.find("{")
        end = output.rfind("}") + 1

        if start != -1 and end != -1:
            data = json.loads(output[start:end])

            return {
                "winner": data.get("winner", "Unknown"),
                "reason": data.get("reason", "")
            }

    except Exception:
        pass

    # Fallback using regex
    winner = re.search(r'"?winner"?\s*:\s*"?(A|B)"?', output, re.IGNORECASE)
    reason = re.search(r'"?reason"?\s*:\s*"([^"]+)"', output)

    return {
        "winner": winner.group(1).upper() if winner else "Unknown",
        "reason": reason.group(1) if reason else output.strip()
    }