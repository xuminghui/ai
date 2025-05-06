from langchain.agents import ZeroShotAgent,Tool,AgentExecutor
from langchain import  LLMChain, PromptTemplate

llm_chain = LLMChain.from_llm(llm, prompt=prompt)
tools=[
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    )
]
