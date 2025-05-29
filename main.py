"""Exemplo simples de agente usando o cliente da OpenAI."""

from __future__ import annotations

import os

from dotenv import load_dotenv
import openai


def main() -> None:
    """Carrega variáveis de ambiente e consulta o modelo."""

    # Carrega as variáveis definidas no arquivo `.env`
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    project = os.getenv("OPENAI_PROJECT_ID")
    org = os.getenv("OPENAI_ORG_ID")

    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY não definido. Crie um arquivo .env com essa variável"
        )

    openai_client = openai.OpenAI(api_key=api_key, project=project, organization=org)

    chat_completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Oi, quem é você?"}],
    )

    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    main()
