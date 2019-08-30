#generating points for UNAVCO plate motion

import numpy as np
from shapely import*
from shapely.geometry import*

def random_point_generator():
    shape, long_lat = key_input()
    
    lon = []
    lat = []
    
    for i in long_lat:
        lon.append(i[0])
        lat.append(i[1])
        
        
    lon_new = []
    lat_new = []
    
    for i in range(30):
        lon_generator = np.random.uniform(min(lon),max(lon))
        lat_generator = np.random.uniform(min(lat),max(lat))
        lon_new.append(lon_generator)
        lat_new.append(lat_generator)
    
    point_new = []
    
    for i, j in zip(lon_new,lat_new):
        point_new.append((i,j))
    print(point_new)
    
    points = []
    
    for i in point_new:
        j = i
        i = Point(i)
        if shape.contains(i) == True:
            points.append(j)
    
    return points


points = random_point_generator()

#extracting from UNAVCO Global Strain Rate data

def GlobalStrainRate():
    shape, long_lat = key_input()
    
    lon = []
    lat = []
    T = []
    P = []
    a = []
    
    with open("Global_strainrate.txt","r") as f:
        for line in f:
            line = line.split()
            if line[0] != 'LAT.' and shape.contains(Point(float(line[0]),float(line[1]))) == True :
                lon.append(float(line[0]))
                lat.append(float(line[1]))
                T.append(float(line[3]))
                P.append(float(line[4]))
                a.append(float(line[2]))
                
    return lon,lat, T, P, a

lon, lat, T, P, Azimuth = GlobalStrainRate()
T_avg = sum(T)/len(T)
P_avg = sum(P)/len(P)
Azimuth_avg = sum(Azimuth)/len(Azimuth)

