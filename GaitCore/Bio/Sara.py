#!/usr/bin/env python3

import itertools

class Sara:

    def __init__(self, sara_data):

        # Create class-wide variables
        self._data = sara_data
        self.units = ""
        self.x_array = []
        self.y_array = []
        self.z_array = []

        # Analyze the data imported
        
        self._analyze_data()
    
    def _analyze_data(self):

        # Assumption: SARA only outputs X, Y, and Z values

        # Check to make sure all lists are the same size
        if len(self._data.get("X")) != len(self._data.get("Y")) or \
           len(self._data.get("Y")) != len(self._data.get("Z")):
                print("Error in Sara: position variables not the same size")
                # TODO: Throw error

        for (x, y, z) in zip(self._data.get("X", {}).get("data"),
                             self._data.get("Y", {}).get("data"),
                             self._data.get("Z", {}).get("data")):
            self.x_array.append(x)
            self.y_array.append(y)
            self.z_array.append(z)
        
        # Check to make sure all units are the same, and set units
        if self._data.get("X", {}).get('unit') == self._data.get("Y", {}).get('unit') and \
           self._data.get("X", {}).get('unit') == self._data.get("Z", {}).get('unit'):
            self.units = self._data.get("X", {}).get('unit')
        else:
            # TODO: Throw error
            print("Error in Sara: not all units are the same!")

