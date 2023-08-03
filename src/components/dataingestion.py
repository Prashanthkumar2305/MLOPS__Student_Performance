import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

from src.components.datatransform import DataTransformation

from src.components.datamodeler import ModelTrainer

@dataclass
class DataIngestion:
    train_path: str = os.path.join('artifacts', 'train.csv')
    test_path: str = os.path.join('artifacts', 'test.csv')
    raw_path: str = os.path.join('artifacts', 'data.csv')


class Data_Config_Transform:
    def __init__(self):
        self.config_ingestion = DataIngestion()

    def get_config_data(self):
        logging.info("read the dataset of std.csv")
        try:
            # Read data from the raw path defined in DataIngestion
            df = pd.read_csv(r'E:\Performance_of_student\src\notebook\Data\stud.csv')
            os.makedirs(os.path.dirname(self.config_ingestion.train_path), exist_ok=True)

            
            df.to_csv(self.config_ingestion.raw_path, index=False, header=True)

            logging.info("initiated train data and test data")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.config_ingestion.train_path, index=False, header=True)

            test_set.to_csv(self.config_ingestion.test_path, index=False, header=True)

            logging.info("It's done about the train and test datasets into csv format from raw_data")
            return (
                self.config_ingestion.train_path,
                self.config_ingestion.test_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    config_transform = Data_Config_Transform()
    train_path,test_path=config_transform.get_config_data()

    trans=DataTransformation()
    train_array,test_array=trans.initiate_data_transformation(train_path,test_path)

    trainer=ModelTrainer()
    trainer.initiate_model_trainer(train_array,test_array)
    