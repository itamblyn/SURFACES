#!/usr/bin/python

import sys
from numpy import *

print 'adjust cx and cy'

def get_center(nCarbon):

    inputFile = open('pos.xyz')
    inputFile.readline() # skip natom
    inputFile.readline() # skip blank
    Cx = 0
    Cy = 0
    for i in range(nCarbon):
        line = inputFile.readline()
        Cx += float(line.split()[1])
        Cy += float(line.split()[2])
    return Cx/float(nCarbon), Cy/float(nCarbon)

    inputFile.close()

def main():
    """
    This is the main function.
    """

    theta = 30

    Cx, Cy = get_center(6)

    theta *= pi/180.

    rotation = matrix([[cos(theta), -sin(theta), 0.0],
                       [sin(theta),  cos(theta), 0.0],
                       [0.0,         0.0,        1.0]])

    inputFile = open('./pos.xyz', 'r')

    natom = int(inputFile.readline().split()[0])
    inputFile.readline() # commentline

    outputXYZFile = open('output.xyz', 'w')
    outputPOSCARFile = open('POSCAR.out', 'w')

    outputXYZFile.write(str(natom)  + '\n')
    outputXYZFile.write('theta: '  + str(theta*(180/pi)) + '\n')

    outputPOSCARFile.write('Selective dynamics\n')
    outputPOSCARFile.write('Cartesian\n')

    for line in inputFile.readlines():

        if line.split()[0] != 'Au':

          name = line.split()[0]
          initial_vector = matrix([float(line.split()[1]) - Cx, float(line.split()[2]) - Cy, float(line.split()[3])])
          final_vector = rotation*initial_vector.T
          outputXYZFile.write(str(name)  + ' ' + str(float(final_vector[0][0]) + Cx) + ' ' + str(float(final_vector[1][0]) + Cy) + ' ' + str(float(final_vector[2][0])) + '\n')
          outputPOSCARFile.write(str(float(final_vector[0][0]) + Cx) + ' ' + str(float(final_vector[1][0]) + Cy) + ' ' + str(float(final_vector[2][0])) + ' T T T\n')

        else:
           outputXYZFile.write(str(line.split()[0]) + ' ' + str(line.split()[1]) + ' ' + str(line.split()[2]) + ' ' + str(line.split()[3]) + '\n')
           outputPOSCARFile.write(str(line.split()[1]) + ' ' + str(line.split()[2]) + ' ' + str(line.split()[3]) + ' F F F\n')

    outputXYZFile.close()
    outputPOSCARFile.close()

if __name__ == '__main__':
    main()

