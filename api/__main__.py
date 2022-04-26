"""
Virus Simulation API.

Usage:
    api 
    api run 
    api -h | --help
    api --version

Options:
    -h --help   Shows this screen.
    --version   Shows version.

"""


if __name__ == '__main__':
    
    import os
    from docopt import docopt

    arguments = docopt(__doc__, version='Virus Simulation API v.1.0.')

    if arguments['run']:

        try: 
            os.system('cd api && python -m flask run --host=0.0.0.0')

        except KeyboardInterrupt:
            print('Exit.')