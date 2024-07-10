

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['resources']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame'],
    'iconfile': 'resources/icon.png',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
