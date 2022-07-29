from .config import Config

class Company:
    def __init__(self, config):
        self.name = config.company_name
        self.listings = []
        self.new_listings = []
    
    def get_listings(self):
        self.listings = config.get_listings()
        return self.listings

    def check_for_new_listings(self):
        pass


