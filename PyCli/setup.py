from setuptools import setup, find_packages
import os


# ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is Project Root

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # This is Base Directory

def read_text(file_name: str) -> str:
    return open(os.path.join(BASE_DIR, f'{file_name}')).read()


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()
with open("requirements.txt", "r", encoding="utf-8") as reqs:
    requirements = reqs.read()


setup(
    name = 'CSV',
    version = '0.0.1',
    author = 'Ali Mohammad Tarif',
    author_email = 'tohin.tarif@gmail.com',
    license = read_text('LICENSE'),
    description = 'Generate Stdout and Save it to excel file',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/tuhintarif/cli_tool_basic',
    py_modules = ['tool', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        iprice = __main__:main
    '''
)