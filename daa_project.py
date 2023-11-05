import csv
#Global Matrix
p = []
b = []

c = []
a = []

# Function to calculate mean of a matrix
def calculate_mean(matrix):
    total = 0
    count = 0
    for row in matrix:
        for val in row:
            if(val != 0):
                total += val
                count += 1
    return total / count if count > 0 else 0

# Function to initialize matrix b and c
def matrix_initialize_b_c(dim_a, dim_b):
    mean_A = calculate_mean(a)
    sqrt_mean_over_d = (mean_A / d) ** 0.5

    # Initialize matrix b
    global b, c
    b = [[sqrt_mean_over_d for _ in range(d)] for _ in range(dim_a)]

    # Initialize matrix c
    c = [[sqrt_mean_over_d for _ in range(dim_b)] for _ in range(d)]



#Function for initializing the value of a matrix a
def matrix_set_a(filename, dim_a, dim_b):
    global a
    a = [[0 for _ in range(dim_b)] for _ in range(dim_a)]

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i < dim_a:
                for j, val in enumerate(row):
                    if j < dim_b:
                        a[i][j] = int(val)


#Function for calculating the value of p by product of b and c matrix
def matrix_set_p(n, m, d):
    # Create a 2D matrix for the 'p' array
    global p,b, c
    p = [[0 for _ in range(m)] for _ in range(n)]

    # Iterate through the 'p' array
    for i in range(n):
        for j in range(m):
            # Calculate the sum of products for each element
            for k in range(d):
                p[i][j] += b[i][k] * c[k][j]

#Function for finding error
def calculate_precision(m, n):

    count = 0
    for i in range(m):
        for j in range(n):
            if a[i][j] != 0:
                count += 1

    sum_val = 0
    for i in range(m):
        for j in range(n):
            sum_val += (a[i][j] - p[i][j]) * (a[i][j] - p[i][j])

    er = (sum_val / count) ** 0.5
    return er

#Setting the value of matrix b as per the formula
def matrix_set_b(n,m,d):
    for r in range(n):
        for s in range(d):
            sum_value = 0
            d_sum_value = 1
            for j in range(m):
                su = 0
                for k in range(d):
                    if k != s:
                        su += b[r][k] * c[k][j]

                sum_value += c[s][j] * (a[r][j] - su)
                d_sum_value += c[s][j] * c[s][j]

            if d_sum_value != 0:
                b[r][s] = sum_value / d_sum_value

#Setting the value of matrix c as per the formula
def matrix_set_c(n,m,d):
    for r in range(d):
        for s in range(m):
            sum_val = 0
            d_sum_val = 1
            for i in range(n):
                su = 0
                for k in range(d):
                    if k != s:
                        su += b[i][k] * c[k][s]

                sum_val += b[i][r] * (a[i][s] - su)
                d_sum_val += b[i][r] * b[i][r]

            if d_sum_val != 0:
                c[r][s] = sum_val / d_sum_val






#Main Program
dim_a = 50
dim_b = 20
d = 100
final_ans = 1

#Initializing the value of a
matrix_set_a('data.csv', dim_a, dim_b)

#Initializing the value of b and c matrix
matrix_initialize_b_c(dim_a,dim_b)


#Set the value of p
matrix_set_p(dim_a,dim_b,d)


#Finding the initial error
initial_error = calculate_precision(dim_a, dim_b)
print(f" \nFor d={d}, initial error: {initial_error}")

#Setting the value of b as per the formula given in assignment
matrix_set_b( dim_a, dim_b, d)


#Setting the value of c as per the formula given in assignment
matrix_set_c(dim_a, dim_b, d)

#Set the new value of p
matrix_set_p(dim_a,dim_b,d)

val = calculate_precision(dim_a, dim_b)
print("For d=", d, ", final error:", val)
threshold = val/initial_error
print("For d=", d, ", Threshold is:", threshold)

#Printing Matrix a
print("\nMatrix A:")
for i in range(dim_a):
    for j in range(dim_b):
        print(a[i][j], end=" ")
    print()

#Printing Matrix b
print("\nMatrix B:")
for i in range(dim_a):
    for j in range(d):
        print(b[i][j], end=" ")
    print()
#Printing Matrix c
print("\nMatrix C:")
for i in range(d):
    for j in range(dim_b):
        print(c[i][j], end=" ")
    print()

#Printing Matrix p
print("\nMatrix P:")
for i in range(dim_a):
    for j in range(dim_b):
        print(p[i][j], end=" ")
    print()




