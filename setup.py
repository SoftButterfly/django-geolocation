from setuptools import setup, find_packages

setup(
    name='django-geolocation',
    version='0.0.0',
    description='A collection of Django utilities to store simple geographical information.',
    author='Martin Vuelta',
    author_email='martin.vuelta@gmail.com',
    url='https://github.com/ZodiacFireworks/django-geolocation',
    download_url='https://github.com/ZodiacFireworks/django-geolocation/tarball/0.0.0',
    keywords=['django', 'geographical information', 'geoposition', 'geolocation'],
    packages=find_packages(),
    zip_safe=True,
    package_data={
        'geolocation': [
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=['django-appconf >= 0.4'],
)
