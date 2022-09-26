# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):

        # Those parameters will be used a lot of times
        self.dt = params.dt
        self.q = params.q
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        return np.matrix([[1, 0, 0, self.dt, 0, 0],
                        [0, 1, 0, 0, self.dt, 0],
                        [0, 0, 1, 0, 0, self.dt],
                        [0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1]])
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        q_1 = self.dt * self.q
        q_2 = (self.dt**2 / 2) * self.q
        q_3 = (self.dt**3 / 3) * self.q
        return np.matrix([[q_3,  0,  0, q_2,  0,  0],
                          [0,  q_3,  0,  0, q_2,  0],
                          [0,   0, q_3,  0,  0, q_2],
                          [q_2,  0,  0, q_1,  0,  0],
                          [0,  q_2,  0,  0, q_1,  0],
                          [0,   0, q_2,  0,  0, q_1]])
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        track.x = self.F() * track.x # state prediction

        track.P = self.F() * track.P * self.F().transpose() + self.Q() # covariance prediction

        track.set_x(track.x)
        track.set_P(track.P)
        return track.x, track.P
        ############
        # END student code
        ############

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        # Update function 
        S = self.S(track, meas, None)
        H = meas.sensor.get_H(track.x) # Jacobian
        K = track.P * H.transpose() * np.linalg.inv(S) # Kalman Gain
        x = track.x + K * self.gamma(track, meas) # State update
        I = np.identity(params.dim_state)
        P = (I - K * H) * track.P # covariance update

        track.set_x(x)
        track.set_P(P)

        ############
        # END student code
        ############ 
        track.update_attributes(meas)

    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        gamma_res = meas.z - meas.sensor.get_hx(track.x)
        return gamma_res
        ############
        # END student code
        ############

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############
        H = meas.sensor.get_H((track.x))
        S = (H * track.P * H.transpose()) + meas.R # covariance of residual
        return S
        ############
        # END student code
        ############