from led_object import ledObject
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

if __name__ == "__main__":
    sample_size = 1000000
    distance = [1.27, 2.54, 3.5, 5.08]
    pinh_rad = 0.15
    light_theta = 7.5
    diff_theta = 7.5
    phcount = np.zeros((4,4))
    x_pos = 0
    z_pos = 0.66

    led = ledObject(sample_size,z_pos, x_pos)
    for i in range(0,4):
        led.calcLEDRotationMatrixes(distance[i])
        led.simDiffuserEffect(light_theta, diff_theta)
        for k in range(0,4):
            phcount[i,k], cap_angle = led.simPinholeEffect(distance[k], pinh_rad)
            print("{}cm LED-diff | {}cm diff-pinhole __ # photons {}/{}".format(distance[i],distance[k],phcount[i,k], sample_size))

    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : 12}
    matplotlib.rc('font', **font)

    fig1 = plt.figure(1)
    plt.plot(distance,phcount[0, :]/sample_size, label="a=0.5''",c='r')
    plt.plot(distance,phcount[1, :]/sample_size, label="a=1.0''",c='g')
    plt.plot(distance,phcount[2, :]/sample_size, label="a=1.5''",c='b')
    plt.plot(distance,phcount[3, :]/sample_size, label="a=2.0''",c='y')
    plt.legend()
    plt.xlabel("distance to pinhole (cm)")
    plt.ylabel("% photons through")

    plt.show()
