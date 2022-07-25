#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-google-analytics-ua",
    version="1.1.3",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_google_analytics-ua"],
    install_requires=[
        "singer-python==5.9.0",
        "requests==2.22.0",
        "backoff==1.8.0",
        "jwt==0.6.1"
    ],
    extras_require={
        'test': [
            'pylint==2.10.2',
            'nose'
        ],
        'dev': [
            'ipdb',
        ]
    },
    entry_points="""
    [console_scripts]
    tap-google-analytics-ua=tap_google_analytics_ua:main
    """,
    packages=["tap_google_analytics_ua"],
    package_data = {
        "tap_google_analytics_ua": ["tap_google_analytics_ua/ga_cubes.json"]
    },
    include_package_data=True,
)
