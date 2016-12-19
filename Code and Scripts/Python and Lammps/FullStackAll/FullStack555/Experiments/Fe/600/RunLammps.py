from Quaternion import Quat, normalize
from WriteLammps import write_lammps
from QuantFunc import QuatMat, find_orient, scale
from ReadLog import read_log
#from GenerateAtoms import GenerateAtoms
import os
#NOTE: axis must be along z of q1
q1=normalize([0.4135, 0.5736, 0.4135, 0.5736])
potential='Fe_2.eam.fs'
element='Fe'
temp=600
tempDamp=0.01
lattice=2.855312
minEng=-4.03765613
A=[1,0,0]
typeAtom='bcc'
GBEnergy =[]
Theta = []

for theta in range(0,91):
    q2=find_orient(theta, A, q1)
    M1=scale(QuatMat(q1))
    M2=scale(QuatMat(q2))
    #M1=QuatMat(q1)
    #M2=QuatMat(q2)
    #print 2
    #GenerateAtoms(M1,M2)
    write_lammps(M1,M2,potential,element,temp,tempDamp,theta,lattice,minEng,typeAtom)
    t=os.system('mpirun -np 4 lmp_mpi < GB.in')
    print t
    GBEnergy.append(read_log())
    Theta.append(theta)


filename = str(element) + "_" + str(temp) + "_Data_" + str(A[0]) + str(A[1]) + str(A[2]) + ".txt"

with open(filename, 'w') as fileData:
    for i in range(0,91):
        fileData.writelines(str(Theta[i]) + " " + str(GBEnergy[i]) + "\n")    

print Theta, GBEnergy    
  
 
