import sys

import CompleteWrite
from Matrix import Matrix
import SimpleRead


def read_from_generator_file(file_name):
    file_obj = open(file_name, "r")
    info = file_obj.read().split()
    return info

def matrix_to_bit_array(matrix):
    res = ""
    for r in matrix:
        for el in r:
            res += str(el)
    return res


def encode(bits_to_encode, generator_matrix):
    word_length = len(generator_matrix)
    words_to_encode = [bits_to_encode[i:i+word_length] for i in range(0, len(bits_to_encode), word_length)]
    print(words_to_encode)
    words_matrix_obj = Matrix(int(len(bits_to_encode)/word_length), word_length, words_to_encode)
    # words_matrix_obj.print_self_matrix()
    words_matrix = words_matrix_obj.get_matrix()
    # print(words_to_encode)
    # Matrix.print_matrix(words_matrix)
    encoded_matrix = Matrix.dot_product(words_matrix, generator_matrix, 2)
    Matrix.print_matrix(encoded_matrix)
    print(len(words_matrix) == len(encoded_matrix))
    # Matrix.print_matrix(encoded_matrix)
    return matrix_to_bit_array(encoded_matrix)


if __name__ == '__main__':
    generator_file = sys.argv[1]
    info_file = sys.argv[2]
    output_file = sys.argv[3]
    gen_info = read_from_generator_file(generator_file)
    generator_obj = Matrix(gen_info[1], gen_info[0], gen_info[2:])
    generator_obj.standardize()
    # generator_obj.print_self_matrix()
    # print(generator_obj.get_column_order())
    generator_obj.return_original_column_order()
    # generator_obj.print_self_matrix()

    bits_to_encode = str(SimpleRead.bytesToBits(SimpleRead.readBytesFromFile(info_file)))[10:-2]
    print(bits_to_encode)
    encoded_bits = encode(bits_to_encode, generator_obj.get_matrix())
    # print(encoded_bits)
    CompleteWrite.writeToFile(output_file, CompleteWrite.addPadding(encoded_bits))
    # print(bits_to_encode)


