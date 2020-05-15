# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-pt5",
    version="1.0",
    author="Damon Rodriguez",
    author_email="drjrodriguez615@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",# required if using a md file for long desc
    # license="MIT",
    url="https://github.com/DRodriguez615/lambdata-pt5",
    # keywords="",
    packages= ["my_lambdata"] #find_packages()  # ["my_lambdata"]
)
