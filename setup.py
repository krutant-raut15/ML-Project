from setuptools import setup, find_packages

from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    ## this function wil return a requirment s
    get_requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        



setup(
    name='mlproject',  # Your package name
    version='0.1.0',
    author='Krutant Raut',
    author_email='krutantraut.com@gmail.com',
    description='A machine learning project example',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
