import json
import os

import yaml


def parse_file(filepath: str) -> dict:
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()

    with open(filepath, "r") as file:
        if ext in (".json",):
            return json.load(file)
        elif ext in (".yml", ".yaml"):
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file format: {ext}") # NOSONAR


def get_file_extension(filepath: str) -> str:
    return os.path.splitext(filepath)[1].lower().replace(".", "") # NOSONAR
