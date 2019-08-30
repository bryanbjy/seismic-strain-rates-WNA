
#extracting scalar moment and magnitude data
%pylab inline
from math import*
from matplotlib.pyplot import*
from numpy import*
from shapely import*
from shapely.geometry import*
from statistics import*

def m0search():
    infile = open("America_m0.txt", "r") # CMT catalog data as text file    
    f = open('ISC_Catalog.txt','r') #ISC catalog data as text file
    f.readline()
    m0 = []
    m1 = []

    shape, long_lat = key_input()

    for line in infile:
        line = line.split() # convert to list by dropping spaces
        if shape.contains(Point(float(line[0]),float(line[1]))) == True:
            m0.append(float(line[13]))
#    for line in f:
#        line = line.split(',') # convert to list by dropping commas
#        if shape.contains(Point(float(line[5]),float(line[4][1:]))) == True:
#            if line[10][1:4] != '':
#                m1.append(float(line[10][1:4]))
            
    return m0, m1

m0, m1 = m0search()

#Kanamori 1977 moment magnitude equation
def mag_earthquake(x):
    mW = []
    for i in x:
        m = (log10(i*10**-7)-9.1)*(2/3)
        mW.append(m)
        
    return mW

#Maximum Likelihood Estimation
def MLE(m):
    return log10(e)/(mean(m)-min(m))

#Obtaining number of earthquakes bigger or equal to some magnitude
m0big = []
m0big.append(mag_quake)
print(m0big)

mag = [[] for i in range(100)]
count = -1
val = linspace(0,7.5,100)
print(val)
print(len(m0big))

for i in val: # elements in val represent magnitude values to check
    count += 1
    for j in m0big: #goes and checks each magnitude value in list
        if j >= i:
            mag[count].append(j)
            

mag_freq = []

for i in mag:
    mag_freq.append(len(i))



#Example of plot set up, this specific output was not used in the project
x = array(val[:97])
y = array(mag_freq)

coefficients =polyfit(x, numpy.log10(y), 1) #python best fit
polynomial = poly1d(coefficients)
ys = polynomial(x)
print(polynomial)

figure(1, figsize=(10, 6))
xlabel('M_w')
ylabel('Number of earthquakes')
scatter(x,y,marker ='x', label='ISC + CMT Catalog')
plot(x,10**(ys), 'r', label = 'polyfit')
pyplot.legend(('Line of best fit', 'ISC + CMT Catalog'))
xlim(0,7.6)
yscale('log')
title('B-value of SA region, B = 0.428')
savefig('mag_SA_ISC.pdf')
pylab.show()



        