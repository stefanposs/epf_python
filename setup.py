from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
     name='epf',
     version='0.1',
     scripts=['lib'],
     author="Stefan Poss",
     author_email="sp@stefanposs.de",
     description="An Event-Driven Framework for data processing in the cloud",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/stefanposs/epf_python",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
