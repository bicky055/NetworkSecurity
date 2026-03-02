'''
 the setup.py file is used to define the package and its dependencies for distribution. It typically includes information such as the package name, 
 version, author, description, and a list of required packages. In this case, the setup.py 
 file would likely include the dependencies listed in the requirements.txt file, which are python-dotenv, pandas, numpy, and scikit-learn. 
 This allows users to easily install the necessary packages when they install the project.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
     this function will return a list of requirements from the requirements.txt file.
       It reads the file and splits the lines into a list, which can then be used in 
       the setup function to specify the install_requires parameter.
    '''
    requiremnt_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # process each line 
            for line in lines:
                requiremnt= line.strip()
                ## ignore empty lines and -e .
                if requiremnt and requiremnt != '-e .':
                    requiremnt_list.append(requiremnt)
    except FileNotFoundError:
        return []
    
    return requiremnt_list

# print(get_requirements())

setup(
    name= "NetworkSecurity",
    version="0.0.1",
    author="Bicky Jha",
    author_email="bickyjha24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)