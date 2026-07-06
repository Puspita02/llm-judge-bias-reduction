"""
Hugging Face Judge
"""

from transformers import pipeline

from judges.model_registry import MODELS


class HuggingFaceJudge:

    def __init__(self, model_name):

        self.model_name = MODELS[model_name]

        print(f"Selected Model: {self.model_name}")

        # We are NOT loading the model yet.
        self.generator = None

    def load_model(self):

        self.generator = pipeline(

            "text-generation",

            model=self.model_name

        )

    def evaluate(self, prompt):

        if self.generator is None:

            raise RuntimeError("Model not loaded.")

        response = self.generator(

            prompt,

            max_new_tokens=150,

            do_sample=False

        )

        return response[0]["generated_text"]