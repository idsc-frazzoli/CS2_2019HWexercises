import math
import numpy as np
import rospy

class Controller():

    def __init__(self):
        self.v_ref = 0.22
	self.rho_ref = 0.1

    def getControlOutput(self, rho, theta, psi, t_delay, dt_last):
        v_out = self.v_ref*(rho-self.rho_ref)*5
        omega_out = -5 * theta
        
        #TODO: Implement your own follow-the-leader controller
        
        return (v_out, omega_out)
