.. _configuration:

=============
Configuration
=============
**Important:** These features are available on Windows only. Linux doesn't support library path modifications during runtime. These configurations override any Geosupport environmental variables.

Geosupport Path
---------------

If you have multiple versions of geosupport and want to switch between them or you simply want to specify the path to Geosupport,
you can pass the installation path to ``Geosupport``:

.. code-block:: python

    from geosupport import Geosupport

    g = Geosupport(geosupport_path="C:\\Program Files\\Geosupport 19B")




Configuration File
------------------

You can also create a configuration file that persists any Geosupport path settings.

Create a `.python-geosupport.cfg` in your home directory that specifies the names and installation paths of your Geosupport versions.

The `.python-geosupport.cfg` file looks like:

.. code-block::

    [versions]
    18b=C:\Program Files\Geosupport Desktop Edition
    18c=C:\Program Files\Geosupport 18C
    18c_32=C:\Program Files (x86)\Geosupport 18C


Then you can select the version by name:

.. code-block:: python

    g = Geosupport(geosupport_version="18c")