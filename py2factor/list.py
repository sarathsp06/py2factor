import logging

from cliff.lister import Lister
from .store import Store
from .totp import get_totp_token

class List(Lister):
    """ Lists all profiles and its totp """
    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(List, self).get_parser(prog_name)
        parser.add_argument('--filter', dest = "filter", default='',help="Account name")
        return parser

    def take_action(self, parsed_args):
        profiles = Store().read_profiles()
        return (("Name","Token"),
        	((key,"{0:03d}".format(profiles[key].totp())) for key in profiles.keys() if key.startswith(parsed_args.filter)))