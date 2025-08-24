import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

project_name = "firstDSProject"

list_of_projects = [
    "logger.py",
    "utils.py",
    "exception.py",
    "artifacts",
    "setup.py",
    "app.py",
    "DockerFile"
    f"src/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transform.py",
    f"src/{project_name}/components/data_trainer.py",
    f"src/{project_name}/components/data_monitor.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
]

for filepath in list_of_projects:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory : {filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating empty file")

    else:
        logging.info(f"{filename} is already exists")
