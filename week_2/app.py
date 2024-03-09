from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q4_0.bin',     # Create a models file to save the models you will download. 
                    model_type='llama',                                 # link to Llama2 quantized model: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})


template = """# Description: {text}
# Task: Write Python code that accomplishes the above task."""

text = "Code that adds numbers from 1 to n."
text_1="Function that calculates n'th Fibonacci numbers recursively"

prompt = PromptTemplate(template=template, input_variables=["text"])

prompt_text = template.format(text=text_1)


response=llm(prompt_text)
print(response)
