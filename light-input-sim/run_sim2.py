from led_object import ledObject
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sample_size = 1000000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    dist_to_pinh = 1.27
    pinh_rad = 0.15
    light_theta = 7.5
    diff_theta = 7.5
    nbins = 100
    x_pos = 0.66
    z_pos = 0

    fig1 = plt.figure(1)

    led2Inch = ledObject(sample_size,z_pos, x_pos)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffusorEffect(light_theta, diff_theta)
    phcount, cap_angle = led2Inch.simPinholeEffect(1.27, pinh_rad)
    capx0 = led2Inch.cap_ph_xpos
    capz0 = led2Inch.cap_ph_zpos
    print("2inch from diffusor, half inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))
    n2, bins2, patches2 = plt.hist(cap_angle, nbins, density=True, color='r',histtype='step', label="a=2.0'',c=0.5''")


    phcount, cap_angle2 = led2Inch.simPinholeEffect(2.54, pinh_rad)
    capx1 = led2Inch.cap_ph_xpos
    capz1 = led2Inch.cap_ph_zpos
    print("2inch from diffusor, 1 inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))
    n2, bins2, patches2 = plt.hist(cap_angle2, nbins, density=True, color='g',histtype='step', label="a=2.0'',c=1.0''")

    phcount, cap_angle3 = led2Inch.simPinholeEffect(3.5, pinh_rad)
    capx2 = led2Inch.cap_ph_xpos
    capz2 = led2Inch.cap_ph_zpos
    print("2inch from diffusor, 1.5 inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))
    n2, bins2, patches2 = plt.hist(cap_angle3, nbins, density=True, color='b',histtype='step', label="a=2.0'',c=1.5''")
    plt.legend()

    phcount, cap_angle4 = led2Inch.simPinholeEffect(5.08, pinh_rad)
    capx3 = led2Inch.cap_ph_xpos
    capz3 = led2Inch.cap_ph_zpos
    print("2inch from diffusor, 2 inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))
    n2, bins2, patches2 = plt.hist(cap_angle4, nbins, density=True, color='y',histtype='step', label='"a=2.0'',c=2.0''"')
    plt.legend()
    plt.xlabel('degrees')
    plt.ylabel('rel # photons, n={}'.format(sample_size))

    fig2 = plt.figure(2)
    plt.scatter(capx0, capz0, c='g',label="a=2.0'',c=1.0''")
    plt.scatter(capx1, capz1, c='g',label="a=2.0'',c=1.0''")
    plt.scatter(capx2, capz2, c='b', label="a=2.0'',c=1.5''")
    plt.scatter(capx3, capz3, c='y', label="a=2.0'',c=2.0''")
    plt.legend()
    plt.xlabel("x (cm)")
    plt.ylabel("z (cm)")
    plt.show()

    #led2Inch.plotPhotonVectors()
