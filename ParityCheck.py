import sys
from Matrix import Matrix


def read_from_file(file_name):
    file_obj = open(file_name, "r")
    info = file_obj.read().split()
    return info


if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    data = read_from_file(in_file)

    m = Matrix(data[1], data[0], data[2:])
    m.gauss_jordan()  # Standardize the generator matrix
    p_check = m.get_parity_check_matrix()  # Get parity check matrix
    m.print_matrix(p_check)
