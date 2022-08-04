from apartment_scraper.lib.config import Config
from apartment_scraper.handlers.appfolio import Appfolio

class ABetterPropertyConfig(Config):
    handler = Appfolio
    company_name = "A Better Property"
    company_url = "https://www.abetterproperty.com/"
    listings_url = "https://abetterproperty.appfolio.com/listings"

    def filter_price(self, listings):
        return listings

    def filter_cheap_two_bedroom(self, listings):
        return listings

    def filter_one_bedroom(self, listings):
        return listings

    def filter_zip_code(self, listings):
        return listings
