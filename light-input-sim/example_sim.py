from random import seed, gauss, randrange
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

def calc_pitch(dist):
    cat = 0.635
    h = math.sqrt(math.pow(cat,2)+math.pow(dist,2))
    dpitch = 90 - math.asin(dist/h)*(180/math.pi)
    pitch = (math.pi/2) - math.asin(dist/h)
    print("distance to difusor: {}  | h: {} | pitch {}º- {}rads".format(dist, h, dpitch, pitch))
    return pitch

def calc_yaw(dist):
    cat = 0.456 #->sen(45) = x/0.645
    h = math.sqrt(math.pow(cat,2)+math.pow(dist,2))
    dyaw = 90 - math.acos(cat/h)*(180/math.pi)
    yaw = (math.pi/2) - math.acos(cat/h)
    print("distance to difusor: {}  | h: {} | yaw {}º - {}rads".format(dist, h, dyaw, yaw))
    return yaw

sample_size = 1000 #sample size
#auxiliary matrixes for quiver plots starting positions
zeropos = np.zeros((sample_size,3))
transpos = np.ones((sample_size, 3))

theta = np.zeros(sample_size) #matriz to hold initial light polar angles
phi = np.zeros(sample_size) #matrix to hold intial light azimuthal angles
ri = np.zeros((sample_size,3)) #matrix to hold inital photon vectors
rri = np.zeros((sample_size,3)) #matrix to hold rotated (led position) photon vectors
rf = np.zeros((sample_size,3)) #matrix to hold final photon vectors after diffusor rotation

#LED position angles
pitch = calc_pitch(5.08)
yaw = calc_yaw(5.08)
#rotation matrixes to calc rri
Rx = np.array([[1, 0, 0],[0, math.cos(pitch), -math.sin(pitch)], [0, math.sin(pitch), math.cos(pitch)]])
Rz = np.array([[math.cos(yaw), -math.sin(yaw), 0],[math.sin(yaw), math.cos(yaw), 0], [0, 0, 1]])

seed(19680801)#seed for random generator - reproducibility
light_theta = 7.5*math.pi/180 #led view angle
diff_theta = 7.5*math.pi/180 #diffusor view angle
print("Light view angle: 7.5º or {} radians".format(light_theta))

for i in range(0, sample_size):
    theta[i] = gauss(0, light_theta) #LED polar angle (from viewangle)
    phi[i] = randrange(0, 360)*math.pi/180 #LED azimuthal angle
    #ri[i, 0] = math.sin(theta[i])*math.cos(phi[i])
    #ri[i, 1] = math.sin(theta[i])*math.sin(phi[i])
    #ri[i, 2] = math.cos(theta[i])
    #shift frame of reference: y'is z, x' is y and z' is x
    ri[i, 0] = math.sin(theta[i])*math.sin(phi[i])
    ri[i, 1] = math.cos(theta[i])
    ri[i, 2] = math.sin(theta[i])*math.cos(phi[i])
    rri[i,:] = np.dot(ri[i,:], Rx)
    rri[i,:] = np.dot(rri[i,:], Rz)
    diff_polar = gauss(0, diff_theta) #difusor polar angle
    #polar angle in ref to y, is a rotation around the z axis
    diffRz = np.array([[math.cos(diff_polar), -math.sin(diff_polar), 0],
                       [math.sin(diff_polar), math.cos(diff_polar), 0],
                       [0, 0, 1]])
    diff_azimuth = randrange(0, 360)*math.pi/180
    #azimuthal angle in this ref is a rotation around the y axis
    diffRy = np.array([[math.cos(diff_azimuth), 0, math.sin(diff_azimuth)],
                       [0, 1, 0],
                       [-math.sin(diff_azimuth), 0, math.cos(diff_azimuth)]])
    rf[i,:] = np.dot(rri[i,:], diffRz)
    rf[i,:] = np.dot(rf[i,:], diffRy)


fig1 = plt.figure(1)
n, bins, patches = plt.hist(theta, 100, density=True, facecolor='g')
n1, bins1, patches1 = plt.hist(phi, 360, density=True, facecolor='y')

plt.title("LED theta and phi histogram distribution")
#plt.ylabel("detected photons (normalized)")

fig2 = plt.figure(2)
ax = fig2.add_subplot(111, projection='3d')
ax.quiver(zeropos[:,0], zeropos[:,1], transpos[:,2], ri[:, 0], ri[:,1], ri[:, 2], length=0.6)
ax.quiver(zeropos[:,0], transpos[:,1], transpos[:,2], rri[:, 0], rri[:,1], rri[:, 2], length=0.6, colors=[(1,0,0)])
ax.quiver(zeropos[:,0], transpos[:,1]*2, zeropos[:,2], rf[:, 0], rf[:,1], rf[:, 2], length=0.6, colors=[(0,1,0)])
ax.set_zlim3d(-1, 1.5)
ax.set_ylim3d(-0.4, 3)
ax.set_xlim3d(-0.4, 1)
plt.show()
