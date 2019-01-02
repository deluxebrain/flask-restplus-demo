from setuptools import setup, find_packages

setup(
    name='flask-restplus-demo',
    version='1.0.0',
    description='Flask-RESTPlus demo',
    url='',
    author='Matt Caton',

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python 3',
        'Programming Language :: Python 3.6',
    ],

    keywords='rest api flask swagger openapi flask-restplus',

    packages=find_packages(),

    install_requires=[
        'flask~=1.0.2',
        'flask-restplus~=0.12.1',
        'python-dotenv~=0.9.1',
        'flask-marshmallow~=0.9.0'
    ],
)

