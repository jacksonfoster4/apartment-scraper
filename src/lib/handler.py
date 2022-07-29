from abc import ABC

class Handler(ABC):
    def __init__(self, config):
        self.config = config
        self.company = Company(**config.__dict__)
        self.site = None

    @abc.abstractproperty
    def load_site(self):
        return 'load site'

    @abc.abstractproperty
    def scrape_listings(self):
        return 'scrape_listings'

    @abc.abstractproperty
    def get_new_listings(self):
        return 'get_new_listings'

    def get_csv(self):
        # load csv
        pass

    def run(self):
        self.load_site()

        self.company.listings = self.scrape_listings()

        listings_csv = self.get_csv()
        new_listings = self.get_new_listings(listings_csv)
        new_listings = self.config.apply_filters(new_listings)

        if new_listings:
            self.company.new_listings = new_listings

        return self.company


class BSHandler(Handler):
    def __init__(self, config):
        super().__init__(config)

    def load_site(self):
        # load site with beatufiul soup
        pass

class WebDriverHandler(Handler):
    def __init__(self, config):
        super().__init__(config)

    def load_site(self):
        # load site with webdriver
        pass
