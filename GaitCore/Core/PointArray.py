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
#     \author    <ajlewis@wpi.edu>
#     \author    Alek Lewis
#     \author    <nagoldfarb@wpi.edu>
#     \author    Nathaniel Goldfarb
#     \version   0.1
# */
# //==============================================================================


import GaitCore.Core.Point as Point
import numpy as np

class PointArray():

    def __init__(self, x: list = [], y: list = [], z: list = []):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def init_point_array(cls):
        """
        Blank init to creat an PointArray object
        :return: PointArray
        """
        return cls(x=[], y=[],z=[])

    @classmethod
    def from_point_array(cls,point_array):
        """

        :param point_array: a list of Point.Point objects
        :return: PointArray
        """
        x = []
        y = []
        z = []
        for p in point_array:
            x.append(p.x)
            y.append(p.y)
            z.append(p.z)
        return cls(x=x, y=y,z=z)

    def append(self,point):
        """

        :param point: Point to append
        :return:
        """
        self._x.append(point.x)
        self._y.append(point.y)
        self._z.append(point.z)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @z.setter
    def z(self, value):
        self._z = value

    def get(self, ind):
        return Point.Point(self.x[ind], self.y[ind], self.z[ind])

    def toarray(self):
        """
        get an numpy as array
        """
        return np.array([self.x,self.y,self.z])
    
    def toPointList(self):
        """
        returns a list of type GaitCore.Core.Point
        """
        l = []
        for i in range(0, len(self._x)):
            l.append(self.get(i))
        return l

    def __add__(self, other):
        """
        over ride to add points
        """
        x = []
        for i in range(len(self.x)):
            x.append(self.x + other.x)

        y = []
        for i in range(len(self.y)):
            x.append(self.y + other.y)

        z = []
        for i in range(len(self.z)):
            x.append(self.z + other.z)

        return PointArray(x, y, z)

    def __sub__(self, other):
        """
        over ride to subtact points
        """
        x = []
        for i in range(len(self.x)):
            x.append(self.x - other.x)

        y = []
        for i in range(len(self.y)):
            x.append(self.y - other.y)

        z = []
        for i in range(len(self.z)):
            x.append(self.z - other.z)

        return PointArray(x, y, z)

    def __mul__(self, other):
        """
        over ride to mul points
        """
        x = []
        for i in range(len(self.x)):
            x.append(self.x * other.x)

        y = []
        for i in range(len(self.y)):
            x.append(self.y * other.y)

        z = []
        for i in range(len(self.z)):
            x.append(self.z * other.z)

        return PointArray(x, y, z)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return " X: " + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z)

    def __getitem__(self, item):

        if isinstance(item, slice):
            return PointArray(self.x[item], self.y[item], self.z[item])
        return Point.Point(self.x[item], self.y[item], self.z[item])

    def __len__(self):
        return len(self._x)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.__len__():
            point = self.get(self.n)
            self.n += 1
            return point
        else:
            raise StopIteration



if __name__ == '__main__':
    p =PointArray.init_point_array()
    p.append(Point.Point(5,5,5))
    p.append(Point.Point(5,5,5))
    print(p[1])