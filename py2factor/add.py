import logging

from cliff.command import Command
from .store import Store
from .profile import Profile 

class Add(Command):
    """ Adds a profile given name and key in base32 encoding """
    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Add, self).get_parser(prog_name)
        parser.add_argument('--name', dest = "name", default='',help="Account name")
        parser.add_argument('--key', dest = "key", default='',help="Auth key")
        parser.add_argument('--url', dest = "url", default='',help="Totp secret url")
        return parser

    def take_action(self, parsed_args):
        self.log.debug("Stroring profile %s:%s:%s",parsed_args.name,parsed_args.key,parsed_args.url)
        if parsed_args.url is not None and parsed_args.url != "":
            try:
                profile = Profile(url=parsed_args.url)
                Store().add_profile(profile)
                self.app.stdout.write("Successfully added profile\n")
                return
            except Exception as e:
                self.app.stderr.write("Failed adding :" + str(e))
                return

        if parsed_args.name  == "" or  parsed_args.key == "":
            self.app.stderr.write("Mandatry parameters missing name and key or url is mandatory")
        try:
            profile = Profile(name=parsed_args.name,secret=parsed_args.key)
            Store().add_profile(profile)
            self.app.stdout.write("Successfully added profile")
        except Exception,e:
            self.app.stderr.write("Failed adding :" + str(e)) 