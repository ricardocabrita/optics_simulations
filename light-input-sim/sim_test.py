from led_object import ledObject
import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
    sample_size = 100000#0
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    light_theta = 7.5
    diff_theta = 7.5
    nbins = 100
    z_pos = 0
    x_pos = 0.66

    ledHalfInch = ledObject(sample_size, z_pos, x_pos)
    ledHalfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[0])
    ledHalfInch.simDiffusorEffect(light_theta, diff_theta)

    led1Inch = ledObject(sample_size, z_pos, x_pos)
    led1Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])
    led1Inch.simDiffusorEffect(light_theta, diff_theta)
    
    led1halfInch = ledObject(sample_size, z_pos, x_pos)
    led1halfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[2])
    led1halfInch.simDiffusorEffect(light_theta, diff_theta)

    led2Inch = ledObject(sample_size, z_pos, x_pos)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffusorEffect(light_theta, diff_theta)

    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : 12}
    matplotlib.rc('font', **font)

    fig1 = plt.figure(1)
    n, bins, patches = plt.hist(ledHalfInch.prev_polar_angle, nbins, density=True, color='r', histtype='step', label='a = 0.5''')
    n2, bins2, patches2 = plt.hist(led1Inch.prev_polar_angle, nbins, density=True, color='g', histtype='step', label="a = 1.0''")
    n2, bins2, patches2 = plt.hist(led1halfInch.prev_polar_angle, nbins, density=True, color='b', histtype='step', label="a = 1.5''")
    n2, bins2, patches2 = plt.hist(led2Inch.prev_polar_angle, nbins, density=True, color='y', histtype='step', label="a = 2.0''")
    plt.xlabel('degrees')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()


    fig1 = plt.figure(2)
    n, bins, patches = plt.hist(ledHalfInch.diff_polar_angle, nbins, density=True, color='r', histtype='step', label='a = 0.5''')
    n2, bins2, patches2 = plt.hist(led1Inch.diff_polar_angle, nbins, density=True, color='g', histtype='step', label="a = 1.0''")
    n2, bins2, patches2 = plt.hist(led1halfInch.diff_polar_angle, nbins, density=True, color='b', histtype='step', label="a = 1.5''")
    n2, bins2, patches2 = plt.hist(led2Inch.diff_polar_angle, nbins, density=True, color='y', histtype='step', label="a = 2.0''")
    plt.xlabel('degrees')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    plt.show()
