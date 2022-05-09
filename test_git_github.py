# This code is for testing

def pow(a, b):
    if b == 1:
        return a

    return a * pow(a, b-1)

if __name__ == "__main__":
    print(pow(2, 1))
    print(pow(2, 2))
    print(pow(2, 3))
    print(pow(2, 4))
    print(pow(2, 5))
    print(pow(2, 6))