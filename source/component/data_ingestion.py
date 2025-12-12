import os
import sys
from source.exception import customException
from source.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataingestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class Dataingestion:
    def __init__(self):
        self.ingestion_config = DataingestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method/component")
        try:
            # FIXED WRONG FILE PATH
            df = pd.read_csv(r"A:\ML projects\Documents\stud.csv")
            logging.info("Read the dataset as a dataframe")

            # Creating artifacts folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path   # FIXED ATTRIBUTE NAME
            )

        except Exception as e:
            raise customException(e, sys)


if __name__ == "__main__":
    obj = Dataingestion()
    obj.initiate_data_ingestion()
