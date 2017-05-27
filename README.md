# Groestlbase58

[![PyPI Version][pypi-image]](https://pypi.python.org/pypi?name=Groestlbase58&:action=display)
[![PyPI Downloads][pypi-downloads-image]](https://pypi.python.org/pypi?name=Groestlbase58&:action=display)

Base58 and Base58Check implementation compatible with what is used by the
Groestlcoin network.


## Command line usage

    $ printf "hello world" | groestlbase58
    StV1DL6CwTryKyV

    $ printf "hello world" | groestlbase58 -c
    3vQB7B6MrGQZaxCuFg4oh

    $ printf "3vQB7B6MrGQZaxCuFg4oh" | groestlbase58 -dc
    hello world

    $ printf "4vQB7B6MrGQZaxCuFg4oh" | groestlbase58 -dc
    Invalid checksum


## Module usage

    >>> import Groestlbase58
    >>> Groestlbase58.b58encode(b'hello world')
    'StV1DL6CwTryKyV'
    >>> Groestlbase58.b58decode(b'StV1DL6CwTryKyV')
    b'hello world'
    >>> Groestlbase58.b58encode_check(b'hello world')
    '3vQB7B6MrGQZaxCuFg4oh'
    >>> Groestlbase58.b58decode_check(b'3vQB7B6MrGQZaxCuFg4oh')
    b'hello world'
    >>> Groestlbase58.b58decode_check(b'4vQB7B6MrGQZaxCuFg4oh')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "base58.py", line 89, in b58decode_check
        raise ValueError("Invalid checksum")
    ValueError: Invalid checksum


[pypi-image]: https://img.shields.io/pypi/v/base58.svg?style=flat
[pypi-downloads-image]: https://img.shields.io/pypi/dm/base58.svg?style=flat
[travis-image]: https://img.shields.io/travis/keis/base58.svg?style=flat
[coveralls-image]: https://img.shields.io/coveralls/keis/base58.svg?style=flat
