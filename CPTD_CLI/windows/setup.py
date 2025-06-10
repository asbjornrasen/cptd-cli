# setup.py — полноценный pip-инсталлятор CLI-команды cptd

from setuptools import setup, find_packages

setup(
    name='cptd',
    version='1.0.0',
    description='CPTD CLI — инструмент для работы с DSL-планировщиком',
    author='Asbjorn Rasen',
    author_email='author@example.com',
    # packages=find_packages(include=['cptd_tools', 'cptd_tools.commands']),
    # заменяем
    packages=find_packages(),                 # без include=…

    entry_points={
        'console_scripts': [
            'cptd = cptd_tools.main:main'
        ]
    },
    install_requires=[
        'argcomplete>=1.12.0'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)

# УСТАНОВКА:
#   pip install .
# УДАЛЕНИЕ:
#   pip uninstall cptd
# ПОСЛЕ УСТАНОВКИ:
#   cptd help

# Если не работает: убедитесь, что Scripts/ в PATH:
#   %APPDATA%\Python\PythonXY\Scripts
