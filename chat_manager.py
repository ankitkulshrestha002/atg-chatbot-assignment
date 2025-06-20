# chat_manager.py
class ChatManager:
    def __init__(self, pipeline):
        self.pipe = pipeline
        self.messages = [
            {
                "role": "system",
                "content": "You are a witty pirate chatbot named Captain Code. You must answer in short, pirate-like sentences. Refer to the user as 'Ankit'.",
            },
        ]
    def generate_reply(self, user_input: str) -> str:
        self.messages.append({"role": "user", "content": user_input})
        prompt = self.pipe.tokenizer.apply_chat_template(
            self.messages, tokenize=False, add_generation_prompt=True
        )
        outputs = self.pipe(
            prompt, max_new_tokens=128, do_sample=True,
            temperature=0.75, top_k=50, top_p=0.95
        )
        full_response = outputs[0]["generated_text"]
        bot_response = full_response[len(prompt):].strip()
        if bot_response.endswith("<|im_end|>"):
            bot_response = bot_response[:-len("<|im_end|>")].strip()
        self.messages.append({"role": "assistant", "content": bot_response})
        self._manage_memory()
        return bot_response
    def _manage_memory(self):
        if len(self.messages) > 7: 
            self.messages = [self.messages[0]] + self.messages[-6:]
