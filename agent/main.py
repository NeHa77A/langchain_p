# # # import os
# # # from dotenv import load_dotenv
# # # from crewai import Agent
# # # from crewai_tools import SerperDevTool
# # # from crewai import Task
# # # from crewai import Crew, Process

# # # # Load environment variables from .env file
# # # load_dotenv()

# # # # Access the environment variables
# # # SERPER_API_KEY = os.getenv("SERPER_API_KEY")
# # # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # # os.environ["SERPER_API_KEY"] = SERPER_API_KEY  # Your serper.dev API key
# # # os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# # # os.environ["OPENAI_MODEL"] = "gpt-4-32k"

# # # search_tool = SerperDevTool()

# # # # Creating a senior researcher agent with memory and verbose mode
# # # researcher = Agent(
# # #     role='Senior Researcher',
# # #     goal='Uncover groundbreaking technologies in {topic}',
# # #     verbose=True,
# # #     memory=True,
# # #     backstory=(
# # #        """ Driven by curiosity, you're at the forefront of
# # #         innovation, eager to explore and share knowledge that could change
# # #         the world."""
# # #     ),
# # #     tools=[search_tool],
# # #     allow_delegation=True
# # # )

# # # # Creating a writer agent with custom tools and delegation capability
# # # writer = Agent(
# # #     role='Writer',
# # #     goal='Narrate compelling tech stories about {topic}',
# # #     verbose=True,
# # #     memory=True,
# # #     backstory=(
# # #         """With a flair for simplifying complex topics, you craft
# # #         engaging narratives that captivate and educate, bringing new
# # #         discoveries to light in an accessible manner."""
# # #     ),
# # #     tools=[search_tool],
# # #     allow_delegation=False
# # # )




# # # research_task = Task(
# # #     description=(
# # #         "Identify the next big trend in {topic}. "
# # #         "Focus on identifying pros and cons and the overall narrative. "
# # #         "Your final report should clearly articulate the key points, "
# # #         "its market opportunities, and potential risks."
# # #     ),
# # #     expected_output="A comprehensive 3 paragraphs long report on the latest AI trends.",
# # #     tools=[search_tool],
# # #     agent=researcher,
# # # )

# # # write_task = Task(
# # #     description=(
# # #         "Compose an insightful article on {topic}. "
# # #         "Focus on the latest trends and how it's impacting the industry. "
# # #         "This article should be easy to understand, engaging, and positive."
# # #     ),
# # #     expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
# # #     tools=[search_tool],
# # #     agent=writer,
# # #     async_execution=False,
# # #     output_file="new-blog-post.md",
# # # )




# # # # Forming the tech-focused crew with enhanced configurations
# # # crew = Crew(
# # #     agents=[researcher, writer],
# # #     tasks=[research_task, write_task],
# # #     process=Process.sequential  # Optional: Sequential task execution is default
# # # )


# # # # Starting the task execution process with enhanced feedback
# # # result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
# # # print(result)
# # import os
# # from dotenv import load_dotenv
# # from crewai import Agent
# # from crewai_tools import SerperDevTool
# # from crewai import Task
# # from crewai import Crew, Process
# # from langchain_groq import ChatGroq

# # # Load environment variables from .env file
# # load_dotenv()

# # # Access the environment variables
# # SERPER_API_KEY = os.getenv("SERPER_API_KEY")
# # GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # os.environ["SERPER_API_KEY"] = SERPER_API_KEY
# # os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# # search_tool = SerperDevTool()

# # # Initialize Groq LLM
# # llm = ChatGroq(
# #     temperature=0.7,
# #     groq_api_key=GROQ_API_KEY,
# #     model_name="llama-70b-v2"  # Using llama-3.3-70b-versatile
# # )

# # # Creating a senior researcher agent with memory and verbose mode
# # researcher = Agent(
# #     role='Senior Researcher',
# #     goal='Uncover groundbreaking technologies in {topic}',
# #     verbose=True,
# #     memory=True,
# #     backstory=(
# #        """ Driven by curiosity, you're at the forefront of
# #         innovation, eager to explore and share knowledge that could change
# #         the world."""
# #     ),
# #     tools=[search_tool],
# #     allow_delegation=True,
# #     llm=llm
# # )

# # # Creating a writer agent with custom tools and delegation capability
# # writer = Agent(
# #     role='Writer',
# #     goal='Narrate compelling tech stories about {topic}',
# #     verbose=True,
# #     memory=True,
# #     backstory=(
# #         """With a flair for simplifying complex topics, you craft
# #         engaging narratives that captivate and educate, bringing new
# #         discoveries to light in an accessible manner."""
# #     ),
# #     tools=[search_tool],
# #     allow_delegation=False,
# #     llm=llm
# # )

# # research_task = Task(
# #     description=(
# #         "Identify the next big trend in {topic}. "
# #         "Focus on identifying pros and cons and the overall narrative. "
# #         "Your final report should clearly articulate the key points, "
# #         "its market opportunities, and potential risks."
# #     ),
# #     expected_output="A comprehensive 3 paragraphs long report on the latest AI trends.",
# #     tools=[search_tool],
# #     agent=researcher,
# # )

# # write_task = Task(
# #     description=(
# #         "Compose an insightful article on {topic}. "
# #         "Focus on the latest trends and how it's impacting the industry. "
# #         "This article should be easy to understand, engaging, and positive."
# #     ),
# #     expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
# #     tools=[search_tool],
# #     agent=writer,
# #     async_execution=False,
# #     output_file="new-blog-post.md",
# # )

# # # Forming the tech-focused crew with enhanced configurations
# # crew = Crew(
# #     agents=[researcher, writer],
# #     tasks=[research_task, write_task],
# #     process=Process.sequential  # Optional: Sequential task execution is default
# # )

