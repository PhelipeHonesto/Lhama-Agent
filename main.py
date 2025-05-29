"""Servidor Flask para integrar o WhatsApp via Twilio a um agente PHChatBot."""

from flask import Flask, request, abort
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse

# A classe PHChatBot é fornecida em outro módulo do projeto
# e possui um metodo responder(texto: str) -> str
from ph_chatbot import PHChatBot
  # type: ignore

# Carrega variáveis de ambiente definidas no arquivo `.env`
load_dotenv()

app = Flask(__name__)
chatbot = PHChatBot()


@app.route("/bot", methods=["POST"])
def bot() -> str:
    """Recebe mensagens do WhatsApp enviadas pelo Twilio e responde."""
    mensagem = request.form.get("Body")
    if not mensagem:
        abort(400, "Body ausente")

    resposta = chatbot.responder(mensagem)

    twilio_resp = MessagingResponse()
    twilio_resp.message(resposta)
    return str(twilio_resp)


if __name__ == "__main__":
    app.run(port=5000)

"""Exemplo simples de agente usando LangChain e GPT-4o."""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os


def main() -> None:
    """Carrega variáveis de ambiente e consulta o modelo."""

    # Carrega as variáveis definidas no arquivo `.env`
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY não definido. Crie um arquivo .env com essa variável"
        )

    # O ChatOpenAI também lê OPENAI_API_KEY automaticamente
    modelo = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)
    resposta = modelo.invoke("Oi, quem é você?")
    print(resposta.content)


if __name__ == "__main__":
    main()
