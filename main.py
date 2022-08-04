from apartment_scraper.configs import configs 
from apartment_scraper.lib.send_results import send_results


def main(*args, **kwargs):
    results = []
    for config in configs:
        handler = config.load_handler()
        company = handler.run()
        if company.new_listings:
            results.append(company)
        else:
            print('no new results')

    if results:
        for company in results:
            for l in company.new_listings:
                print(f"{company.name}: {l.address}-{l.price}")

        return send_results(results)

if __name__ == "__main__":
    main()


# load Config
#   includes company name, target url, website url
# pass config to handler
# handler.get_listings() will return company with listings and new listings
# if company.new_listings:
#
