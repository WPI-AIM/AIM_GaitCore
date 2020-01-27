
class Joint(object):
    """
    joint class
    """
    def __init__(self, angle, moment, power, force):
        """
        Holds the joint data form the model output
        :param angle: angles
        :param moment: moments
        :param power: power
        :param force: forces
        """

        self._angle = angle
        self._moment = moment
        self._power = power
        self._force = force

    @property
    def angle(self):
        """
        get the angles for the joint
        """
        return self._angle

    @property
    def power(self):
        """
        get the power of the joint
        """
        return self._power

    @property
    def force(self):
        """
        get the forces of the joint
        """
        return self._force

    @property
    def moment(self):
        """
        get the moment of the joint
        """
        return self._moment

    # @angle.setter
    # def angle(self, value):
    #     self._angle = value
    #
    # @power.setter
    # def power(self, value):
    #     self._power = value
    #
    # @force.setter
    # def force(self, value):
    #     self._force = value
    #
    # @moment.setter
    # def moment(self, value ):
    #     self._moment = value

