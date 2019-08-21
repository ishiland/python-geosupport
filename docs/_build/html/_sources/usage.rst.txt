.. _usage:

=====
Usage
=====

Basic Usage
-----------


.. code-block:: python

    # Import the library and create a `Geosupport` object.
    from geosupport import Geosupport
    g = Geosupport()

    # Call the address processing function by name
    result = g.address(house_number=125, street_name='Worth St', borough_code='Mn')


``result`` is a dictionary with the output from Geosupport. For example:

.. code-block:: js

    {
        '2010 Census Block': '1012',
        '2010 Census Tract': '31',
        'Assembly District': '65',
        'Atomic Polygon': '112',
        'B10SC - First Borough and Street Code': '14549001010',
        'BOE Preferred B7SC': '14549001',
        'BOE Preferred Street Name': 'WORTH STREET',
        'BOROUGH BLOCK LOT (BBL)': {
            'BOROUGH BLOCK LOT (BBL)': '1001680032',
            'Borough Code': '1',
            'Tax Block': '00168',
            'Tax Lot': '0032'
        },
        'Blockface ID': '0212261942',
        ...
    }


Calling Geosupport Functions
----------------------------
`python-geosupport` is flexible with how you call functions. You can use either Geosupport function codes or human readable alternate names, and access them either through python object attribute notation or dictionary item notation:

.. code-block:: python

    # Different ways of calling function 3S which processes street stretches
    g.street_stretch(...)
    g['street_stretch'](...)
    g['3S'](...)
    g.call({'function': '3S', ...})
    g.call(function='3S', ...)

You can pass arguments as a dictionary, keyword arguments.

.. code-block:: python

    # Use a dictionary with short names
    g.street_stretch({'borough_code': 'MN', 'on': '1 Av', 'from': '1 st', 'to': '2 st'})
    # Use keyword arguments with short names
    g.street_stretch(
        borough_code='MN', street_name_1='1 Av',
        street_name_2='1 st', street_name_3='9 st'
    )
    # Use dictionary with full names
    g.street_stretch({
        'Borough Code-1': 'MN',
        'Street Name-1': '1 Av',
        'Street Name-2': '1 st',
        'Street Name-3': '9 st'
    })


Mode
----
A number of Geosupport functions support several modes: Exetended, Long, and TPAD Long. You can set the flags individually as you would with using Geosupport directly, but python-geosupport makes it easier with the ``mode`` argument. ``mode`` can be one of ``regular`` (default), ``extended``, ``long`` and ``long+tpad``.

.. code-block:: python

    # Call BL (Block and Lot) function in long mode
    g.BL(mode='long', ...)
    g.BL(mode='long+tpad', ...) # With TPAD

    # Call 3 (Street Segment) function in extended mode
    g.street_segment(mode='extended', ...)