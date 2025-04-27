# Data Ingestion Config Schema/Data Class
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: Path
    local_dataset_zip_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path