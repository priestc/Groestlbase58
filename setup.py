from setuptools import setup, find_packages

setup(
    name='groestlbase58',
    py_modules=['groestlbase58'],
    #packages=find_packages(),
    version='0.2.5',
    description='Base58 and Base58Check implementation with Groestl hashing',
    author='Chris Priest',
    author_email='cp368202@ohiou.edu',
    url='https://github.com/priestc/Groestlbase58',
    license='MIT',
    entry_points={
        'console_scripts': [
            'groestlbase58 = groestlbase58:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
    dependency_links=['git+https://github.com/groestlcoin/groestlcoin-hash-python#egg=groestlcoin_hash'],
)
