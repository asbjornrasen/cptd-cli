# setup.py — полноценный pip-инсталлятор CLI-команды cptd

from setuptools import setup, find_packages
from pathlib import Path


setup(
    name='cptd',
    version='2.0.4',
    description='CPTD CLI',
    author='Asbjorn Rasen',
    author_email='asbjornrasen@gmail.com',
    url='https://www.cptdcli.com',
    project_urls={
    "License": "https://creativecommons.org/licenses/by-nd/4.0/",
    "Homepage": "https://www.cptdcli.com",
    "Source": "https://github.com/asbjornrasen/cptd-dsl"
    },
    license="CC BY-ND 4.0",
    # packages=find_packages(include=['cptd_tools', 'cptd_tools.commands']),
    # заменяем
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',

    
    packages=find_packages(),                 # без include=…

    include_package_data=True,
    package_data={'cptd_tools': ['cptd_manifest.cptd', 'create_command.md']},


    entry_points={
        'console_scripts': [
            'cptd = cptd_tools.main:main'
        ]
    },
    install_requires=[
        'argcomplete>=1.12.0',
        'PyYAML>=6.0'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent'
    ],
)

