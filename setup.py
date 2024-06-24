# Importing the libraries 
from setuptools import find_packages, setup 
from typing import List 


HYPHEN_E_DOT_REQUIREMENT = '-e .'

def get_requirements(file_path:str) ->List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT_REQUIREMENT in requirements:
        requirements.remove(HYPHEN_E_DOT_REQUIREMENT)


__version__ = "0.0.1"
SRC_REPO = "Stroke_Prediction"

setup(
    name = SRC_REPO,
    version = __version__,
    description = "This is a project to predict Stroke Prediction",
    author = "Sulayman Yusuf",
    author_email = "xyronoyusuf@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirments.txt')
)