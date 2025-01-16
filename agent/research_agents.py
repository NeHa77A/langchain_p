# # import os
# # from dotenv import load_dotenv
# # from crewai import Agent, Task, Crew
# # from crewai_tools import SerperDevTool
# # from langchain_openai import ChatOpenAI

# # load_dotenv()

# # SERPER_API_KEY = os.getenv("SERPER_API_KEY")
# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # search_tool = SerperDevTool()

# # def create_research_agent():

# #     llm = ChatOpenAI(model="gpt-3.5-turbo")
  
# #     return Agent(
# #         role="Research Specialist",
# #         goal="Conduct thorough research on given topics",
# #         backstory="You are an experienced researcher with expertise in finding and synthesizing information from various sources",
# #         verbose=True,
# #         allow_delegation=False,
# #         tools=[search_tool],
# #         llm=llm,
# #     )




# # def create_research_task(agent, topic):
# #     return Task(
# #         description=f"Research the following topic and provide a comprehensive summary: {topic}",
# #         agent=agent,
# #         expected_output = "A detailed summary of the research findings, including key points and insights related to the topic"
# #     )

# # def run_research(topic):
# #     agent = create_research_agent()
# #     task = create_research_task(agent, topic)
# #     crew = Crew(agents=[agent], tasks=[task])
# #     result = crew.kickoff()
# #     return result

# # if __name__ == "__main__":
# #     print("Welcome to the Research Agent!")
# #     topic = input("Enter the research topic: ")
# #     result = run_research(topic)
# #     print("Research Result:")
# #     print(result)

# import os
# from dotenv import load_dotenv
# from crewai import Agent, Task, Crew
# from crewai_tools import SerperDevTool
# from langchain_groq import ChatGroq

# load_dotenv()

# SERPER_API_KEY = os.getenv("SERPER_API_KEY")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# search_tool = SerperDevTool()

# def create_research_agent():
#     llm = ChatGroq(
#         temperature=0.7,
#         groq_api_key=GROQ_API_KEY,
#         model_name="llama-70b-v2"  # Using llama-3.3-70b-versatile
#     )
    
#     return Agent(
#         role="Research Specialist",
#         goal="Conduct thorough research on given topics",
#         backstory="You are an experienced researcher with expertise in finding and synthesizing information from various sources",
#         verbose=True,
#         allow_delegation=False,
#         tools=[search_tool],
#         llm=llm,
#     )

# def create_research_task(agent, topic):
#     return Task(
#         description=f"Research the following topic and provide a comprehensive summary: {topic}",
#         agent=agent,
#         expected_output="A detailed summary of the research findings, including key points and insights related to the topic"
#     )

# def run_research(topic):
#     agent = create_research_agent()
#     task = create_research_task(agent, topic)
#     crew = Crew(agents=[agent], tasks=[task])
#     result = crew.kickoff()
#     return result

# if __name__ == "__main__":
#     print("Welcome to the Research Agent!")
#     topic = input("Enter the research topic: ")
#     result = run_research(topic)
#     print("Research Result:")
#     print(result)
# research_agents.py
# research_agents.py
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from typing import List, Dict, Any
import requests
import abc

# Load environment variables
load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

search_tool = SerperDevTool()

class BaseLLM(abc.ABC):
    @abc.abstractmethod
    def chat(self, messages: List[Dict[str, Any]], **kwargs: Any) -> str:
        pass

class GroqLLM(BaseLLM):
    def __init__(self):
        self.model = "llama2-70b-4096"
        
    def chat(self, messages: List[Dict[str, Any]], **kwargs: Any) -> str:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4096
        }
        
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data
            )
            
            if response.status_code != 200:
                print(f"Error from Groq API: {response.text}")
                raise Exception(f"Groq API error: {response.status_code}")
                
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error calling Groq API: {str(e)}")
            raise

def create_research_agent():
    """Create a research agent with the Groq LLM"""
    llm = GroqLLM()
    
    return Agent(
        role="Research Specialist",
        goal="Conduct thorough research on given topics",
        backstory="""You are an experienced researcher with expertise in 
        finding and synthesizing information from various sources. You have 
        a keen eye for detail and can identify key trends and patterns.""",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool],
        llm=llm,
    )

def create_research_task(agent, topic):
    """Create a research task for the agent"""
    return Task(
        description=f"""Research the following topic and provide a comprehensive summary: {topic}
        Focus on the following aspects:
        1. Current state and recent developments
        2. Key challenges and opportunities
        3. Future implications and potential impact
        4. Notable organizations and people involved
        5. Relevant statistics and data points
        """,
        agent=agent,
        expected_output="""A detailed summary of the research findings, including:
        - Overview of the topic
        - Key insights and trends
        - Supporting data and evidence
        - Expert opinions and analysis
        - Recommendations or future outlook"""
    )

def run_research(topic):
    """Execute the research process"""
    try:
        print(f"\nInitiating research on: {topic}")
        agent = create_research_agent()
        task = create_research_task(agent, topic)
        crew = Crew(
            agents=[agent], 
            tasks=[task],
            verbose=2
        )
        
        print("\nExecuting research task...")
        result = crew.kickoff()
        return result
    
    except Exception as e:
        print(f"\nError during research execution: {str(e)}")
        raise

if __name__ == "__main__":
    print("Welcome to the Research Agent!")
    print("--------------------------------")
    try:
        topic = input("Enter the research topic: ")
        result = run_research(topic)
        
        print("\nResearch Results:")
        print("----------------")
        print(result)
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please check your API keys and network connection.")