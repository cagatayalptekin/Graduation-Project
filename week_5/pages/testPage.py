import streamlit as st
from denem_test import get_function_name_and_params

st.markdown("Düzenlenecek")
st.sidebar.markdown("#düzenlenecek")

st.header("Test Page")

# Initialize input_values in session state if not already done
if 'input_values' not in st.session_state:
    st.session_state['input_values'] = {}

if 'store' not in st.session_state:
    st.session_state.store = True 

function_code = st.text_area('Enter the generated code', height=275)

def run_function_with_params(function_name, function_code, params):
    locals_dict = params.copy()  # Parameters as local variables

    try:
        exec(function_code, {}, locals_dict) 
        result = locals_dict[function_name](*params.values())
        return result
    except Exception as e:
        raise ValueError(f"Error executing function: {e}")


def main():
    function_name, function_params = get_function_name_and_params(function_code) 

    # If parameters are found:
    if function_params:
        st.write(f"Enter values for parameters of {function_name}:")
        
        for param in function_params:
            # Retrieve the current value from session state
            current_value = st.session_state['input_values'].get(param, '')
            # Display the text input field with the current value
            user_input = st.text_input(param)#, value=current_value
            # Update the session state with the new value
            st.session_state['input_values'][param] = user_input
        
        expected_output = st.text_input("Enter the expected output")

        if st.button("Run Test"):
            # Option A (Caution):
            try:
                input_values = st.session_state['input_values'].copy()  # Collect input values from Streamlit
                result = run_function_with_params(function_name, function_code, input_values)
                st.write(result)
                if int(result) == int(expected_output): 
                    st.success("Test Passed!")
                else:
                    st.error("Test Failed!")
            except Exception as e:
                st.error(f"Error during execution: {e}")
    else:
        st.warning("No parameters detected in the function.")
    
    


if st.button("Analyze and Test") or st.session_state.store:
    main()

    





