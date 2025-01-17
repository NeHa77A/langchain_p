from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

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
    
    return {
        "animal": inputs["animal"].lower().strip(),
        "fact_count": int(inputs["fact_count"]),
        "detail_level": "intermediate",
        "focus": "biology and behavior"
    }

def format_prompt(inputs):
    print("\n2. Formatting prompt with inputs:")
    print(f"Inputs for prompt: {inputs}")
    formatted = prompt_template.format(**inputs)
    print("\n3. Generated Prompt:")
    print(f"Final prompt: {formatted}")
    return formatted

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a facts expert who knows facts about {animal}. Provide {detail_level} level details focusing on {focus}."),
    ("human", "Tell me {fact_count} facts.")
])

# Restructured sequence to maintain state correctly
sequence = (
    RunnablePassthrough.assign(
        inputs=generate_facts
    )
    | RunnablePassthrough.assign(
        prompt=lambda x: format_prompt(x["inputs"])
    )
    | RunnablePassthrough.assign(
        response=lambda x: llm.invoke(x["prompt"])
    )
    | RunnablePassthrough.assign(
        output=lambda x: StrOutputParser().invoke(x["response"])
    )
)

def main():
    try:
        animal = input("Enter an animal name: ")
        fact_count = input("How many facts would you like? ")
        
        print("\n--- Chain Execution Start ---")
        
        result = sequence.invoke({
            "animal": animal,
            "fact_count": fact_count
        })
        
        print("\n4. Final Output:")
        print(result["output"])
        
    except KeyError as e:
        print(f"\nKey Error: Missing key {e} in the data structure")
        import traceback
        print(f"Full error trace:\n{traceback.format_exc()}")
    except ValueError as e:
        print(f"\nValue Error: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        import traceback
        print(f"Full error trace:\n{traceback.format_exc()}")

if __name__ == "__main__":
    main()