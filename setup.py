from setuptools import setup, find_packages

setup(
    name='project6',
    version='0.1',
    packages=find_packages(exclude=['validate_data*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Caleb Okon',
    author_email='calebachiever07@gmail.com'
)