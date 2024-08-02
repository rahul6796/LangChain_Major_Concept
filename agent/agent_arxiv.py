


from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun


def arxiv_agent_tool():
    try:
        api = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
        tool = ArxivQueryRun(api_wrapper=api)
        return tool
    except Exception as ex:
        print(f'error is coming from given agent arxiv :: {ex}')
