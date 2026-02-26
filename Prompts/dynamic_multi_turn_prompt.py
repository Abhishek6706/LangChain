from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate(
    [('system', 'you are a expert in {domain}'),
     ('human', 'tell me about {topic} in 10 lines')]
)

prompt = chat_template.invoke({'domain':'AI', 'topic':'LangChain'})

model = ChatOpenAI(model='gpt-4.1', temperature= 0.2)

result = model.invoke(prompt)

print(result.content)
