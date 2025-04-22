import os
import urllib.request as request
from src.textSummarizer.logging import logger
import zipfile
from src.textSummarizer.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_zip(self):
        if not os.path.exists(self.config.local_dataset_zip_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, 
                filename=self.config.local_dataset_zip_file
            )
            logger.info("File has been downloaded")
        else:
            logger.info("File already exists")

    def extract_zip(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_dataset_zip_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)