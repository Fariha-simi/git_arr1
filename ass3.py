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
