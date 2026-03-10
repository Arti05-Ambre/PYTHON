filename = "data.txt"

with open(filename, "r") as file:
    content = file.read()
    
    characters = len(content)
    words = len(content.split())
    lines = len(content.splitlines())

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of lines:", lines)


output
Number of characters: 10
Number of words: 2
Number of lines: 1
