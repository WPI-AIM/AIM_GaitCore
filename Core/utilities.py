import numpy as np


def smooth(y, box_pts=10):
    """
    smooth data using a running average
    """
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth