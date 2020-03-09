import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import math

if __name__ == "__main__":

    #speed of light
    cspeed = 299792458 #m/s
    filename = "thisTimeSpectrum.txt"

    with open(filename, 'r') as fh:
        lines = fh.readlines()

    d = np.zeros(len(lines))
    counts = np.zeros(len(lines))

    for l in range(0, len(lines)):
        aux = lines[l].split(" ")
        #d = c * t
        d[l] = (cspeed/math.pow(10,9))*float(aux[0])
        counts[l] = aux[1]
        print("line {}: distance: {} counts: {}".format(l, d[l], counts[l]))

    alpha, loc, beta = stats.gamma.fit(counts)
    print("Gamma params: alpha {} | loc {} | beta {}".format(alpha,loc,beta))
    #print("counts size: {}".format(counts.size))
    #fitted_data = stats.gamma.pdf(d, alpha, loc=loc, scale=beta)
    plt.figure(1)
    plt.plot(d, counts)
    #plt.hist(d, counts, histtype='stepfilled')
    plt.title("Photon traveled length")
    plt.xlabel("distance (meters)")
    plt.ylabel("photon counts")
    plt.xlim(0,17)

    plt.figure(2)
    #rv = stats.gamma(alpha)
    #plt.plot(d, stats.gamma.pdf(d, alpha, loc, beta), 'r-')
    plt.show()
