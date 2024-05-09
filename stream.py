import streamlit as st
import pandas as pd
import db_utils
import openai_utils

def set_bg_style():
    # Set page config to wide mode
    st.set_page_config(layout="wide")

    # Define the style using CSS
    style = """
    <style>
    .stApp {
        background-image: linear-gradient(to right, #2193b0, #6dd5ed, #ff758c);
    }
    </style>
    """

    # Use the local CSS file using st.markdown
    st.markdown(style, unsafe_allow_html=True)

def main():
    st.title("🔍 CSV File Query Tool")

    # Upload CSV file
    uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the uploaded CSV file into a pandas DataFrame
        
        df = pd.read_csv(uploaded_file)
        database = db_utils.dataframe_to_database(df, "DB")
        # Display the first 5 rows of the DataFrame
        st.write("📊 First 5 rows of the uploaded CSV file:")
        st.write(df.head())        
        
        
        system_prompt = openai_utils.create_system_prompt(df, "DB")

        # Ask user for a query
        query = st.text_input("💬 Enter your query (e.g., filter, groupby, etc.):")
        if query:
            try:
                proposed_query = openai_utils.send_to_openai(system_prompt,query)
                st.write('🤖 Proposed query: \n\n',proposed_query)
                # Execute the user's query on the DataFrame
                result = db_utils.execute_query(database, proposed_query)
                # Display query results
                st.subheader("📈 Query results:\n")
                st.dataframe(result)
            except pd.errors.ParserError:
                st.error("Invalid query. Please check your input.")

if __name__ == "__main__":
    set_bg_style()
    main()
