"""
MongoEngine-Pagination
--------------

Basic Pagination for MongoEngine.

Shamelessly based on Flask-MongoEngine by Dan Jacob http://bitbucket.org/danjac/flask-mongoengine

Links
`````

* `development version
  <https://github.com/mechanicalchopsticks/MongoEngine-Pagination/raw/master#egg=Flask-MongoEngine-dev>`_


"""
from setuptools import setup


setup(
    name='MongoEnginePagination',
    version='0.1',
    url='https://github.com/mechanicalchopsticks/MongoEngine-Pagination',
    license='BSD',
    author='Juan Barrientos',
    author_email='mechanicalchopsticks@gmail.com',
    description='Pagination support for MongoEngine',
    long_description=__doc__,
    packages=['mongoenginepagination'],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'mongoengine',
    ],
    tests_require=[
        'nose',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

