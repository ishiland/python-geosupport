.. _development:

===========
Development
===========

Running tests
-------------

.. code-block:: sh

    $ python setup.py test

Installing the dev dependencies (nosetests and invoke) will give you more control over running tests. Install in develop mode with dev dependencies with:

.. code-block:: sh

    $ pip install -e .[dev]

And then run tests with:

.. code-block:: sh

    $ invoke test unit
    $ invoke test functional
    $ invoke test all