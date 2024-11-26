# we have creted thie constant file becuae we have two folder config.yaml amd parma.yaml
# we have to read these file and return
# we will putting the path fo these two files in the this becauses they are constant and their path 
# will not be changing
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

