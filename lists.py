# # # # Example
# # # my_list = [1, 2, 3, "apple", True]

# # # # Accessing elements (index starts at 0)
# # # print(my_list[0])  # Outputs 1

# # # # Modifying an element
# # # my_list[1] = 10

# # # # Adding and removing elements
# # # my_list.append("banana")  # Add to the end
# # # my_list.remove(10)  # Remove element


# #  #pyhton tuples
# #  # 1. Creating a tuple
# # my_tuple = (1, 2, 3, 4, 5)
# # print("Original tuple:", my_tuple)

# # # 2. Accessing elements in a tuple
# # print("First element:", my_tuple[0])
# # print("Last element:", my_tuple[-1])

# # # 3. Slicing a tuple
# # print("Elements from index 1 to 3:", my_tuple[1:4])

# # # 4. Tuples are immutable, so you cannot change elements
# # try:
# #     my_tuple[0] = 10
# # except TypeError as e:
# #     print("Error:", e)

# # # 5. Concatenating two tuples
# # tuple1 = (6, 7, 8)
# # tuple2 = (9, 10)
# # new_tuple = tuple1 + tuple2
# # print("Concatenated tuple:", new_tuple)

# # # 6. Unpacking a tuple
# # a, b, c, d, e = my_tuple
# # print("Unpacked values:", a, b, c, d, e)

# # # 7. Using tuples in functions
# # def get_coordinates():
# #     return (5, 10)

# # coordinates = get_coordinates()
# # print("Function returned tuple:", coordinates)

# # # 8. Length of a tuple
# # print("Length of my_tuple:", len(my_tuple))

# # # 9. Checking if an element exists in a tuple
# # if 3 in my_tuple:
# #     print("3 is in the tuple")

# # # 10. Looping through a tuple
# # for item in my_tuple:
# #     print("Tuple element:", item)
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return "Stack is empty"

#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             return "Stack is empty"

#     def is_empty(self):
#         return len(self.stack) == 0

# # Example usage
# stack = Stack()
# stack.push(1)
# stack.push(2)
# print("Top element:", stack.peek())
# print("Popped element:", stack.pop())
# print("Is stack empty?", stack.is_empty())
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()
