from random import seed, gauss, randrange
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

def calc_pitch(dist, cat):
    h = math.sqrt(math.pow(cat,2)+math.pow(dist,2))
    dpitch = 90 - math.asin(dist/h)*(180/math.pi)
    pitch = (math.pi/2) - math.asin(dist/h)
    print("distance to difusor: {}  | h: {} | pitch {}º- {}rads".format(dist, h, dpitch, pitch))
    return pitch

def calc_yaw(dist, cat):
    cat = 0.456 #->sen(45) = x/0.645
    h = math.sqrt(math.pow(cat,2)+math.pow(dist,2))
    dyaw = 90 - math.acos(cat/h)*(180/math.pi)
    yaw = (math.pi/2) - math.acos(cat/h)
    print("distance to difusor: {}  | h: {} | yaw {}º - {}rads".format(dist, h, dyaw, yaw))
    return yaw

class ledObject(object):
    def __init__(self, sample_size, z_pos=0.66, x_pos=0):
        self.led_z_pos = z_pos #z position of LED in the matrix
        self.led_x_pos = x_pos
        self.sample_size = sample_size
        #auxiliary matrixes for quiver plots starting positions
        self.zeropos = np.zeros((sample_size,3))
        self.transpos = np.ones((sample_size, 3))

        self.theta = np.zeros(sample_size) #matriz to hold initial light polar angles
        self.phi = np.zeros(sample_size) #matrix to hold intial light azimuthal angles
        self.ri = np.zeros((sample_size,3)) #matrix to hold inital photon vectors
        self.rri = np.zeros((sample_size,3)) #matrix to hold rotated (led position) photon vectors
        self.auxrri = np.zeros((sample_size,3)) #matrix to hold rotated (led position) photon vectors
        self.diff_radi = np.zeros(sample_size)
        self.diff_points = np.zeros((sample_size,3)) #matriz to hold photon points at diffuser plane
        self.pinh_points = np.zeros((sample_size,3)) #matriz to hold photon points at the pinhole plane
        self.rf = np.zeros((sample_size,3)) #matrix to hold final photon vectors after diffusor rotation
        self.diff_polar_angle = np.zeros(sample_size) #matrix to hold values of polar angle after diffuser effect
        self.prev_polar_angle = np.zeros(sample_size) #matrix to hold values of polar angle previous to diffuser effect

    def calcLEDRotationMatrixes(self, dist_to_targetcenter):
        #LED position angles
        self.dist_to_diff = dist_to_targetcenter
        self.Rx = None
        self.Rz = None

        if self.led_z_pos != 0:
            pitch = calc_pitch(dist_to_targetcenter, self.led_z_pos)
            self.Rx = np.array([[1, 0, 0],[0, math.cos(pitch), -math.sin(pitch)], [0, math.sin(pitch), math.cos(pitch)]])

        if self.led_x_pos != 0:
            yaw = calc_yaw(dist_to_targetcenter, self.led_x_pos)
            self.Rz = np.array([[math.cos(yaw), -math.sin(yaw), 0],[math.sin(yaw), math.cos(yaw), 0], [0, 0, 1]])

        return self.Rx, self.Rz

    def simDiffusorEffect(self, light_theta, diff_theta, seednr=19680801):
        seed(seednr)#seed for random generator - reproducibility
        self.light_theta = light_theta*math.pi/180 #led view angle
        self.diff_theta = diff_theta*math.pi/180 #diffusor view angle

        for i in range(0, self.sample_size):
            self.theta[i] = gauss(0, self.light_theta) #LED polar angle (from viewangle)
            self.phi[i] = randrange(0, 360)*math.pi/180 #LED azimuthal angle

            #shift frame of reference: y'is z, x' is y and z' is x
            # self.ri[i, 0] = math.sin(self.theta[i])*math.sin(self.phi[i])#+self.led_x_pos
            # self.ri[i, 1] = math.cos(self.theta[i])
            # self.ri[i, 2] = math.sin(self.theta[i])*math.cos(self.phi[i])#+self.led_z_pos
            self.ri[i,1] = 1 #y direction
            initialRz = np.array([[math.cos(self.theta[i]), -math.sin(self.theta[i]), 0],
                               [math.sin(self.theta[i]), math.cos(self.theta[i]), 0],
                               [0, 0, 1]])
            initialRy = np.array([[math.cos(self.phi[i]), 0, math.sin(self.phi[i])],
                               [0, 1, 0],
                               [-math.sin(self.phi[i]), 0, math.cos(self.phi[i])]])
            self.ri[i,:] = np.dot(self.ri[i,:], initialRz)
            self.ri[i,:] = np.dot(self.ri[i,:], initialRy)
            #self.ri[i,0] += self.led_x_pos
            #self.ri[i,2] += self.led_z_pos

            if self.led_z_pos != 0 and self.led_x_pos ==0:
                self.rri[i,:] = np.dot(self.ri[i,:], self.Rx)
            elif self.led_z_pos == 0 and self.led_x_pos != 0:
                self.rri[i,:] = np.dot(self.ri[i,:], self.Rz)
            else:
                self.rri[i,:] = np.dot(self.ri[i,:], self.Rx)
                self.rri[i,:] = np.dot(self.rri[i,:], self.Rz)

            #self.auxrri[i,:] = self.rri[i,:]
            #boost vector to diffusor
            self.diff_points[i,:] = self._intersectWithPlane(self.dist_to_diff, self.rri[i,:], self.led_x_pos, self.led_z_pos)
            r = math.sqrt(math.pow(self.rri[i,0],2)+math.pow(self.rri[i,1],2)+math.pow(self.rri[i,2],2))
            self.prev_polar_angle[i] = (math.acos(self.rri[i,1]/r)*(180/math.pi))
            #self.diff_radi[i] = math.sqrt(math.pow(self.rri[i,0],2)+math.pow(self.rri[i,2],2))
            diff_polar = gauss(0, self.diff_theta) #difusor polar angle
            #polar angle in ref to y, is a rotation around the z axis
            diffRz = np.array([[math.cos(diff_polar), -math.sin(diff_polar), 0],
                               [math.sin(diff_polar), math.cos(diff_polar), 0],
                               [0, 0, 1]])
            diff_azimuth = randrange(0, 360)*math.pi/180
            #azimuthal angle in this ref is a rotation around the y axis
            diffRy = np.array([[math.cos(diff_azimuth), 0, math.sin(diff_azimuth)],
                               [0, 1, 0],
                               [-math.sin(diff_azimuth), 0, math.cos(diff_azimuth)]])
            self.rf[i,:] = np.dot(self.rri[i,:], diffRz)
            self.rf[i,:] = np.dot(self.rf[i,:], diffRy)
            r = math.sqrt(math.pow(self.rf[i,0],2)+math.pow(self.rf[i,1],2)+math.pow(self.rf[i,2],2))
            #self.diff_polar_angle[i] = 90 - (math.acos(self.rf[i,2]/r)*(180/math.pi))
            self.diff_polar_angle[i] = (math.acos(self.rf[i,1]/r)*(180/math.pi))

    def simPinholeEffect(self, dist_to_pinh, pinh_rad):
        #use only after simDiffusorEffect
        phcount = 0
        self.cap_ph_xpos = []
        self.cap_ph_zpos = []
        self.cap_points= []
        self.cap_polar_angle = []
        is_diam = 8.382
        pinh_y = self.dist_to_diff+dist_to_pinh
        for i in range(self.sample_size):
            self.pinh_points[i,:] = self._intersectWithPlane(pinh_y, self.rf[i,:],self.led_x_pos, self.led_z_pos)
            test = math.pow(self.pinh_points[i,0],2)+math.pow(self.pinh_points[i,2],2)
            if(test < math.pow(pinh_rad,2)): #if inside pinh radi, calc points at cap and store polar angle
                phcount += 1
                self.cap_points.append(self._intersectWithPlane(pinh_y+is_diam, self.rf[i,:],self.led_x_pos, self.led_z_pos)) #photon points at cap
                self.cap_ph_xpos.append(self.cap_points[-1][0])
                self.cap_ph_zpos.append(self.cap_points[-1][2])
                #r = math.sqrt(math.pow(self.rf[i,0],2)+math.pow(self.cap_photons[-1][1],2)+math.pow(self.cap_photons[-1][2],2))
                self.cap_polar_angle.append(self.diff_polar_angle[i])

        return phcount, self.cap_polar_angle

    def plotPhotonVectors(self, f=1):
        #auxiliary function to validate geometry
        fig = plt.figure(f)
        ax = fig.add_subplot(111, projection='3d')
        #ax.quiver(self.zeropos[:,0], self.zeropos[:,1], self.zeropos[:,2],
        #          self.ri[:, 0], self.ri[:,1], self.ri[:, 2], length=0.6)
        #ax.quiver(self.zeropos[:,0], self.transpos[:,1], self.zeropos[:,2],
        #          self.rri[:, 0], self.rri[:,1], self.rri[:, 2], length=0.6, colors=[(1,0,0)])
        ax.quiver(self.transpos[:,0]*self.led_x_pos, self.zeropos[:,1], self.transpos[:,2]*self.led_z_pos, self.ri[:, 0], self.ri[:,1], self.ri[:, 2])
        ax.set_zlim3d(-1, 1.5)
        ax.set_ylim3d(-0.4, 3)
        ax.set_xlim3d(-0.4, 1)
        plt.show()

    def _intersectWithPlane(self, y_val, d, xi=0, zi=0):
        #plane parallel with XoZ with y = y_val
        #yi = 0 always
        t = y_val/d[1]
        x = t*d[0] + xi
        z = t*d[2] + zi
        return [x,y_val,z]
