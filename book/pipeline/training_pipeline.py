from book.components.data_ingestion import DataIngestion
from book.components.data_validation import DataValidation
from book.components.data_transformation import DataTransformation
from book.components.model_training import ModelTrainer

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_validation = DataValidation()
        self.data_transformation = DataTransformation()
        self.model_training = ModelTrainer()

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
        self.data_transformation.initiate_data_transformation()
        self.model_training.initiate_model_trainer()