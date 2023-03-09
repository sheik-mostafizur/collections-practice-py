from show_list_items import show_list_items
from single_item import single_item
from change_item import change_item



# user_value = input("Give me list items: ")
# list = user_value.split(" ")
list = ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry']


print("""What do you want?
0. Show my list items.
1. Access list item.
2. Change list item.""")
options = input("Options: ")
print("\n")

if options == "0":
    show_list_items(list)

elif options == "1":
    single_item(list)

elif options == "2":
    change_item(list)

else:
    print("Data not found")

