#File is in the project directory
def toLowerCase(filename):
    with open(filename, 'r') as fileinput:
        for line in fileinput:
            line = line.lower()
            print(line)

if __name__ == '__main__':
    filename = input()
    toLowerCase(filename)
