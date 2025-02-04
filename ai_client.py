from openai import OpenAI
import random
class AIClient:
    def __init__(self):
        self.moderator = OpenAI()
        self.specialist = OpenAI()
        self.current = self.moderator

    def switch_client(self):
        self.current = self.specialist if self.current == self.moderator else self.moderator

    def get_stream_response(self, question, role, summary):
        return self.current.chat.completions.create(
            model="gpt-4o",
            stream=True,
            temperature=0.7,
            messages=[
                {"role": "system", "content": role + " Das bisherige Gespräch: " + summary },
                {"role": "user", "content": question}
            ]
        )
    
    def get_summary_response(self, conversation_text):
        summary_client = OpenAI()
        response = summary_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Sie sind eine Zusammenfassungs KI."},
                {"role": "user", "content": f"Fassen Sie dieses Gespräch zwischen A und B kurz zusammen:\n\n{conversation_text}"}
            ]
        )
        return response.choices[0].message.content
