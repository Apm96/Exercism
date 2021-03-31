def distance(strand_a, strand_b):
    i=0
    j=0
    k = 0
    count = 0;
    arraya = []
    arrayb = []
    for i, in strand_a:
        arraya.append(i)
    for j, in strand_b:
        arrayb.append(j)
        
    if len(strand_a) != len(strand_b):
        raise ValueError("Longitudes de cadenas diferentes")
    
    
    for k in range(0,len(strand_a)):
        if arraya[k] != arrayb[k]:
            count = count + 1
    
    return count
