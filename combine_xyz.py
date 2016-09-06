import numpy as np


def get_center_of_mass(molecule):

    natom = len(molecule)
    Cx = 0.
    Cy = 0.
    for i in range(natom):
        Cx += float(molecule[i][0])
        Cy += float(molecule[i][1])
    return Cx/natom, Cy/natom


def main():

  molecule_coords = np.loadtxt('N_linear.xyz',skiprows=2, usecols=(1,2,3))
  molecule_species = np.loadtxt('N_linear.xyz',dtype=str,skiprows=2, usecols=(0,))

  surface_coords =  np.loadtxt('armchair.xyz',skiprows=2, usecols=(1,2,3))
  surface_species = np.loadtxt('armchair.xyz',dtype=str,skiprows=2, usecols=(0,))

  combined_coords = np.vstack((molecule_coords, surface_coords))
  combined_species = np.concatenate((molecule_species, surface_species), axis=0)

  shifted_molecule = get_center_of_mass(molecule_coords)
  print(shifted_molecule)

  natom = len(combined_coords)

  outputFile = open('test.out','w')

  for i in range(natom):
      outputFile.write(str(combined_species[i][-2]) +'\n')



if __name__ == '__main__':
    main()

