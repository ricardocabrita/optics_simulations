import matplotlib.pyplot as plt
import numpy as np
import math

if __name__ == "__main__":

    filename = 'reflectanceSensitivity.csv'
    with open(filename, 'r') as fh:
        lines = fh.readlines()

    reflectance = np.zeros(len(lines))
    normalized = np.zeros(len(lines))
    hits = np.zeros(len(lines))
    max = 0
    for i in range(len(lines)):
        aux = lines[i].split(',')
        reflectance[i] = aux[0]
        hits[i] = aux[1]
        if(hits[i] > max):
            max = hits[i]

    for i in range(len(lines)):
        normalized[i] = hits[i]/max

    plt.figure(1)
    plt.plot(reflectance, normalized)
    plt.title("Set-up sensitivity to reflectance (100000 incident photons)")
    plt.xlabel("reflectance")
    plt.ylabel("detected photons (normalized)")
    plt.xlim(0.95,1)
    plt.show()
