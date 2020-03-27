from led_object import ledObject
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sample_size = 10000
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    light_theta = 7.5
    diff_theta = 7.5
    led_z_pos = 0.66

    led2Inch = ledObject(sample_size, 0.66)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])
    led2Inch.simDiffusorEffect(light_theta, diff_theta)

    print(led2Inch.auxrri[3,:])
    fig1 = plt.figure(1)
    #plt.scatter(led2Inch.rf[:,0], led2Inch.rf[:,2], label="after diffuser")
    plt.scatter(led2Inch.rri[:,0], led2Inch.rri[:,2], label="at diffuser")
    plt.scatter(led2Inch.ri[:,0], led2Inch.ri[:,2], label="start")
    plt.scatter(led2Inch.auxrri[:,0], led2Inch.auxrri[:,2], label="led positioned")
    # n2, bins2, patches2 = plt.hist(led2Inch.diff_polar_angle, 100, density=True, facecolor='r', histtype='step', label="2 inch from LED to diffusor")
    plt.legend()
    # #plt.title("Final polar angle distribution")
    # plt.xlabel('degrees')
    # plt.ylabel('rel # photons')
    #
    plt.show()

    #led2Inch.plotPhotonVectors()
