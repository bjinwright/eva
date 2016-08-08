#!/usr/bin/env python

from setuptools import setup

setup(
    name='eva',
    version='0.1',
    description='Plugin for virtualenvwrapper to automatically '
                'export config vars found in your project level '
                '.env file.',
    author='Brian Jinwright',
    author_email='opensource@ipoots.com',
    url='https://github.com/bjinwright/eva',
    namespace_packages=['virtualenvwrapper'],
    packages=['virtualenvwrapper'],
    py_modules=['eva.cli'],

    install_requires=[
        'virtualenv',
        'virtualenvwrapper>=2.11',
        'click>=6.6',
        'terminaltables>=3.0.0',
    ],
    entry_points={
        'virtualenvwrapper.pre_activate': [
            'configvars = virtualenvwrapper.configvars:pre_activate',
        ],
        'virtualenvwrapper.pre_activate_source': [
            'configvars = virtualenvwrapper.configvars:pre_activate_source',
        ],
        'virtualenvwrapper.post_deactivate': [
            'configvars = virtualenvwrapper.configvars:post_deactivate',
        ],
        'virtualenvwrapper.post_deactivate_source': [
            'configvars = virtualenvwrapper.configvars:post_deactivate_source',
        ],
        'console_scripts':[
            'eva=eva.cli:eva'
        ]
    },

)
