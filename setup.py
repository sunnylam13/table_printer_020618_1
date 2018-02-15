try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Prints and arranges a table using lists as columns.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/table_printer_020618_1',
	'download_url': 'https://github.com/sunnylam13/table_printer_020618_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Table Printer Using Lists'
}

setup(**config)