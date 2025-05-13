#list of squares of number from 1 to 10
#syntax for lst comp [expression for item in iterable if condition
def result(n):
    print([x**2 for x in range(n+1)])

result(10)
