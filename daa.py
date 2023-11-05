import math


def convert(s):
    num = 0
    for i in range(len(s)):
        num = num * 10 + (ord(s[i]) - ord('0'))
    return num

def set_A(n, m):
    with open("./data.csv") as f:
        ans = []
        for line in f:
            ans.append(line.strip())

    global a
    inc = 0
    a = [[convert(ans[inc]) for j in range(m)] for i in range(n)]

def initial(n, m, d):
    sum_value = 0
    for i in range(n):
        for j in range(m):
            sum_value += a[i][j]

    v = sum_value / (n * m)
    res = (math.sqrt(v) // d)
    return res

def set_BC(iv, n, m, d):
    global b, c

    b = [[iv for j in range(d)] for i in range(n)]
    c = [[iv for j in range(m)] for i in range(d)]

def set_B(n, m, d):
    global b

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

def set_C(n, m, d):
    global c

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

def setp(n, m, d):
    global p

    for i in range(n):
        for j in range(m):
            for k in range(d):
                p[i][j] += b[i][k] * c[k][j]

def find_precision(n, m):
    c = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] != 0:
                c += 1

    sum_val = 0
    for i in range(n):
        for j in range(m):
            sum_val += (a[i][j] - p[i][j]) * (a[i][j] - p[i][j])

    er = math.sqrt(sum_val / c)
    return er

if __name__ == "__main__":
    dim_a = 50
    dim_b = 20

    set_A(dim_a, dim_b)
    d = 2
    final_ans = 1

    set_BC(initial(dim_a, dim_b, d), dim_a, dim_b, d)
    setp(dim_a, dim_b, d)
    initial_error = find_precision(dim_a, dim_b)
    print("\nFor d=" + str(d) + ", initial error:", initial_error)

    set_BC(initial(dim_a, dim_b, d), dim_a, dim_b, d)
    set_C(dim_a, dim_b, d)
    set_B(dim_a, dim_b, d)
    setp
