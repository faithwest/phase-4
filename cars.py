# def carplates():
#     plate = "KAA 001 A"
#     k = plate.split(" ")
#     print('plate', k)
#     if k[A]=="A":






#     # if k[2] == "A":
#     #     if k[1] not in arrA or k[2] not in arrB:
#     #         arrA.append(k[1]) 
#     #         arrB.append(chr(ord(k[2]) + 1))
#     #         return True
    

# arrA = []
# arrB = []

# print(carplates())
# print("Updated arrA:", arrA)
# print("Updated arrB:", arrB)
# Example empty array

def solution(plate):
    if plate == "KZZ999Z":
        return plate
    current_plate = list(plate)
    i = len(current_plate) - 1
    while i >= 0:
        print("second last index", current_plate[i])
        if current_plate[i] < "Z":
            current_plate[i] = chr(ord(current_plate[i]) + 1)
            break
        elif current_plate[i] == "Z":
            current_plate[i] = "A"
            i -= 1
            if i < 0:
                break

return "".join(current_plate)
print(solution("KAA008Z"))