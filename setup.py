from setuptools import setup

setup(
    name='SalesforceIQ',
    version='0.1',
    url='https://github.com/50onRed/apisdk',
    description='SalesforceIQ API',
    long_description=__doc__,
    package_dir={'': 'python'},
    packages=['relateiq'],
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
