from led_object import ledObject
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    sample_size = 1000000
    distance_to_diffuserCenter = 5.08

    diff_theta = 7.5
    nbins = 50

    led1_theta = 15
    x1_pos = 0
    z1_pos = 0
    led1 = ledObject(sample_size, z_pos = z1_pos, x_pos = x1_pos, distribution="gauss", rotate_led=False)
    led1.dist_to_diff = distance_to_diffuserCenter
    led1.simDiffuserEffect(led1_theta, diff_theta)
    print("[checkpoint] Done with diffusor simulation")

    phcount, cap_angle = led1.simPinholeEffect(5.5, 0.05)
    print("Got {}/{} through pinhole!".format(phcount, sample_size))
    # led2_theta = 15
    # x2_pos = 2.66
    # z2_pos = 0
    # led2 = ledObject(sample_size, z_pos = z2_pos, x_pos = x2_pos, distribution="gauss", rotate_led=False)
    # led2.dist_to_diff = distance_to_diffuserCenter
    # led2.simDiffuserEffect(led2_theta, diff_theta)
    # print("[checkpoint] Done with diffusor simulation")
    #
    # led3_theta = 15
    # x3_pos = 0
    # z3_pos = 0.7
    # led3 = ledObject(sample_size, z_pos = z3_pos, x_pos = x3_pos, distribution="gauss", rotate_led=False)
    # led3.dist_to_diff = distance_to_diffuserCenter
    # led3.simDiffuserEffect(led3_theta, diff_theta)
    # print("[checkpoint] Done with diffusor simulation")


    fig1 = plt.figure(1)

    #plt.scatter(led2.diff_x, led2.diff_z, c='g',label="photons at difuser (2.66,0,0)")
    #plt.scatter(led3.diff_x, led3.diff_z, c='b',label="photons at difuser (0, 0, 0.66)")
    plt.scatter(led1.diff_x, led1.diff_z, c='r',label="photons at difuser (0,0,0)")
    h = plt.scatter(led1.entry_xpos, led1.entry_zpos, nbins,label="photons at entry")
    plt.xlim([-15, 15])
    plt.ylim([-15, 15])
    plt.xlabel('cm')
    plt.ylabel('cm')
    plt.legend()

    #fig2 = plt.figure(2)
    #h = plt.hist2d(led1.diff_x, led1.diff_z, nbins,label="photons at difuser")
    # h = plt.hist2d(led2.diff_x, led2.diff_z, nbins,label="photons at difuser")
    # h = plt.hist2d(led3.diff_x, led3.diff_z, nbins,label="photons at difuser")
    # plt.colorbar(h[3])
    # plt.legend()

    fig3 = plt.figure(3)
    n2, bins2, patches2 = plt.hist(led1.diff_x, nbins, density=True, color='r',histtype='step', label="x positions at difuser (0,0,0)")
    #n2, bins2, patches2 = plt.hist(led2.diff_x, nbins, density=True, color='g',histtype='step', label="x positions at difuser (2.66,0,0)")
    #n2, bins2, patches2 = plt.hist(led3.diff_x, nbins, density=True, color='b',histtype='step', label="x positions at difuser (0,0,0.66)")

    plt.xlabel('cm')
    plt.ylabel('# photons')
    plt.legend()

    fig4 = plt.figure(4)
    n2, bins2, patches2 = plt.hist(led1.diff_z, nbins, density=True, color='r',histtype='step', label="z positions at difuser (0,0,0)")
    #n2, bins2, patches2 = plt.hist(led2.diff_z, nbins, density=True, color='g',histtype='step', label="z positions difuser (2.66,0,0)")
    #n2, bins2, patches2 = plt.hist(led3.diff_z, nbins, density=True, color='b',histtype='step', label="z positions difuser (0,0,0.66)")
    plt.xlabel('cm')
    plt.ylabel('# photons')
    plt.legend()

    fig5 = plt.figure(5)
    # n2, bins2, patches2 = plt.hist(led1.diff_polar_angle, nbins, density=True, color='r',histtype='step', label="(0,0,0)")
    # n2, bins2, patches2 = plt.hist(led2.diff_polar_angle, nbins, density=True, color='g',histtype='step', label="(2.66,0,0)")
    # n2, bins2, patches2 = plt.hist(led3.diff_polar_angle, nbins, density=True, color='b',histtype='step', label="(0, 0, 0.66)")
    ax = fig5.add_subplot(111, projection='3d')
    ax.scatter(led1.cut_vx,led1.cut_vy, led1.cut_vz, marker='o')
    ax.scatter(0,0, 0, marker='^')

    # fig6 = plt.figure(6)
    # # n2, bins2, patches2 = plt.hist(led1.diff_polar_angle, nbins, density=True, color='r',histtype='step', label="(0,0,0)")
    # # n2, bins2, patches2 = plt.hist(led2.diff_polar_angle, nbins, density=True, color='g',histtype='step', label="(2.66,0,0)")
    # # n2, bins2, patches2 = plt.hist(led3.diff_polar_angle, nbins, density=True, color='b',histtype='step', label="(0, 0, 0.66)")
    # ax = fig6.add_subplot(111, projection='3d')
    # ax.scatter(0,0, 0, marker='^')
    # ax.scatter(led1.difused_vector[:,0],led1.difused_vector[:,1], led1.difused_vector[:,2], marker='o')



    plt.show()
