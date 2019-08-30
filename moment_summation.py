from shapely import*
from shapely.geometry import*

def M_summation():
    infile = open("America.txt", "r") #CMT catalog data in text file

    Mlist = []

    m11_new = 0
    m22_new = 0
    m33_new = 0
    m12_new = 0
    m13_new = 0
    m23_new = 0

    shape = key_input() #for subregion by subregion input

#   boxes = automate_parse() #for parsing through all subregion from text file
#   for i in boxes:
#       print(i)
#       shapes = Polygon(i)


    for line in infile:
        line = line.split() 

        if shape.contains(Point(float(line[0]),float(line[1]))) == True:
            m11 = float(line[3]) * 10**float(line[9]) 
            m22 = float(line[4]) * 10**float(line[9])
            m33 = float(line[5]) * 10**float(line[9])
            m12 = float(line[6]) * 10**float(line[9])
            m13 = float(line[7]) * 10**float(line[9])
            m23 = float(line[8]) * 10**float(line[9])

            print(float(line[0]),float(line[1]))

            m11_new += m11 
            m22_new += m22
            m33_new += m33
            m12_new += m12
            m13_new += m13
            m23_new += m23

        else:
            continue


    Mlist= [m11_new, m22_new, m33_new, m12_new, m13_new, m23_new] 

    return Mlist

