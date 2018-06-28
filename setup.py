from setuptools import setup, find_packages

setup(
    name='tpd',
    version='0.0.1',
    description="AWS Traffic Policy Document creation library",
    author="Tony Tiger",
    author_email="thatrascaltiger@gmail.com",
    url="https://github.com/tigertoes/tpd",
    license="New BSD license",
    packages=find_packages(),
    test_suite="tests",
    use_2to3=True
)
