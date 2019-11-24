from setuptools import setup

setup(
    name='test_repo',
    url='https://github.com/YeOldProgrammer/test_repo',
    author='Tim Olker',
    author_email='tim@olker.us',
    # Needed to actually package something
    packages=['test_repo'],
    # Needed for dependencies
    install_requires=['requests'],
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    long_description=open('README.txt').read(),
)