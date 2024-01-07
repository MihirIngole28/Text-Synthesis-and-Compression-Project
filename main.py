from src.textSynthesisAndCompression.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSynthesisAndCompression.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e