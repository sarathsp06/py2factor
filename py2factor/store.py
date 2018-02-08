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
        self.log.info("Reading profiles")
        try:
            self.profiles  = pickle.load(open(self.db))
        except:
            self.log.debug("Error reading profiles")
            pass
        return self.profiles

    def store_profiles(self):
        self.log.info("storing profiles %s",repr(self.profiles))
        pickle.dump(self.profiles,open(self.db,'w+'))

    def add_profile(self,name,profile):
        self.log.info("storing profiles %s:%s",name,profile)
        self.read_profiles()
        self.profiles[name] = profile
        self.store_profiles()