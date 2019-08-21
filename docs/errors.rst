.. _errors:

==============
Error Handling
==============

`python-geosupport` will raise a ``GeosupportError`` when Geosupport returns an error code. Sometimes there is more information returned, in which case the exception will have a result dictionary.

.. code-block:: python

    from geosupport import GeosupportError

    try:
        g.get_street_code(borough='MN', street='Wort Street')
    except GeosupportError as e:
        print(e) # 'WORT STREET' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.
