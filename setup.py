from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shorturl/__init__.py
from shorturl import __version__ as version

setup(
	name="shorturl",
	version=version,
	description="A Frappe URL shortener",
	author="Senwize B.V.",
	author_email="info@senwize.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
