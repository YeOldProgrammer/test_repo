from setuptools import setup

setup(
    name='test_repo',
    url='https://github.com/YeOldProgrammer/test_repo',
    author='Tim Olker',
    author_email='tim@olker.us',
    # Needed to actually package something
    packages=['test_repo'],
    entry_points={'console_scripts': ['test_repo = test_repo.file1:hw']},
    # Needed for dependencies
    install_requires=['requests'],
    version='0.2',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    long_description=open('README.txt').read(),
)