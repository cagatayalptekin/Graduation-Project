import streamlit as st
import time
from GenerateResponse import GetResponse_codellama, GetRespons_llama, GetRespons_mistral

# --- Page Configuration ---
st.set_page_config(page_title="week 5", layout="wide")  # Wide layout option

# --- Sidebar: Model Selection ---
st.sidebar.title("Select Your Model")

selected_model_name = st.sidebar.selectbox("Available Models", ("codellama-7b", "llama-7b", "mistral-7b"))
selected_language = st.sidebar.radio("Programming Language", ("Python", "JavaScript"))


# --- Sidebar: User Input ---
st.sidebar.header("Enter Your Text")
user_input = st.sidebar.text_area("Input Text Here", height=300)

# --- Main Content Area ---
st.title("Demo - Page 1")  


if st.sidebar.button("Generate Response"):
    try:
            
            if not user_input:
                raise ValueError("Please enter some text") 

            #loading logic ...
            if selected_model_name == "codellama-7b":
                with st.spinner("Generating response..."):
                    model_output=GetResponse_codellama("codellama-7b-instruct.Q5_K_M.gguf", "llama", user_input, selected_language)
                
            if selected_model_name == "llama-7b":
                with st.spinner("Generating response..."):
                    model_output=GetRespons_llama("llama-2-7b-chat.Q5_K_M.gguf", "llama", user_input, selected_language)
            if selected_model_name == "mistral-7b":
                with st.spinner("Generating response..."):
                    model_output=GetRespons_mistral("mistral-7b-instruct-v0.1.Q5_K_M.gguf", "mistral", user_input, selected_language)

            st.write("Model Output:")
            st.code(model_output)  # Output in code block


    except ValueError as e:  # Catching a specific error type
        st.error(str(e)) 
    except Exception as e:  # Catching general errors 
        st.error(f"An unexpected error occurred: {e}")
    