
import os
import logging

import pandas as pd
from openai import OpenAI
import os

import db_utils
import openai_utils



# I*******NITIATE CLIENT*******


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# openai.api_key = os.environ["OPENAI_API_KEY"]

if __name__ == "__main__":
    logging.info("Loading data...")
    df = pd.read_csv("sales_data_sample.csv")
    logging.info(f"Data Format: {df.shape}")

    logging.info("Converting to database...")
    database = db_utils.dataframe_to_database(df, "Sales")
    
    system_prompt = openai_utils.create_system_prompt(df, "Sales")
    logging.info(f"Fixed SQL Prompt: {system_prompt}")

    logging.info("Waiting for user input...")
    user_input = openai_utils.user_query_input()
    final_prompt = 'System Prompt: '+system_prompt+'\n'+'User Input: '+user_input
    logging.info(f"Final Prompt: {final_prompt}")

    logging.info("Sending to OpenAI...")
    proposed_query = openai_utils.send_to_openai(system_prompt,user_input)
    logging.info(f"Response obtained. Proposed sql query: {proposed_query}")
    result = db_utils.execute_query(database, proposed_query)
    logging.info(f"Result: {result}")
    print(result)
    
    
