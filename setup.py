import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='concept-assignment-fib-calculator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='No License',  # example license
    description='concept-assignment-fib-calculator',
    long_description=README,
    url='https://github.com/apurvagupta123/concept_assign/',
    author='Apurva Gupta',
    author_email='apurvagupta1991@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2.6',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: No License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)