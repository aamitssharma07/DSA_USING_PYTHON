import csv
import statistics


def initialize_bc_values(dimA, dimB):
    mean_value_a = mean_matrix(aMatrix)
    sqrt_mean_over_d = (mean_value_a / d) ** 0.5

    # Initialize matrix bMatrix
    global bMatrix, cMatrix
    bMatrix = [[sqrt_mean_over_d for _ in range(d)] for _ in range(dimA)]

    # Initialize matrix cMatrix
    cMatrix = [[sqrt_mean_over_d for _ in range(dimB)] for _ in range(d)]

def add_values_to_a(filename, dimA, dimB):
    global aMatrix
    aMatrix = [[0 for _ in range(dimB)] for _ in range(dimA)]

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i < dimA:
                for j, val in enumerate(row):
                    if j < dimB:
                        aMatrix[i][j] = int(val)

def set_p_matrix(n, m, d):
    global pMatrix, bMatrix, cMatrix
    pMatrix = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(d):
                pMatrix[i][j] += bMatrix[i][k] * cMatrix[k][j]

def calculate_error(m, n):
    count = 0
    for i in range(m):
        for j in range(n):
            if aMatrix[i][j] != 0:
                count += 1

    sum_val = 0
    for i in range(m):
        for j in range(n):
            sum_val += (aMatrix[i][j] - pMatrix[i][j]) * (aMatrix[i][j] - pMatrix[i][j])

    er = (sum_val / count) ** 0.5
    return er

def add_values_to_b(n, m, d):
    for r in range(n):
        for s in range(d):
            sum_value = 0
            d_sum_value = 1
            for j in range(m):
                su = 0
                for k in range(d):
                    if k != s:
                        su += bMatrix[r][k] * cMatrix[k][j]

                sum_value += cMatrix[s][j] * (aMatrix[r][j] - su)
                d_sum_value += cMatrix[s][j] * cMatrix[s][j]

            if d_sum_value != 0:
                bMatrix[r][s] = sum_value / d_sum_value


def mean_matrix(matrix):
    non_zero_values = [val for row in matrix for val in row if val != 0]
    return statistics.mean(non_zero_values) if non_zero_values else 0

def add_values_to_c(n, m, d):
    for r in range(d):
        for s in range(m):
            sum_val = 0
            d_sum_val = 1
            for i in range(n):
                su = 0
                for k in range(d):
                    if k != s:
                        su += bMatrix[i][k] * cMatrix[k][s]

                sum_val += bMatrix[i][r] * (aMatrix[i][s] - su)
                d_sum_val += bMatrix[i][r] * bMatrix[i][r]

            if d_sum_val != 0:
                cMatrix[r][s] = sum_val / d_sum_val

# Main Program
dimA = 50
dimB = 20
pMatrix = []
bMatrix = []
cMatrix = []
aMatrix = []
d = 100

#
add_values_to_a('data.csv', dimA, dimB)


initialize_bc_values(dimA, dimB)

set_p_matrix(dimA, dimB, d)


initial_error = calculate_error(dimA, dimB)
print(f"\nFor d={d}, INITIAL ERROR: {initial_error}")
val = initial_error;


#Continuously updating the value of b and c and then calculating threashhold
for i in range(1000):

    add_values_to_b(dimA, dimB, d)


    add_values_to_c(dimA, dimB, d)

    # Set the new value of pMatrix
    set_p_matrix(dimA, dimB, d)
    initial_error = val
    val = calculate_error(dimA, dimB)
    threshold = val / initial_error
print("For d=", d, ", LAST ERROR:", val)
print("For d=", d, ", THRESH HOLD:", threshold)





print("\nMatrix A:")
for i in range(dimA):
    for j in range(dimB):
        print(aMatrix[i][j], end=" ")
    print()


print("\nMatrix B:")
for i in range(dimA):
    for j in range(d):
        print(bMatrix[i][j], end=" ")
    print()


print("\nMatrix C:")
for i in range(d):
    for j in range(dimB):
        print(cMatrix[i][j], end=" ")
    print()

print("\nMatrix P:")
for i in range(dimA):
    for j in range(dimB):
        print(pMatrix[i][j], end=" ")
    print()