# # # Starting the task execution process with enhanced feedback
# # result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
# # print(result)
# import os
# from dotenv import load_dotenv
# from crewai import Agent, Task, Crew, Process
# from crewai_tools import SerperDevTool
# import litellm
# from langchain_core.language_models.chat_models import BaseChatModel
# from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
# from typing import List, Dict, Any, Optional, Union

# # Load environment variables from .env file
# load_dotenv()

# # Access the environment variables
# SERPER_API_KEY = os.getenv("SERPER_API_KEY")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# os.environ["SERPER_API_KEY"] = SERPER_API_KEY
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# search_tool = SerperDevTool()

# class CustomGroqLLM(BaseChatModel):
#     def __init__(self):
#         super().__init__()
        
#     def _generate(self, 
#                  messages: List[BaseMessage], 
#                  stop: Optional[List[str]] = None, 
#                  run_manager: Optional[Any] = None, 
#                  **kwargs) -> Any:
#         try:
#             message_dicts = [{"role": msg.type, "content": msg.content} for msg in messages]
#             response = litellm.completion(
#                 model="groq/llama-3-70b",
#                 messages=message_dicts,
#                 api_key=GROQ_API_KEY,
#                 api_base="https://api.groq.com/openai/v1"
#             )
#             return {"generations": [{"text": response.choices[0].message.content}]}
#         except Exception as e:
#             print(f"Error in CustomGroqLLM completion: {str(e)}")
#             raise

#     @property
#     def _llm_type(self) -> str:
#         return "custom_groq"

# # Initialize our custom LLM
# llm = CustomGroqLLM()

# # Creating a senior researcher agent with memory and verbose mode
# researcher = Agent(
#     role='Senior Researcher',
#     goal='Uncover groundbreaking technologies in {topic}',
#     verbose=True,
#     memory=True,
#     backstory=(
#        """Driven by curiosity, you're at the forefront of
#         innovation, eager to explore and share knowledge that could change
#         the world."""
#     ),
#     tools=[search_tool],
#     allow_delegation=True,
#     llm=llm
# )

# # Creating a writer agent with custom tools and delegation capability
# writer = Agent(
#     role='Writer',
#     goal='Narrate compelling tech stories about {topic}',
#     verbose=True,
#     memory=True,
#     backstory=(
#         """With a flair for simplifying complex topics, you craft
#         engaging narratives that captivate and educate, bringing new
#         discoveries to light in an accessible manner."""
#     ),
#     tools=[search_tool],
#     allow_delegation=False,
#     llm=llm
# )

# research_task = Task(
#     description=(
#         "Identify the next big trend in {topic}. "
#         "Focus on identifying pros and cons and the overall narrative. "
#         "Your final report should clearly articulate the key points, "
#         "its market opportunities, and potential risks."
#     ),
#     expected_output="A comprehensive 3 paragraphs long report on the latest AI trends.",
#     tools=[search_tool],
#     agent=researcher,
# )

# write_task = Task(
#     description=(
#         "Compose an insightful article on {topic}. "
#         "Focus on the latest trends and how it's impacting the industry. "
#         "This article should be easy to understand, engaging, and positive."
#     ),
#     expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
#     tools=[search_tool],
#     agent=writer,
#     async_execution=False,
#     output_file="new-blog-post.md",
# )

# # Forming the tech-focused crew with enhanced configurations
# crew = Crew(
#     agents=[researcher, writer],
#     tasks=[research_task, write_task],
#     process=Process.sequential
# )

# if __name__ == "__main__":
#     # Starting the task execution process with enhanced feedback
#     result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
#     print(result)
# main.py
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming import StreamingStdOutCallbackHandler
from crewai.llms.base import LLM
from typing import List, Dict, Any, Optional

# Load environment variables
load_dotenv()

# Access the environment variables
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["SERPER_API_KEY"] = SERPER_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

search_tool = SerperDevTool()

class GroqLLM(LLM):
    def __init__(self):
        super().__init__(model="llama-3-70b")
        self.callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        
    def call(self, messages: List[Dict[str, Any]], **kwargs: Any) -> Any:
        import requests
        
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama2-70b-4096",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4096
        }
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        
        if response.status_code != 200:
            raise Exception(f"Error from Groq API: {response.text}")
            
        result = response.json()
        return result["choices"][0]["message"]["content"]

# Initialize our custom LLM
llm = GroqLLM()

# Creating a senior researcher agent
researcher = Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
       """Driven by curiosity, you're at the forefront of
        innovation, eager to explore and share knowledge that could change
        the world."""
    ),
    tools=[search_tool],
    allow_delegation=True,
    llm=llm
)

# Creating a writer agent
writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        """With a flair for simplifying complex topics, you craft
        engaging narratives that captivate and educate, bringing new
        discoveries to light in an accessible manner."""
    ),
    tools=[search_tool],
    allow_delegation=False,
    llm=llm
)

research_task = Task(
    description=(
        "Identify the next big trend in {topic}. "
        "Focus on identifying pros and cons and the overall narrative. "
        "Your final report should clearly articulate the key points, "
        "its market opportunities, and potential risks."
    ),
    expected_output="A comprehensive 3 paragraphs long report on the latest AI trends.",
    tools=[search_tool],
    agent=researcher,
)

write_task = Task(
    description=(
        "Compose an insightful article on {topic}. "
        "Focus on the latest trends and how it's impacting the industry. "
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
    tools=[search_tool],
    agent=writer,
    async_execution=False,
    output_file="new-blog-post.md",
)

# Forming the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

if __name__ == "__main__":
    # Starting the task execution process
    result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
    print(result)