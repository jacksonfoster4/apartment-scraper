from apartment_scraper.lib import BSHandler

class Appfolio(BSHandler):
    def __init__(self, config):
        super().__init__(config)

    def scrape_listings(self):
        final = []
        for listing in listings:
            l = Listing(listing)

        self.company.listings = final
        return final

    def get_new_listings(self):
        pass






