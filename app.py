from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

import streamlit as st
import sqlite3
import google.generativeai as genai

## Configure genai api key
genai.configure(api_key=os.getenv("Gemini_API_KEY"))


## function to load google gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## function to retrive query from sql database
def read_sql_query(sql,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows

## Define prompt for gemini model
prompt=["""
    You are an expert in converting english questions to SQL query!
    The SQL database has a table named student with columns Name, Roll, Marks, Subject. For Example\n
    Example 1: How many entries are there in the table the answer should be like this SELECT COUNT(*) FROM student;\n
    Example 2: What are the names of students who have scored more than 80 marks? The answer should be like this SELECT Name FROM student WHERE Marks>80;\n
    also the sql query should not have ``` in begining or end of the query and sql word in the query 
"""]

## Streamlit app
st.set_page_config(page_title="SQL Query Generator",page_icon=":bar_chart:",layout="centered",initial_sidebar_state="expanded")
st.title("SQL Query Generator")
st.header("Generate SQL query using Google Gemini AI")

question=st.text_area("Input: ",key="input")

submit=st.button("Generate SQL Query")

## if submit button is clicked
if submit:
    response=get_gemini_response(question,prompt)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is: ")
    for row in data:
        st.header(row)
