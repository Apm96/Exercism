def convert(number):
    Pling = "Pling" #3
    Plang = "Plang" #5
    Plong = "Plong" #7
    
    if number % 3 == 0 and  number % 5 == 0 and  number % 7 == 0:
        return Pling + Plang + Plong
    elif number % 3 == 0 and  number % 5 == 0:
        return Pling + Plang     
    elif number % 3 == 0 and  number % 7 == 0:
        return Pling + Plong  
    elif number % 5 == 0 and  number % 7 == 0:
        return Plang + Plong  
    elif number % 3 == 0 :
        return Pling
    elif number % 5 == 0 :
        return Plang
    elif number % 7 == 0 :
        return Plong
    else:
        return str(number)