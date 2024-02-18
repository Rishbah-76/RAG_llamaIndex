from dotenv import load_dotenv
import os 
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_eng import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import India_engine
POPULATION_PATH = os.path.join("data", "WorldPopulation2023.csv")
population_df=pd.read_csv(POPULATION_PATH) 
load_dotenv()

poplutation_query_engine=PandasQueryEngine(df=population_df,verbose=True,instruction_str=instruction_str)
print(population_df.head())

# poplutation_query_engine.update_prompts({"pandas_prompts": new_prompt})
# poplutation_query_engine.query("What is the population of India")

tools=[note_engine,
       QueryEngineTool(query_engine=poplutation_query_engine,
                       metadata=ToolMetadata(name="population Query tool",
                                             description="This tools gives info from the population demographics using df")
                       ),
        QueryEngineTool(
        query_engine=India_engine,
        metadata=ToolMetadata(
            name="India_data",
            description="this gives detailed information about INDIA the country",
        ),
    ),
       
]
llm_agent=OpenAI(model="gpt-3.5-turbo-0613")
agent=ReActAgent.from_tools(tools,llm=llm_agent,verbose=True,context=context)


while(prompt:=input("Enter your Prompt or (q to quit): ")!="q"):
    result=agent.query(prompt)
    print(result)