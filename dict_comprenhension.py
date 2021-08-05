def run():
    dict_comprehension= {i:i*i for i in range(1,101)}
    for i in dict_comprehension:
        for key, value in dict_comprehension.items():
            print(key, ":", value)




if __name__ == '__main__':
    run()