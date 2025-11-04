# Import Libraries
from sqlalchemy import create_engine, inspect
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import re
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# Step 1: Extract Schema

db_url = "sqlite:///retail.db"

def extract_schema(db_url):
    engine = create_engine(db_url)
    inspector = inspect(engine)
    schema = {}

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = [col['name'] for col in columns]
    return json.dumps(schema)

# Step 2: Text to SQL (OpenAI gpt-4.1-mini)

def text_to_sql(schema, prompt):
    SYSTEM_PROMPT = """
    You are an expert SQL Query Generator. Your primary function is to translate a user's natural language request into a single, valid, and executable SQL query. You must adhere strictly to the provided database schema.
    
    Core Directives:

    Strict Compliance: The generated SQL query must be syntactically correct and only use the exact table names and column names provided in the schema.

    Single Query Output: Output only the final SQL query. Do not include any explanatory text, conversational filler, markdown formatting (like ```sql), comments, headers, or surrounding text. No preamble please.

    Ambiguity Handling: If a user's request is ambiguous or references a column/table not in the schema, you must make a reasonable and informed guess based on the schema and standard SQL conventions. For example, if a user asks for a "count," use COUNT(*).

    No Hallucination: You must never invent tables, columns, functions, or data not explicitly available in the provided schema.

    Data Type Consideration: Infer the correct SQL operations and functions (e.g., date functions, string functions, numerical aggregations) based on the likely data types of the columns. 
    """
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Schema:\n{schema}\n\nQuestion: {user_prompt}\n\nSQL_QUERY:")
    ])
    
    model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.0)
    
    chain = prompt_template | model
    
    raw_response = chain.invoke({"schema": schema, "user_prompt": prompt})

    return raw_response.content

def get_data_from_database(prompt):
    schema = extract_schema(db_url)
    sql_query = text_to_sql(schema, prompt)
    conn = sqlite3.connect("retail.db")
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    results = res.fetchall()
    conn.close()
    
    return results
