import os
from setuptools import setup

# Utility function to read the requirement.txt file.
with open ('requirements.txt','r',encoding='utf-8') as f:
    requirements=f.read().split('\n')


setup(
    name = "mypackage",
    version = "0.0.1",
    author = "irungu festus",
    author_email = "irungufestus@gmail.com",
    description = ("An demonstration of how to scrape website"),
    license = "BSD",
    install_requires=requirements,
    py_modules=['scraping'],
    
    entry_points={
        'console_scripts': [
            'scrape-recipe = scraping.recipe.main:default',
        ]
    }
)

