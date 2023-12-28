# code for reading data from dataset, dividing it into train and test dataset.
# related to work of big data team, seggregating work

# reads data from local source, we can also read from cloud, mongodb, etc.

import os
import sys
#for exceptions

from src.exception import CustomException
from src.logger import logging

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# class for inputs, paths for train test dataset
# use for only defining variables
@dataclass # used for defining instance variables
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv') # output path
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #object

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion component")
        try:
            df = pd.read_csv('../../notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=3)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)