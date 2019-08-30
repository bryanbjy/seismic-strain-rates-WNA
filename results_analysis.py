#Results for strain, strain rate and velocity
import pandas as pd
import os
from statistics import*

data = pd.read_csv('Results(units).txt', sep=" ", header=0)

vel_calculated = round(data['plate_velocity'],1)

vel_dev = round(stdev(vel_calculated),1)
vel_var = round(variance(vel_calculated),1)
vel_mean = round(mean(vel_calculated),1)
vel_median = round(median(vel_calculated),1)

# Geodetic velocities
data3 = pd.read_csv('vel_compare.txt', sep=",", header=0)

vel_geo = round(data3[' Velocity(mmyr-1)'],1)
vel_g_dev = round(stdev(vel_geo),1)
vel_g_var = round(variance(vel_geo),1)
vel_g_mean = round(mean(vel_geo),1)
vel_g_median = round(median(vel_geo))


#percentage differences in velocity
v_diff = []
for i, j in zip(vel_calculated,vel_geo):
    v_diff.append(round((((j-i)/j) * 100),1))
 

#average depth calculation and plot
depth = []
with open('Variables of Box.txt','r') as f:
    f.readline()
    for line in f:
        line = line.split()
        depth.append(float(line[2]))

%pylab inline
from math import*
from matplotlib.pyplot import*
x = linspace(1,21,21)
print(x)
bar(x,depth, color = 'red')
xlabel('Box number')
ylabel('Average Depth(m)')
title('Depth average of all sub regions')
savefig('depth_average')
pylab.show()

#depth correction calculation and plot

depth = []
fault_depth = []
with open('Variables of Box.txt','r') as f:
    f.readline()
    for line in f:
        line = line.split()
        depth.append(float(line[2]))
        fault_depth.append(float(line[4]))
        

fault_depth2 = []
fault_depth3 = []
fault_depth4 = []

with open('Variables of Box copy.txt','r') as f:
    f.readline()
    for line in f:
        line = line.split()
        ratio = (float(line[4]))/(float(line[2]))
        fault_depth2.append(3*ratio*1000)
        fault_depth3.append(6*ratio*1000)
        fault_depth4.append(9*ratio*1000)

        
val_ratio = []
val_ratio2 = []
val_ratio3 = []
for i in depth:
    val_ratio.append(3000/i)
    print(i)

for i in depth:
    val_ratio2.append(6000/i)
    print(i)
    
for i in depth:
    val_ratio3.append(9000/i)
    print(i)

vel_corrected = []
for i,j in zip(vel_calculated,val_ratio):
    vel_corrected.append(i/j)
print(vel_corrected[6:])

vel_corrected2 = []
for i,j in zip(vel_calculated,val_ratio2):
    vel_corrected2.append(i/j)
print(vel_corrected2[6:])

vel_corrected3 = []
for i,j in zip(vel_calculated,val_ratio3):
    vel_corrected3.append(i/j)
print(vel_corrected3[6:])

v_diff2 = []
for i,j in zip(vel_geo, vel_corrected):
    a = (i-j)/i
    v_diff2.append(round((a*100),1))

v_diff3 = []
for i,j in zip(vel_geo, vel_corrected2):
    a = (i-j)/i
    v_diff3.append(round((a*100),1))

v_diff4 = []
for i,j in zip(vel_geo, vel_corrected3):
    a = (i-j)/i
    v_diff4.append(round((a*100),1))

import numpy as np
import matplotlib.pyplot as plt

N = 21
ind = np.arange(N)  # the x locations for the groups
width = 0.18# the width of the bars

fig = figure(1, figsize=(15, 8))
ax = fig.add_subplot(111)

rects1 = ax.bar(ind, v_diff2[:], width, color='purple')
rects2 = ax.bar(ind+width, v_diff3[:], width, color='orange')
rects3 = ax.bar(ind+2*width, v_diff4[:], width, color='pink')
rects4 = ax.bar(ind+3*width, v_diff[:], width, color='royalblue')


# add plot
ax.set_ylabel('Percentage Difference (%)')
ax.set_title('Geodetic velocity percentage differences of original and depth-corrected velocities')
ax.set_xticks(ind + 3*width/2 )
ax.set_xticklabels( ('7', '8', '9', 
                     '10', '11', '12', 
                    '13','14', '15', '16',
                    '17', '18', '19', '20','21') )

ax.legend((rects1[0], rects2[0],rects3[0],rects4[0]), ( 'd = 3km corrected velocity','d = 6km corrected velocity','d = 9km corrected velocity','Original velocity') )
ax.set_ylim(-100,100)
ax.axhline(0, color="black")
plt.show()
