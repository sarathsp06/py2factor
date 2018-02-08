#!/usr/bin/env python

import sys

import pickle
from cliff.app import App
from cliff.commandmanager import CommandManager

VERSION  = "0.1.1"

class Py2Factor(App):
    def __init__(self): 
        self.profiles = dict()
        super(Py2Factor, self).__init__(
            description='python 2 factor auth commandline application',
            version=VERSION,
            command_manager=CommandManager('py2factor.commands'),
            deferred_help=True,
            )
    def initialize_app(self, argv):
        self.LOG.debug('initializing application')

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err is not None:
            self.LOG.debug('got an error: %s', err)

def main(argv=sys.argv[1:]):
    py2factor = Py2Factor()
    return py2factor.run(argv)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))