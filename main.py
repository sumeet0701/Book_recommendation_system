from book.exception import CustomException
from book.logger import logging
from book.config.Configuration import AppConfiguration
from book.components.data_ingestion import DataIngestion
import os
from book.pipeline.training_pipeline import TrainingPipeline


def main():
    try:
        pipeline = TrainingPipeline()
        pipeline.start_training_pipeline()

    except Exception as e:
            logging.error(f"{e}")
            print(e)


if __name__ == "__main__":
     main()