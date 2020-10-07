import numpy as np
# Create an empty array
x = np.empty([4], np.int16)
print(x)

# import numpy as np
# x = [10, 20, 30]
# print("Original array:")
# print(x)
# x = np.append(x, [[40, 50, 60], [70, 80, 90]])
# print("After append values to the end of the array:")
# print(x)

x = np.append(x, 40)
print("After append values to the end of the array:")
print(x)
x = np.append(x, 22)
print("After append values to the end of the array:")
print(x)
x = np.append(x, 15)
print("After append values to the end of the array:")
print(x)
x = np.append(x, 10)
print("After append values to the end of the array:")
print(x)

x = np.append(x, 9)
print("After append values to the end of the array:")
print(x)