import streamlit as st
import importlib
import unittest
import os
import sys
import plotly.express as px
import pandas as pd

#sys.path.append("..")

st.title("Comparing models")
st.write("Comparison of LLM models based on question levels.") 

available_models = ["codellama", "llama", "mistral"]

results_by_difficulty = {
        'codellama': {'Easy': {'passed': 0, 'failed': 0},
                    'Medium': {'passed': 0, 'failed': 0},
                    'Difficult': {'passed': 0, 'failed': 0}},
        'llama':  {'Easy': {'passed': 0, 'failed': 0},
                'Medium': {'passed': 0, 'failed': 0},
                'Difficult': {'passed': 0, 'failed': 0}},
        'mistral': {'Easy': {'passed': 0, 'failed': 0},
                    'Medium': {'passed': 0, 'failed': 0},
                    'Difficult': {'passed': 0, 'failed': 0}}
    }

if st.button("Run Tests"):
    

    
    total_tests = 0
    test_results = []

    # Difficulty Ranges
    difficulty_ranges = {
        "Easy": range(1, 6),  
        "Medium": range(6, 11), # TODO: düzeltilecek
        "Difficult": range(11, 16) 
    }
    for model in available_models:
        for difficulty_level, query_range in difficulty_ranges.items():
            total_tests_level = 0
            passed_tests_level = 0
            failed_tests_level = 0

            for query_num in query_range:
                try:
                    code_module = importlib.import_module(f"pages.codes_and_tests.codes.{model}.query{query_num}")
                    test_module = importlib.import_module(f"pages.codes_and_tests.tests.{model}.test_query{query_num}")

                    test_suite = unittest.TestLoader().loadTestsFromModule(test_module)
                    test_runner = unittest.TextTestRunner()
                    test_result = test_runner.run(test_suite)

                    total_tests_level += test_result.testsRun
                    failed_tests_level += len(test_result.failures) + len(test_result.errors)
                    passed_tests_level += test_result.testsRun - len(test_result.failures) - len(test_result.errors)

                except ModuleNotFoundError:
                    st.warning(f"Query {query_num} or its test file not found")

            # Update results 
            results_by_difficulty[model][difficulty_level]['passed'] = passed_tests_level
            results_by_difficulty[model][difficulty_level]['failed'] = failed_tests_level
            total_tests += total_tests_level
    
    model_names = ['codellama', 'llama', 'mistral']
    passed_counts = [
        results_by_difficulty['codellama']['Easy']['passed']*2,
        results_by_difficulty['llama']['Easy']['passed']*2,
        results_by_difficulty['mistral']['Easy']['passed']*2
    ]

    # Create the Plotly bar chart
    fig = px.bar(x=model_names, y=passed_counts,
                labels={'x': 'Model', 'y': 'Passed Count (Easy)'},
                title="Comparison of Models on Easy Tasks")

    # Display the chart in Streamlit
    st.plotly_chart(fig)


    model_names = ['codellama', 'llama', 'mistral']
    passed_counts = [
        results_by_difficulty['codellama']['Medium']['passed']*2,
        results_by_difficulty['llama']['Medium']['passed']*2,
        results_by_difficulty['mistral']['Medium']['passed']*2
    ]

    # Create the Plotly bar chart
    fig = px.bar(x=model_names, y=passed_counts,
                labels={'x': 'Model', 'y': 'Passed Count (Easy)'},
                title="Comparison of Models on Medium Tasks")

    # Display the chart in Streamlit
    st.plotly_chart(fig)




    model_names = ['codellama', 'llama', 'mistral']
    passed_counts = [
        results_by_difficulty['codellama']['Difficult']['passed']*2,
        results_by_difficulty['llama']['Difficult']['passed']*2,
        results_by_difficulty['mistral']['Difficult']['passed']*2
    ]

    # Create the Plotly bar chart
    fig = px.bar(x=model_names, y=passed_counts,
                labels={'x': 'Model', 'y': 'Passed Count (Easy)'},
                title="Comparison of Models on Difficult Tasks")

    # Display the chart in Streamlit
    st.plotly_chart(fig)
    
    overall_results_by_model = {}

    for model, difficulties in results_by_difficulty.items():
        overall_results_by_model[model] = {
            'passed': 2*sum(results['passed'] for results in difficulties.values()),
            'failed': 2*sum(results['failed'] for results in difficulties.values())
        }
    
    model_names = list(overall_results_by_model.keys())
    passed_counts = [result['passed'] for result in overall_results_by_model.values()]
    failed_counts = [result['failed'] for result in overall_results_by_model.values()]



    fig = px.bar(x=model_names, y=[passed_counts],
             barmode='group',
             labels={'x': 'Model', 'y': 'Count'},
             title="Overall Results by Model (Passed vs. Failed)")
    st.plotly_chart(fig)
