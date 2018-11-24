import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="dolibarr",
	version="0.0.1",
	author="Simple Software Management Inc",
	author_email="support@simplesoftwaremanagement.com",
	description="A python package for working with the Dolibarr API",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/wtfbrb/dolibarr",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
