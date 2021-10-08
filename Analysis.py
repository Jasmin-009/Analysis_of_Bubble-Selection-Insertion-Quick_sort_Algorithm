size=[10000,20000,50000,100000]
algoBu_s=[6.28918194770813,25.189634323120117,159.7248408794403,672.5682911872864]
algoBu_u=[17.130190134048462,68.6713490486145,434.44215178489685,1841.2352640628815]
algoBu_r=[11.466334819793701,46.13661479949951,292.3579227924347,1244.9343662261963]

algoIn_s=[0.002991914749145508,0.0049855709075927734,0.011967658996582031,0.02593088150024414]
algoIn_u=[15.829405307769775,63.20769143104553,396.22968339920044,1701.398619890213]
algoIn_r=[7.795156478881836,31.340184688568115,199.2878224849701,845.0197792053223]

algoSe_s=[4.953391075134277,19.64346933364868,123.77096343040466,498.2464978694916]
algoSe_u=[5.23390531539917,20.88235330581665,131.23458671569824,528.6622250080109]
algoSe_r=[4.925585508346558,19.671255826950073,123.83245086669922,497.10890078544617]

algoQi_s=[13.875180006027222,55.56071925163269,352.1024212837219,1411.619601726532]
algoQi_u=[8.767875671386719,35.368497133255005,227.07579493522644,903.13676404953]
algoQi_r=[0.15514397621154785,0.5767226219177246,3.5308501720428467,14.208581686019897]

algoMs_s=[0.05884265899658203,0.12644577026367188,0.3440995216369629,0.7350339889526367]
algoMs_u=[0.0578463077545166,0.12366962432861328,0.3410987854003906,0.7250611782073975]
algoMs_r=[0.06682014465332031,0.1436154842376709,0.424835205078125,0.840749979019165]

import numpy as np
import matplotlib.pyplot as plt
N = 4
ind = np.arange(N) 
width = 0.25
#--------Bubble-------------------------------------------  
bar1 = plt.bar(ind, algoBu_s, width, color = 'r')
bar2 = plt.bar(ind+width, algoBu_u, width, color='g')
bar3 = plt.bar(ind+width*2, algoBu_r, width, color = 'b')
  
plt.xlabel("Size")
plt.ylabel('Time (s)')
plt.title("Bubble Sort")
  
plt.xticks(ind+width,size)
plt.legend( (bar1, bar2, bar3), ('Sorted(Aesc)', 'Sorted(Desc)', 'Random') )
plt.show()
#--------Insertion-------------------------------------------  

bar1 = plt.bar(ind, algoIn_s, width, color = 'r')
bar2 = plt.bar(ind+width, algoIn_u, width, color='g')
bar3 = plt.bar(ind+width*2, algoIn_r, width, color = 'b')
  
plt.xlabel("Size")
plt.ylabel('Time (s)')
plt.title("Insertion Sort")
  
plt.xticks(ind+width,size)
plt.legend( (bar1, bar2, bar3), ('Sorted(Aesc)', 'Sorted(Desc)', 'Random') )
plt.show()
#--------Selection-------------------------------------------  

bar1 = plt.bar(ind, algoSe_s, width, color = 'r')
bar2 = plt.bar(ind+width, algoSe_u, width, color='g')
bar3 = plt.bar(ind+width*2, algoSe_r, width, color = 'b')
  
plt.xlabel("Size")
plt.ylabel('Time (s)')
plt.title("Selection Sort")
  
plt.xticks(ind+width,size)
plt.legend( (bar1, bar2, bar3), ('Sorted(Aesc)', 'Sorted(Desc)', 'Random') )
plt.show()
#--------Quick-------------------------------------------  

bar1 = plt.bar(ind, algoQi_s, width, color = 'r')
bar2 = plt.bar(ind+width, algoQi_u, width, color='g')
bar3 = plt.bar(ind+width*2, algoQi_r, width, color = 'b')
  
plt.xlabel("Size")
plt.ylabel('Time (s)')
plt.title("Quick Sort")
  
plt.xticks(ind+width,size)
plt.legend( (bar1, bar2, bar3), ('Sorted(Aesc)', 'Sorted(Desc)', 'Random') )
plt.show()
N = 4
ind = np.arange(N) 
width = 0.2
#--------Sorted------------------------------------------- 
bar1 = plt.bar(ind, algoBu_s, width, color = 'r')
bar2 = plt.bar(ind+width, algoIn_s, width, color='g')
bar3 = plt.bar(ind+(width*2), algoSe_s, width, color = 'b')
bar4 = plt.bar(ind+(width*3), algoQi_s, width, color = 'y')
  

plt.xlabel("Size")
plt.ylabel('Time (s)')
plt.title("Sorted (Aesc)")
  
plt.xticks(ind + width + width/2,size)
plt.legend( (bar1, bar2, bar3,bar4), ('Bubble', 'Insertion', 'Selection','Quick') )
plt.show() 
#--------UnSorted------------------------------------------- 
bar1 = plt.bar(ind, algoIn_u, width, color = 'r')
bar2 = plt.bar(ind+width,algoBu_u , width, color='g')
bar3 = plt.bar(ind+(width*2), algoSe_u, width, color = 'b')
bar4 = plt.bar(ind+(width*3), algoQi_u, width, color = 'y')
  

plt.xlabel("Size")
plt.ylabel('Time (s)')
plt.title("Sorted(Desc)")
  
plt.xticks(ind + width + width/2,size)
plt.legend( (bar1, bar2, bar3,bar4), ('Bubble', 'Insertion', 'Selection','Quick') )
plt.show()  
#--------Random-------------------------------------------  
bar1 = plt.bar(ind, algoBu_r, width, color = 'r')
bar2 = plt.bar(ind+width, algoIn_r, width, color='g')
bar3 = plt.bar(ind+(width*2), algoSe_r, width, color = 'b')
bar4 = plt.bar(ind+(width*3), algoQi_r, width, color = 'y')
  

plt.xlabel("Size")
plt.ylabel('Time (s)')
plt.title("Random")
plt.xticks(ind + width + width/2,size)
plt.legend( (bar1, bar2, bar3,bar4), ('Bubble', 'Insertion', 'Selection','Quick') )
plt.show()
