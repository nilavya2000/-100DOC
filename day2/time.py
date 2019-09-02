#task is to take the 12 hr format time and convert it into the 24hr format.
def timeConversion(str1):
    
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 

     
    elif str1[-2:] == "AM": 
        return str1[:-2] 

    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 

    else: 

        return str(int(str1[:2]) + 12) + str1[2:8] 


s = input()
result = timeConversion(s)
print(result)
