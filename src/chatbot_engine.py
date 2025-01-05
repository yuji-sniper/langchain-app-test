from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


def chat(message: str, histories: list):
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        verbose=True
    )
    
    messages = []
    
    for history in histories:
        messages.append(HumanMessage(content=history["content"]))
    
    messages.append(HumanMessage(content=message))
    
    return llm.invoke(messages).content
