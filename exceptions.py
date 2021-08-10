def run():
    try:
        num = 1
        if num == 1:
            raise Exception("num is 1")
        print(1/0)
    except ZeroDivisionError:
        print("You can't divide by zero!")




if __name__ == '__main__':
    run()