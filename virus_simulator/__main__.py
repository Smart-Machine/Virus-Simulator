"""
Virus Simulation.

Usage:
    virus_simulator.py 
    virus_simulator.py run
    virus_simulator.py debug
    virus_simulator.py -h | --help
    virus_simulator.py --version

Options:
    -h --help   Shows this screen.
    --version   Shows version.

"""

def run_server():
    import os
    os.system('python api')


if __name__ == '__main__':

    import virus_simulator
    from docopt import docopt
    from threading import Thread

    arguments = docopt(__doc__, version='Virus Simulation v.1.0.')

    if arguments['run']:
        api_process = Thread(target = run_server)
        app = virus_simulator.App()

        api_process.start()
        app.run()
        api_process.join()
    
    if arguments['debug']:
        #run in debug mode
        pass 


    # if arguments['']:
    #     ...
