from setuptools import setup

setup(
    name ="githubactivity",
    version = '1.0',
    py_modules = ['main'],
    install_requires = ["requests"],
    entry_points = {
        'console_scripts':['githubactivity = main:main'],
    },

)
