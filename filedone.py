f1 = "sample1.txt"
f2= "friends1.txt"

with open(f1, "r") as file1:
    content = file1.read()

with open(f2, "w") as file2:
    file2.write(content)

print("File copied successfully.")


output
File copied successfully.
