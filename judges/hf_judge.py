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

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=False
            )

        generated = outputs[0][inputs["input_ids"].shape[1]:]

        return self.tokenizer.decode(
            generated,
            skip_special_tokens=True
        )
    def judge(self, question, answer_a, answer_b, system_prompt):

        prompt = f"""
    {system_prompt}

    Question:
    {question}

    Response A:
    {answer_a}

    Response B:
    {answer_b}

    Which response is better?

    Return ONLY valid JSON.
    """

        return self.generate(prompt)