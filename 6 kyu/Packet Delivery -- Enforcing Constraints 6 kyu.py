class Package(object):
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.volume = self.length * self.width * self.height

    def __setattr__(self, key, value):
        if key == 'length':
            if value < 0 or value > 350:
                raise DimensionsOutOfBoundError(key, value)
        if key == 'width':
            if value < 0 or value > 300:
                raise DimensionsOutOfBoundError(key, value)
        if key == 'height':
            if value < 0 or value > 150:
                raise DimensionsOutOfBoundError(key, value)
        if key == 'weight':
            if value < 0 or value > 40:
                raise DimensionsOutOfBoundError(key, value)
        self.__dict__[key] = value
        if len(self.__dict__) > 3:
            self.__dict__['volume'] = self.__dict__['length'] * self.__dict__['width'] * self.__dict__['height']


class DimensionsOutOfBoundError(Exception):
    def __init__(self, name, variable):
        self.name = name
        self.variable = variable

    def __str__(self):
        if self.name == 'length':
            bounds = '0 < length <= 350'
        elif self.name == 'width':
            bounds = '0 < width <= 300'
        elif self.name == 'height':
            bounds = '0 < height <= 150'
        else:
            bounds = '0 < weight <= 40'
        return f"Package {self.name}=={self.variable} out of bounds, should be: {bounds}"
