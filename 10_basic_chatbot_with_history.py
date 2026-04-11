from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 1. Base Model
llm = OpenAI(temperature=0.7)

chat_history = []

initial_ai_message = "AI: Hi How can I help you?"
print(initial_ai_message)
chat_history.append(initial_ai_message)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # 2. Append the user string with a "User:" label
    chat_history.append(f"User: {user_input}")
    
    # 3. Add an empty "AI:" label to force the autocomplete pattern
    chat_history.append("AI:")

    # 4. CRITICAL FIX: Join the list into ONE massive string
    prompt_string = "\n".join(chat_history)

    # 5. Invoke with the single string
    result = llm.invoke(prompt_string)

    # 6. Clean up the output and print
    clean_result = result.strip()
    print("AI:", clean_result)

    # 7. Add the generated text to the last "AI:" label in the history
    chat_history[-1] = f"AI: {clean_result}"