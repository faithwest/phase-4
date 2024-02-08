# arr = []

# begin="A"
# last_letter="Z"
# for k in range(ord(begin),ord(last_letter)+1):
#     char=chr(k)
#     if k == 'A':
#         arr.append(chr(ord(char) + 1))  # Increment 'A' to 'B' and append to arr
#     else:
#         arr.append(k)  # Append other kacters as they are

# # Print the updated array
# print("Updated array:", arr)
# array=[]

#     if platenumber in array:
#         print('NUMBER PLATE EXIST!!':platenumber)
#     elif:
-#         array.append(arr[i])
#         print('NUMBER PLATE NOT FOUND!!')
#         array.append(arr[-1])
#         array.
#         new-plate = array[array.index(arr[1])]
#         print('NEW NUMBER PLATE IS :',new-plate)

# arr = ['001','008','025']
# print(checkPlateExist(arr,'009'))
# print("Updated array:", arr)
#         arr.append(chr(ord(char) + 1))  # Increment 'A' to 'B' and append to arr
#     else:
#         arr.append(k)  
arr = ['001', '002', '003']  # Example array
carplate_to_check = '002'  # Number plate to check

# Check if the number plate exists in the array
if carplate_to_check in arr:
    print('NUMBER PLATE EXISTS:', carplate_to_check)
else:
    print('NUMBER PLATE NOT FOUND:', carplate_to_check)
    # If the number plate doesn't exist, add it to the array and increment
    arr.append(arr[-1])  # Append the last element of the array
    num = int(arr[-1]) + 1  # Increment the last element
    #arr[-1] = str(num).zfill(3)  # Convert back to string and zero-pad to three digits
    print('NEW NUMBER PLATE ADDED:', arr[-1])

# Print the updated array
print("Updated array:", arr)
