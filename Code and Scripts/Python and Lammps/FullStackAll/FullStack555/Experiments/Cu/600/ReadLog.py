from re import findall

def read_log():
    log=open('log.lammps','r')
    for i in log.readlines():
        t = i.find('GB energy')
        if(t == 0):
            Energy=i.split(' ')
            GBEnergy = float(Energy[3])
    return GBEnergy
    

