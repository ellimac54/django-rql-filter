import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-rql-filter",
    version="0.1.3",
    author="Nicolas Joyard",
    author_email="joyard.nicolas@gmail.com",
    description=("A RQL-enabled filter backend for django-rest-framework"),
    license="MIT",
    keywords="django filter drf rest rql rsql fiql",
    url="https://github.com/njoyard/django-rql-filter",
    packages=[
        'rql_filter',
        'rql_filter.parser'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'djangorestframework>=3,<4',
        'grako>=3.12,<3.13',
    ],
    extras_require={
        'testing': [
            'codecov>=2,<3',
            'django-responsediff>=0.6,<0.7',
            'flake8>=2,<3',
            'pytest>=2,<3',
            'pytest-cov>=2,<3',
            'pytest-django>=2,<3',
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
