

class Matrix:
    def __init__(self, rows, columns, data):
        self.num_rows = int(rows)
        self.num_columns = int(columns)
        self.matrix = self.create_matrix(data)
        self.gauss_jordan()
        # print(self.matrix)

    @staticmethod
    def create_matrix(data):
        matrix = []
        for r in range(len(data)):
            matrix.append([])
            for i in range(len(data[r])):
                matrix[r].append(int(data[r][i]))
        return matrix

    def subtract_rows(self, from_index, to_subtr_index):
        to_subtr = self.matrix[to_subtr_index]
        for i in range(self.num_columns):
            self.matrix[from_index][i] = self.matrix[from_index][i] ^ to_subtr[i]

    def subtract_from_lower_rows(self, row_num, pivot_index):
        pivot = self.matrix[row_num][pivot_index]
        # print(row_num, pivot_index, self.num_rows, len(self.matrix))
        for i in range(row_num+1, self.num_rows):
            if self.matrix[i][pivot_index] != 0:
                self.subtract_rows(i, row_num)
            self.print_matrix(self.matrix)

    def gauss_jordan(self):
        pivot_index = -1
        for i in range(self.num_rows):
            pivot_index += 1
            # pivot = -1
            for j in range(self.num_columns):
                if self.matrix[i][j] != 0:
                    pivot_index = j
                    # pivot = self.matrix[i][j]
                    break
            self.subtract_from_lower_rows(i, pivot_index)

    @staticmethod
    def print_matrix(matrix):
        for r in matrix:
            print(r)
        print()