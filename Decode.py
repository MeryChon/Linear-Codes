import sys

import CompleteRead
# import SimpleRead
import CompleteWrite
from Matrix import Matrix


def get_parity_and_syndrome_info(info_file):
    file_obj = open(info_file)
    raw_info = file_obj.read().split()
    num_rows = int(raw_info[1])
    parity_matrix_obj = Matrix(raw_info[1], raw_info[0], raw_info[2:])
    syndrome_map_list = raw_info[num_rows + 2:]
    syndrome_map = {}
    for i in range(0, len(syndrome_map_list) - 1, 2):
        syndrome_map[syndrome_map_list[i]] = [int(s) for s in syndrome_map_list[i+1]]
    file_obj.close()
    return parity_matrix_obj, syndrome_map


def read_encoded_data_as_matrix(in_file, code_word_length):
    bits_to_correct = CompleteRead.removePadding(CompleteRead.bytesToBits(CompleteRead.readBytesFromFile(in_file)))
    encoded_words = [bits_to_correct[i:i + code_word_length] for i in range(0, len(bits_to_correct), code_word_length)]
    encoded_matrix = Matrix(len(bits_to_correct)/code_word_length, code_word_length, encoded_words)
    return encoded_matrix


def get_syndromes(parity_check_m_obj, encoded_words_m_obj):
    parity_m = parity_check_m_obj.get_matrix()
    trans_encoded_m = Matrix.transpose(encoded_words_m_obj.get_matrix())
    prod = Matrix.dot_product(parity_m, trans_encoded_m, 2)
    return Matrix.transpose(prod)


def xor(v1, v2, mod):
    res = []
    for i in range(len(v1)):
        res.append((v1[i] ^ v2[i]) % mod)
    return res


def matrix_to_bit_array(matrix):
    res = ""
    for r in matrix:
        for el in r:
            res += str(el)
    return res


def correct_codes(syndrome_map, syndromes_matr, encoded_matr):
    zero_syndrome = "".join("0" for i in range(len(syndromes_matr[0])))
    res = []
    for i in range(len(syndromes_matr)):
        if 1 in syndromes_matr[i]:
            syndr_str = "".join(str(el) for el in syndromes_matr[i])
            error_v = syndrome_map[syndr_str]
            corrected = xor(error_v, encoded_matr[i], 2)
            res.append(corrected)
        else:
            res.append(encoded_matr[i])
    return res


if __name__ == '__main__':
    parity_and_syndrome_file = sys.argv[1]
    data_file = sys.argv[2]
    out_file = sys.argv[3]

    parity_check_matrix, syndrome_map = get_parity_and_syndrome_info(parity_and_syndrome_file)
    encoded_words_matrix = read_encoded_data_as_matrix(data_file, parity_check_matrix.get_num_columns())
    syndromes = get_syndromes(parity_check_matrix, encoded_words_matrix)
    # TODO: too many argument passes and returns; may slow down the execution
    corrected_code_words = correct_codes(syndrome_map, syndromes, encoded_words_matrix.get_matrix())
    CompleteWrite.writeToFile(out_file, CompleteWrite.addPadding(matrix_to_bit_array(corrected_code_words)))


