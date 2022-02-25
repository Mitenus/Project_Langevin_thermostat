# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:49:00 2022

@author: youri
"""

import Langevin_thermostat
import utils
import hypothesis
import numpy as np
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given

@given(natoms=st.integers(1,10000)) 
def test_CheckWall(natoms):
    args = utils.inputParams()
    ndim = 3
    box = args['box']
    positions = np.ones((natoms, ndim))
    velocities = np.random.rand(natoms, ndim)
    afterCheckVelocities = velocities.copy()
    for i in range(ndim):
            positions[:,i] *= box[i][0] + (box[i][1] - box[i][0])
    Langevin_thermostat.CheckWall(positions, afterCheckVelocities, box)
    assert np.array_equal(velocities, -1*afterCheckVelocities)
    