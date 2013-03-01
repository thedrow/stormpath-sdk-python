__author__ = 'ecrisostomo'

from distutils.core import setup

from stormpath import __version__


# To install the stormpath library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
REQUIRES = ["httplib2 (>= 0.7)", "unittest2py3k"]

setup(
    name = "stormpath",
    version = __version__,
    description = "Stormpath SDK used to interact with the Stormpath REST API",
    author = "Elder Crisostomo",
    author_email = "elder@stormpath.com",
    url = "https://github.com/stormpath/stormpath-sdk-python",
    keywords = ["stormpath","authentication"],
    requires = REQUIRES,
    packages = ['stormpath'],
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
        "Programming Language :: Python :: 3.2",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        ],
    long_description = """\
    Stormpath SDK
    -------------

    DESCRIPTION
    The Stormpath Python SDK allows any Python-based application to easily use the
    Stormpath user management service for all authentication and access control needs.

    When you make SDK method calls, the calls are translated into HTTPS requests to
    the Stormpath REST+JSON API. The Stormpath Python SDK therefore provides a clean
    object-oriented paradigm natural to Python developers and alleviates the need to
    know how to make REST+JSON requests.

    LICENSE The Hello World Library is distributed under the Apache Software License.
    """ )