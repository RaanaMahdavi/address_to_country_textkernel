from setuptools import setup, find_packages

setup(
    name='text_kernel_assignment',
    packages=find_packages(),
    install_requires=[
        'unidecode',
        'pycountry',
        'setuptools>=18.0',
        'python-Levenshtein==0.23.0',
    ],
)
