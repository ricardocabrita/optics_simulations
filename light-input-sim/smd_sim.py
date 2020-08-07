from led_object import ledObject
import matplotlib.pyplot as plt

'''
    sim for smd LEDs

'''

if __name__ == "__main__":
    sample_size = 1000000
    distance_to_diffusorCenter = 3.5
    dist_to_pinh = 1.27
    pinh_rad = 0.15
    light_theta = 7.5
    diff_theta = 7.5
    nbins = 100
    x_pos = 0.66
    z_pos = 0

    fig1 = plt.figure(1)

    ledUVsmd = ledObject(sample_size,z_pos, x_pos, distribu_flag=1, rotate_led=False)
    #ledUVsmd = ledObject(sample_size,z_pos, x_pos)
    #ledUVsmd.calcLEDRotationMatrixes(distance_to_diffusorCenter)
    ledUVsmd.dist_to_diff = distance_to_diffusorCenter
    ledUVsmd.simDiffusorEffect(light_theta, diff_theta)
    print("[checkpoint] Done with diffusor simulation")
    phcount, cap_angle = ledUVsmd.simPinholeEffect(1.27, pinh_rad)
    capx0 = ledUVsmd.cap_ph_xpos
    capz0 = ledUVsmd.cap_ph_zpos
    print("2inch from diffusor, half inch from pinhole - Got {}/{} through pinhole!".format(phcount, sample_size))
    n2, bins2, patches2 = plt.hist(cap_angle, nbins, density=True, color='r',histtype='step', label="a=2.0'',c=0.5''")

    fig2 = plt.figure(2)
    plt.scatter(capx0, capz0, c='g',label="a=2.0'',c=1.0''")

    fig3 = plt.figure(3)
    n, bins, patches = plt.hist(ledUVsmd.theta, nbins, density=True, color='r',histtype='step', label="a=2.0'',c=0.5''")

    plt.show()
