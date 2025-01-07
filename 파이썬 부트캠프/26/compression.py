names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

if __name__ == "__main__" :
    number = [1, 2, 3]

    new_list = [n+1 for n in number]

    name = "Angela"
    new_list = [letter for letter in name]
    print(new_list)

    numbers = [1, 2, 3 ,4 ]
    new_numbers = [num*2 for num in numbers]
    print(new_numbers)



    short_names = [name for name in names if len(name) < 5]
    short_names = [name.upper() for name in names if len(name) >= 5]
    print(short_names)
