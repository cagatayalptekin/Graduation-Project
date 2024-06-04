from denem_test import get_function_name
import streamlit as st

if 'store' not in st.session_state:
    st.session_state.store = True 

if 'input_values' not in st.session_state:
    st.session_state['input_values'] = ""

code_string = st.text_area("Paste your code here", height=200)
code_name = get_function_name(code_string)





if st.button("Paste Code") or st.session_state.store:
    assertion_template =f"""
def example_test_function1():
    assert {code_name}(params) == expected_value
    
def example_test_function2():
    assert {code_name}(params) == example output

def example_test_function3():
    assert {code_name}(params) == example output

def example_test_function4():
    assert {code_name}(params) == example output

def example_test_function5():
    assert {code_name}(params) == example output
    """
    st.session_state['input_values']=st.text_area("Assertion Code (Auto-generated)", assertion_template, height=300)







def run_tests():
   test_functions = [
     lambda: example_test_function1(),
     lambda: example_test_function2(),
     lambda: example_test_function3(),
     lambda: example_test_function4(),
     lambda: example_test_function5(),
   ]

   success_count = 0

   for test in test_functions:
     try:
       test()
       print(f"{test.__name__}: Success")
       success_count += 1   
     except AssertionError:
       print(f"{test.__name__}: Failure")

   return f"\nTotal successful tests: {success_count} out of {len(test_functions)}"
   

if st.button("Test Code"):
    try:
        # Construct final test code (more on this below)
        #test_code = ...  

        # Import the user's function dynamically
        exec(code_string)  # Import user's code
        exec(st.session_state['input_values'])   # Import the test code

        # Call the run_tests function
        st.success(run_tests())  # Pass the user's function

    except Exception as e:
        st.error(f"Code execution failed: {e}")



