import streamlit as st
import importlib
import unittest
import os
import sys
import plotly.express as px
import pandas as pd

#sys.path.append("..")

st.title("All Test Cases")
st.write("A tool to test code produced by Language Models") 

model_options = ["codellama", "llama", "mistral"]
selected_model = st.selectbox("Select Model to Test:", model_options)

if st.button("Run Tests"):
    #selected_model = st.session_state['model']
    results_by_difficulty = {'Easy': {'passed': 0, 'failed': 0},
                         'Medium': {'passed': 0, 'failed': 0},
                         'Difficult': {'passed': 0, 'failed': 0}}

    total_test=0
    total_easy_tests = 0
    passed_easy_tests = 0
    failed_easy_tests = 0
    test_results = []

    for query_num in range(1, 6):  # Easy
        try:
            code_module = importlib.import_module(f"pages.codes_and_tests.codes.{selected_model}.query{query_num}")
            test_module = importlib.import_module(f"pages.codes_and_tests.tests.{selected_model}.test_query{query_num}")

            test_suite = unittest.TestLoader().loadTestsFromModule(test_module)
            test_runner = unittest.TextTestRunner()
            test_result = test_runner.run(test_suite)


            for test_case, error_message in test_result.failures + test_result.errors:  
                test_name = str(test_case) 
                function_name = test_name.split('.')[1]  
                status = 'Failed'
                error_reason = str(error_message) 

                test_results.append({
                    'Query': query_num,
                    'Test Name': test_name,
                    'Function': function_name,
                    'Status': status
                })

            total_easy_tests += test_result.testsRun
            failed_easy_tests += len(test_result.failures) + len(test_result.errors) 
            passed_easy_tests += test_result.testsRun - len(test_result.failures) - len(test_result.errors) 
            

        except ModuleNotFoundError:
            st.warning(f"Query {query_num} or its test file not found")
    

    

    # st.subheader("Summary Metrics")
    # st.metric("Total Tests Run", total_easy_tests)
    # st.metric("Tests Passed", passed_easy_tests)
    # st.metric("Tests Failed", failed_easy_tests)

    results_by_difficulty["Easy"]["passed"]=2*passed_easy_tests
    results_by_difficulty["Easy"]["failed"]=2*failed_easy_tests
    total_test+=total_easy_tests
    

    # st.subheader("Overall Pass/Fail Distribution")
    # fig = px.pie(values=[passed_easy_tests, failed_easy_tests], names=['Passed', 'Failed'])
    # st.plotly_chart(fig)


    #medium level
    total_medium_tests = 0
    passed_medium_tests = 0
    failed_medium_tests = 0

    for query_num in range(6, 11):  # medium
        try:
            code_module = importlib.import_module(f"pages.codes_and_tests.codes.{selected_model}.query{query_num}")
            test_module = importlib.import_module(f"pages.codes_and_tests.tests.{selected_model}.test_query{query_num}")

            test_suite = unittest.TestLoader().loadTestsFromModule(test_module)
            test_runner = unittest.TextTestRunner()
            test_result = test_runner.run(test_suite)

            for test_case, error_message in test_result.failures + test_result.errors:  
                test_name = str(test_case) 
                function_name = test_name.split('.')[1]  
                status = 'Failed'
                error_reason = str(error_message) 

                test_results.append({
                    'Query': query_num,
                    'Test Name': test_name,
                    'Function': function_name,
                    'Status': status
                })

            total_medium_tests += test_result.testsRun
            failed_medium_tests += len(test_result.failures) + len(test_result.errors) 
            passed_medium_tests += test_result.testsRun - len(test_result.failures) - len(test_result.errors) 
            

        except ModuleNotFoundError:
            st.warning(f"Query {query_num} or its test file not found")
    

    # st.subheader("Summary Metrics")
    # st.metric("Total Tests Run", total_medium_tests)
    # st.metric("Tests Passed", passed_medium_tests)
    # st.metric("Tests Failed", failed_medium_tests)

    results_by_difficulty["Medium"]["passed"]=2*passed_medium_tests
    results_by_difficulty["Medium"]["failed"]=2*failed_medium_tests
    total_test+=total_medium_tests


    # st.subheader("Overall Pass/Fail Distribution")
    # fig = px.pie(values=[passed_medium_tests, failed_medium_tests], names=['Passed', 'Failed'])
    # st.plotly_chart(fig)


    # Hard Level
    total_hard_tests = 0
    passed_hard_tests = 0
    failed_hard_tests = 0

    for query_num in range(11, 16):  # Hard
        try:
            code_module = importlib.import_module(f"pages.codes_and_tests.codes.{selected_model}.query{query_num}")
            test_module = importlib.import_module(f"pages.codes_and_tests.tests.{selected_model}.test_query{query_num}")

            test_suite = unittest.TestLoader().loadTestsFromModule(test_module)
            test_runner = unittest.TextTestRunner()
            test_result = test_runner.run(test_suite)

            for test_case, error_message in test_result.failures + test_result.errors:  
                test_name = str(test_case) 
                function_name = test_name.split('.')[1]  
                status = 'Failed'
                error_reason = str(error_message) 

                test_results.append({
                    'Query': query_num,
                    'Test Name': test_name,
                    'Function': function_name,
                    'Status': status
                })

            total_hard_tests += test_result.testsRun
            failed_hard_tests += len(test_result.failures) + len(test_result.errors) 
            passed_hard_tests += test_result.testsRun - len(test_result.failures) - len(test_result.errors) 
            

        except ModuleNotFoundError:
            st.warning(f"Query {query_num} or its test file not found")
    

    # st.subheader("Summary Metrics")
    # st.metric("Total Tests Run", total_hard_tests)
    # st.metric("Tests Passed", passed_hard_tests)
    # st.metric("Tests Failed", failed_hard_tests)

    results_by_difficulty["Difficult"]["passed"]=2*passed_hard_tests
    results_by_difficulty["Difficult"]["failed"]=2*failed_hard_tests
    total_test+=total_hard_tests
    total_test*=2


    # st.subheader("Overall Pass/Fail Distribution")
    # fig = px.pie(values=[passed_hard_tests, failed_hard_tests], names=['Passed', 'Failed'])
    # st.plotly_chart(fig)

  
    #passed failed according to difficulty
    st.subheader("Pass/Fail Distribution by Difficulty")

    for difficulty_level in results_by_difficulty:
        st.subheader(difficulty_level)
        st.metric("Total Tests Run", results_by_difficulty[difficulty_level]['failed'] + results_by_difficulty[difficulty_level]['passed'])
        st.metric("Tests Passed", results_by_difficulty[difficulty_level]['passed'])
        st.metric("Tests Failed", results_by_difficulty[difficulty_level]['failed'])

        df = pd.DataFrame({
            'Status': ['Passed', 'Failed'], 
            'Count': [results_by_difficulty[difficulty_level]['passed'], results_by_difficulty[difficulty_level]['failed']]
        })

        fig = px.pie(df, values='Count', names='Status', color='Status', title=difficulty_level,
                    color_discrete_map={'Passed': 'green', 'Failed': 'red'})
        st.plotly_chart(fig)


    # Chart Title (Customize Here)
    chart_title = "Test Results by Difficulty Level (Passed/Failed)"

    # Bar Chart
    st.subheader(chart_title)
    difficulty_levels = list(results_by_difficulty.keys())
    passed_values = [results_by_difficulty[level]['passed'] for level in difficulty_levels]
    failed_values = [results_by_difficulty[level]['failed'] for level in difficulty_levels]

    passed_color = 'green'
    failed_color = 'red'
    color_map = {'passed': passed_color, 'failed': failed_color}

    # Generate list of colors based on the data
    colors = [color_map['passed'] if value == 'passed' else color_map['failed'] for value in ['passed', 'failed']]

    # Bar Chart
    fig = px.bar(x=difficulty_levels, y=[passed_values, failed_values], 
                barmode='stack',  # Stack bars for passed/failed comparison
                color_discrete_sequence=colors,  # Color bars based on color map
                title=chart_title)

    fig.update_traces(marker_line_color='black',  # Add black outline to bars
                    marker_line_width=1)  # Adjust line width for better visibility

    # Display Chart
    st.plotly_chart(fig)


    st.subheader("Detailed Test Results")
    df = pd.DataFrame(test_results)
    st.dataframe(df) 