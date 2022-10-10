# Lab 4-1

# 1. nothing will come out

def print_star():
    print('*******************************')


print_star()
print_star()
print_star()
print_star()
print_star()
print_star()


# Lab 4-2
def print_star2():
    print('*******************************')
    print('*******************************')


print_star2()
print_star2()
print_star2()
print_star2()
print_star2()


# Lab 4-3
def print_star():
    print('*************************')


def print_plus():
    print('++++++++++++++++++++++++')


def print_hash():
    print('#########################')


print_hash()
print_star()
print_plus()
print_plus()
print_star()
print_hash()


# LAB 4-4
def print_star(n):
    for _ in range(n):
        print('*************************')


print_star(10)


def print_hash(n):
    for _ in range(n):
        print('#########################')


print_hash(10)
print_hash(6)


def print_hash(n):
    for _ in range(n):
        for i in range(0, 6):
            print(i, '#########################')


print_hash(1)


# LAB 4-5

def print_sub(a, b):
    result = a - b
    print(a, '과', b, '의 차는', result, '입니다.')


print_sub(10, 20)


def print_mult(a, b):
    result = a * b
    print(a, '과', b, '의 곱은', result, '입니다.')


print_mult(10, 20)


# LAB 4-6
def print_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('해는', r1, '또는', r2)


print_root(1, 4, -21)
print_root(1, -6, 8)


def print_area(a, b):
    r = (a * b) / 2
    print('밑변', a, '높이', b, '인 삼각형의 면적은 :', r)

print_area(10, 20)

# LAB 4-7
def print_circle_area_circum(r):
    a = (3.14 * r ** 2)
    c = (2 * 3.14 * r)
    return a, c
a, c = print_circle_area_circum(10)
print('반지름', 10, '인 원의 면적은', a, '원의 둘레는', c)

# LAB 4-8
def multiples(n, m):
 r1 = n * (m - 3)
 r2 = n * (m - 2)
 r3 = n * (m - 1)
 r4 = n * m
 return r1, r2, r3, r4

r1, r2, r3, r4 = multiples(3, 4)
print(r1, r2, r3, r4)

def multiples(n, m):
 r1 = n * (m - 4)
 r2 = n * (m - 3)
 r3 = n * (m - 2)
 r4 = n * (m - 1 )
 r5 = n * m
 return r1, r2, r3, r4, r5

r1, r2, r3, r4, r5 = multiples(2, 5)
print(r1, r2, r3, r4, r5)

# LAB 4 - 9
def print_name(honorifics, first_name, last_name):
        print(honorifics, first_name, last_name)

print_name(first_name= 'Gildong', last_name='Hong', honorifics='Dr.')
print_name('Gildong', 'Hong', 'Dr.')
# The output will be arranged the same way as it is in between brackets, meaning Gildong Hong Dr., this line of code didn't even use the function of codes above

# LAB 4 - 10
def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result
print('3 개의 인지 (10, 20, 30)'"\n" '합계:', sum_nums(10, 20, 30), ', 평균:', sum_nums(10, 20, 30)/3)
print('5 개의 인지 (10, 20, 30, 40, 50)'"\n" '합계:', sum_nums(10, 20, 30, 40, 50), ', 평균:', sum_nums(10, 20, 30, 40, 50)/5)

def min_nums(*numbers):
    result = min(20, 40, 50, 10)
    return result
print('최솟값은', min_nums(20, 40, 50, 10))

# LAB 4 - 11
name = input('당신의 이름을 입력해주세요 : ')
age = input('나이를 입력해주세요 : ')
job = input('직업을 입력해주세요 : ')
home = input('사는 곳을 입력해주세요: ')
print('당신의 이름은 {}, 나이는 {}살, 직업은 {}, 사는 곳은 {}입니다.'.format(name, age, job, home))


name = input('당신의 이름을 입력해주세요 : ')
age = input('나이를 입력해주세요 : ')
job = input('직업을 입력해주세요 : ')
home = input('사는 곳을 입력해주세요: ')
print('당신의 이름은', name, ', 나이는',age, '살', ', 직업은', job, ', 사는 곳은', home, '입니다.')

# LAB 4 - 12
print('_'.join('ABCD'))

s = 'My favorite thing is monsters'
print(s.replace('monsters', 'cartoons'))



