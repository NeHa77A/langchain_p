#### create chain with RunnableLambda(pipe chaining)

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

def generate_facts(inputs):
    print("\n1. Input received in generate_facts:")
    print(f"Raw inputs: {inputs}")
    
    transformed_input = {
        "animal": inputs["animal"].lower().strip(),
        "fact_count": int(inputs["fact_count"]),
        "detail_level": "intermediate",
        "focus": "biology and behavior"
    }
    
    print("\n2. Transformed inputs:")
    print(f"Processed inputs: {transformed_input}")
    return transformed_input

def debug_prompt(prompt):
    print("\n3. Generated Prompt:")
    print(f"Final prompt: {prompt}")
    return prompt

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a facts expert who knows facts about {animal}. Provide {detail_level} level details focusing on {focus}."),
    ("human", "Tell me {fact_count} facts.")
])

# Create chain using the | operator
chain = (
    RunnableLambda(generate_facts)
    | prompt_template 
    | RunnableLambda(debug_prompt)
    | llm 
    | StrOutputParser()
)

def main():
    try:
        animal = input("Enter an animal name: ")
        fact_count = input("How many facts would you like? ")
        
        print("\n--- Chain Execution Start ---")
        
        result = chain.invoke({
            "animal": animal,
            "fact_count": fact_count
        })
        
        print("\n4. Final Output:")
        print(result)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()