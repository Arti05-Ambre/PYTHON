print("file contents:\n")
try:
    with open("sample1.txt","r")as file:
        for line in file:
            print(line,end="")
except FileNotFoundError:
    print("File not found.Please create sample.txt first.")









output

file contents:

Sahakar Maharshi Bhausaheb Thorat
Arti Dipak Ambre
BSC Computer science
