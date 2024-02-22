class College:
    def __init__(self, college_name, college_abbreviation):
        self._college_name = college_name
        self._college_abbreviation = college_abbreviation
        self._points = 0.0
        self._matches = None

    @property
    def name(self):
        return self._college_name
    
    @property
    def abbreviation(self):
        return self._college_abbreviation
    
    @property
    def points(self):
        return self._points
    
    def add_points(self, points):
        self._points += points
    
