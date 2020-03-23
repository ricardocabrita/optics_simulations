from led_object import ledObject
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sample_size = 1000000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    dist_to_pinh = 1.27
    pinh_rad = 0.15
    light_theta = 7.5
    diff_theta = 7.5

    led2Inch = ledObject(sample_size)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffusorEffect(light_theta, diff_theta)
    phcount, cap_angle = led2Inch.simPinholeEffect(1.27, pinh_rad)
    print("2inch from diffusor, half inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))

    fig1 = plt.figure(1)
    n2, bins2, patches2 = plt.hist(cap_angle, 100, density=True, color='b', histtype='step',label='2in LED-diffuser, 0.5in diffuser-pinhole')
    #n, bins, patches = plt.hist(ledHalfInch.diff_polar_angle, 100, density=True, facecolor='g', label='0.5 inch from LED to diffusor')

    phcount, cap_angle2 = led2Inch.simPinholeEffect(2.54, pinh_rad)
    print("2inch from diffusor, 1 inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))
    n2, bins2, patches2 = plt.hist(cap_angle2, 100, density=True, color='g',histtype='step', label='2in LED-diffuser, 1in diffuser-pinhole')


    phcount, cap_angle3 = led2Inch.simPinholeEffect(3.5, pinh_rad)
    print("2inch from diffusor, 1.5 inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))
    n2, bins2, patches2 = plt.hist(cap_angle3, 100, density=True, color='y',histtype='step', label='2in LED-diffuser, 1.5in diffuser-pinhole')
    plt.legend()


    phcount, cap_angle4 = led2Inch.simPinholeEffect(5.08, pinh_rad)
    print("2inch from diffusor, 2 inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))
    n2, bins2, patches2 = plt.hist(cap_angle4, 100, density=True, color='r',histtype='step', label='2in LED-diffuser, 2 inch diffuser-pinhole')
    plt.legend()

    # fig1 = plt.figure(1)
    # plt.scatter(led1Inch.cap_ph_xpos, led1Inch.cap_ph_zpos)
    # plt.title("Spot - X/Y distribution at 1.5'' cap - 1 inch dif-pinhole")

    plt.show()

    #led2Inch.plotPhotonVectors()
