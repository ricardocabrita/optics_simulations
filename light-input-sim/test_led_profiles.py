from led_object import ledObject
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    nbins = 100
    sample_size = 10000000
    distance_to_diffuserCenter = 5.08
    #default distance to diffuser is 5.08
    diff_theta = 7.5
    d1 = 1.27 #0.5in
    d2 = 7.62 #3in
    pinh_rad = 0.05

    x = 0.225

    led405nm_theta = 15
    led405nm = ledObject(sample_size, z_pos=0, x_pos=x, distribution='gauss', dist_to_diff=distance_to_diffuserCenter, rotate_led=False)
    led405nm.calcLEDRotationMatrixes(distance_to_diffuserCenter)
    led405nm.simDiffuserEffect(led405nm_theta, diff_theta)

    ledwide_theta = 30
    ledwide = ledObject(sample_size, z_pos=0, x_pos=x, distribution='gauss', dist_to_diff=distance_to_diffuserCenter, rotate_led=False)
    ledwide.calcLEDRotationMatrixes(distance_to_diffuserCenter)
    ledwide.simDiffuserEffect(ledwide_theta, diff_theta)

    ledsmd_theta = 15
    ledsmd = ledObject(sample_size, z_pos=0, x_pos=x, distribution='bull', dist_to_diff=distance_to_diffuserCenter, rotate_led=False)
    ledsmd.calcLEDRotationMatrixes(distance_to_diffuserCenter)
    ledsmd.simDiffuserEffect(ledsmd_theta, diff_theta)

    fig1 = plt.figure(1)
    plt.hist(led405nm.theta*180/math.pi, nbins, density=True, color='r',histtype='step',label="LED 1")
    plt.hist(ledwide.theta*180/math.pi, nbins, density=True, color='g',histtype='step',label="LED 2")
    plt.hist(ledsmd.theta*180/math.pi, nbins, density=True, color='b',histtype='step',label="LED 3")

    plt.xlabel('degrees')
    plt.ylabel('# photons')
    plt.legend()

    fig2 = plt.figure(2)
    plt.hist(led405nm.diff_polar_angle, nbins, density=True, color='r',histtype='step',label="LED 1")
    plt.hist(ledwide.diff_polar_angle, nbins, density=True, color='g',histtype='step',label="LED 2")
    plt.hist(ledsmd.diff_polar_angle, nbins, density=True, color='b',histtype='step',label="LED 3")

    plt.xlabel('degrees')
    plt.ylabel('# photons')
    plt.legend()

    phcount1, cap_angle1 = led405nm.simPinholeEffect(d1, d2, pinh_rad)
    print("LED1(0, {}, 0) - Got {}/{} through pinhole!".format(x, phcount1, sample_size))
    phcount2, cap_angle2 = ledwide.simPinholeEffect(d1, d2, pinh_rad)
    print("LED2 (0, {}, 0) - Got {}/{} through pinhole!".format(x, phcount2, sample_size))
    phcount3, cap_angle3 = ledsmd.simPinholeEffect(d1, d2, pinh_rad)
    print("LED3(0, {}, 0) - Got {}/{} through pinhole!".format(x, phcount3, sample_size))

    fig2 = plt.figure(3)
    plt.hist(led405nm.cap_polar_angle, nbins, density=True, color='r',histtype='step',label="LED 1")
    plt.hist(ledwide.cap_polar_angle, nbins, density=True, color='g',histtype='step',label="LED 2")
    plt.hist(ledsmd.cap_polar_angle, nbins, density=True, color='b',histtype='step',label="LED 3")

    plt.xlabel('degrees')
    plt.ylabel('# photons')
    plt.legend()

    plt.show()
