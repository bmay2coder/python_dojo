import pdb;pdb.set_trace()

def add(x, y):
    sum=x+y
    return sum

def main():
    x = input("Number 1 : ")
    y = input("Number 2 : ")
    # x = int(input("Number 1 : "))
    # y = int(input("Number 2 : "))
    # breakpoint()
    z = add(x, y)
    print(z)

if __name__ == "__main__":
    main()