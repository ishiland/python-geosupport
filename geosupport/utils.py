import sys
from ctypes import cdll

def check_env():

    '''
    Ensures operating system, python environment and Geosupport Desktop are installed, supported and compatible.
    '''

    global platform
    try:
        global lib
        global python_bit
        if sys.maxsize > 2 ** 32:
            python_bit = '64'
        else:
            python_bit = '32'
        if sys.platform == 'win32':
            platform = 'Windows'
            lib = cdll.LoadLibrary("NYCGEO.dll")
        # For future support of Linux
        # elif sys.platform == 'linux' or sys.platform == 'linux2':
        #     platform = 'Linux'
        #     lib = cdll.LoadLibrary("libgeo.so")
        else:
            sys.exit('Sorry, Windows is currently the only platform supported.')
        print('Detected Geosupport Desktop and a {}-bit Python environment on {}.'.format(python_bit, platform))
    except OSError as e:
        sys.exit(
            'There was an error loading the Geosupport Desktop libraries: {}\n\n'
            'You are currently using a {} bit Python executable. Is the configured '
            'version of Geosupport {} bit? They must match.'.format(e, python_bit,
                                                                    python_bit))
