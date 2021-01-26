from led_object import ledObject
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    nbins = 100
    sample_size = 100000000
    distance_to_diffuserCenter = 5
    #default distance to diffuser is 5.08
    diff_theta = 7.5
    d1 = 1.5
    d2 = 13.8
    pinh_rad = 0.05

    light_theta = 55

    nbins = 100
    x_pos = 0.225
    z_pos = 0

    fig1 = plt.figure(1)

    ledUVsmd = ledObject(sample_size,z_pos, x_pos, distribution="box", rotate_led=False)
    ledUVsmd.dist_to_diff = distance_to_diffuserCenter
    ledUVsmd.simDiffuserEffect(light_theta, diff_theta)
    print("[checkpoint] Done with diffusor simulation")
    phcount0, cap_angle0 = ledUVsmd.simPinholeEffect(d1, d2, pinh_rad)
    entryx0 = ledUVsmd.entry_xpos
    entryz0 = ledUVsmd.entry_zpos
    print("2inch from diffusor, half inch from pinhole - Got {}/{} through pinhole!".format(phcount0, sample_size))

    x_pos = 0.7
    light_theta = 7.5
    ledvis = ledObject(sample_size,z_pos, x_pos, distribution="gauss", rotate_led=True)
    ledvis.calcLEDRotationMatrixes(distance_to_diffuserCenter)
    ledvis.simDiffuserEffect(light_theta, diff_theta)
    print("[checkpoint] Done with diffusor simulation")
    phcount1, cap_angle1 = ledvis.simPinholeEffect(d1, d2, pinh_rad)
    entryx1 = ledvis.entry_xpos
    entryz1 = ledvis.entry_zpos
    print("2inch from diffusor, half inch from pinhole - Got {}/{} through pinhole!".format(phcount1, sample_size))

    light_theta = 15
    ledvis2 = ledObject(sample_size,z_pos, x_pos, distribution="gauss", rotate_led=True)
    ledvis2.calcLEDRotationMatrixes(distance_to_diffuserCenter)
    ledvis2.simDiffuserEffect(light_theta, diff_theta)
    print("[checkpoint] Done with diffusor simulation")
    phcount2, cap_angle2 = ledvis2.simPinholeEffect(d1, d2, pinh_rad)
    entryx2 = ledvis2.entry_xpos
    entryz2 = ledvis2.entry_zpos
    print("2inch from diffusor, half inch from pinhole - Got {}/{} through pinhole!".format(phcount2, sample_size))

    n2, bins2, patches2 = plt.hist(cap_angle2, nbins, density=True, color='g',histtype='step', label="DIP-15")
    n2, bins2, patches2 = plt.hist(cap_angle1, nbins, density=True, color='b',histtype='step', label="DIP-7.5")
    n2, bins2, patches2 = plt.hist(cap_angle0, nbins, density=True, color='r',histtype='step', label="SMD")
    plt.xlabel('degrees')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()
    plt.savefig('windowAngle.pdf')

    fig2 = plt.figure(2)
    plt.scatter(entryx2, entryz2, s=1, c='g',label="DIP-15")
    plt.scatter(entryx1, entryz1, s=1, c='b',label="DIP-7.5")
    plt.scatter(entryx0, entryz0, s=1, c='r',label="SMD")
    plt.xlabel('cm')
    plt.ylabel('cm')
    plt.legend()
    plt.savefig('spotPinhole.pdf')

    fig3 = plt.figure(3)
    n2, bins2, patches2 = plt.hist(ledvis2.cut_dif_angle, nbins, density=True, color='g',histtype='step', label="DIP-15")
    n2, bins2, patches2 = plt.hist(ledvis.cut_dif_angle, nbins, density=True, color='b',histtype='step', label="DIP-7.5")
    n2, bins2, patches2 = plt.hist(ledUVsmd.cut_dif_angle, nbins, density=True, color='r',histtype='step', label="SMD")
    plt.xlabel('degrees')
    plt.ylabel('# photons (normalized)')
    plt.legend()
    plt.savefig('diffAngle.pdf')

    fig4 = plt.figure(4)
    n2, bins2, patches2 = plt.hist(ledvis2.theta*(180/math.pi), nbins, density=True, color='g',histtype='step', label="DIP-15")
    n2, bins2, patches2 = plt.hist(ledvis.theta*(180/math.pi), nbins, density=True, color='b',histtype='step', label="DIP-7.5")
    n2, bins2, patches2 = plt.hist(ledUVsmd.theta*(180/math.pi), nbins, density=True, color='r',histtype='step', label="SMD")
    plt.xlabel('degrees')
    plt.ylabel('# photons (normalized)')
    plt.legend()
    plt.savefig('ledProfiles.pdf')

    #plt.show()
