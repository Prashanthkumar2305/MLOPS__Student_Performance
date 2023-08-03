import os
import sys
from setuptools import setup,find_packages
from typing  import List


hyphen_e_dot="-e ."

def get_requirements(file_path:str)->List[str]:
    """"This will provide list , what we need to install
    """
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[require.replace('/n','') for require in requirement]

        if hyphen_e_dot in requirement:
            requirement.remove(hyphen_e_dot)


setup(
    name='Student-Performance',
    version='0.0.1',
    author='Prashanthkumar k',
    author_email='prashanthpacchin103@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)