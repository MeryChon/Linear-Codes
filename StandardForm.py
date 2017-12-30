import numpy as np
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
        to_write += "\n"
    for i in column_order:
        to_write += str(i) + " "
    to_write.strip()
    file_obj.write(to_write)
    file_obj.close()


def check_answer(res_file, check_file):
    res_file_obj = open(res_file, 'r')
    info = res_file_obj.read().split()
    num_columns = int(info[0])
    num_rows = int(info[1])
    res_m_obj = Matrix(num_rows, num_rows, info[2:])
    res_m = res_m_obj.get_matrix()
    res_m_col_order = res_m_obj.get_column_order()
    for i in range(len(res_m_col_order)):
        if res_m_col_order[i] != i+1:
            res_m.swap_columns(i, res_m_col_order[i]-1)
    res_m = np.array(res_m)
    print(res_m)
    print("===================================")
    in_file_obj = open(check_file, 'r')
    in_info = in_file_obj.read().split()
    parity_m = np.array(Matrix.create_matrix(in_info[2:]))
    print(parity_m)
    print("===================================")

    res = np.dot(res_m, Matrix.transpose(parity_m))
    print(res)


if __name__ == '__main__':
    infile_name = sys.argv[1]
    outfile_name = sys.argv[2]
    data = read_from_file(infile_name)
    matrix = Matrix(data[1], data[0], data[2:])
    matrix.standardize()
    write_to_file(outfile_name, matrix.get_matrix(), matrix.get_column_order())
    # check_file = sys.argv[3]
    # check_answer(outfile_name, check_file)
