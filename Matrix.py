

class Matrix:
    def __init__(self, rows, columns, data):
        self.num_rows = int(rows)
        self.num_columns = int(columns)
        self.matrix = self.create_matrix(data)
        self.column_order = [i for i in range(1, self.num_columns+1)]
        # self.gauss_jordan()

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
    def transpose(matrix):
        transposed = []
        for i in range(len(matrix[0])):
            transposed.append([])
        for cn in range(len(matrix[0])):
            for rn in range(len(matrix)):
                transposed[cn].append(matrix[rn][cn])
        return transposed

    # Returns the A part of G = [I A] matrix
    def get_A(self):
        res = []
        for rn in range(self.num_rows):
            res.append([])
            for cn in range(self.num_rows, self.num_columns):
                res[rn].append(self.matrix[rn][cn])
        return res

    # Should only be called after calling gauss - jordan;
    # Returns P = [A I]
    def get_parity_check_matrix(self):
        a = self.get_A()
        a_transposed = self.transpose(a)
        identity_matrix = self.make_identity_matrix(len(a_transposed))
        res = self.build_horizontally(a_transposed, identity_matrix)
        return res

    @staticmethod
    def build_horizontally(m1, m2):
        res = []
        for i in range(len(m1)):
            res.append([])
            res[i] += [val for val in m1[i] + m2[i]]
        return res

    @staticmethod
    def make_identity_matrix(size):
        identity_m = []
        for rn in range(size):
            identity_m.append([])
            for cn in range(size):
                if cn == rn:
                    identity_m[rn].append(1)
                else:
                    identity_m[rn].append(0)
        return identity_m

    @staticmethod
    def print_matrix(matrix):
        for r in matrix:
            print(r)
        print()
