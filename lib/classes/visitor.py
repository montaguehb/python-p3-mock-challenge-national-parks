class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        from classes.trip import Trip
        return list({trip.national_park for trip in self.trips()})

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15 and not hasattr(self, "_name"):
            self._name = name
        else:
            raise AttributeError