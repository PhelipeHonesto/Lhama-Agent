"""Exemplo simples de agente usando a OpenAI API com chaves `sk-proj`."""

import os
from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    """Carrega variáveis de ambiente e consulta o modelo."""

    # Carrega as variáveis definidas no arquivo `.env`
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    project_id = os.getenv("OPENAI_PROJECT_ID")
    org_id = os.getenv("OPENAI_ORG_ID")
    if not api_key or not project_id or not org_id:
        raise EnvironmentError(
            "Defina OPENAI_API_KEY, OPENAI_PROJECT_ID e OPENAI_ORG_ID em um arquivo .env"
        )

    client = OpenAI(
        api_key=api_key,
        project=project_id,
        organization=org_id,
    )

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Oi, quem é você?"}],
    )
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
