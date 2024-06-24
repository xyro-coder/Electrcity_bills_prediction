import logging
from datetime import datetime
import os
import sys

#create the logging file
log_file_name = f"{datetime.now().strftime('%y_%m_%d_%H_%M_%S')}.log"

#Define the log file path
log_file_path = os.path.join(os.getcwd(),"logs",log_file_name)

#create the log directory if it doesnt exsit    
os.makedirs(os.path.dirname(log_file_path),exist_ok=True)

#logger configuration
logging.basicConfig(
    format= "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    handlers=[
        logging.FileHandler(log_file_path), #output logs
        logging.StreamHandler(sys.stdout),
    ]
)
logger = logging.getLogger("StrokePrediction")
