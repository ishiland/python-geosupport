import os


def build_win_dll_path(geosupport_path=None, dll_filename='nycgeo.dll'):
    """"
    Windows specific function to return full path of the nycgeo.dll
    example: 'C:\\Program Files\\Geosupport Desktop Edition\\Bin\\NYCGEO.dll'
    """
    # return the provided geosupport path with the proper suffix pointing to the dll
    if geosupport_path:
        return os.path.join(geosupport_path, 'bin', dll_filename)
    # otherwise try to find the nycgeo.dll from system path entries
    system_path_entries = os.environ['PATH'].split(';')
    # look for directories ending with 'bin' since this is where the nycgeo.dll is stored
    bin_directories = [b for b in system_path_entries if b.endswith('bin')]
    # scan the bin directories for the nycgeo.dll, returning first occurrence.
    for b in bin_directories:
        file_names = [fn for fn in os.listdir(b)]
        for file in file_names:
            if file.lower() == dll_filename.lower():
                return os.path.join(b, file)
    raise Exception(
        "Unable to locate the {0} within your system. Ensure the Geosupport 'bin' directory is in your system path.".format(
            dll_filename))
