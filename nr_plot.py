import matplotlib.pyplot as plt
import numpy as np
import math

cspeed = 299792458 #m/s

def calc_ev_mass(A, Z):
    #in MeV
    proton_mass = 938.272#/math.pow(cspeed,2)
    neutron_mass = 939.56#/math.pow(cspeed,2)

    return A*proton_mass+Z*neutron_mass

def reduced_mass(m1, m2):
    return (m1*m2)/(m1+m2)

def calc_NR_energy(mN, mX):
    vx = math.pow(10,-3)#*cspeed
    u = reduced_mass(mX, mN)
    return 2*math.pow(u,2)*math.pow(vx,2)/mN

if __name__ == "__main__":
    h2_mass = calc_ev_mass(1,2)
    #si_mass = calc_ev_mass(14,28)
    argon_mass = calc_ev_mass(18,40)
    print("H2 mass: {} MeV".format(h2_mass))
    print("Si28 mass: {} MeV".format(argon_mass))

    mX = np.zeros(20) #in MeV
    Enr_h2 = np.zeros(20)
    #Enr_si = np.zeros(20)
    Enr_ar = np.zeros(20)
    mX[0] = 10#/math.pow(cspeed,2)

    for i in range(0,20):
        Enr_h2[i] = calc_NR_energy(h2_mass, mX[i])*math.pow(10,6) #eV
        #Enr_si[i] = calc_NR_energy(si_mass, mX[i])*math.pow(10,6) #eV
        Enr_ar[i] = calc_NR_energy(argon_mass, mX[i])*math.pow(10,6) #eV
        if i < 19:
            mX[i+1] = mX[i]+20#/math.pow(cspeed,2)

    plt.figure(1)
    plt.plot(mX, Enr_h2)
    #plt.plot(mX, Enr_si)
    plt.plot(mX, Enr_ar)
    plt.title("Nuclear recoil energy as a function of dark matter mass")
    plt.xlabel("mX (MeV)")
    plt.ylabel("Enr (eV)")
    plt.legend(["Hydrogen", "Argon"])
    plt.show()
