from apartment_scraper.configs import configs 


def main(*args, **kwargs):
    results = []
    for config in configs:
        handler = config.load_handler()
        company = handler.run()
        if company.new_listings:
            results.push(company)
        else:
            print('no new results')

    if results:
        return send_results(results)

if __name__ == "__main__":
    main()


# load Config
#   includes company name, target url, website url
# pass config to handler
# handler.get_listings() will return company with listings and new listings
# if company.new_listings:
#
