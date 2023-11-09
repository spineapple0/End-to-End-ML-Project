from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def getRequirments(filePath: str)->List[str]:
    requirments = []
    with open(filePath) as fileObj:
        requirments = fileObj.readlines()
        requirments = [req.replace('\n', '') for req in requirments]
        
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    return requirments


setup(
    name='ml_project',
    version='0.0.1',
    author='spineapple',
    author_email="swapnanilmukhopadhyay002@gmail.com",
    packages=find_packages(),
    install_requires= getRequirments('requirments.txt'),
)