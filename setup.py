from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-geolocation',

    version='0.0.0',

    description='A collection of Django utilities to store simple geographical information.',
    long_description=long_description,

    author='Martin Vuelta',
    author_email='martin.vuelta@gmail.com',

    license='MIT',

    url='https://github.com/ZodiacFireworks/django-geolocation',
    download_url='https://github.com/ZodiacFireworks/django-geolocation/tarball/0.0.0',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords=['django', 'geographical information', 'geoposition', 'geolocation'],

    zip_safe=True,

    packages=find_packages(
        exclude=[
            'contrib',
            'docs',
            'tests'
        ]
    ),

    package_data={
        'geolocation': [
        ],
    },

    install_requires=[
        'django-appconf >= 0.4',
    ],
)
