from led_object import ledObject
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sample_size = 10000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    light_theta = 7.5
    diff_theta = 7.5

    ledHalfInch = ledObject(sample_size)
    ledHalfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[0])
    ledHalfInch.simDiffusorEffect(light_theta, diff_theta)
    photons = ledHalfInch.getPhotonsThroughPinhole(0.5, 0.15)
    print("(0.5 inch to diffusor) Photons through pinhole: {}/{}".format(photons, sample_size))

    led1Inch = ledObject(sample_size)
    led1Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])
    led1Inch.simDiffusorEffect(light_theta, diff_theta)
    photons = led1Inch.getPhotonsThroughPinhole(0.5, 0.15)
    print("(1 inch to diffusor) Photons through pinhole: {}/{}".format(photons, sample_size))

    led1halfInch = ledObject(sample_size)
    led1halfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[2])
    led1halfInch.simDiffusorEffect(light_theta, diff_theta)
    photons = led1halfInch.getPhotonsThroughPinhole(0.5, 0.15)
    print("(1.5 inch to diffusor) Photons through pinhole: {}/{}".format(photons, sample_size))

    led2Inch = ledObject(sample_size)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffusorEffect(light_theta, diff_theta)
    photons = led2Inch.getPhotonsThroughPinhole(0.5, 0.15)
    print("(2 inch to diffusor) Photons through pinhole: {}/{}".format(photons, sample_size))

    fig1 = plt.figure(1)
    n, bins, patches = plt.hist(ledHalfInch.final_polar_angle, 100, density=True, facecolor='g', label='0.5 inch from LED to diffusor')
    n2, bins2, patches2 = plt.hist(led1Inch.final_polar_angle, 100, density=True, facecolor='b', label="1 inch from LED to diffusor")
    n2, bins2, patches2 = plt.hist(led1halfInch.final_polar_angle, 100, density=True, facecolor='y', label="1.5 inch from LED to diffusor")
    n2, bins2, patches2 = plt.hist(led2Inch.final_polar_angle, 100, density=True, facecolor='r', label="2 inch from LED to diffusor")
    plt.legend()
    plt.title("Final polar angle distribution")

    plt.show()

    #led2Inch.plotPhotonVectors()
