try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Web IMAP client',
    'author': 'Victor',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'vic.toad.tor@free.free',
    'version': '0.1',
    'install_requires': ['nose', 'bottle'],
    'packages': ['pymap'],
    'scripts': [],
    'name': 'pymap'
}

setup(**config)
