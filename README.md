# 🌟 Natural Language to SQL Query Conversion System 🌟

## Overview 📜
Welcome to the magical world of SQL query generation! 🧙‍♂️✨ This system transforms your natural language wishes into SQL spells, using a sprinkle of Python and a dash of OpenAI's secret sauce.

## File Structure 📂
- **File 1**: 🧰 Database Utilities (`db_utils.py`)
- **File 2**: 🤖 OpenAI Integration (`openai_utils.py`)
- **File 3**: 🎨 User Interface (`stream.py`)

## File 1: Database Utilities (`db_utils.py`) 🧰

### Importing Modules
We kick things off by summoning the necessary modules from SQLAlchemy's mystical realm. `create_engine` is our portal to the database dimension, and `text` is our spellbook for SQL incantations.

### Defining `dataframe_to_database` Function
This enchantment takes a humble pandas DataFrame (`df`) and a table name (`table_name`) and transmutes it into a database table. By invoking SQLAlchemy's `create_engine`, we conjure a database engine, and with the `to_sql` alchemy, we bind the DataFrame into the database under the chosen name.

### Defining `execute_query` Function
With an SQLAlchemy engine (`engine`) and a SQL query (`query`) in hand, this function casts the query into the database cauldron, stirs it with `text`, and reveals the results with `fetchall`.

### Usage of SQLAlchemy
We harness SQLAlchemy for its powerful ORM spells and SQL query charms.

### SQLite Database
For our demonstrations, we conjure an SQLite in-memory database (`'sqlite:///:memory:'`)—no need for heavy server beasts!

## File 2: OpenAI Integration (`openai_utils.py`) 🤖

### Setting Up OpenAI API
We align the stars with the OpenAI module and whisper our API key for entry into the AI's inner sanctum.

### Creating System Prompt
The `create_system_prompt` ritual prepares a stage for our SQL table, inviting users to craft their SQL queries.

### User Query Input
The `user_query_input` incantation beckons users to voice their data desires, guiding the SQL query genesis.

### Sending Prompt and User Input to OpenAI
Our `send_to_openai` messenger dispatches the system prompt and user's query to the OpenAI oracle, seeking the wisdom of `gpt-3.5-turbo`.

### Handling OpenAI Response
We decode the oracle's visions, extracting the SQL prophecy to be shared with the seeker.

## File 3: User Interface (`stream.py`) 🎨

### Page Configuration and Styling
We weave a web of wide-mode configurations and CSS spells to dress our page in a gradient robe.

### Main Functionality
- **Title Display**: "🔍 CSV File Query Tool" shines atop our digital parchment.
- **CSV File Upload**: Seekers may present their CSV scrolls here.
- **CSV File Processing**: Scrolls are transcribed into pandas DataFrames.
- **Displaying DataFrame**: Behold the first 5 rows of your scroll!
- **System Prompt Creation**: We craft a system prompt from the DataFrame's essence.
- **User Query Input**: Query thy heart's content in our text field.
- **Query Processing and Execution**: We commune with OpenAI and execute the SQL revelation upon the SQLite altar.
- **Displaying Query Results**: The fruits of your query are laid bare in a Streamlit DataFrame display.
- **Error Handling**: Should your query be amiss, we shall catch and illuminate the error.

## Getting Started 🚀
Embark on this adventure by ensuring all mystical components are in place and your OpenAI API key is whispered into the `openai_utils.py` scroll.

## Dependencies 📦
- SQLAlchemy
- pandas
- OpenAI
- Streamlit

## Usage 🛠️
Invoke the `stream.py` script to raise the Streamlit application from the ether and follow the celestial prompts to upload your CSV scroll and articulate your queries.
