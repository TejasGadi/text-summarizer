from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import create_directories,read_yaml
from src.textSummarizer.config_entity import DataIngestionConfig
from box import ConfigBox

# Create Configuration Manager: This has basic information required before staring any module/components

class ConfigurationManager:
    def __init__(self, config_path = CONFIG_FILE_PATH, params_path = PARAMS_FILE_PATH):
        self.config:ConfigBox = read_yaml(config_path)
        self.params:ConfigBox = read_yaml(params_path)

        # Create Artifacts Root dir
        create_directories([self.config.artifacts_root])
    
    # Read Data Ingestion Config
    def get_data_ingestion_config(self)->DataIngestionConfig:
        data_config = self.config.data_ingestion

        # create data root directory
        create_directories([data_config.root_dir])


        # This is the input that will go to the Data Ingestion c omponent
        data_ingestion_config = DataIngestionConfig(
            root_dir= data_config.root_dir,
            source_url= data_config.source_url,
            local_dataset_zip_file=data_config.local_dataset_zip_file,
            unzip_dir=data_config.unzip_dir
        )

        return data_ingestion_config
