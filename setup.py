import os
from setuptools import setup


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    name='highrise-python',
    version=0.1,
    author='avalanchy',
    author_email='avalanchy@gmail.com',
    description='Python bindings for the Highrise API',
    keywords='highrise api python wrapper sdk bindings',
    url='https://github.com/avalanchy/highrise-python',
    long_description=read('README.md'),
    license=read('LICENSE'),
    install_requires=[
        'requests',
    ],
)