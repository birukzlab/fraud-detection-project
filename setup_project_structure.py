import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files and directories to create
list_of_files = [
    "src/__init__.py",
    "src/main.py",
    "src/utils.py",
    "src/components/__init__.py",
    "src/components/test_component.py",
    ".env",
    "requirements.txt",
    "README.md"
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            if "README.md" in filename:
                f.write("# Fraud Detection Project\n\nDescription of your project.")
            if "requirements.txt" in filename:
                f.write("pandas\nnumpy\npsycopg2\npython-dotenv\n")
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

