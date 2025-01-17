# ## static
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableLambda
# from typing import Dict
# from operator import itemgetter

# load_dotenv()

# # Initialize the LLM
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=1,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2
# )

# # Create separate prompt templates for plot and character analysis
# plot_template = ChatPromptTemplate.from_messages([
#     ("system", "You are a movie critic specializing in plot analysis."),
#     ("human", """Analyze the plot of {movie_name}. Include:
#     - Main plot points
#     - Story structure
#     - Themes
#     - Plot strengths and weaknesses""")
# ])

# character_template = ChatPromptTemplate.from_messages([
#     ("system", "You are a movie critic specializing in character analysis."),
#     ("human", """Analyze the characters in {movie_name}. Include:
#     - Main character descriptions
#     - Character development
#     - Character strengths and weaknesses
#     - Character relationships""")
# ])

# # Create the chains
# def create_chain(prompt):
#     return prompt | llm | StrOutputParser()

# plot_chain = create_chain(plot_template)
# character_chain = create_chain(character_template)

# # Create parallel chains
# from langchain_core.runnables import RunnableParallel

# parallel_chain = RunnableParallel(
#     plot_analysis=plot_chain,
#     character_analysis=character_chain
# )

# # Function to format the final output
# def format_analysis(parallel_output: Dict) -> str:
#     return f"""
# Movie Analysis:

# Plot Analysis:
# {parallel_output['plot_analysis']}

# Character Analysis:
# {parallel_output['character_analysis']}
# """

# # Final chain with formatting
# final_chain = parallel_chain | RunnableLambda(format_analysis)

# # Example usage
# if __name__ == "__main__":
#     movie_name = "The Dark Knight"
#     result = final_chain.invoke({"movie_name": movie_name})
#     print(result)



##Dynamic

### movie_name ---> summary ----> plot ---->character analysis


from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from typing import Dict
from operator import itemgetter

load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

# Create separate prompt templates for plot and character analysis
plot_template = ChatPromptTemplate.from_messages([
    ("system", "You are a movie critic specializing in plot analysis."),
    ("human", """Analyze the plot of {movie_name}. Include:
    - Main plot points
    - Story structure
    - Themes
    - Plot strengths and weaknesses""")
])

character_template = ChatPromptTemplate.from_messages([
    ("system", "You are a movie critic specializing in character analysis."),
    ("human", """Analyze the characters in {movie_name}. Include:
    - Main character descriptions
    - Character development
    - Character strengths and weaknesses
    - Character relationships""")
])

# Create the chains
def create_chain(prompt):
    return prompt | llm | StrOutputParser()

plot_chain = create_chain(plot_template)
character_chain = create_chain(character_template)

# Create parallel chains
from langchain_core.runnables import RunnableParallel

parallel_chain = RunnableParallel(
    plot_analysis=plot_chain,
    character_analysis=character_chain
)

# Function to format the final output
def format_analysis(parallel_output: Dict) -> str:
    return f"""
Movie Analysis:

Plot Analysis:
{parallel_output['plot_analysis']}

Character Analysis:
{parallel_output['character_analysis']}
"""

# Final chain with formatting
final_chain = parallel_chain | RunnableLambda(format_analysis)

# Function to get movie name from user
def get_movie_name():
    while True:
        movie_name = input("\nEnter the name of the movie to analyze (or 'quit' to exit): ").strip()
        if movie_name.lower() == 'quit':
            return None
        if movie_name:
            return movie_name
        print("Please enter a valid movie name.")

# Main execution
if __name__ == "__main__":
    print("Welcome to Movie Analysis System!")
    print("This system will analyze both plot and characters of your chosen movie.")
    
    while True:
        movie_name = get_movie_name()
        if movie_name is None:
            print("\nThank you for using Movie Analysis System!")
            break
            
        print(f"\nAnalyzing '{movie_name}'... Please wait...\n")
        try:
            result = final_chain.invoke({"movie_name": movie_name})
            print(result)
        except Exception as e:
            print(f"An error occurred while analyzing the movie: {str(e)}")
        
        print("\n" + "="*50)