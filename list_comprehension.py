def run():
    squares = [i**2 for i in range(1,101) if i%3 != 0]
    print(squares)
    squares_4_6_9 = [i for i in range(1,1001) if( (i%4==0) and (i%6==0) and (i%9==0))]
    print(squares_4_6_9)


# List with first numbers cuadrados
# def square_numbers(nums):
#     result = []
#     for i in range(nums + 1):
#         result.append(i**2)
#     print(result)


if __name__ == '__main__':
    run()