from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

def get_ai_responses(user_input):
    # First model (Mixtral)
    llm_mixtral = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )

    messages = [
        ("system", "You are a helpful assistant that provide the information."),
        ("human", user_input)
    ]

    ai_msg = llm_mixtral.invoke(messages)
    print(f"Answer from Mixtral: {ai_msg.content}")
    print("." * 70)
    print()

    # Second model (Llama)
    llm_llama = ChatGroq(
        model="llama3-8b-8192",
        temperature=1,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )

    ai_msg_llama = llm_llama.invoke(messages)
    print(f"Answer from Llama: {ai_msg_llama.content}")

# Get user input and run the models
user_input = input("Please enter your question: ")
get_ai_responses(user_input)