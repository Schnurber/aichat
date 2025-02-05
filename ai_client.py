from langchain_openai.chat_models import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from openai import OpenAI

import random
class AIClient:
    def __init__(self):
        model = "gpt-4o"
        temperature = 0.7
        self.store = {}
        self.cptModel = OpenAI()
        moderator =  ChatOpenAI(model_name=model, temperature=temperature, streaming=True)
        specialist = ChatOpenAI(model_name=model, temperature=temperature, streaming=True)
        
        self.moderator = RunnableWithMessageHistory(moderator, self.get_session_history)
        self.specialist = RunnableWithMessageHistory(specialist, self.get_session_history)
        self.current = self.moderator

    def get_stream_response(self, question, role, summary):
        return self.current.invoke(
           question,
            config={"configurable": {"session_id": '1' if self.current == self.moderator else '2'}},
            messages=[
                {"role": "system", "content": role },
                {"role": "user", "content": question}
            ]
        )
    
    def get_session_history(self, session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in self.store:
           self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]


    def switch_client(self):
        self.current = self.specialist if self.current == self.moderator else self.moderator

    
    def get_summary_response(self, conversation_text):
        response = self.cptModel.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a summary AI."},
                {"role": "user", "content": f"Summarize this conversation between A and B:\n\n{conversation_text}"}
            ]
        )
        return response.choices[0].message.content
