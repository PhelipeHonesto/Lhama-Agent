# Lhama-Agent

Exemplo de uso do cliente oficial da OpenAI com o modelo GPT‑4o. O script lê
as variáveis de ambiente de um arquivo `.env` e realiza uma chamada simples ao
modelo. Para executar o projeto instale as dependências e configure as três
variáveis no arquivo `.env` conforme o exemplo.

```bash
pip install -r requirements.txt
cp .env.example .env  # edite o arquivo e preencha com seus dados
python main.py
```

O `.env` deve conter:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
OPENAI_PROJECT_ID=proj_xxxxxxxxxxxxxxxxx
OPENAI_ORG_ID=org_xxxxxxxxxxxxxxxxx
```
