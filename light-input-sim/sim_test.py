from led_object import ledObject
import matplotlib.pyplot as plt
import matplotlib

if __name__ == "__main__":
    sample_size = 100000#0
    distance_to_diffusorCenter = [1.27, 2.54, 3.5, 5.08]
    light_theta = 7.5
    diff_theta = 7.5
    nbins = 100
    z_pos = 1
    x_pos = 0

    ledHalfInch = ledObject(sample_size, z_pos, x_pos)
    ledHalfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[0])

    led1Inch = ledObject(sample_size, z_pos, x_pos)
    led1Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[1])

    led1halfInch = ledObject(sample_size, z_pos, x_pos)
    led1halfInch.calcLEDRotationMatrixes(distance_to_diffusorCenter[2])

    led2Inch = ledObject(sample_size, z_pos, x_pos)
    led2Inch.calcLEDRotationMatrixes(distance_to_diffusorCenter[3])
