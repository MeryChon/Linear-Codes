import numpy
import sys
from Matrix import Matrix


def read_from_file(file_name):
    file_obj = open(file_name, "r")
    info = file_obj.read().split()
    return info


def write_to_file(file_name, matrix):
    file_obj = open(file_name, "w")
    to_write = str(len(matrix[0])) + " " + str(len(matrix)) + "\n"
    for r in matrix:
        for i in r:
            to_write += str(i)
        to_write += "\n"
    file_obj.write(to_write)
    file_obj.close()


def check_answer(res_file, in_file):
    res_file_obj = open(res_file, 'r')
    info = res_file_obj.read().split()
    num_columns = int(info[0])
    num_rows = int(info[1])
    res_m_obj = Matrix(num_rows, num_columns, info[2:])
    res_m = numpy.array(res_m_obj.transpose(res_m_obj.get_matrix()))
    print(res_m)

    in_file_obj = open(in_file, 'r')
    in_info = in_file_obj.read().split()
    in_num_columns = int(in_info[0])
    in_num_rows = int(in_info[1])
    generator_m_obj = Matrix(in_num_rows, in_num_columns, in_info[2:])
    column_order = generator_m_obj.get_column_order()
    for i in range(len(column_order)):
        if column_order[i] != i+1:
            generator_m_obj.swap_columns(i, column_order[i]-1)
    # generator = generator_m_obj.get_matrix()
    generator_m = numpy.array(generator_m_obj.get_matrix())
    print(generator_m)
    product = numpy.dot(generator_m, res_m)
    print(type(product), type(product[0]))
    Matrix.print_matrix(product)


if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    check_file = sys.argv[3]
    data = read_from_file(in_file)

    m = Matrix(data[1], data[0], data[2:])
    p_check = m.get_parity_check_matrix()  # Get parity check matrix
    write_to_file(out_file, p_check)
    # check_answer(out_file, check_file)
