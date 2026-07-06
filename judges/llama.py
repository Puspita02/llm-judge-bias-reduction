from judges.hf_judge import HuggingFaceJudge
from judges.model_registry import MODELS


class LlamaJudge(HuggingFaceJudge):

    def __init__(self):

        super().__init__(MODELS["llama"])