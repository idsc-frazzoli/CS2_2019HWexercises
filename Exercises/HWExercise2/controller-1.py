import math
import numpy as np
import rospy

class Controller():

    def __init__(self):
        self.v_ref = 0.22

    def getControlOutput(self, rho, theta, psi, t_delay, dt_last):
        if rho < 0.4:
            v_out = 0.0
            omega_out = 0.0
        else:
            v_out = self.v_ref
            omega_out = - 2 * theta
        
        return (v_out, omega_out)