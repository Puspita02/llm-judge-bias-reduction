from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class HuggingFaceJudge:

    def __init__(self, model_name):

        self.model_name = model_name
        self.tokenizer = None
        self.model = None

    def load_model(self):

        print(f"Loading {self.model_name}...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float32
        )

        print("Model loaded successfully!")

    def generate(self, prompt):

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt"
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=100
        )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )