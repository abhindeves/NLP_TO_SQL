from openai import OpenAI
import os



#*******Initiate client*******
client  = 1

def create_system_prompt(df,df_name):
    
    prompt = """You are an SQL expert. Here is sqlite SQL table, with their properties:
    
    {}({})
    
    your job is to write queries given a users request. Only Output the SQL query.
    Start with SELECT statement""".format(df_name,",".join(df.columns.tolist()))
    return prompt

def user_query_input():
    """Ask the user what they want to know about the data.

    Returns:
        string: User input
    """
    user_input = input("Ask what you want to know about the data: ")
    return user_input

# def combine_prompt(fixed_sql_prompt, user_query):
#     """Combine the fixed SQL prompt with the user query.

#     Args:
#         fixed_sql_prompt (string): Fixed SQL prompt
#         user_query (string): User query

#     Returns:
#         string: Combined prompt
#     """
#     final_user_input = f"### A query to answer: {user_query}\nSELECT"
#     return fixed_sql_prompt + final_user_input

def send_to_openai(sys,usr):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":f"{sys}"},
        {"role":"user","content":f"{usr}"}
    ],
    stop = [';']
    )
    response = completion.choices[0].message.content
    return response

