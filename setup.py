from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in mejorasv2/__init__.py
from mejorasv2 import __version__ as version

setup(
	name='mejorasv2',
	version=version,
	description='Mejoras para qlip Business',
	author='Mentum Group',
	author_email='aryrosa.fuentes@MENTUM.group',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
