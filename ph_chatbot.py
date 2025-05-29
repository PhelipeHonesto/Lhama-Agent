# ph_chatbot.py atualizado para GPT-4o
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class PHChatBot:
    def responder(self, pergunta):
        resposta_openai = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Você é PH, um chatbot criativo, pragmático, apaixonado por tecnologia, filosofia e automação."},
                {"role": "user", "content": pergunta}
            ],
            max_tokens=150
        )

        return resposta_openai.choices[0].message.content.strip()
