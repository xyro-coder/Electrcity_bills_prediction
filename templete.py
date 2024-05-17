#import the neccesary libraries
import os
from pathlib import Path

#Define package name
package_name ="ElectricyBill"

#Write down the files needed to be created
list_of_files = [
    Path(".github") / "workflows" / ".gitkeep", #Github workflow directory
    'src/__init__.py',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/components/__init__.py',
    f'src/{package_name}/components/c_01_data_ingestion.py',
    f'src/{package_name}/components/c_02_data_validation.py',
    f'src/{package_name}/components/c_03_data_transformation.py',
    f'src/{package_name}/components/c_04_model_trainer.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/utils/commons.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/config/configurations.py',
    f'src/{package_name}/pipelines/__init__.py',
    f'src/{package_name}/pipelines/p_01_data_ingestion.py',
    f'src/{package_name}/pipelines/p_02_data_validation.py',
    f'src/{package_name}/pipelines/p_03_data_transformation.py',
    f'src/{package_name}/pipelines/p_02_model_training.py',
    f'src/{package_name}/entity/__init__.py',
    f'src/{package_name}/entity/configuration_entity.py',
    f'src/{package_name}/constants/__init__.py',
    f'src/{package_name}/exceptions.py',
    f'src/{package_name}/logger.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',  
    'main.py',
    'app.py',
    'setup.py',
    'requirments.txt',
    'research/trials.py',
    'templates/home.html',
    'templates/index.html'
]
#Loop through the list 
for filepath in list_of_files:
    filepath = Path(filepath)

    #spilt the file path into a directory and file name
    filedir, filename = os.path.split(filepath)

    #create directory if it does not exist
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)

    #create an empty file if it doesn't exist or if empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass


