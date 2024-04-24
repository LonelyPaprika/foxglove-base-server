from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='foxglove_base_server',
    version='0.1',
    packages=find_packages(),
    install_requires=Path('requirements.txt').read_text().splitlines(),
)