### CHAINING TYPE
## 1) Sequencial chaining
## 2) Parallel chaining
## 3) conditional chaining(base on condition switch branch)


from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate  # Changed from PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # Added missing import

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",  # Keeping your original model choice
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

prompt_template = ChatPromptTemplate.from_messages([  # Changed to ChatPromptTemplate
    ("system", "You are a facts expert who knows facts about {animal}."),
    ("human", "Tell me {fact_count} facts.")
])

chain = prompt_template | llm | StrOutputParser()

result = chain.invoke({"animal": "cat", "fact_count": 2})
print(result)