import sys

from Matrix import Matrix
from itertools import permutations


def read_from_generator_file(file_name):
    file_obj = open(file_name, "r")
    info = file_obj.read().split()
    return info


def read_num(file_name):
    file_obj = open(file_name, 'r')
    return int(file_obj.read())


def get_error_vectors(num_errors, parity_check_m):
    res = []
    indices_of_ones = []
    vector_length  = len(parity_check_m[0])
    l = [i for i in range(vector_length)]

    for i in range(1, num_errors+1):
        perm = list(permutations(l, i))
        indices_of_ones += perm

    for p in indices_of_ones:
        error_v = []

        for j in range(vector_length):
            if j in p:
                error_v.append(1)
            else:
                error_v.append(0)
        res.append(error_v)
    return res


def get_syndromes(error_vects, parity_check_m):
    errors_transposed = Matrix.transpose(error_vects)
    return Matrix.dot_product(parity_check_m, errors_transposed, 2)


def map_syndromes_with_errors(syndromes, errors) :
    res_map = {}
    for si in range(len(syndromes)):
        key = "".join(str(b) for b in syndromes[si])
        res_map[key] = errors[si]
    return res_map


def write_to_file(output_file, parity_check_matrix, syndromes_map):
    file_obj = open(output_file, 'w')

    num_rows = len(parity_check_matrix)
    num_cols = len(parity_check_matrix[0])
    to_write = str(num_cols) + " " + str(num_rows) + "\n"
    for r in parity_check_matrix:
        for i in r:
            to_write += str(i)
        to_write += "\n"

    for synd in syndromes_map:
        to_write += synd + " " + "".join(str(eb) for eb in syndromes_map[synd]) + "\n"

    file_obj.write(to_write)
    file_obj.close()


if __name__ == '__main__':
    generator_file = sys.argv[1]
    num_file = sys.argv[2]
    out_file = sys.argv[3]

    gen_info = read_from_generator_file(generator_file)
    generator_obj = Matrix(gen_info[1], gen_info[0], gen_info[2:])
    parity_matrix = generator_obj.get_parity_check_matrix()

    num = read_num(num_file)

    error_vectors = get_error_vectors(num, parity_matrix)

    syndromes = get_syndromes(error_vectors, parity_matrix)

    syndrome_map = map_syndromes_with_errors(Matrix.transpose(syndromes), error_vectors)

    write_to_file(out_file, parity_matrix, syndrome_map)


