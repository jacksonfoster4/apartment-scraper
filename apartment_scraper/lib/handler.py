import csv
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from apartment_scraper.lib.company import Company


class Handler(ABC):
    def __init__(self, config):
        self.config = config
        self.company = Company(config=config)
        self.soup = None

    @property
    @abstractmethod
    def load_site(self):
        return 'load site'

    @property
    @abstractmethod
    def scrape_listings(self):
        return 'scrape_listings'

    def get_new_listings(self, listings_csv):
        reader = csv.DictReader(listings_csv)
        addresses = list(map( lambda listing: listing, self.company.listings))

        for r in reader:
            if r['address'] in addresses:
                addresses.remove(reader['address'])

        addresses = list(filter(lambda listing: listing.address in addresses, self.company.listings))
        return addresses

    def get_csv_name(self):
        csv_name = self.config.company_name.lower().replace(" ", "-")
        csv_name = f"{csv_name}-listings.csv"
        return csv_name

    def get_csv(self):
        csv_name = self.get_csv_name()
        try:
            csv_file = open(csv_name, 'r')
            return csv_file
        except FileNotFoundError:
            return self.write_csv(self.company.listings, return_as='r')
    
    def write_csv(self, listings, return_as='close'):
        header = ['address', 'price', 'beds', 'square_footage', 'available', 'link', 'image_url' ]
        f = open(self.get_csv_name(), 'w')
        writer = csv.writer(f)
        writer.writerow(header)

        for listing in listings:
            row = []
            for el in header:
                row.append(getattr(listing, el))
            writer.writerow(row) 

        if return_as == 'close':
            f.close()
            return

        if return_as == 'r':
            f.close()
            f = open(self.get_csv_name(), 'r')
        
        

    def run(self):
        self.load_site()

        self.company.listings = self.scrape_listings()

        listings_csv = self.get_csv()
        new_listings = self.get_new_listings(listings_csv)
        new_listings = self.config.apply_filters(new_listings)

        if new_listings:
            self.company.new_listings = new_listings

        self.write_csv(self.company.listings)

        return self.company


class BSHandler(Handler):
    def __init__(self, config):
        super().__init__(config)

    def load_site(self):
        crawled = requests.get(self.config.listings_url)
        soup = BeautifulSoup(crawled.text, 'lxml')
        self.soup = soup

class WebDriverHandler(Handler):
    def __init__(self, config):
        super().__init__(config)

    def load_site(self):
        # load site with webdriver
        pass
