def change_item(list):
    
    user = input("Give me index or item(Case Sensitive): ")
    print("_"*30)

    index = user if user.isdigit() else list.index(user)
    item = list[int(user)] if user.isdigit() else list[list.index(user)]
    print(f"Index: {index} and Item: {item}")

    
    new_item = input("Give me new item: ")

    list.remove(item)
    list.insert(int(index), new_item)
    print(f"Item is changed.\nYour old item ({item}) and new item ({new_item}).")