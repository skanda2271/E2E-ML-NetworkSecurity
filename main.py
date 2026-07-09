from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.data_transformation import DataTransformation
import sys


if __name__ == '__main__':
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        data_ingestion = DataIngestion(dataIngestionConfig)
        logging.info("Initiating Data Ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        data_validation_config = DataValidationConfig(trainingPipelineConfig)
        data_validation = DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info("Data Validation started")
        data_validation.initiate_data_validation()
        logging.info("Data Validation completed")
        print(data_ingestion_artifact)
        data_trans_config = DataTransformationConfig(trainingPipelineConfig)
        data_trans_artifact = DataTransformation(data_validation_artifact=data_validation,data_transformation_config=data_trans_config)
        print(data_trans_artifact)
        logging.info("Data Transformation Completed")

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    


    
