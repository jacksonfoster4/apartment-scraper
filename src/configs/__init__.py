from apartment_scraper.lib import Config
from apartment_scraper.handlers import Appfolio

class ABetterPropertyConfig(Config):
    handler = Appfolio
    company_name = "A Better Property"
    company_url = "https://www.abetterproperty.com/"
    listings_url = "https://abetterproperty.appfolio.com/listings"

    def filter_price(self, listings, price):
        pass

    def filter_cheap_two_bedroom(self, listings):
        pass

    def filter_one_bedroom(self, listings):
        pass

    def filter_zip_code(self, listings):
        pass

configs = [ABetterPropertyConfig()]
