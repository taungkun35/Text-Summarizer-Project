from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trianer_config = config.get_model_trainer_config()
        model_trianer = ModelTrainer(config=model_trianer_config)
        model_trianer.train()