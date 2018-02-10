import logging

from cliff.lister import Lister
from .store import Store
from .totp import get_totp_token

class Profiles(Lister):
    """ Lists all profiles with its details """
    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Profiles, self).get_parser(prog_name)
        parser.add_argument('--filter', dest = "filter", default='',help="Account name")
        return parser

    def take_action(self, parsed_args):
        profiles = Store().read_profiles()
        titles = ('name','issuer','algorithm','digits','period','secret','url')
        profiles_list = ((p.name,p.issuer,p.algorithm,p.digits,p.period,p.secret,p.url) 
            for p in profiles.values() if p.name.startswith(parsed_args.filter))
        return (titles,profiles_list)