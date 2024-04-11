from setuptools import setup, find_packages

setup(
    name='Practice',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'wheel',
        'setuptools',
        'mypy',
        'flake8',
        'requests',
        'ipython',
        'django',
        'beautifulsoup'
    ],
)