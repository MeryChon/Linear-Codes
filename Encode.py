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

    words_matrix_obj = Matrix(int(len(bits_to_encode)/word_length), word_length, words_to_encode)
    words_matrix = words_matrix_obj.get_matrix()

    encoded_matrix = Matrix.dot_product(words_matrix, generator_matrix, 2)
    return matrix_to_bit_array(encoded_matrix)


if __name__ == '__main__':
    generator_file = sys.argv[1]
    info_file = sys.argv[2]
    output_file = sys.argv[3]

    gen_info = read_from_generator_file(generator_file)
    generator_obj = Matrix(gen_info[1], gen_info[0], gen_info[2:])

    bits = str(SimpleRead.bytesToBits(SimpleRead.readBytesFromFile(info_file)))[10:-2]
    encoded_bits = encode(bits, generator_obj.get_matrix())
    CompleteWrite.writeToFile(output_file, CompleteWrite.addPadding(encoded_bits))
