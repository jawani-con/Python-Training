def func(*args):
    pro=1
    for arg in args:
        pro= pro*arg
    return pro

def main():
    sum = func(1,2,3,4,5)
    print(sum)

main()