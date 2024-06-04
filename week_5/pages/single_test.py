from denem_test import get_function_name
import streamlit as st

if 'store' not in st.session_state:
    st.session_state.store = True 

if 'input_values' not in st.session_state:
    st.session_state['input_values'] = ""


code_string = st.text_area("Paste your code here", height=200)

if st.button("Paste Code") or st.session_state.store:
    code_name = get_function_name(code_string)

    assertion_template = f"assert {code_name}(parameters) == expected_value"
    st.session_state['input_values']=st.text_area("Assertion Code (Auto-generated)", assertion_template, height=100)


if st.button("Test Code"):
    try:
        safe_globals = {"__builtins__": None}
        exec(code_string)
        exec(st.session_state['input_values'])

        st.success("Test passed!")

    except AssertionError:
        st.error("Test failed: Assertion error")
    except Exception as e:
        st.error(f"Code execution failed: {e}")