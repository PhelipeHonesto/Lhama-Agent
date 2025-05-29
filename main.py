from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

modelo = ChatOpenAI(model="gpt-4o")

resposta = modelo.invoke("Oi, quem é você?")
print(resposta.content) 