from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are an AI assistant. You will be given a task. You must generate a detailed and long answer.
Here is the conversation history:
{history}

Question: {question}
"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def get_llm_response(history, question):
    inputs = {"history": history, "question": question}
    result = chain.invoke(inputs)
    return result
