arr = [1, 2, 3, 16, 18, 4, 43, 2, 2, 4]

threshold1 = 2
threshold2 = 4

twoexist = False
fourexist = False

for element in arr:   
    
    if element == threshold1 :
        twoexist = True
        print("2 exists")
        
    if element == threshold2 :
        fourexist = True
        print("4 exists")
    else:
        print("it is not 2 or 4.")

    
    
