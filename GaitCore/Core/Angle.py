#!/usr/bin/env python3
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
#     \author    <alextac98@gmail.com>
#     \author    Alex Tacescu
#     \version   0.1
# */
# //==============================================================================

class Angle():
    """
    Angle class
    """

    def __init__(self, angle_data: dict = None):
        
        self._rx = angle_data.get('RX', {}).get('data', [])
        self._ry = angle_data.get('RY', {}).get('data', [])
        self._rz = angle_data.get('RZ', {}).get('data', [])

        self._tx = angle_data.get('TX', {}).get('data', [])
        self._ty = angle_data.get('TY', {}).get('data', [])
        self._tz = angle_data.get('TZ', {}).get('data', [])

        # Set rotational units
        rot_units =    [angle_data.get('RX', {}).get('unit'),
                        angle_data.get('RY', {}).get('unit'),
                        angle_data.get('RZ', {}).get('unit')]

        if not self.check_units(unit_list=rot_units):
            # TODO: Throw error
            print("Units not the same")
            self._rot_unit = "units_not_same"
        else:
            self._rot_unit = rot_units[0]

        # Set translational units
        trans_units =  [angle_data.get('TX', {}).get('unit'),
                        angle_data.get('TY', {}).get('unit'),
                        angle_data.get('TZ', {}).get('unit')]

        if not self.check_units(unit_list=trans_units):
            # TODO: Throw error
            print("Units not the same")
            self._trans_unit = "units_not_same"
        else:
            self._trans_unit = trans_units[0]

    @property
    def rot_unit(self):
        return self._rot_unit

    @property
    def trans_unit(self):
        return self._trans_unit

    @property
    def rx(self):
        return self._rx

    @property
    def ry(self):
        return self._ry

    @property
    def rz(self):
        return self._rz

    @property
    def tx(self):
        return self._tx

    @property
    def ty(self):
        return self._ty

    @property
    def tz(self):
        return self._tz

    def check_units(self, unit_list:list):
        unit_tmp = unit_list[0]
        for unit in unit_list:
            if unit != unit_tmp:
                # TODO: Throw error
                return False

        return True