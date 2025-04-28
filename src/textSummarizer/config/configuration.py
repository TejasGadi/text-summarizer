from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import create_directories,read_yaml
from src.textSummarizer.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
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

    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        ) 

        return data_transformation_config

    def get_model_trainer_config(self)->ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs=self.params.num_train_epochs,
            warmup_steps=self.params.warmup_steps,
            per_device_train_batch_size=self.params.per_device_train_batch_size,
            weight_decay=self.params.weight_decay,
            logging_steps=self.params.logging_steps,
            eval_strategy=self.params.eval_strategy,
            eval_steps=self.params.eval_steps,
            save_steps=self.params.save_steps,
            gradient_accumulation_steps=self.params.gradient_accumulation_steps
        )

        return model_trainer_config