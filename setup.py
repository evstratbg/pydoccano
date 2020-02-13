import json

from setuptools import setup, find_packages

from pydoccano import __version__


def requirements():
    requirements_list = []

    with open('Pipfile.lock', "r") as requirements:
        data = json.load(requirements)
    data = data['default']
    for i in data:
        try:
            req = i + data[i]['version'].replace('==', '>=')
        except KeyError:
            req = f"-e git+{data[i]['git']}@{data[i]['ref']}#egg={i}"
        requirements_list.append(req)
    return requirements_list


setup(
    name='pydoccano',
    version=__version__,
    description='This package for API of doccano',
    author='Bogdan Evstratenko)',
    author_email='evstrat.bg@gmail.com',
    url='https://github.com/evstratbg/pydoccano',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=requirements(),
)
