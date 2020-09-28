from led_object import ledObject
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    sample_size = 10000000
    distance_to_diffuserCenter = 5.08

    diff_theta = 7.5
    nbins = 50

    led1_theta = 30
    x1_pos = 0
    z1_pos = 0

    led1 = ledObject(sample_size, x1_pos, z1_pos, distribution="gauss", rotate_led=False)
    led1.dist_to_diff = distance_to_diffuserCenter
    led1.simDiffusorEffect(led1_theta, diff_theta)
    print("[checkpoint] Done with diffusor simulation")

    fig1 = plt.figure(1)
    plt.scatter(led1.diff_x, led1.diff_z, c='b',label="photons at difuser")
    plt.xlabel('cm')
    plt.ylabel('cm')
    plt.legend()

    fig2 = plt.figure(2)
    h = plt.hist2d(led1.diff_x, led1.diff_z, nbins,label="photons at difuser")
    plt.colorbar(h[3])
    plt.legend()

    fig3 = plt.figure(3)
    n2, bins2, patches2 = plt.hist(led1.diff_x, nbins, density=True, color='r',histtype='step', label="x position of photons at difuser")
    #n2, bins2, patches2 = plt.hist(led1.theta*180/math.pi, nbins, density=True, color='r',histtype='step', label="x position of photons at difuser")
    plt.xlabel('cm')
    plt.ylabel('# photons')
    plt.legend()

    fig4 = plt.figure(4)
    n2, bins2, patches2 = plt.hist(led1.diff_z, nbins, density=True, color='r',histtype='step', label="z position of photons at difuser")
    plt.xlabel('cm')
    plt.ylabel('# photons')
    plt.legend()

    plt.show()
