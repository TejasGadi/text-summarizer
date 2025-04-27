## Data Transfomation operation libraries import

import os
from src.textSummarizer.logging import logger
from transformers import AutoTokenizer 
from datasets import load_from_disk
from src.textSummarizer.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig):
        self.config = data_transformation_config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    # Transforming data into seq to seq model required format for model training
    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch["dialogue"], max_length=1024, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch["summary"], max_length=1024, truncation=True)
        
        return {
            'input_ids':input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def apply_transformation_to_dataset(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(function=self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))
