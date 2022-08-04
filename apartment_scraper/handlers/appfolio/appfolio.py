from email.mime import image
from urllib.parse import urlparse, urljoin
from apartment_scraper.lib.handler import BSHandler
from apartment_scraper.lib.listing import Listing

class Appfolio(BSHandler):
    def __init__(self, config):
        super().__init__(config)

    def label_to_value(self, labels, target):
        final = list(filter(lambda label: label.text == target, labels ))
        if len(final):
            return final[0].find_next_sibling().text
        
    def make_absolute(self, path):
        return urljoin(self.config.listings_url, path)

    def scrape_listings(self):
        final = []
        listings = self.soup.find_all('div', class_="listing-item")
        import pdb
        for listing in listings:
            # get detail box where text == 'RENT'
            # find sibling element which == rent
            labels = listing.find_all("dt", class_="detail-box__label")
            price = self.label_to_value(labels, 'RENT')
            beds = self.label_to_value(labels, 'Bed / Bath')
            square_footage = self.label_to_value(labels, 'Square Feet')
            available = self.label_to_value(labels, 'Available')
            address = listing.find("span", class_="js-listing-address").text
            link = self.make_absolute(self.soup.find("a", class_="js-link-to-detail")['href'])
            image_url = listing.find('img', class_="listing-item__image")['src']

            listing = Listing(
                price=price,
                square_footage=square_footage,
                beds=beds,
                available=available,
                address=address,
                link=link,
                image_url=image_url
            )


            final.append(listing)

        return final





