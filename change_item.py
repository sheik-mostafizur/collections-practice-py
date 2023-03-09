def change_item(list):
    user = input("Give me index or item: ")
    if user.isdigit():
        index = list[int(user)]
    print(user.isdigit())