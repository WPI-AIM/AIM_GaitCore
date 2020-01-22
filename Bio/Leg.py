class Leg():

    def __init__(self, hip, knee, ankle):

        self._hip = hip
        self._knee = knee
        self._ankle = ankle

    @property
    def hip(self):
        return self._hip

    @property
    def knee(self):
        return self._knee

    @property
    def ankle(self):
        return self._ankle

    @hip.setter
    def hip(self, value):
        self._hip = value

    @knee.setter
    def knee(self, value):
        self._knee = value

    @knee.setter
    def ankle(self, value):
        self._ankle = value
