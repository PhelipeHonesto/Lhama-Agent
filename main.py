from flask import Flask, request, abort
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
from ph_chatbot import PHChatBot

load_dotenv()

app = Flask(__name__)
chatbot = PHChatBot()

@app.route("/bot", methods=["POST"])
def bot():
    mensagem = request.form.get("Body")
    if not mensagem:
        abort(400, "Body ausente")

    resposta = chatbot.responder(mensagem)

    twilio_resp = MessagingResponse()
    twilio_resp.message(resposta)
    return str(twilio_resp)

if __name__ == "__main__":
    app.run(port=5000)
