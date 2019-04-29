import math
import numpy
import control

class Controller():

    def __init__(self):

        self.C_I = 0

        self.Q_u = numpy.array ([[4,0, 0], [0, 4.5, 0], [0, 0, 2]])
        self.Norm=numpy.array([[2,0,0],[0,0.1,0],[0,0,0.02]])
        self.Q=self.Q_u*self.Norm;

        self.R = numpy.array ([[0.1*0.25]])

    def getControlOutput(self, d_est, phi_est, d_ref, phi_ref, v_ref, t_delay, dt_last):

        #Exception handler for dt_last==0
        if (dt_last==0) : dt_last=0.0001

        err = d_ref - d_est
        self.C_I = self.C_I + dt_last * err

        X = numpy.array ([[d_est], [phi_est], [self.C_I]])

        Ad = numpy.array ([[1, v_ref*dt_last, 0 ], [0, 1, 0],[-dt_last, -0.5*v_ref*dt_last*dt_last, 1]])
        Bd = numpy.array ([[0.5*v_ref*dt_last*dt_last], [dt_last], [-(1/6)*v_ref*dt_last*dt_last*dt_last]])

        (O,L,G) = control.dare(Ad,Bd,self.Q,self.R)

        v_out = 0.8*v_ref
        omega_out = -G.dot(X)
        
        #Adjust speed depending on duckiebot
        return (1.2*v_out, omega_out)
