## user feedback -----> category(positive, negative, neutral) -----> result

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch
import json

load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

# Create prompt template for sentiment analysis
sentiment_template = ChatPromptTemplate.from_messages([
    ("system", "You are a sentiment analyzer. Categorize the feedback as 'positive', 'negative', or 'neutral'. Return ONLY the category."),
    ("human", "Analyze this movie feedback: {feedback}")
])

# Create different response templates based on sentiment
positive_template = ChatPromptTemplate.from_messages([
    ("system", "You are an enthusiastic movie critic responding to positive feedback."),
    ("human", """Respond to this positive feedback about {movie_name}: {feedback}
    Include:
    - Agreement points
    - Additional positive aspects
    - Recommendations for similar movies""")
])

negative_template = ChatPromptTemplate.from_messages([
    ("system", "You are an empathetic movie critic responding to negative feedback."),
    ("human", """Address this negative feedback about {movie_name}: {feedback}
    Include:
    - Acknowledgment of concerns
    - Possible alternative perspectives
    - Recommendations for better-suited movies""")
])

neutral_template = ChatPromptTemplate.from_messages([
    ("system", "You are a balanced movie critic responding to neutral feedback."),
    ("human", """Address this neutral feedback about {movie_name}: {feedback}
    Include:
    - Analysis of both positive and negative aspects
    - Deeper insights into the movie
    - Recommendations based on specific interests mentioned""")
])

# Create the sentiment analysis chain
sentiment_chain = sentiment_template | llm | StrOutputParser()

# Create response chains for each sentiment
def create_response_chain(template):
    return template | llm | StrOutputParser()

positive_chain = create_response_chain(positive_template)
negative_chain = create_response_chain(negative_template)
neutral_chain = create_response_chain(neutral_template)

# Create the conditional branch
branch = RunnableBranch(
    (lambda x: "positive" in x["sentiment"].lower(), positive_chain),
    (lambda x: "negative" in x["sentiment"].lower(), negative_chain),
    (neutral_chain),  # default branch
)

# Create the main chain
def combine_inputs(data):
    return {
        "sentiment": data["sentiment"],
        "feedback": data["feedback"],
        "movie_name": data["movie_name"]
    }

main_chain = (
    RunnablePassthrough() 
    | {
        "sentiment": sentiment_chain,
        "feedback": lambda x: x["feedback"],
        "movie_name": lambda x: x["movie_name"]
    }
    | branch
)

def get_user_feedback():
    movie_name = input("\nEnter the movie name: ").strip()
    feedback = input("Enter your feedback about the movie: ").strip()
    return {"movie_name": movie_name, "feedback": feedback}

def process_feedback():
    print("\nWelcome to Movie Feedback Analyzer!")
    print("This system will analyze your feedback and provide a tailored response.")
    
    while True:
        user_input = get_user_feedback()
        if not user_input["movie_name"] or not user_input["feedback"]:
            print("Please provide both movie name and feedback.")
            continue
            
        print("\nAnalyzing your feedback...\n")
        try:
            result = main_chain.invoke(user_input)
            print("\nAnalysis Result:")
            print("=" * 50)
            print(result)
            print("=" * 50)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        if input("\nWould you like to analyze another movie? (yes/no): ").lower() != 'yes':
            print("\nThank you for using Movie Feedback Analyzer!")
            break

if __name__ == "__main__":
    process_feedback()