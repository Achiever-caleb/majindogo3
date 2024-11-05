"""
This module, `data_ingestion`, is designed to connect to an SQLite database and extract data from various tables 
using SQL joins to create a comprehensive dataset that integrates geographic, weather, soil, and crop-related 
features, as well as farm management practices.

Also, it imports supplementary weather data from two external URLs for further analysis. 
Logging is configured to capture events, providing timestamps and context from the 'data_ingestion' logger.

Modules:
- sqlalchemy: Used to create a connection to the SQLite database.
- logging: Configured to track the workflow and events within the module, very useful for testing.
- pandas: Utilized for data handling and potential further data processing.

Parameters:
- db_path (str): The path to the SQLite database file.
- sql_query (str): SQL query to extract and join data from different tables in the database.
- weather_data_URL (str): URL for the external weather station data.
- weather_mapping_data_URL (str): URL for mapping data to match weather data with fields.

"""
from sqlalchemy import create_engine, text
import logging
import pandas as pd
# Name our logger so we know that logs from this module come from the data_ingestion module
logger = logging.getLogger('data_ingestion')
# Set a basic logging message up that prints out a timestamp, the name of our logger, and the message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


### START FUNCTION
def create_db_engine(db_path):
    """
    Creates and tests a SQLAlchemy database engine for the specified database path.
    Parameters:
        db_path (str): The path to the SQLite database.
    Returns:
        sqlalchemy.engine.Engine: The created database engine.
    Raises:
        ImportError: If SQLAlchemy is not installed.
        Exception: For any other errors encountered while creating the engine.
    """
    try:
        engine = create_engine(db_path)
        # Test connection
        with engine.connect() as conn:
            pass
        # test if the database engine was created successfully
        logger.info("Database engine created successfully.")
        return engine # Return the engine object if it all works well
    except ImportError: #If we get an ImportError, inform the user SQLAlchemy is not installed
        logger.error("SQLAlchemy is required to use this function. Please install it first.")
        raise e
    except Exception as e:# If we fail to create an engine inform the user
        logger.error(f"Failed to create database engine. Error: {e}")
        raise e
        
    
def query_data(engine, sql_query):
    """
    Executes a SQL query on the provided database engine and returns the result as a DataFrame.
    Parameters:
        engine (sqlalchemy.engine.Engine): The database engine to use for the query.
        sql_query (str): The SQL query to execute.
    Returns:
        pandas.DataFrame: DataFrame containing the query results.
    Raises:
        ValueError: If the query returns an empty DataFrame.
        Exception: If the query execution fails.
    """
    try:
        with engine.connect() as connection:
            df = pd.read_sql_query(text(sql_query), connection)
        if df.empty:
            # Log a message or handle the empty DataFrame scenario as needed
            msg = "The query returned an empty DataFrame."
            logger.error(msg)
            raise ValueError(msg)
        logger.info("Query executed successfully.")
        return df
    except ValueError as e: 
        logger.error(f"SQL query failed. Error: {e}")
        raise e
    except Exception as e:
        logger.error(f"An error occurred while querying the database. Error: {e}")
        raise e
    
def read_from_web_CSV(URL):
    """
    Reads a CSV file from a specified web URL and returns it as a DataFrame.
    Parameters:
        URL (str): The URL of the CSV file.
    Returns:
        pandas.DataFrame: DataFrame containing the CSV data.
    Raises:
        pandas.errors.EmptyDataError: If the URL does not contain a valid CSV file.
        Exception: For any other errors encountered while reading the CSV.
    """
    try:
        df = pd.read_csv(URL)
        logger.info("CSV file read successfully from the web.")
        return df
    except pd.errors.EmptyDataError as e:
        logger.error("The URL does not point to a valid CSV file. Please check the URL and try again.")
        raise e
    except Exception as e:
        logger.error(f"Failed to read CSV from the web. Error: {e}")
        raise e
### END FUNCTION