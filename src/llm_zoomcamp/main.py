#%%
from dotenv import load_dotenv
load_dotenv()

from llm_zoomcamp.ingest import load_faq_data, build_index
from llm_zoomcamp.rag_helper import RAGBase
from openai import OpenAI


documents = load_faq_data()
index = build_index(documents)

openai_client = OpenAI()

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
)

answer = assistant.rag("I just discovered the course. Can I join now?")
# %%
assistant.rag("How do I get a certificate?")
assistant.rag("Can I still join the course after it started?")
# %%
