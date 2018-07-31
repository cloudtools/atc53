from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='atc53',
    version='0.1.0',
    description='AWS Traffic Policy Document creation library',
    long_description=readme(),
    author='Tony Tiger',
    author_email='thatrascaltiger@gmail.com',
    url='https://github.com/cloudtools/atc53',
    license='New BSD license',
    packages=find_packages(),
    test_suite='tests',
    use_2to3=True
)
