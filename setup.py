from setuptools import find_packages, setup
# find_packages finds all the packages present in the directory 
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'mlops',
    version = '0.0.1',
    author = 'Manav',
    author_email = 'manavchan03@gmail.com',
    packages = find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn'] 
    install_requires = get_requirements('requirements.txt')
)

# for setup.py to find out the number of packages, it will see the directory that have file __init_.py and will consider that directory as a package, builds it therefore we can import it.