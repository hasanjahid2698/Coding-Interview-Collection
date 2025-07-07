import sys
import os

# Function to redirect input and output to files
def use_files(input_file, output_file):
    if os.path.exists(input_file):
        sys.stdin = open(input_file, 'r')
    if output_file:
        sys.stdout = open(output_file, 'w')

# Fast input function
def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, sys.stdin.readline().split()))

def get_int():
    return int(sys.stdin.readline())

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    use_files(input_file, output_file)

    # Your main program logic here
    n = get_int()
    for i in range(n):
        a, b = get_ints()
        print(a + b)