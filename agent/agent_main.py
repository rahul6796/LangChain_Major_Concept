

## combined all the tool 
## whatever i have created the agents

from langchain_community.llms import Ollama
from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor

from agent_arxiv import arxiv_agent_tool
from agent_custom import custom_agent_tool
from agent_wikipedia import wikipedia_agent_tool
from langchain import hub
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os



tools = [arxiv_agent_tool, custom_agent_tool, wikipedia_agent_tool]
prompt = hub.pull('hwchase17/openai-functions-agent')



def main():

    # llm = Ollama(model = 'llama3.1')
    llm = ChatOpenAI(model='gpt-3.5-turbo-0125', temperature=0.2)
    agent = create_openai_tools_agent(llm,tools,prompt)
    agent_exc = AgentExecutor(agent=agent,tools=tools, verbose=True)
    x = agent_exc.invoke({'input': 'tell me about LangSmith'})
    print(x)



if __name__ == "__main__":
    main()



