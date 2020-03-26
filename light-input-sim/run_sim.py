from led_object import ledObject
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sample_size = 100000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    light_theta = 7.5
    diff_theta = 7.5

    ledHalfInch = ledObject(sample_size)
    ledHalfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[0])
    ledHalfInch.simDiffusorEffect(light_theta, diff_theta)

    led1Inch = ledObject(sample_size)
    led1Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])
    led1Inch.simDiffusorEffect(light_theta, diff_theta)

    led1halfInch = ledObject(sample_size)
    led1halfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[2])
    led1halfInch.simDiffusorEffect(light_theta, diff_theta)

    led2Inch = ledObject(sample_size)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
    led2Inch.simDiffusorEffect(light_theta, diff_theta)

    fig1 = plt.figure(1)
    n, bins, patches = plt.hist(ledHalfInch.diff_polar_angle, 100, density=True, facecolor='g', histtype='step', label='0.5 inch from LED to diffusor')
    n2, bins2, patches2 = plt.hist(led1Inch.diff_polar_angle, 100, density=True, facecolor='b', histtype='step', label="1 inch from LED to diffusor")
    n2, bins2, patches2 = plt.hist(led1halfInch.diff_polar_angle, 100, density=True, facecolor='y', histtype='step', label="1.5 inch from LED to diffusor")
    n2, bins2, patches2 = plt.hist(led2Inch.diff_polar_angle, 100, density=True, facecolor='r', histtype='step', label="2 inch from LED to diffusor")
    plt.legend()
    #plt.title("Final polar angle distribution")
    plt.xlabel('degrees')
    plt.ylabel('rel # photons')

    fig2 = plt.figure(2)
    # n, bins, patches = plt.hist(ledHalfInch.diff_radi, 100, density=True, facecolor='g', histtype='step', label='0.5 inch from LED to diffusor')
    # n2, bins2, patches2 = plt.hist(led1Inch.diff_radi, 100, density=True, facecolor='b', histtype='step', label="1 inch from LED to diffusor")
    # n2, bins2, patches2 = plt.hist(led1halfInch.diff_radi, 100, density=True, facecolor='y', histtype='step', label="1.5 inch from LED to diffusor")
    # n2, bins2, patches2 = plt.hist(led2Inch.diff_radi, 100, density=True, facecolor='r', histtype='step', label="2 inch from LED to diffusor")
    #plt.scatter(led2Inch.auxrri[:,0], led2Inch.rri[:,2], label="2 in LED-diffuser")
    #plt.scatter(led1Inch.auxrri[:,0], led1Inch.rri[:,2], label="1 in LED-diffuser")
    plt.legend()
    # plt.xlabel('dist to center of diff (cm)')
    # plt.ylabel('rel # photons')


    plt.show()

    #led2Inch.plotPhotonVectors()
