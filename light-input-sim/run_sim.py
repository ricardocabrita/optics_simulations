from led_object import ledObject
import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
    sample_size = 1000000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    light_theta = 7.5
    diff_theta = 7.5
    nbins = 100
    z_pos = 0
    x_pos = 0.66

    ledHalfInch = ledObject(sample_size, z_pos, x_pos)
    ledHalfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[0])
    ledHalfInch.simDiffuserEffect(light_theta, diff_theta)

    led1Inch = ledObject(sample_size, z_pos, x_pos)
    led1Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])
    led1Inch.simDiffuserEffect(light_theta, diff_theta)

    led1halfInch = ledObject(sample_size, z_pos, x_pos)
    led1halfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[2])
    led1halfInch.simDiffuserEffect(light_theta, diff_theta)

    led2Inch = ledObject(sample_size, z_pos, x_pos)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffuserEffect(light_theta, diff_theta)

    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : 12}
    matplotlib.rc('font', **font)

    fig1 = plt.figure(1)
    n, bins, patches = plt.hist(ledHalfInch.diff_polar_angle, nbins, density=True, color='r', histtype='step', label='a = 0.5''')
    n2, bins2, patches2 = plt.hist(led1Inch.diff_polar_angle, nbins, density=True, color='g', histtype='step', label="a = 1.0''")
    n2, bins2, patches2 = plt.hist(led1halfInch.diff_polar_angle, nbins, density=True, color='b', histtype='step', label="a = 1.5''")
    n2, bins2, patches2 = plt.hist(led2Inch.diff_polar_angle, nbins, density=True, color='y', histtype='step', label="a = 2.0''")
    plt.xlabel('degrees')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    fig2 = plt.figure(2)
    n, bins, patches = plt.hist(ledHalfInch.diff_points[:,0], nbins, density=True, color='r', histtype='step', label='x distro at diff')
    n, bins, patches = plt.hist(ledHalfInch.diff_points[:,2], nbins, density=True, color='b', histtype='step', label='z distro at diff')
    plt.xlabel('(cm)')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    fig3 = plt.figure(3)
    n2, bins2, patches2 = plt.hist(led1Inch.diff_points[:,0], nbins, density=True, color='r', histtype='step', label="x distro at diff")
    n2, bins2, patches2 = plt.hist(led1Inch.diff_points[:,2], nbins, density=True, color='b', histtype='step', label="z distro at diff")
    plt.xlabel('(cm)')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    fig4 = plt.figure(4)
    n2, bins2, patches2 = plt.hist(led1halfInch.diff_points[:,0], nbins, density=True, color='r', histtype='step', label="x distro at diff")
    n2, bins2, patches2 = plt.hist(led1halfInch.diff_points[:,2], nbins, density=True, color='b', histtype='step', label="z distro at diff")
    plt.xlabel('(cm)')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    fig5 = plt.figure(5)
    n2, bins2, patches2 = plt.hist(led2Inch.diff_points[:,0], nbins, density=True, color='r', histtype='step', label="x distro at diff")
    n2, bins2, patches2 = plt.hist(led2Inch.diff_points[:,2], nbins, density=True, color='b', histtype='step', label="z distro at diff")
    plt.xlabel('(cm)')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    plt.show()

    #led2Inch.plotPhotonVectors()
