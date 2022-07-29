from apartment_scraper.lib import Config
from apartment_scraper.handlers import Appfolio

class ABetterPropertyConfig(Config):
    handler = Appfolio
    company_name = "A Better Property"
    company_url = "https://www.abetterproperty.com/"
    listing_url = "https://abetterproperty.appfolio.com/listings"
