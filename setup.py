try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

description = 'Toolbox for anomaly detection.'

config = {
    'name': 'anomatools',
    'description': description,
    'long_description': readme(),
    'url': 'https://github.com/Vincent-Vercruyssen/anomatools',
    'author': 'Vincent Vercruyssen',
    'author_email': 'V.Vercruyssen@gmail.com',
    'version': '2018.01',
    'install_requires': ['numpy',
                         'scipy',
                         'matplotlib'],
    'packages': ['anomatools'],
    'package_dir' : {'anomatools': 'anomatools'},
    'keywords': 'anomaly detection',
    'include_package_data': True,
    'classifiers':['Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Programming Language :: Python :: 3']
}

setup(**config)
