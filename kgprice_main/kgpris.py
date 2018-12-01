import sys

def main():
    if (len(sys.argv) != 3):
        print("ERROR: Input price and weight")
        return 1
    price = float(sys.argv[1])
    mass = float(sys.argv[2])
    print(calculate(price, mass))

def calculate(price, mass):
    if (mass >= 1000):
        return mass/1000.0*price
    else:
        return 1000.0/mass*price

if (__name__ == "__main__"):
    main()
