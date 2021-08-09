def divisors(num):
    divisor = [x for x in range(1, num + 1) if num % x == 0]
    return divisor



def run():
    num = int(input("Introduce un número:"))
    print(divisors(num))




if __name__ == "__main__":
    run()