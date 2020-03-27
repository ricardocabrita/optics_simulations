from led_object import ledObject
import matplotlib.pyplot as plt
import numpy as np
import math

if __name__ == "__main__":
    sample_size = 1000000
    distance = [1.27, 2.54, 3.5, 5.08]
    pinh_rad = 0.15
    light_theta = 7.5
    diff_theta = 7.5
    phcount = np.zeros((4,4))
    phlog = np.zeros((4,4))

    led = ledObject(sample_size)
    for i in range(0,4):
        led.calcLEDRotationMatrixes(distance[i])
        led.simDiffusorEffect(light_theta, diff_theta)
        for k in range(0,4):
            phcount[i,k], cap_angle = led.simPinholeEffect(distance[k], pinh_rad)
            phlog[i,k] = math.log(phcount[i,k])
            print("{}cm LED-diff | {}cm diff-pinhole __ # photons {}/{}".format(distance[i],distance[k],phcount[i,k], sample_size))


    fig1 = plt.figure(1)
    plt.plot(distance,phcount[0, :], label='0.5in LED-diffuser')
    plt.plot(distance,phcount[1, :], label='1in LED-diffuser')
    plt.plot(distance,phcount[2, :], label='1.5in LED-diffuser')
    plt.plot(distance,phcount[3, :], label='2in LED-diffuser')
    plt.legend()
    plt.xlabel("distance to pinh (cm)")
    plt.ylabel("#photons through")

    fig2 = plt.figure(2)
    plt.plot(distance,phlog[0, :], label='0.5in LED-diffuser')
    plt.plot(distance,phlog[1, :], label='1in LED-diffuser')
    plt.plot(distance,phlog[2, :], label='1.5in LED-diffuser')
    plt.plot(distance,phlog[3, :], label='2in LED-diffuser')
    plt.legend()
    plt.xlabel("distance to pinh (cm)")
    plt.ylabel("#photons through (log)")
    plt.show()
