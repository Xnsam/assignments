"""Python to execute python fibonacci."""


def fibo(x):
    """Function to calculate the fibonacci series."""
    if x < 2:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)


num = int(input('Enter the number : \t'))
for i in range(num):
    print(fibo(i))
