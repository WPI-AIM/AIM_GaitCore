class Data(object):

    def __init__(self,data, time):
        self._data = data
        self._time = time

    @property
    def data(self):
        return self._data

    @property
    def time(self):
        return self._time

    @data.setter
    def data(self, value):
        self._data = value

    def time(self, value):
        self._time = value