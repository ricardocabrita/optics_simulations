from led_object import ledObject
import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
    sample_size = 1000000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    light_theta = 7.5
    diff_theta = 7.5
    nbins = 50

    ledHalfInch = ledObject(sample_size, 0, 0.66)
    ledHalfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[0])
    ledHalfInch.simDiffusorEffect(light_theta, diff_theta)

    led1Inch = ledObject(sample_size, 0, 0.6)
    led1Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])
    led1Inch.simDiffusorEffect(light_theta, diff_theta)

    led1halfInch = ledObject(sample_size, 0, 0.6)
    led1halfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[2])
    led1halfInch.simDiffusorEffect(light_theta, diff_theta)

    led2Inch = ledObject(sample_size, 0, 0.6)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffusorEffect(light_theta, diff_theta)

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
    n, bins, patches = plt.hist(ledHalfInch.rri[:,0], nbins, density=True, color='r', histtype='step', label='x distro at diff')
    n, bins, patches = plt.hist(ledHalfInch.rri[:,2], nbins, density=True, color='b', histtype='step', label='z distro at diff')
    plt.xlabel('(cm)')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    fig3 = plt.figure(3)
    n2, bins2, patches2 = plt.hist(led1Inch.rri[:,0], nbins, density=True, color='r', histtype='step', label="x distro at diff")
    n2, bins2, patches2 = plt.hist(led1Inch.rri[:,2], nbins, density=True, color='b', histtype='step', label="z distro at diff")
    plt.xlabel('(cm)')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    fig4 = plt.figure(4)
    n2, bins2, patches2 = plt.hist(led1halfInch.rri[:,0], nbins, density=True, color='r', histtype='step', label="x distro at diff")
    n2, bins2, patches2 = plt.hist(led1halfInch.rri[:,2], nbins, density=True, color='b', histtype='step', label="z distro at diff")
    plt.xlabel('(cm)')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    fig5 = plt.figure(5)
    n2, bins2, patches2 = plt.hist(led2Inch.rri[:,0], nbins, density=True, color='r', histtype='step', label="x distro at diff")
    n2, bins2, patches2 = plt.hist(led2Inch.rri[:,2], nbins, density=True, color='b', histtype='step', label="z distro at diff")
    plt.xlabel('(cm)')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    plt.legend()
    plt.show()

    #led2Inch.plotPhotonVectors()
