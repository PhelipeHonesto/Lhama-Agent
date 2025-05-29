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
