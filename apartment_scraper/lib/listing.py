class Listing:
    def __init__(self, *args, **kwargs):
        self.price = kwargs.get('price')
        self.beds = kwargs.get('beds') 
        self.square_footage = kwargs.get('square_footage')
        self.available = kwargs.get('available')
        self.address = kwargs.get('address')
        self.link = kwargs.get('link') 
        self.image_url = kwargs.get('image_url') 
