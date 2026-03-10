file = open("data.txt", "r")
print("Pointer location before reading:", file.tell())
content = file.read(6)
print("Read content:", content)
print("Pointer location after reading:", file.tell())
file.seek(0)
print("Pointer after seek(0):", file.tell())
content_again = file.read(6)
print("Re-read first 6 characters:", content_again)

file.close()


output
Pointer location before reading: 0
Read content: Ambre 
Pointer location after reading: 6
Pointer after seek(0): 0
Re-read first 6 characters: Ambre 
import os
