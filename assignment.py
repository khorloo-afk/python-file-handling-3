# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    # Write your code here
    pass

# Exercise 2
def reverse_lines(source, destination):
    def reverse_lines(source, destination):
    with open(source, "r") as f:
        lines = [line.strip() for line in f]
    lines.reverse()
    with open(destination, "w") as f:
        for line in lines:
            f.write(line + "\n")
            
    return len(lines)

# Exercise 3
def merge_files(first, second, destination):
    # Write your code here
    pass

# Exercise 4
def find_score(filename, name):
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
