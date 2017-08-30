# Custom composite types
# All types must contain the __composite_values__ method

class Coordinates(object):
    """Geographic coordinates"""
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return f"Coordinates(longitude={self.longitude}, latitude={self.latitude})"

    def __eq__(self, other):
        return isinstance(other, Coordinates) \
           and self.longitude == other.longitude \
           and self.latitude == other.latitude

    def __composite_values__(self):
        return self.longitude, self.latitude