import sys
from Matrix import Matrix

def read_from_file(file_name):
    file_obj = open(file_name, "r")
    info = file_obj.read().split()
    return info


if __name__ == '__main__':
    infile_name = sys.argv[1]
    outfile_name = sys.argv[2]
    data = read_from_file(infile_name)
    matrix = Matrix(data[1], data[0], data[2:])