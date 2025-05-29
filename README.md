# Lhama-Agent

Exemplo de agente baseado em Flask integrado ao WhatsApp via Twilio e
utilizando `langchain-openai` com o modelo GPT‑4o.

```bash
pip install -r requirements.txt
cp .env.example .env   # edite o arquivo e coloque sua chave
python main.py  # inicia o servidor em http://localhost:5000
```

O endpoint `/bot` receberá as mensagens do WhatsApp enviadas pelo Twilio e
responderá automaticamente usando a classe `PHChatBot`.
