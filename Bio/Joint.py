
class Joint(object):
    """
    joint class
    """
    def __init__(self, angle, moment, power, force):
        """

        :param angle:
        :param moment:
        :param power:
        :param force:
        """

        self._angle = angle
        self._moment = moment
        self._power = power
        self._force = force

    @property
    def angle(self):
        return self._angle

    @property
    def power(self):
        return self._power

    @property
    def force(self):
        return self._force

    @property
    def moment(self):
        return self._moment

    @angle.setter
    def angle(self, value):
        self._angle = value

    @power.setter
    def power(self, value):
        self._power = value

    @force.setter
    def force(self, value):
        self._force = value

    @moment.setter
    def moment(self, value ):
        self._moment = value

