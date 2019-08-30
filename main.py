def key_input():
    
    raw_input = input('(Longitude 1, Latitude 1, Longitude 2, Latitude 2...)  of at least 3 points: ').split(' ') 
    print(raw_input) #allows for N number of longitude and latitude pairs, delimited by whitespace 
    starter = []
    long_lat = []
    count = 0
    iteration = 0
    
    for i in raw_input:
        iteration += 1

        if count < 2:
            starter.append(float(i))
            if iteration == len(raw_input):
                long_lat.append(starter)

        else:
            long_lat.append(starter)
            starter = []
            starter.append(float(i))
            count = 0
        count += 1


    shape = Polygon(long_lat)
    
    print(long_lat)
    
    return shape