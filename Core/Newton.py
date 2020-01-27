class Newton(object):

    def __init__(self, angle, force, moment, power):
        self._angle = angle
        self._force = force
        self._moment = moment
        self._power = power

    @property
    def angle(self):
        return self._angle

    @property
    def force(self):
        return self._force

    @property
    def moment(self):
        return self._moment

    @property
    def power(self):
        return self._power

    # @angle.setter
    # def angle(self, value):
    #     self._angle = value
    #
    # @force.setter
    # def force(self, value):
    #     self._force = value
    #
    # @moment.setter
    # def moment(self, value):
    #     self._moment = value
    #
    # @power.setter
    # def power(self, value):
    #     self._power = value
