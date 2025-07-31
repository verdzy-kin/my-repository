# arr = int(input("Enter the numbers for your array: "))
# for i in arr[5]:
#     arr = arr[i]

# print(arr)

Arr = [2,3,4,5,9,6]
target = int(input("Enter target: "))
average = sum(Arr)/len(Arr)
print(f"average is: {average}") 
for num in Arr:
    if num == target:
        print(f"SEEN!! the average of your array is: {average}")
        break
    else:
        print(f"NOT SEEN!!! the average of your array is: {average}")
        break