#### Static
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# llm = ChatGroq(
#     model="llama3-8b-8192",  # corrected model name
#     temperature=1,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2
# )

# template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max."

# prompt_template = PromptTemplate.from_template(template)

# # Create the prompt
# prompt = prompt_template.format(
#     tone="energetic",  # fixed typo
#     company="Tata",
#     position="GenAI Developer",  # fixed parameter name
#     skill="GenAI"
# )

# # Get response from LLM
# result = llm.invoke(prompt)

# print(result.content)

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max."

prompt_template = PromptTemplate.from_template(template)

# Get user input
print("\nPlease provide the following information:")
tone = input("Enter the tone of the email (e.g., energetic, professional, formal): ").strip()
company = input("Enter the company name: ").strip()
position = input("Enter the position you're applying for: ").strip()
skill = input("Enter your key skill: ").strip()

# Create the prompt
prompt = prompt_template.format(
    tone=tone,
    company=company,
    position=position,
    skill=skill
)

try:
    # Get response from LLM
    result = llm.invoke(prompt)
    print("\nGenerated Email:")
    print("-" * 50)
    print(result.content)
    print("-" * 50)
except Exception as e:
    print(f"\nError: {str(e)}")