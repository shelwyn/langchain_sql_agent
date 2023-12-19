import psycopg2
from langchain_experimental.sql import SQLDatabaseChain
from langchain.utilities import SQLDatabase
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

api_key = '<YOUR_OPEN_AI_API_KEY'

input_db = SQLDatabase.from_uri('postgresql+psycopg2://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>')

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = OpenAI(openai_api_key=api_key)
llm_chain = LLMChain(prompt=prompt, llm=llm)
question=input("question: ")

db_agent = SQLDatabaseChain(llm = llm,database = input_db,verbose=False)
answer=db_agent.run(question)
print(answer)
