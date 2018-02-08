import logging

from cliff.lister import Lister
from .store import Store
from cliff.show import ShowOne

class Delete(ShowOne):
    """ Lists all profiles and its totp """
    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Delete, self).get_parser(prog_name)
        parser.add_argument('--name', dest = "name", default='',help="Account name")
        return parser

    def take_action(self, parsed_args):
        profiles = Store().read_profiles()
        profile = profiles.get(parsed_args.name,None)
        if profile is None:
            self.app.stderr.write("No profile found for name:" + parsed_args.name)
            return
        Store().remove_profile(parsed_args.name)
        p = profile
        titles = ('name','issuer','algorithm','digits','period','secret','url')
        profile_tuple = (p.name,p.issuer,p.algorithm,p.digits,p.period,p.secret,p.url)
        return (titles,profile)