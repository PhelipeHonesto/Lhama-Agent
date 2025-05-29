"""Servidor Flask para integrar o WhatsApp via Twilio a um agente PHChatBot."""

from flask import Flask, request, abort
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse

# A classe PHChatBot é fornecida em outro módulo do projeto
# e possui um metodo responder(texto: str) -> str
from ph_chatbot import PHChatBot  # type: ignore

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
