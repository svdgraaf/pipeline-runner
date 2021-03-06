
#!/usr/bin/env python
from setuptools import setup, find_packages

try:
    README = open('README.md').read()
except:
    README = None

try:
    LICENSE = open('LICENSE.txt').read()
except:
    LICENSE = None

setup(
    name = 'pipeline-runner',
    version = '1.1.5',
    description='Run your Bitbucket Pipeline in the current environment (eg: Bamboo)',
    long_description=README,
    author = 'Sander van de Graaf',
    author_email = 'mail@svdgraaf.nl',
    license = LICENSE,
    url = 'http://github.com/svdgraaf/pipeline-runner/',
    # packages = find_packages(),
    install_requires=['PyYAML>=3.11'],
    scripts=['pipeline-runner/pipeline-runner'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
