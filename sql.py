import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import sqlite3
from dotenv import load_dotenv
from io import StringIO
import re

load_dotenv()
API_KEY = os.getenv("GEMINI_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon=":robot:")
    st.markdown(
    """
        <div style= "text-align: center;">
        <h1> SQL Query Generator 😏</h1>
        <h3> I can generate SQL queries for you with explanations </h3>
        <p> this is a simple tool that allows you to generate sql queries based on prompt </p>
    """,
    unsafe_allow_html=True,
    )
    
    text_input  = st.text_area("Enter your prompt here: ")
    
    
    submit  = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template = """"
                Create a SQL query using the below text:
                
                ```
                    {text_input}
                ```
                I just want a SQL query
                
                
            """
            formatted_template = template.format(text_input=text_input)
            
            response = model.generate_content(formatted_template)
            sql_query = response.text
            
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
        
            expected_output = """"
                What would be the expected response of the sql query snippet:
                
                ```
                    {sql_query}
                ```
                Provide sample tabular response with no explanation:
                
                
            """
            expected_output_formatted = expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_formatted)
            eoutput = eoutput.text
            

            explanation = """"
                Explain this SQL query:
                
                ```
                    {sql_query}
                ```
                Please provide with the simplest of  explanation:
                
                
            """
            explanation_formatted = explanation.format(sql_query=sql_query)
            exp = model.generate_content(explanation_formatted)
            exp = exp.text
            
            with st.container():
                st.success("SQL Query generated successfully. Here is your Query below: ")
                st.code(sql_query,language="sql")
                
                st.success("Expected Output of this SQL query will be: ")
                st.markdown(eoutput)
                
                st.success("Explanation of this SQL Query: ")
                st.markdown(exp)

main()
