from setuptools import setup,find_packages
setup(name = "census_income",version = "0.0.1",
author = "Akash Paarvathala",
author_email = "akashparvathala001@gmail.com",
packages = find_packages(),
install_requires = ["pandas","numpy","Flask"]
)