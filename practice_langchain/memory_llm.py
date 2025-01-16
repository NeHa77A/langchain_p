from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

def create_chatbot():
    # Initialize the model
    llm = ChatGroq(
        model="llama-3.1-8b-instant",  # You can change the model if you prefer
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    
    # Initialize chat history
    chat_history = []
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for exit command
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nGoodbye!")
            break
            
        # Create messages including chat history
        messages = [
            ("system", "You are a helpful assistant that provides information."),
        ]
        
        # Add chat history to messages
        for msg in chat_history:
            messages.append(msg)
            
        # Add current user input
        messages.append(("human", user_input))
        
        try:
            # Get AI response
            ai_response = llm.invoke(messages)
            
            # Print AI response
            print("\nAssistant:", ai_response.content)
            
            # Update chat history
            chat_history.append(("human", user_input))
            chat_history.append(("assistant", ai_response.content))
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    print("Welcome! Type 'exit', 'quit', or 'bye' to end the conversation.")
    create_chatbot()