from led_object import ledObject
import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
    sample_size = 10000000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    dist_to_pinh = 3.5
    pinh_rad = 0.15
    light_theta = 7.5
    diff_theta = 7.5
    nbins = 100
    x_pos = 0.66
    z_pos = 0
    ledHalfInch = ledObject(sample_size,z_pos, x_pos)
    ledHalfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[0])
    ledHalfInch.simDiffuserEffect(light_theta, diff_theta)
    phcount, angles = ledHalfInch.simPinholeEffect(dist_to_pinh, pinh_rad)
    print("0.5 inch from diffusor - Got {}/{} through pinhole!".format(phcount, sample_size))

    led1Inch = ledObject(sample_size,z_pos, x_pos)
    led1Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])
    led1Inch.simDiffuserEffect(light_theta, diff_theta)
    phcount, angles = led1Inch.simPinholeEffect(dist_to_pinh, pinh_rad)
    print("1 inch from diffusor - Got {}/{} through pinhole!".format(phcount, sample_size))

    led1halfInch = ledObject(sample_size,z_pos, x_pos)
    led1halfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[2])
    led1halfInch.simDiffuserEffect(light_theta, diff_theta)
    phcount, angles = led1halfInch.simPinholeEffect(dist_to_pinh, pinh_rad)
    print("1.5 inch from diffusor - Got {}/{} through pinhole!".format(phcount, sample_size))

    led2Inch = ledObject(sample_size,z_pos, x_pos)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffuserEffect(light_theta, diff_theta)
    phcount, angles = led2Inch.simPinholeEffect(dist_to_pinh, pinh_rad)
    print("2inch from diffusor - Got {}/{} through pinhole!".format(phcount, sample_size))

    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : 12}
    matplotlib.rc('font', **font)
    fig1 = plt.figure(1)
    plt.scatter(led1Inch.cap_ph_xpos, led1Inch.cap_ph_zpos, c='g',label="a=1.0'',c=1.5''")
    plt.scatter(led2Inch.cap_ph_xpos, led2Inch.cap_ph_zpos, c='y', label="a=2.0'',c=1.5''")
    plt.xlabel('cm')
    plt.ylabel('cm')
    plt.legend()

    fig2 = plt.figure(2)
    n, bins, patches = plt.hist(ledHalfInch.cap_polar_angle, nbins, density=True, color='r',  histtype='step', label="a=0.5'',c=1.5''")
    n, bins, patches = plt.hist(led1Inch.cap_polar_angle, nbins, density=True, color='g',  histtype='step', label="a=1.0'',c=1.5''")
    n, bins, patches = plt.hist(led1halfInch.cap_polar_angle, nbins, density=True, color='b',  histtype='step', label="a=1.5'',c=1.5''")
    n2, bins2, patches2 = plt.hist(led2Inch.cap_polar_angle, nbins, density=True, color='y',  histtype='step', label="a=2.0'',c=1.5''")
    plt.xlabel('degrees')
    plt.ylabel('rel # photons, n={}'.format(sample_size))
    plt.legend()

    plt.show()
