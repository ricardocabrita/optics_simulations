import matplotlib.pyplot as plt
import math
import numpy as np

def rayleigh_Xsec_molecule(wl, alpha):
    '''
        wl - wavelength
        alpha - polarizability
    '''
    return (16*math.pow(math.pi, 5))/3*(math.pow(alpha,2)/math.pow(wl,4))

def calc_polarizability(M, p, n):
    '''
        M - molar mass
        p - density
        n - refractive index
    '''
    #avogadros constant
    nA = 6.022*math.pow(10,23)
    #molar refractivity
    R = (M/p)*((math.pow(n,2)-1)/(math.pow(n,2)+2))
    #polarizability
    return (R/nA)*(3/(4*math.pi))

if __name__ == "__main__":
    #physcis constants
    nA = 6.022*math.pow(10,23)
    # from https://refractiveindex.info/
    '''
        At 500nm, water's refractive index - 1.335
    '''
    wl = 250*math.pow(10,-9) #wavelength in meters
    n = 1.362#1.396#1.335
    M = 18.01528 #g/mol water molar mass
    p = 997000 #g/m3 water density

    alpha = calc_polarizability(M,p,n)
    print("Polarizability of water: {}".format(alpha))

    xsec = rayleigh_Xsec_molecule(wl, alpha)
    print("Rayleigh Cross section of water at 250nm: {}".format(xsec))

    #N - number of molecules per unit volume (m3)
    N = (p/M)*nA
    print("Number of water molecules per m3: {}".format(N))

    #rayleigh mean free path (m)
    rmfp = 1/(N*xsec)
    print("Rayleigh mean free path for water at 250nm in m: {}".format(rmfp))
