from show_list_items import show_list_items
from single_item import single_item
from change_item import change_item



# user_value = input("Give me list items: ")
# list = user_value.split(" ")
list = ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry.', 'Lorem', 'Ipsum', 'been', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', '1500s,', 'when', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book.', 'survived', 'only', 'five', 'centuries,', 'also', 'leap', 'into', 'electronic', 'typesetting,', 'remaining', 'essentially', 'unchanged.', 'popularised', '1960s', 'with', 'release', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages,', 'more', 'recently', 'with', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'Lorem', 'Ipsum.']


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

