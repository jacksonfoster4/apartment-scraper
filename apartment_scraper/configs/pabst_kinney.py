from apartment_scraper.lib.config import Config
from apartment_scraper.handlers.appfolio import Appfolio

class PabstKinneyConfig(Config):
    handler = Appfolio
    company_name = "Pabst Kinney"
    company_url = "https://www.pabstkinney.com/"
    listings_url = "https://pabstkinney.appfolio.com/listings"

    def filter_price(self, listings):
        return listings

    def filter_cheap_two_bedroom(self, listings):
        return listings

    def filter_one_bedroom(self, listings):
        return listings

    def filter_zip_code(self, listings):
        return listings
