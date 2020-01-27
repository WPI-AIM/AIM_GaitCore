
class Leg(object):
    """
    Hold the joints of a leg
    """
    def __init__(self, hip, knee, ankle):
        """
        :param hip: hip joint
        :param knee: knee joint
        :param ankle: ankle joint
        """
        self._hip = hip
        self._knee = knee
        self._ankle = ankle

    @property
    def hip(self):
        """
        Get the hip joint
        """
        return self._hip

    @property
    def knee(self):
        """
        get the knee joint
        """
        return self._knee

    @property
    def ankle(self):
        """
        Get the ankle joint
        """
        return self._ankle

    # @hip.setter
    # def hip(self, value):
    #     self._hip = value
    #
    # @knee.setter
    # def knee(self, value):
    #     self._knee = value
    #
    # @knee.setter
    # def ankle(self, value):
    #     self._ankle = value
