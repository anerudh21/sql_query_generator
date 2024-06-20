import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import sqlite3
from dotenv import load_dotenv
from io import StringIO
import re

# Load environment variables
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("GEMINI_KEY")
st.title("Anerudh's ChatBot")

# Configure Gemini API key
genai.configure(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_csv" not in st.session_state:
    st.session_state.uploaded_csv = None

# Function to display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    # Read the CSV file
    st.session_state.uploaded_csv = pd.read_csv(uploaded_file)
    st.write("CSV Loaded Successfully")
    st.write(st.session_state.uploaded_csv)

# User input for chat
if prompt := st.chat_input("Enter your message here"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if st.session_state.uploaded_csv is not None:
        # Include CSV content in the prompt
        csv_preview = st.session_state.uploaded_csv.head().to_csv(index=False)
        prompt_with_csv = f"{prompt}\n\nHere is the first few rows of the CSV:\n{csv_preview}\nGenerate a SQL query for this data."

        with st.chat_message("assistant"):
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt_with_csv)
            assistant_response = response.text
            st.markdown(assistant_response)

        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        # Extract SQL query from the response
        sql_query_match = re.search(r'SELECT .*;', assistant_response, re.DOTALL | re.IGNORECASE)
        if sql_query_match:
            sql_query = sql_query_match.group(0)

            try:
                # Create an in-memory SQLite database
                conn = sqlite3.connect(":memory:")
                st.session_state.uploaded_csv.to_sql("data", conn, index=False, if_exists='replace')

                # Execute the SQL query
                result_df = pd.read_sql_query(sql_query, conn)
                st.write("Query Result:")
                st.write(result_df)

                # Close the connection
                conn.close()
            except Exception as e:
                st.error(f"Error executing query: {e}")
        else:
            st.error("Generated text does not contain a valid SQL SELECT query.")
    else:
        st.error("Please upload a CSV file first.")
