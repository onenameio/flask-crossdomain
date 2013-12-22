from setuptools import setup

setup(
    name='flask-crossdomain',
    version='0.1',
    description='HTTP Access Control helper.',
    url='http://github.com/iurisilvio/flask-crossdomain',
        
    author='Iuri de Silvio',
    author_email='iurisilvio@gmail.com',
    license='Public Domain',

    py_modules=['flask_crossdomain'],

    install_requires=[
        'Flask'
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
