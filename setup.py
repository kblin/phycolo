try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Pyholgenetic Codon-based Localization of Gene Clusters',
    'author': 'Kai Blin',
    'author_email': 'kai.blin@biotech.uni-tuebingen.de',
    'url': 'https://github.com/kblin/phycolo',
    'install_requires': ['helperlibs'],
    'packages': ['phycolo'],
    'scripts': ['bin/phycolo'],
    'name': 'phycolo',
}
