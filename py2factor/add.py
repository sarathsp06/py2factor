import logging

from cliff.command import Command
from .store import Store

class Add(Command):
    """ Adds a profile given name and key in base32 encoding """
    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Add, self).get_parser(prog_name)
        parser.add_argument('--name', dest = "name", default='',help="Account name")
        parser.add_argument('--key', dest = "key", default='',help="Auth key")
        return parser

    def take_action(self, parsed_args):
        self.log.debug("Stroring profile %s:%s",parsed_args.name,parsed_args.key)
        Store().add_profile(parsed_args.name,parsed_args.key)