"""
Virus Simulation.

Usage:
    virus_simulator 
    virus_simulator run
    virus_simulator -h | --help
    virus_simulator --version

Options:
    -h --help   Shows this screen.
    --version   Shows version.

"""

import threading


def run_server():
    import os
    os.system('python api run')


if __name__ == '__main__':

    import virus_simulator
    from docopt import docopt
    from threading import Thread

    arguments = docopt(__doc__, version='Virus Simulation v.1.0.')

    if arguments['run']:

        try: 
            api_process = Thread(target = run_server)
            app = virus_simulator.App()

            api_process.start()
            app.run()
            api_process.join()

        except KeyboardInterrupt:
            print("Exit.")

