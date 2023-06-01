class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "_name"):
            self._name = name
        else:
            raise AttributeError
        
    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.national_park is self]
        
    
    def visitors(self):
        from classes.trip import Trip
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        return max(self.visitors(), key=lambda visitor: visitor.name)
            