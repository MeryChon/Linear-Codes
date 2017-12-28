import sys
from Matrix import Matrix


def read_from_file(file_name):
    file_obj = open(file_name, "r")
    info = file_obj.read().split()
    return info


def write_to_file(file_name, matrix, column_order):
    file_obj = open(file_name, "w")
    to_write = str(len(matrix[0])) + " " + str(len(matrix)) + "\n"
    for r in matrix:
        for i in r:
            to_write += str(i)
        to_write+="\n"
    for i in column_order:
        to_write += str(i) + " "
    to_write.strip()
    file_obj.write(to_write)


if __name__ == '__main__':
    infile_name = sys.argv[1]
    outfile_name = sys.argv[2]
    data = read_from_file(infile_name)
    matrix = Matrix(data[1], data[0], data[2:])
    matrix.gauss_jordan()
    write_to_file(outfile_name, matrix.get_matrix(), matrix.get_column_order())