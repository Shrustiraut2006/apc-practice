# #file handling

# #read
# file = open("example.txt", "r")
# print(file.read())
# file.close()

# #write
# file = open("example.txt", "w")
# data = input("Enter data to write: ")
# file.write(data)
# file.close()
# print("Data written successfully.")

# #Append
# file = open("example.txt", "a")
# data = input("Enter data to append: ")
# file.write("\n" + data)
# file.close()
# print("Data appended successfully.")

# #read and write
# file = open("example.txt", "r+")
# print("Existing content:")
# print(file.read())
# data = input("Enter data to write: ")
# file.write(data)
# file.close()

# #write and read
# file = open("example.txt", "w+")
# data = input("Enter data: ")
# file.write(data)
# file.seek(0)
# print("File content:")
# print(file.read())
# file.close()

# #Append and read
# file = open("example.txt", "a+")
# data = input("Enter data to append: ")
# file.write("\n" + data)
# file.seek(0)
# print("File content:")
# print(file.read())
# file.close()

# #Create and write
# filename = input("Enter new file name: ")
# file = open(filename, "x")
# data = input("Enter data: ")
# file.write(data)
# file.close()
# print("File created successfully.")

# #read()
# file = open("example.txt", "r")
# print(file.read())
# file.close()

# #readline()
# file = open("example.txt", "r")
# print(file.readline())
# file.close()

# #readlines()
# file = open("example.txt", "r")
# print(file.readlines())
# file.close()

# #writelines()
# file = open("example.txt", "w")
# data1 = input("Enter first line: ")
# data2 = input("Enter second line: ")
# data3 = input("Enter third line: ")
# lines = [data1 + "\n", data2 + "\n", data3 + "\n"]
# file.writelines(lines)
# file.close()
# print("Data written successfully.")