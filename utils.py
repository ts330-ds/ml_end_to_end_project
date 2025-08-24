import os
import sys
import pymysql
import pandas as pd
from dotenv import load_dotenv
from src.firstDSProject.logger import logging
from src.firstDSProject.exception import CustomException

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')


def read_sql_data() -> pd.DataFrame:
    logging.info("Reading SQL database started")
    try:
        mysql = pymysql.connect(
            host=host,
            password=password,
            user=user,
            database=db
        )
        logging.info("Database connected ", mysql)

        df = pd.read_sql_query('Select * from students', mysql)
        print(df.head())
        return df
    except Exception as e:
        raise CustomException(e)
