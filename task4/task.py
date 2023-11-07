from math import log2

def make_sets():
    columns, strings = set(), set()
    for i in range(6):
        for j in range(6):
            columns.add((i + 1) * (j + 1))
            strings.add(i + j + 2)
    columns = list(columns)
    columns.sort()
    return columns, list(strings)

def make_table(columns, strings):
    table = [[0 for i in columns] for i in strings]
    for i in range(6):
        for j in range(6):
            if (i + 1) * (j + 1) in columns:
                table[strings.index(i + j + 2)][columns.index((i + 1) * (j + 1))] += 1
    return table

def make_table_of_prop(table):
    Pi = sum([sum(i) for i in table])
    return [[i / Pi for i in st] for st in table]

def h_a(table_of_prop):
    return sum([-sum(i) * log2(sum(i)) for i in table_of_prop])

def h_b(table_of_prop):
    s = [sum(table_of_prop[i][j] for i in range(len(table_of_prop))) for j in range(len(table_of_prop[0]))]
    return sum([-i * log2(i) for i in s])

def h_ab(table_of_prop):
    return sum([sum(-i * log2(i) for i in st if i) for st in table_of_prop])

def make_table_of_usl_prop(table):
    return [[i / sum(st) for i in st] for st in table]

def h_a_b(table_of_prop, table_of_usl_prop):
    Pi = [sum(st) for st in table_of_prop]
    Hsi_b = [sum([-i * log2(i) for i in st if i]) for st in table_of_usl_prop]
    return sum([Pi[i] * Hsi_b[i] for i in range(len(Pi))])

def i_ab(H_b, H_a_b):
    return H_b - H_a_b

def task():
    columns, strings = make_sets()
    table = make_table(columns, strings)
    table_of_prop = make_table_of_prop(table)
    table_of_usl_prop = make_table_of_usl_prop(table)
    H_b, H_a_b = h_b(table_of_prop), h_a_b(table_of_prop, table_of_usl_prop)
    return(h_ab(table_of_prop),
           h_a(table_of_prop),
           H_b,
           H_a_b,
           i_ab(H_b, H_a_b))

if __name__ == "__main__":
    print(*task(), sep='\t')