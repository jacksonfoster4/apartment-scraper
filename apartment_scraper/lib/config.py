import abc

class Config:
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def handler(self):
        return 'handler'

    @abc.abstractproperty
    def company_name(self):
        return 'company name'

    @abc.abstractproperty
    def company_url(self):
        return 'company url'

    @abc.abstractproperty
    def listings_url(self):
        return 'listings url'

    def load_handler(self):
        return self.handler(self)

    def load_filters(self):
        filters = []
        for name in dir(self):
            if name.startswith("filter_"):
               _filter = getattr(self, name)
               filters.append(_filter)
        return filters

    def apply_filters(self, listings):
        filters = self.load_filters()
        filtered_listings = set(listings)
        for _filter in filters:
            filtered = _filter(listings)
            if len(filtered):
                for el in filtered:
                    filtered_listings.add(el)

        return filtered_listings
