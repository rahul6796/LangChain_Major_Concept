

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper



def wikipedia_agent_tool():

    try:
        api = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
        tool = WikipediaQueryRun(api_wrapper=api)
        return tool
    except Exception as ex:
        print(f'error is coming form given wikipedia :: {ex}')




# if __name__ == "__main__":
#     x = agent_wikipedia()
#     print(x.name)