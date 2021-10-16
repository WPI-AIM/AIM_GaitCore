#!/usr/bin/env python
# //==============================================================================
# /*
#     Software License Agreement (BSD License)
#     Copyright (c) 2020, AIMGaitCore
#     (www.aimlab.wpi.edu)

#     All rights reserved.

#     Redistribution and use in source and binary forms, with or without
#     modification, are permitted provided that the following conditions
#     are met:

#     * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.

#     * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.

#     * Neither the name of authors nor the names of its contributors may
#     be used to endorse or promote products derived from this software
#     without specific prior written permission.

#     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#     "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#     LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#     FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#     COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#     INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#     BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#     LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#     CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#     LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#     ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#     POSSIBILITY OF SUCH DAMAGE.

#     \author    <http://www.aimlab.wpi.edu>
#     \author    <nagoldfarb@wpi.edu>
#     \author    Nathaniel Goldfarb
#     \version   0.1
# */
# //==============================================================================

from GaitCore.Bio.Sara import Sara
from GaitCore.Bio.Score import Score
from GaitCore.Core.Angle import Angle


class Joint():
    """
    joint class
    """
    def __init__(self, name: str, angle_data=None, moment = None, power = None, force = None):
        """
        Holds the joint data form the model output
        :param angle: angles
        :param moment: moments
        :param power: power
        :param force: forces
        """

        self._name = name
        self._angle = angle_data
        self._moment = moment
        self._power = power
        self._force = force

        self._sara = None
        self._score = None

    @property
    def name(self):
        """
        Returns:
            str: Name of the joint
        """
        return self._name

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

    @moment.setter
    def moment(self, data: list):
        self._moment = data

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score_obj: Score):
        self._score = score_obj

    @property
    def sara(self):
        return self._sara

    @sara.setter
    def sara(self, sara_obj: Sara):
        self._sara = sara_obj