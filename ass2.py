arr = [1, 2, 2, 4, 10, 11, 4, 16, 18, 4, 43, 2, 2, 4]
threshold1 = 2
threshold2 = 4
countthreshold1 = 0
countthreshold2 = 0

for element in arr:
    if element == threshold1 and element==threshold2:
        print(True)

    else:
        print(False)
for element in arr:
    if element == threshold1:
        countthreshold1 +=1
        print("2 exists "+ str(countthreshold1) + "times")
    if element == threshold2:
        countthreshold2 +=1
        print("4 exists "+ str(countthreshold2) + "times")
print("Thanks")


