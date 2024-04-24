# A class for tracking a data point (tuple) and its associated distance
class DataPoint:
    # A constructor that receives the tuple and distance and stores them
    def __init__(self, tuple, distance):
        self.tuple = tuple
        self.distance = distance