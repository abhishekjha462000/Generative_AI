from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

print("AI: Hi How can I help you:")
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    result = llm.invoke(user_input)
    print("AI:", result) 