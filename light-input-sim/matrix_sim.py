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

    led405nm_theta = 15
    led405nm = ledObject(sample_size, z_pos=0, x_pos=0.7, distribution='gauss', dist_to_diff=distance_to_diffuserCenter)
    led405nm.calcLEDRotationMatrixes(distance_to_diffuserCenter)
    led405nm.simDiffuserEffect(led405nm_theta, diff_theta)

    fig1 = plt.figure(1)
    plt.hist(led405nm.theta*180/math.pi, nbins, density=True, color='b',histtype='step',label="smd UV LED angular profile")
    #plt.hist(led405nm.theta*180/math.pi, nbins, density=True, color='b',histtype='step',label="405nm LED angular profile")
    plt.xlabel('degrees')
    plt.ylabel('# photons')
    plt.legend()

    fig2 = plt.figure(2)
    plt.hist(led405nm.cut_dif_angle, nbins, density=True, color='r',histtype='step',label="dif polar angle (cut), smd UVLED")
    #plt.hist(led405nm.cut_dif_angle, nbins, density=True, color='r',histtype='step',label="dif polar angle, 405nm LED")
    plt.xlabel('degrees')
    plt.ylabel('# photons')
    plt.legend()

    phcount, cap_angle = led405nm.simPinholeEffect(d1, d2, pinh_rad)
    print("405nm LED (0, 0.7, 0) - Got {}/{} through pinhole!".format(phcount, sample_size))

    fig3 = plt.figure(3)
    #plt.hist(cap_angle, nbins, density=True, color='g',histtype='step',label="cap polar angle, 405nm LED")
    plt.hist(cap_angle, nbins, density=True, color='g',histtype='step',label="cap polar angle, smd UV LED")
    plt.xlabel('degrees')
    plt.ylabel('# photons')
    plt.legend()

    fig4 = plt.figure(4)
    plt.scatter(led405nm.entry_xpos, led405nm.entry_zpos, c='r',label="Internal colimator spot, smd UV LED")
    #plt.scatter(led405nm.entry_xpos, led405nm.entry_zpos, c='r',label="Internal colimator spot, 405nm LED")
    plt.xlabel('cm')
    plt.ylabel('cm')
    plt.legend()

    fig5 = plt.figure(5)
    plt.hist(led405nm.diff_polar_angle, nbins, density=True, color='c',histtype='step',label="dif polar angle, smd UVLED")
    #plt.hist(led405nm.cut_dif_angle, nbins, density=True, color='r',histtype='step',label="dif polar angle, 405nm LED")
    plt.xlabel('degrees')
    plt.ylabel('# photons')
    plt.legend()

    plt.show()
