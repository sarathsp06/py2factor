import pickle
import logging
from os import  path 

class Store(object):
    log = logging.getLogger(__name__)
    db = path.expanduser("~/.py2factor_profiles.db")
    def __init__(self): 
        self.profiles = dict()
        super(Store, self).__init__()

    def read_profiles(self):
        try:
            self.profiles  = pickle.load(open(self.db))
        except:
            self.log.debug("Error reading profiles")
            pass
        return self.profiles

    def store_profiles(self):
        pickle.dump(self.profiles,open(self.db,'w+'))

    def add_profile(self,profile):
        if profile.name is None or profile.name == "":
            raise ValueError("Profile without name wont be stored")
        self.log.info("adding profile %s:%s",profile.name,profile)
        self.read_profiles()
        self.profiles[profile.name] = profile
        self.store_profiles()

    def remove_profile(self,name):
        self.read_profiles()
        del(self.profiles[name])
        self.store_profiles()