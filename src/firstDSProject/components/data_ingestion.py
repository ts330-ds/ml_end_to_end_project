import os
import pandas as pd
import sys
from dataclasses import dataclass
from src.firstDSProject.exception import CustomException
from src.firstDSProject.logger import logging
from utils import read_sql_data
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Start")
        try:
            df = read_sql_data()
            os.makedirs(os.path.dirname(self.ingestion.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, random_state=42, test_size=0.2)
            train_set.to_csv(self.ingestion.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion.test_data_path, index=False, header=True)

            logging.info("Ingestion is completed")

            return (
                self.ingestion.train_data_path,
                self.ingestion.test_data_path
            )
        except Exception as e:
            raise CustomException(e)
