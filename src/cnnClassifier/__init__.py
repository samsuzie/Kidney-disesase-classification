# here we will create logging functionality
# we are creating  loggigng file in the constructor file/__init__.py  so that whenever we need to import these logging/exception files in any of our files in components, it will be easy
import os
import sys
# using python inbuilt logging so that we  can create our custom logging
import logging

logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

log_dir= "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        # with the help of below line we will be able to print all the logs in the terminal as well
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("cnnClassifierLogger")
