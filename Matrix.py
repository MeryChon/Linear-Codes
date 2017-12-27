

class Matrix:
    def __init__(self, rows, columns, data):
        self.num_rows = int(rows)
        self.num_columns = int(columns)
        self.matrix = self.create_matrix(data)
        self.column_order = [i for i in range(1, self.num_columns+1)]
        self.gauss_jordan()

    def get_matrix(self):
        return self.matrix

    def get_column_order(self):
        return self.column_order

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

    def subtract_from_other_rows(self, row_num, pivot_index):
        for i in range(self.num_rows):
            if i != row_num and self.matrix[i][pivot_index] != 0:
                self.subtract_rows(i, row_num)

    def swap_columns(self, first, second):
        for i in range(self.num_rows):
            self.matrix[i][first], self.matrix[i][second] = self.matrix[i][second], self.matrix[i][first]
        self.column_order[first], self.column_order[second] = self.column_order[second], self.column_order[first]

    def gauss_jordan(self):
        pivot_index = -1
        for i in range(self.num_rows):
            pivot_index += 1
            if self.matrix[i][i] == 0:
                for j in range(self.num_columns):
                    if self.matrix[i][j] != 0:
                        self.swap_columns(i, j)
                        break
            self.subtract_from_other_rows(i, pivot_index)

    @staticmethod
    def print_matrix(matrix):
        for r in matrix:
            print(r)
        print()
