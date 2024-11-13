# in this file we will keep all of our common code
# in this we are goin to write our box exception using python-box that we installed in our requirements.txt
import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
# we need this function to read the yaml content that we are goin to write inside the yaml file
# we are going to give the yaml file path and it will return the yaml content
# ->ConfigBox , by doing this we are specifying the return type
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml(str): path like imput
    Raises:
        ValueError:if yaml file is empty
        e:empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
# this function is used to create the directories like artifacts directory which we will be creating
# we need json file because we want to save our model metrics in json format
def create_directories(path_to_directories:list,verbose=True):
    """create list of directories
    Args:
        path_to_directories(list):list of apth of directories
        ignore_log(bool,optional):ignore if multiple dirs is to be created.Defaults to False. 
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at :{path}")


@ensure_annotations
def save_json(path:Path,data:dict):
    """save json data
    Args:
        path(Path):path to json file
        data(dict):data to be saved in json file
        """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

# to load any json file we will be using load_json function
@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """load json file data
    Args:
    path(Path):path to json file
    Returns:
    ConfigBox:data as class attribute insead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded suceesfully from :{path}")
    return ConfigBox(content)


# we will be using save bi  function when we want to save outr file as in binary format
# python function to save machine learning model and other large datasets in binary format
#joblib save data in binary format which is efficient for storing large datasets
@ensure_annotations
def save_bin(data:Any,path:Path):
    """save binary file
    Args:
        data(Any):data to be saved as binary
        path(Path):path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at:{path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())