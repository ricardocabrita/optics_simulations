from random import seed, gauss, randrange, weibullvariate
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
    #cat = 0.456 #->sen(45) = x/0.645
    h = math.sqrt(math.pow(cat,2)+math.pow(dist,2))
    dyaw = 90 - math.acos(cat/h)*(180/math.pi)
    yaw = (math.pi/2) - math.acos(cat/h)
    print("distance to difusor: {}  | h: {} | yaw {}º - {}rads".format(dist, h, dyaw, yaw))
    return yaw

class ledObject(object):
    def __init__(self, sample_size, z_pos=0.66, x_pos=0, distribution="gauss", rotate_led=False, dist_to_diff=5.08):
        self.led_z_pos = z_pos #z position of LED in the matrix
        self.led_x_pos = x_pos
        self.sample_size = sample_size
        print("Sample size: {}".format(self.sample_size))
        self.dist_to_diff = dist_to_diff

        self.theta = np.zeros(sample_size) #matriz to hold initial light polar angles
        self.phi = np.zeros(sample_size) #matrix to hold intial light azimuthal angles
        self.initial_vector = np.zeros((sample_size,3)) #matrix to hold inital photon vectors
        self.rotated_vector = np.zeros((sample_size,3)) #matrix to hold rotated (led position) photon vectors
        self.diff_radi = np.zeros(sample_size)
        self.diff_x = np.zeros(sample_size)
        self.diff_z = np.zeros(sample_size)
        self.diff_points = np.zeros((sample_size,3)) #matriz to hold photon points at diffuser plane
        self.pinh_points = np.zeros((sample_size,3)) #matriz to hold photon points at the pinhole plane
        self.difused_vector = np.zeros((sample_size,3)) #matrix to hold final photon vectors after diffusor rotation
        self.diff_polar_angle = np.zeros(sample_size) #matrix to hold values of polar angle after diffuser effect
        self.prev_polar_angle = np.zeros(sample_size) #matrix to hold values of polar angle previous to diffuser effect

        self.distribution = distribution
        self.rotate_led = rotate_led

    def calcLEDRotationMatrixes(self, dist_to_targetcenter):
        #LED position angles
        self.dist_to_diff = dist_to_targetcenter
        self.Rx = None
        self.Rz = None

        if self.led_z_pos != 0:
            pitch = calc_pitch(dist_to_targetcenter, self.led_z_pos)
            self.Rx = self._rx(pitch)

        if self.led_x_pos != 0:
            yaw = calc_yaw(dist_to_targetcenter, self.led_x_pos)
            self.Rz = self._rz(-yaw)

        return self.Rx, self.Rz

    def simDiffusorEffect(self, light_theta, diff_theta, seednr=19680801):
        seed(seednr)#seed for random generator - reproducibility
        self.light_theta = light_theta*math.pi/180 #led view angle
        self.diff_theta = diff_theta*math.pi/180 #diffusor view angle

        print("Calculating diffuser effect")
        for i in range(0, self.sample_size):
            if self.distribution == "bull":
                if i > self.sample_size//2:
                    self.theta[i] = -self.theta[i-self.sample_size//2]
                else:
                    self.theta[i] = self._alternateBullDistribution()*math.pi/180
            elif self.distribution == "gauss":
                self.theta[i] = gauss(0, self.light_theta) #LED polar angle (from viewangle)
            else:
                print("Error, unknown distribution: {}".format(self.distribution))
                return False

            self.phi[i] = randrange(0, 360)*math.pi/180 #LED azimuthal angle

            #initial vector is (0,1,0) - y direction of propagation
            self.initial_vector[i,1] = 1

            #apply azimuthal and polar angle LED rotations
            self.initial_vector[i,:] = self._z_rotation(self.initial_vector[i,:], self.theta[i])
            self.initial_vector[i,:] = self._y_rotation(self.initial_vector[i,:], self.phi[i])

            #LED inclination
            if self.led_z_pos != 0 and self.led_x_pos ==0 and self.rotate_led:
                self.rotated_vector[i,:] = np.dot(self.initial_vector[i,:], self.Rx)
            elif self.led_z_pos == 0 and self.led_x_pos != 0 and self.rotate_led:
                self.rotated_vector[i,:] = np.dot(self.initial_vector[i,:], self.Rz)
            elif self.led_z_pos != 0 and self.led_x_pos != 0 and self.rotate_led:
                self.rotated_vector[i,:] = np.dot(self.initial_vector[i,:], self.Rx)
                self.rotated_vector[i,:] = np.dot(self.rotated_vector[i,:], self.Rz)
            else:
                self.rotated_vector[i,:] = self.initial_vector[i,:]
            #if both zero, do nothing

            #calculate points at difuser
            self.diff_points[i,:] = self.intersectWithPlane(self.dist_to_diff, self.rotated_vector[i,:], xi=self.led_x_pos, zi=self.led_z_pos)

            self.diff_x[i] = self.diff_points[i,0]
            self.diff_z[i] = self.diff_points[i,2]

            diff_polar = gauss(0, self.diff_theta) #difusor polar angle
            #polar angle in ref to y, is a rotation around the z axis
            self.difused_vector[i,:] = self._z_rotation(self.rotated_vector[i,:], diff_polar)
            diff_azimuth = randrange(0, 360)*math.pi/180
            #azimuthal angle in this ref is a rotation around the y axis
            self.difused_vector[i,:] = self._y_rotation(self.difused_vector[i,:], diff_azimuth)
            r = math.sqrt(math.pow(self.difused_vector[i,0],2)+math.pow(self.difused_vector[i,1],2)+math.pow(self.difused_vector[i,2],2))

            self.diff_polar_angle[i] = (math.acos(self.difused_vector[i,1]/r)*(180/math.pi))

        return True

    def simPinholeEffect(self, dist_to_pinh, pinh_rad):
        #use only after simDiffusorEffect
        phcount = 0
        self.cap_ph_xpos = []
        self.cap_ph_zpos = []
        self.cap_points= []
        self.entry_points = []
        self.entry_xpos = []
        self.entry_zpos = []
        self.cap_polar_angle = []
        is_diam = 8.382
        entry = 3.81
        pinh_y = self.dist_to_diff+dist_to_pinh
        print("Pinhole y: {} -- +entry: {}".format(pinh_y, pinh_y+entry))
        for i in range(self.sample_size):
            self.pinh_points[i,:] = self.intersectWithPlane(pinh_y, self.difused_vector[i,:],xi=self.diff_points[i,0], yi=self.diff_points[i,1], zi=self.diff_points[i,2])
            test = math.pow(self.pinh_points[i,0],2)+math.pow(self.pinh_points[i,2],2)
            if(test < math.pow(pinh_rad,2)): #if inside pinh radi, calc points at cap and store polar angle
                phcount += 1
                self.entry_points.append(self.intersectWithPlane(pinh_y+entry, self.difused_vector[i,:],xi=self.diff_points[i,0], yi=self.diff_points[i,1], zi=self.diff_points[i,2])) #photon points at entry
                print("test radi: {}, angle: {}".format(test, self.diff_polar_angle[i]))
                print(self.pinh_points[i, :], self.difused_vector[i,:])
                print(self.entry_points[-1])
                self.entry_xpos.append(self.entry_points[-1][0])
                self.entry_zpos.append(self.entry_points[-1][2])
                self.cap_points.append(self.intersectWithPlane(pinh_y+entry+is_diam, self.difused_vector[i,:],xi=self.diff_points[i,0], yi=self.diff_points[i,1], zi=self.diff_points[i,2])) #photon points at cap
                self.cap_ph_xpos.append(self.cap_points[-1][0])
                self.cap_ph_zpos.append(self.cap_points[-1][2])
                self.cap_polar_angle.append(self.diff_polar_angle[i])

        return phcount, self.cap_polar_angle

    def intersectWithPlane(self, y_val, d, xi=0, zi=0, yi=0):
        #plane parallel with XoZ with y = y_val
        t = (y_val-yi)/d[1]
        x = t*d[0] + xi
        z = t*d[2] + zi
        return [x,y_val,z]

    def _alternateBullDistribution(self, lmbda=20, k=1.5):
        theta = weibullvariate(lmbda, k)-(lmbda//4)
        if theta > 75:
            theta = gauss(45,5)
        elif theta < 0:
            theta = gauss(7.5,3)
        return theta

    def _x_rotation(self, arr, angle):
        return np.dot(arr, self._rx(angle))

    def _y_rotation(self, arr, angle):
        return np.dot(arr, self._ry(angle))

    def _z_rotation(self, arr, angle):
        return np.dot(arr, self._rz(angle))

    def _rx(self, angle):
        return np.array([[1, 0, 0],\
                        [0, math.cos(angle), -math.sin(angle)],\
                        [0, math.sin(angle), math.cos(angle)]])

    def _ry(self, angle):
        return np.array([[math.cos(angle), 0, math.sin(angle)],
                           [0, 1, 0],
                           [-math.sin(angle), 0, math.cos(angle)]])
    def _rz(self, angle):
        return np.array([[math.cos(angle), -math.sin(angle), 0],
                         [math.sin(angle), math.cos(angle), 0],
                         [0, 0, 1]])
