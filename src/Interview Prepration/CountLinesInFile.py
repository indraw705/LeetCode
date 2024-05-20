# print number of lines in given file

def countLines(fileName):
    with open(fileName) as f:
        return len(f.readline())
        

print(countLines("../Marevellious/Assingment 5.py"))