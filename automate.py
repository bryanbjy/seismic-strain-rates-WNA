def automate_parse():
    with open('coordinates_boxes.txt','r') as f: #file of longitude, latitude pairs that bound a subregion
        boxes = [[] for i in range(21)]
        counter = -1
        for line in f:
            line = line.split()
            if line[0][0] == "-":
                line[0] = float(line[0])
                line[1] = float(line[1])
                boxes[counter].append(line)
            else:
                counter += 1
                
    
    return boxes