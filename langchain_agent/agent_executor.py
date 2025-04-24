from langchain.agents import ZeroShotAgent,Tool,AgentExecutor
from langchain import  LLMChain, PromptTemplate
llm_chain = LLMChain.from_llm(llm, prompt=prompt)
