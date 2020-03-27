from led_object import ledObject
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sample_size = 1000000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    dist_to_pinh = 5.08
    pinh_rad = 0.15
    light_theta = 7.5
    diff_theta = 7.5


    ledHalfInch = ledObject(sample_size)
    ledHalfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[0])
    ledHalfInch.simDiffusorEffect(light_theta, diff_theta)
    phcount, angles = ledHalfInch.simPinholeEffect(dist_to_pinh, pinh_rad)
    print("0.5 inch from diffusor - Got {}/{} through pinhole!".format(phcount, sample_size))

    led1Inch = ledObject(sample_size)
    led1Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])
    led1Inch.simDiffusorEffect(light_theta, diff_theta)
    phcount, angles = led1Inch.simPinholeEffect(dist_to_pinh, pinh_rad)
    print("1 inch from diffusor - Got {}/{} through pinhole!".format(phcount, sample_size))

    led1halfInch = ledObject(sample_size)
    led1halfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[2])
    led1halfInch.simDiffusorEffect(light_theta, diff_theta)
    phcount, angles = led1halfInch.simPinholeEffect(dist_to_pinh, pinh_rad)
    print("1.5 inch from diffusor - Got {}/{} through pinhole!".format(phcount, sample_size))

    led2Inch = ledObject(sample_size)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffusorEffect(light_theta, diff_theta)
    phcount, angles = led2Inch.simPinholeEffect(dist_to_pinh, pinh_rad)
    print("2inch from diffusor - Got {}/{} through pinhole!".format(phcount, sample_size))

    fig1 = plt.figure(1)
    plt.scatter(led1Inch.cap_ph_xpos, led1Inch.cap_ph_zpos)
    plt.scatter(led2Inch.cap_ph_xpos, led2Inch.cap_ph_zpos, c='red')
    # plt.title("Spot - X/Y distribution at 1.5'' cap")

    fig2 = plt.figure(2)
    n, bins, patches = plt.hist(ledHalfInch.cap_polar_angle, 100, density=True, facecolor='g',  histtype='step', label='0.5in LED-diffuser, 0.5in diffuser-pinhole')
    n, bins, patches = plt.hist(led1Inch.cap_polar_angle, 100, density=True, facecolor='b',  histtype='step', label='1in LED-diffuser, 0.5in diffuser-pinhole')
    n, bins, patches = plt.hist(led1halfInch.cap_polar_angle, 100, density=True, facecolor='y',  histtype='step', label='1.5in LED-diffuser, 0.5in diffuser-pinhole')
    n2, bins2, patches2 = plt.hist(led2Inch.cap_polar_angle, 100, density=True, facecolor='r',  histtype='step', label='2in LED-diffuser, 0.5in diffuser-pinhole')
    plt.legend()

    plt.show()
