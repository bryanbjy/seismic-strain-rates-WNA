#using average between sides to calculate length and width
#Great Circle Distance in metres
from math import*
from numpy import*
def GreatCircleDistance(): #for 4 point polygons
    raw_input = input('(Longitude 1, Latitude 1, Longitude 2, Latitude 2...)  of at least 3 points: ').split(' ')
    R = 6371. * 10**3
    distance_list = []
    side = len(raw_input)/2
    
    if side == 5: #as psmeca format of closing shape with repeated first lon,lat pair
        for i in range(4): 
            if i%2 == 1:
                lon1 = deg2rad(float(raw_input[0 + 2*(i-1)]))
                lat1 = deg2rad(float(raw_input[1 + 2*(i-1)]))
                lon2 = deg2rad(float(raw_input[6]))
                lat2 = deg2rad(float(raw_input[7]))

            elif i%2 == 0:
                lon1 = deg2rad(float(raw_input[int(0+2*i)]))
                lat1 = deg2rad(float(raw_input[int(1+2*i)]))
                lon2 = deg2rad(float(raw_input[2]))
                lat2 = deg2rad(float(raw_input[3]))


#Haversine formula was taken from stackoverflow faq https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2.)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2.)**2
            c = 2. * atan2(sqrt(a), sqrt(1. - a))

            distance = R * c
            print(distance)
            distance_list.append(distance)
                    

    l = (distance_list[0] + distance_list[3])/2
    w = (distance_list[1] + distance_list[2])/2
    
    length = max(l,w) #choosing longer side as length
    return length


#for N!=4 point polygons, using manual inspection
def GreatCircleDistanceM(): 
    raw_input = input('(Longitude 1, Latitude 1, Longitude 2, Latitude 2)  of only 2 points: ').split(' ')
    R = 6371. * 10**3
    lon1 = deg2rad(float(raw_input[0]))
    lat1 = deg2rad(float(raw_input[1]))
    lon2 = deg2rad(float(raw_input[2]))
    lat2 = deg2rad(float(raw_input[3]))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2.)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2.)**2
    c = 2. * atan2(sqrt(a), sqrt(1. - a))

    distance = R * c
    
    return distance


#Area 
import pyproj    
import shapely
import shapely.ops as ops
from shapely.geometry.polygon import Polygon
from functools import partial

def Area_of_zone():
    shape = key_input() #for subregion by subregion input
    
    geom_area = ops.transform(
    partial(
        pyproj.transform,
        pyproj.Proj(init='EPSG:4326'),
        pyproj.Proj(
            proj='aea', #AEA projection
            lat1=shape.bounds[1],
            lat2=shape.bounds[3])),
    shape)
    
    return geom_area.area

#Depth 
#using average depth of earthquake catalog
from shapely import*
from shapely.geometry import*

def depth_of_zone():
    infile = open("America.txt", "r") #CMT catalog data in text file
    shape = key_input()
    depth = []

    for line in infile:
        line = line.split() 

        if shape.contains(Point(float(line[0]),float(line[1]))) == True:
            depth.append(float(line[2]))

        else:
            continue


    depth_avg = sum(depth)/len(depth)

    print(depth)
    print(depth_avg)
    
    return depth_avg*10**3

#Volume 
def Volume(area,depth_avg): #use output of Area_of_zone() and depth_of_zone() as inputs
    return area * depth_avg  

#Fault Depth
#use mttk to get dip of box 
def fault_depth(depth_avg):
    dip = deg2rad(float(input("insert avg dip of zone:"))) #dip should be closer to 90 
    return depth_avg / sin(dip)

#Time Catalogue
from shapely import*
from shapely.geometry import*

def plain_time():
    infile = open("America.txt", "r") #CMT Catalog data in text file
    shape = key_input()

    dates = []

    for line in infile:
        line = line.split() 

        if shape.contains(Point(float(line[0]),float(line[1]))) == True:
            dates.append(line[12])

        else:
            continue

    first_date = dates[0]
    last_date = dates[-1]
    
    return first_date, last_date #takes first and last date info in CMT catalog 

first_date, last_date = plain_time()

def set_time(date):
    if len(date) <= 7: #distinguishing between two writing structures of date info in CMT catalog
        month = int(date[0:2])
        day = int(date[2:4])
        year = int(date[4:6])

        if year < 76:
            year += 100

    else:
        month = int(date[4:6])
        day = int(date[6:8])
        year = int(date[0:4]) - 2000 + 100 
        
    return day,month,year

start = set_time(first_date)
end = set_time(last_date)

def time_catalogue(s,e):
    day1 = s[0]
    month1 = s[1]
    year1 = s[2]
    
    day2 = e[0]
    month2 = e[1]
    year2 = e[2]
    
            
    day_diff = (day2 - day1) * 24. * 60 * 60
    month_diff = (month2 - month1) * 30.4 * 24 * 60 * 60
    year_diff = (year2 - year1) * 12 * 30.4 * 24 * 60 * 60
    
    print(day2-day1, month2-month1, year2-year1)
    total_time = day_diff + month_diff + year_diff 
    
    return total_time

total_time = time_catalogue(start,end)

print(total_time)


