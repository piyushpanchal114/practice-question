# Variation 1: To print the value of the given point in pascal triangle

r = 5
c = 3


def get_point_value(n, r):
    n -= 1
    r -= 1
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


print(get_point_value(r, c))


# variation 2: To print the row of pascal triangle

n = 5


def get_row(n):
    for i in range(1, n+1):
        res = get_point_value(n, i)
        print("res", res)


get_row(5)


def generate_row(n: int):
    ans = 1
    res = [1]
    for i in range(1, n):
        ans *= (n - i)
        ans //= i
        res.append(ans)
    return res


print(generate_row(5))


# Variation 3: To Generate the pascal triangle upto nth row


def pascal_triangle(n):
    res = []
    for i in range(1, n+1):
        res.append(generate_row(i))
    return res


print(pascal_triangle(5))
