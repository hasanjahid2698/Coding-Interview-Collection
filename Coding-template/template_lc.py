import sys
import os
import ast  # To safely parse string representation of lists

def use_files(input_file, output_file):
    if os.path.exists(input_file):
        sys.stdin = open(input_file, 'r')
    if output_file:
        sys.stdout = open(output_file, 'w')

def get_line():
    return sys.stdin.readline().strip()

def get_nested_list():
    return ast.literal_eval(get_line())

def solve(edges):
    return sum(len(edge) for edge in edges)

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    use_files(input_file, output_file)

    edges = get_nested_list() 

    result = solve(edges) 

    print(result)
