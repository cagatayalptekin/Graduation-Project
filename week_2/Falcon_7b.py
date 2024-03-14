from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate

llm = CTransformers(model='models/falcon-7b-instruct.ggccv1.q8_0.bin',          # link to Falcon quantized model: https://huggingface.co/TheBloke/Falcon-7B-Instruct-GGML
                    model_type='falcon',                                                    
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