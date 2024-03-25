from ctransformers import AutoModelForCausalLM
from langchain.prompts import PromptTemplate

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("models/llama-2-7b-chat.Q5_K_M.gguf", model_type="llama", gpu_layers=50)

template = """# Description: {text}
# Task: Write Python code that accomplishes the above task. Just write code:"""

#easy
query_1="Function that calculates n'th Fibonacci numbers recursively"
query_2="Write a function that takes an integer as input and determines if it's a prime number"
query_3="Write a function that takes two integers as input and finds their greatest common divisor."
query_4="Write a function that takes an integer as input and determines if it's a palindrome"
query_5="Write a program that takes an integer as input and determines if it's an Armstrong number."
#medium


#hard 

prompt = PromptTemplate(template=template, input_variables=["text"])

prompt_text = template.format(text=query_5)


response=llm(prompt_text)
print(response)
