# -*- coding: utf-8 -*-
"""
9.5 — Lese dyrebestand-data fra fil

Opphav   : LEO (Lars Erik Opdal), urørt
Status   : LEOs original. To løsninger i én fil: alternativ og pensumbokas
MANGLER  : dyrebestand.txt finnes ikke lokalt — skriptet kan ikke kjøre

Created on Wed Aug 27 10:36:40 2025   (Spyder-stempel fra LEOs egen maskin: @author sto som "lopda".
                             Det var beviset på opphav)
"""

#%% alt. løsning oppg9.5
import numpy as np
import matplotlib.pyplot as plt

M = np.loadtxt('dyrebestand.txt', delimiter=' ')        #data fra 2005-2015
A1 = M[:, 0] #Henter all data fra først kolonne
A2 = M[:, 1] #Henter all data fra andre kolonne

print('M =', M)
print('A1 =', A1)
print('A2 =', A2)


#finn alle fra 2007 - 2011 = 5 år totalt; 5*12 = 60 mnd.

#1år = 12mnd, 2år = 24mnd. osv.
#2005 + 2 år = 2007

# Derfor:
slutt_mnd_nr = 60 + 24 
start_mnd_nr = 24

slutt_mnd_index = slutt_mnd_nr - 1
start_mnd_index = start_mnd_nr - 1

intervall_A1 = A1[start_mnd_index:slutt_mnd_index]
intervall_A2 = A2[start_mnd_index:slutt_mnd_index]

#skal gi ut 24:83
#print(intervall_A1)

min_population = 9999

for index in range(len(intervall_A1)):
    
    print(f'mnd.nr {intervall_A1[index]}, og antlal rein: {intervall_A2[index]} ')
    if min_population > intervall_A2[index]:
        year = divmod(index,12)[0]
        resulat = f'Minste bestand var i år: {year}, mnd.nr {int(intervall_A1[index])},  antall: {intervall_A2[index]}'  


print(resulat)
    

plt.plot(intervall_A1,intervall_A2)
plt.ylabel('Antall rein')
plt.xlabel('Mnd. nr.')


# Antall mnd. med 1000 eller mer observasjoner:
count = np.count_nonzero(A2>1000)

print(f'Det var {count} mnd. tilsammen, der det var observert mer enn 1000 rein..')

#%% løsning pensumboka:
import matplotlib.pyplot as plt
import numpy as np


M = np.loadtxt('dyrebestand.txt', delimiter=' ')

mnd = M[:, 0] 
antall = M[:, 1] 

#pkt1
print('Antall observerte villrein jan 2007 var', 
      antall[12*2])
print('Antall observerte villrein jan 2011 var', 
      antall[12*6])

#pkt2
min_ant = np.argmin(antall)
min_mnd = mnd[min_ant]
aar, maaned = divmod(min_mnd, 12) 
print("Bestanden var paa sitt minste i", int(2005+aar),"i mnd", int(maaned), "med ",int(antall[min_ant])," rein")

#pkt4
tot_mnd = 0
for i in range(0, len(mnd), 1):
    if (antall[i] > 1000):
        tot_mnd = tot_mnd + 1
        
print('Bestanden var over 1000 dyr i', tot_mnd,'mnd')     

#pkt3
plt.close('all')
plt.plot(mnd,antall)
plt.xlabel('mnd')
plt.ylabel('antall')
plt.grid()

# plt.savefig('plott_dyrebestand.pdf')
plt.show()
