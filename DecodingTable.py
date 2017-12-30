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
        # TODO: improve key/value types
        res_map[str(syndromes[si])] = errors[si]
    return res_map


if __name__ == '__main__':
    generator_file = sys.argv[1]
    num_file = sys.argv[2]
    out_file = sys.argv[3]

    gen_info = read_from_generator_file(generator_file)
    generator_obj = Matrix(gen_info[1], gen_info[0], gen_info[2:])
    parity_matrix = generator_obj.get_parity_check_matrix()
    Matrix.print_matrix(parity_matrix)

    num = read_num(num_file)

    error_vectors = get_error_vectors(num, parity_matrix)
    Matrix.print_matrix(error_vectors)

    syndromes = get_syndromes(error_vectors, parity_matrix)
    Matrix.print_matrix(syndromes)

    syndrome_map = map_syndromes_with_errors(Matrix.transpose(syndromes), error_vectors)
    for s in syndrome_map:
        print(s, " : ", syndrome_map[s])

    # TODO: write to file;


