from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model='gpt-4.1', temperature= 0.2)

messages = [
    SystemMessage(content='You are a expert in explaining thing'),
    HumanMessage(content='Tell me about langchain in professional manner, in 10 lines')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
