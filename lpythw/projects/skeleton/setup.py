try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'https://github.com/xinjianhou/python',
	'download_url': 'https://github.com/xinjianhou/python',
	'author_email': 'houxinjian7@outlook.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)