for i in range(100):
    if (i+1) % 3 == 0 and (i+1) % 4 == 0:
        print("FIZZ BUZZ")
    
    elif (i+1) % 3 == 0 and (i+1) % 4 !=0 :
        print("Fizz")
    elif (i+1) % 4 == 0 and (i+1) % 3 !=0:
        print ("BUZZ")
    else:
        print (i+1)