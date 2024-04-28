from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='foxglove_base_server',
    version='1.0.1',
    packages=find_packages(),
    package_data={'foxglove_base_server': ['examples/test.py']},
    install_requires=Path('requirements.txt').read_text().splitlines(),
    entry_points={
        'console_scripts': [
            'foxglove_base_server_example1 = foxglove_base_server.examples.example1:main',
        ],
    },
)