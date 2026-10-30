# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    if line_number <= 0:
        return ""
    file = open(filename, "r")
    line = ""
    for _ in range(line_number):
        line = file.readline()
        if line == "":
            file.close()  # Close the file before returning if line isn't found
            return ""
    file.close()  # Close the file after finding the target line
    return line.rstrip("\n")
# Exercise 2
def reverse_lines(source, destination):
    file = open(source, "r")
    lines = file.readlines()
    file.close()

    output = open(destination, "w")

    count = 0

    for line in reversed(lines):
        output.write(line.strip() + "\n")
        count = count + 1

    output.close()

    return count
# Exercise 3
def merge_files(first, second, destination):
    file1 = open(first, "r")
    lines1 = file1.readlines()
    file1.close()

    file2 = open(second, "r")
    lines2 = file2.readlines()
    file2.close()

    file3 = open(destination, "w")

    count = 0

    for line in lines1:
        file3.write(line.strip() + "\n")
        count = count + 1

    for line in lines2:
        file3.write(line.strip() + "\n")
        count = count + 1

    file3.close()

    return count

# Exercise 4
def find_score(filename, name):
    file = open(filename, "r")

    for line in file:
        data = line.strip().split(",")

        if data[0] == name:
            score = int(data[1])
            file.close()
            return score

    file.close()

    return -1


# Exercise 5
def update_score(filename, name, new_score):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    found = False

    for i in range(len(lines)):
        data = lines[i].strip().split(",")

        if data[0] == name:
            lines[i] = name + "," + str(new_score) + "\n"
            found = True
            break

    if found == False:
        return False

    file = open(filename, "w")

    for line in lines:
        file.write(line)

    file.close()

    return True
