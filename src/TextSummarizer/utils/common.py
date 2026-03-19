import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ 
    Reads a yaml file and returns
    
    Args:
        path_to_yaml (str) : path like input where yaml file is located
        
    Raises:
        ValueError: If yaml file is empty
        e: Empty yaml file
        
    Returns:
        ConfigBox: ConfigBox type object for yaml file
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list,verbose = True):
    """
    Creates list of directories

    Args:
        path_to_directories (list): list of path of directories to be created
        verbose (bool, optional): whether to log info messages. Defaults to True.
        ignore_log(bool,optional): ignore if multiple directories is to be created. Defualts to False.

    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok = True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path:Path) -> str:
    """
    get the size in KB

    Args:
        path (Path): path of the file

    Returns
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024,2)
    return f"~{size_in_kb} KB"