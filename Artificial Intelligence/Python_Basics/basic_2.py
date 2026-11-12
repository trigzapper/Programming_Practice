def print_list(x):
    for i, fruit in enumerate(x):
        print(f"ind:{i} , fructo: {fruit}")


def sum_output(a, b):
    c = a + b
    return c

def slicing_test(l):
    print(l[0:6])
    print(l[0:7:3])
    print(l[8:1:-1])
    print(l[::-2])



#x = ["apple", "banana", "cherry", "date", "elderberry"]
#print_list(x)
#a , b = map(int, input("Enter two numbers: ").split())
#op = sum_output(a,b)
#print(f"Sum of {a} and {b} is: {op}")

#l = [1,2,3,4,5,6,7,8,9,10]
#slicing_test(l) 

sq = [ x**2 for x in range(7)]
print(sq)


