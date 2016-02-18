from setuptools import setup

setup(
    name='SalesforceIQ',
    version='0.2',
    url='https://github.com/50onRed/apisdk',
    description='SalesforceIQ API',
    long_description=__doc__,
    package_dir={'': 'python'},
    packages=['relateiq'],
    install_requires=[
        'requests>=2.6.0',
        'nameparser>=0.3.4',
        'validate_email>=1.3',
        'pytz>=2015.2'
        ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
