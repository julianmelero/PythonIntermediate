def run():
    my_list = [1,"hello", True, 4.5]
    my_dict = {
        "firstname": "Julián",
        "lastname": "Melero"
    }


    super_list = [
    {
        "firstname": "Julián",
        "lastname": "Melero"
    },
    {
        "firstname": "Ana",
        "lastname": "Anita"
    },
    {
        "firstname": "Concha",
        "lastname": "Conxa"
    }
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,-3,-4,-5],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


    for i in super_list:
        for key, value in i.items():
            print(key, "-", value)

        print(key, "-", value)


if __name__ == "__main__":
    run()