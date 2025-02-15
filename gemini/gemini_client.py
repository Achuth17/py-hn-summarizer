import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class GeminiClient:
    def __init__(self):
        # Create the model
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 65536,
            "response_mime_type": "text/plain",
        }
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            generation_config=generation_config,
        )

    def ask_gemini(self, query: str) -> str:        
        chat_session = self.model.start_chat(history=[])

        response = chat_session.send_message(query)
        return response.text