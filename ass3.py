arr = [
    1, 2, 3,
    [
        "A", "B",
        [
            "string1", "string2", "string3"
        ]
    ]
]

print(arr[3][2][2])

arr[3][2][2] = "string4"
arr1 = arr[3][2][2]

print(arr1)
print(arr)

arr2 = arr[3][2].pop(2)
print(arr)

arr[3][2].append("string5")
print(arr)

arr3 = [3, 5, 1, 3, 5, 4, 10]
arr3.sort()
print(arr3)

arr3.reverse()
print(arr3)
