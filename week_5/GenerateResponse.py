from ctransformers import AutoModelForCausalLM
from langchain.prompts import PromptTemplate
import re

def GetResponse_codellama(modelName, modelType, userInput, selected_language):
    llm = AutoModelForCausalLM.from_pretrained(f"Models/{modelName}", model_type=modelType, gpu_layers=50)
    

    template = """[INST] Write {selected_language} code to solve the following problem ```:
{text}
[/INST]
""" 

    prompt = PromptTemplate(template=template, input_variables=["text"])

    prompt_text = template.format(selected_language=selected_language, text=userInput) 


    response=llm(prompt_text)#temperature=0.6, top_k=40, repetition_penalty=1.2, presence_penalty=0.7
    return response

def GetRespons_llama(modelName, modelType, userInput, selected_language):
    llm = AutoModelForCausalLM.from_pretrained(f"Models/{modelName}", model_type=modelType, gpu_layers=50)
    

    template = """[INST] <<SYS>>
Write {selected_language} code to solve the following problem:
<</SYS>>
{text}[/INST]
"""

    prompt = PromptTemplate(template=template, input_variables=["text"])

    prompt_text = template.format(selected_language=selected_language, text=userInput) 


    response=llm(prompt_text)
    return response

def GetRespons_mistral(modelName, modelType, userInput, selected_language):
    llm = AutoModelForCausalLM.from_pretrained(f"Models/{modelName}", model_type=modelType, gpu_layers=50)
    

    template = "<s>[INST] Write {selected_language} code to solve the following problem: {text} [/INST]"

    prompt = PromptTemplate(template=template, input_variables=["text"])

    prompt_text = template.format(selected_language=selected_language, text=userInput) 


    response=llm(prompt_text)
    return response


class load_and_generate_response():
    def __init__(self, modeName, modelType):
        self.llm=AutoModelForCausalLM.from_pretrained(f"models/{modeName}", model_type=modelType, gpu_layers=50)
    
    def GetAnswer(self, query):
        template = """# Description: {text}
# Task: Write Python code that accomplishes the above task. Just write code:"""
        prompt = PromptTemplate(template=template, input_variables=["text"])

        prompt_text = template.format(text=query)       

        response=self.llm(prompt_text)
        return response
