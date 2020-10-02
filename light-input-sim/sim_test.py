from led_object import ledObject
import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
    sample_size = 10000000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    view_half_angle = [4, 8, 15, 30]
    phcount = [0,0,0,0]
    dist_to_pinh = 5.08
    diff_theta = 7.5
    nbins = 100
    z_pos = 1
    x_pos = 0
    pinh_rad = 0.15

    led2Inch = ledObject(sample_size, z_pos, x_pos)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])

    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : 12}
    matplotlib.rc('font', **font)
    fig1 = plt.figure(1)

    led2Inch.simDiffuserEffect(view_half_angle[0], diff_theta)
    phcount[0], cap_angle = led2Inch.simPinholeEffect(dist_to_pinh, pinh_rad)
    phcount[0]/sample_size
    print("View half angle {} - Got {}/{} through pinhole!".format(view_half_angle[0], phcount, sample_size))
    capx0 = led2Inch.cap_ph_xpos
    capz0 = led2Inch.cap_ph_zpos
    n2, bins2, patches2 = plt.hist(cap_angle, nbins, density=True, color='r',histtype='step', label="FHWM 4")
    plt.legend()

    led2Inch.simDiffuserEffect(view_half_angle[1], diff_theta)
    phcount[1], cap_angle = led2Inch.simPinholeEffect(dist_to_pinh, pinh_rad)
    phcount[1]/sample_size
    print("View half angle {} - Got {}/{} through pinhole!".format(view_half_angle[1], phcount, sample_size))
    capx1 = led2Inch.cap_ph_xpos
    capz1 = led2Inch.cap_ph_zpos
    n2, bins2, patches2 = plt.hist(cap_angle, nbins, density=True, color='g',histtype='step', label="FHWM 8")
    plt.legend()

    led2Inch.simDiffuserEffect(view_half_angle[2], diff_theta)
    phcount[2], cap_angle = led2Inch.simPinholeEffect(dist_to_pinh, pinh_rad)
    phcount[2]/sample_size
    print("View half angle {} - Got {}/{} through pinhole!".format(view_half_angle[2], phcount, sample_size))
    capx2 = led2Inch.cap_ph_xpos
    capz2 = led2Inch.cap_ph_zpos
    n2, bins2, patches2 = plt.hist(cap_angle, nbins, density=True, color='b',histtype='step', label="FHWM 10")
    plt.legend()

    led2Inch.simDiffuserEffect(view_half_angle[3], diff_theta)
    phcount[3], cap_angle = led2Inch.simPinholeEffect(dist_to_pinh, pinh_rad)
    phcount[3]/sample_size
    print("View half angle {} - Got {}/{} through pinhole!".format(view_half_angle[3], phcount, sample_size))
    capx3 = led2Inch.cap_ph_xpos
    capz3 = led2Inch.cap_ph_zpos
    n2, bins2, patches2 = plt.hist(cap_angle, nbins, density=True, color='y',histtype='step', label="FHWM 15")
    plt.legend()

    fig2 = plt.figure(2)
    plt.scatter(capx0, capz0, c='r',label="FHWM 4")
    plt.scatter(capx1, capz1, c='g',label="FHWM 8")
    plt.scatter(capx2, capz2, c='b', label="FHWM 10")
    plt.scatter(capx3, capz3, c='y', label="FHWM 15")
    plt.legend()
    plt.xlabel("x (cm)")
    plt.ylabel("z (cm)")


    fig3 = plt.figure(3)
    plt.plot(view_half_angle, phcount)
    plt.xlabel("view half angle º")
    plt.ylabel("% of photons through")
    plt.show()
