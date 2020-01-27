
class Data(object):
    """
    Call to hold data with a time sequence
    """
    def __init__(self,data, time):
        """
        :param data: array of data
        :param time: array of time
        """
        self._data = data
        self._time = time

    @property
    def data(self):
        """
        get the data
        """
        return self._data

    @property
    def time(self):
        """
        get the time
        """
        return self._time


    # @data.setter
    # def data(self, value):
    #     """
    #     get the data
    #     """
    #     self._data = value
    #
    # @time.setter
    # def time(self, value):
    #     """
    #     get the time
    #     """
    #     self._time = value
