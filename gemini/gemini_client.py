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
        chat_session = self.model.start_chat(
        history=[
            {
            "role": "user",
            "parts": [
                #files[0],
                "Look at this sequence of three shapes - Triangle, Square, Pentagon. What shape should come as the fourth shape? Explain your reasoning with detailed descriptions of the first shapes.",
            ],
            },
            {
            "role": "model",
            "parts": [
                "Okay, let's analyze the sequence of shapes and determine the fourth shape.\n\n**Analysis:**\n\n1.  **Triangle:** The first shape is a triangle, characterized by three straight lines connecting to form three sides and three vertices.\n2. **Square:** The second shape is a square. Squares have four straight sides of equal length connected at right angles, forming four sides and four vertices.\n3.  **Pentagon:** The third shape is a pentagon. A pentagon has five straight sides, making a closed shape with five vertices.\n\n**Pattern and Reasoning**\n\n* **Increasing Sides:** The sequence follows an increase in the number of sides in each subsequent shape. A triangle has 3 sides, a square has 4 sides, and a pentagon has 5 sides. Therefore, the number of sides is increasing by one with each shape.\n\n**Determining the Fourth Shape:**\n\nFollowing the pattern of an increase of one side at each subsequent shape, the fourth shape should have 6 sides. A shape with 6 sides is a **Hexagon.**\n\nTherefore, the fourth shape in the sequence should be a hexagon.",
            ],
            },
        ]
        )

        response = chat_session.send_message(query)
        return response.text